from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# ----------------------------
# Path to your PDF
# ----------------------------
pdf_path = r"C:\Users\Students.DESKTOP-B4HV036.000\Desktop\RAG_SYSTEM\mypdf\A_Brief_Introduction_To_AI.pdf"  # replace with your PDF

# ----------------------------
# Load PDF and extract text
# ----------------------------
print("Loading PDF...")
reader = PdfReader(pdf_path)
text = ""
for i, page in enumerate(reader.pages):
    print(f"Processing page {i+1}...")
    text += page.extract_text() or ""
print("PDF loaded and text extracted")

# ----------------------------
# Split text into smaller chunks
# ----------------------------
text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)  # smaller chunks
texts = text_splitter.split_text(text)
print(f"Text split into {len(texts)} chunks")

# ----------------------------
# Generate numeric embeddings
# ----------------------------
print("Generating embeddings...")
model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
embeddings_list = model.embed_documents(texts)
print("Embeddings generated")

# ----------------------------
# Save embeddings and texts
# ----------------------------
save_folder = "readable_embeddings"
os.makedirs(save_folder, exist_ok=True)

# Save embeddings
with open(os.path.join(save_folder, "embeddings.txt"), "w", encoding="utf-8") as f:
    for emb in embeddings_list:
        f.write(", ".join([str(x) for x in emb]) + "\n")

# Save texts
with open(os.path.join(save_folder, "texts.txt"), "w", encoding="utf-8") as f:
    for chunk in texts:
        f.write(chunk.replace("\n", " ") + "\n")

print("Embeddings and texts saved!")