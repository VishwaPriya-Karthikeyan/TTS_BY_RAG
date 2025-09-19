TTS_BY_RAG

Text-to-Speech PDF Q&A using RAG

This project is a chatbot for your PDF files.
It uses RAG (Retrieval-Augmented Generation) to:

Read your documents

Understand them

Answer your questions in its own words (not just copy-paste)


If you ask something outside the PDF, it will politely say:

> "You are a helpful assistant that answers questions based only on the given context".



The app runs offline with a lightweight HuggingFace model and provides a simple Streamlit interface with text-to-speech (TTS) support.


---

 Features

1.Chat with your PDF (ask natural questions)
2.Answers are generated (not direct copy-paste)
3.Rejects unrelated questions politely
4.Speaks answers aloud using pyttsx3
5.Fully offline (no API key required)


---

Tools Used

Python 3.11.9 – programming language (tested version)

LangChain – connects LLM with ChromaDB and retriever logic

HuggingFace Transformers – loads the FLAN-T5 model

ChromaDB – stores embeddings (vector database)

Streamlit – builds the web interface

pyttsx3 – converts text answers to speech



---

📂 Project Structure

RAG_SYSTEM/
│── app.py                # Main app (Streamlit interface)
│── create_embeddings.py  # Converts PDF into text + embeddings
│── create_chromadb.py    # Creates and saves Chroma vector DB
│── requirements.txt      # All dependencies
│── chroma_db/            # Vector DB (auto-created after running scripts)
│── mypdf/                # Folder for your PDF files


---

 Step-by-Step Setup Guide

>  These instructions assume you are using Python 3.11.9. Please make sure you have it installed.



1.Clone the repository

git clone https://github.com/VishwaPriya-Karthikeyan/TTS_BY_RAG/blob/main/README.md

2.Create a virtual environment (inside Python 3.11.9)

python -m venv myenv

Activate it:

myenv\Scripts\activate    # On Windows

3.Install dependencies

pip install -r requirements.txt

4.Place your PDF

Put your study notes or any PDF file inside the mypdf/ folder.

5.Generate embeddings

This step converts your PDF into vector embeddings for search.

python create_embeddings.py

6.Create ChromaDB

This builds and saves the vector database.

python create_chromadb.py

7.Run the app

streamlit run app.py

After running, Streamlit will give you a local URL in the terminal.
Open it in your browser and start chatting with your PDF 


---

Example Usage

Q (from PDF):

What are the main types of data in data science?

A (generated):

Data can be structured or unstructured. It is also classified by how it is measured, 
such as numerical, categorical, or time-series data. These classifications help 
decide how analysis methods are applied.

Q (not in PDF):
"How are you"

A:

"You are a helpful assistant that answers questions based only on the given context".


---

 Future Improvements

Multiple PDF support

GPU acceleration

Smarter refusal for unrelated queries

Better summarization models



---

 Author

Developed by:

Vishwa Priya K

Sharmila L

Adhithian A