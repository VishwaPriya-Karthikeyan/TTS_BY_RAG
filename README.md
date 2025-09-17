# TTS_BY_RAG
Text to speech using RAG

📘 RAG-Based PDF Q&A System (Offline)

This project is a chatbot for your PDF files.
It uses RAG (Retrieval-Augmented Generation) to read your documents, understand them, and answer your questions in its own words.

If you ask something outside the PDF, it will politely say:

> "You are a helpful assistant that answers questions based only on the given context".


The app runs offline with a lightweight HuggingFace model and provides a simple Streamlit interface.



 Features

Chat with your PDF (ask natural questions)
 Generates answers in its own words (not just copy-paste)
 Rejects unrelated questions
 Speaks answers aloud using text-to-speech
 Offline model (no API key required)



 Tools Used

Python – programming language

LangChain – connects LLM with ChromaDB and retriever logic

HuggingFace Transformers – loads the FLAN-T5 model

ChromaDB – stores embeddings (vector database)

Streamlit – builds the web interface

pyttsx3 – converts text answers to speech



---

 Project Structure

RAG_SYSTEM/
│── app.py                # Main app (Streamlit interface)
│── create_embeddings.py  # Converts PDF into text + embeddings
│── create_chromadb.py    # Creates and saves Chroma vector DB
│── requirements.txt      # All dependencies
│── chroma_db/            # Vector DB (auto-created after running scripts)
│── mypdf/                # Folder for your PDF files


---

 Step-by-Step Setup Guide

1 Clone the repository

git clone https://github.com/your-username/RAG_SYSTEM.git
cd RAG_SYSTEM

2 Create a virtual environment

python -m venv myenv
myenv\Scripts\activate    # On Windows

3 Install dependencies

pip install -r requirements.txt

4 Place your PDF

Put your study notes or any PDF file into the mypdf/ folder.

5 Generate embeddings

This converts your PDF into vector embeddings for search.

python create_embeddings.py

6 Create ChromaDB

Builds and saves the vector database.

python create_chromadb.py

7 Run the app

streamlit run app.py

After this, you’ll see a local link in your terminal.
Open it in your browser → ask questions to your PDF!



 Example Usage

 Question (from PDF):

What are the main types of data in data science?

 Answer (generated):

Data can be structured or unstructured. It is also classified by how it is measured, such as numerical, categorical, or time-series data. These classifications help decide how analysis methods are applied.

 Question (not in PDF):

Who is BTS?

 Answer:

"You are a helpful assistant that answers questions based only on the given context".




 Future Improvements

Multiple PDF support

GPU acceleration

Smarter refusal for unrelated queries

Better summarization models





 Author

Developed by Vishwa Priya.K,Sharmila.L,Adhithian.A





