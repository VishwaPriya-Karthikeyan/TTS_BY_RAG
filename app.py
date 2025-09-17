import streamlit as st
import pyttsx3
from langchain_community.vectorstores import Chroma
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

# ----------------------------
# Load embeddings
# ----------------------------
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ----------------------------
# Load Chroma DB
# ----------------------------
db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": 2})  # fetch top 2 docs

# ----------------------------
# Load lightweight model
# ----------------------------
qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",   # better than small/mini
    device=-1  # CPU
)
llm = HuggingFacePipeline(pipeline=qa_pipeline)

# ----------------------------
# Custom Prompt
# ----------------------------
prompt_template = """
You are a helpful assistant that answers questions based only on the provided context.

Context:
{context}

Question: {question}

Answer clearly and in your own words.
If the context does not contain the answer, reply with exactly:
"Sorry, my job is only to chat with your PDF."
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
qa_chain = LLMChain(llm=llm, prompt=prompt)

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("📘 Offline PDF Q&A (Smart Mode)")
st.write("Ask questions from your PDF (offline).")

query = st.text_input("Enter your question:")

if query:
    # Step 1: Retrieve relevant context
    docs = retriever.get_relevant_documents(query)
    context_text = " ".join([doc.page_content for doc in docs]) if docs else ""

    # Step 2: Reject if context is empty
    if not context_text.strip():
        answer = "Sorry, my job is only to chat with your PDF."
    else:
        # Step 3: Generate final answer
        answer = qa_chain.run({"context": context_text, "question": query})

    st.write("### Answer:")
    st.write(answer)

    if st.button("🔊 Speak Answer"):
        engine = pyttsx3.init()
        engine.say(answer)
        engine.runAndWait()