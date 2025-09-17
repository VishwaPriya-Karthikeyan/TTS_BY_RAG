from langchain_community.vectorstores import Chroma

# --------------------------
# Load text chunks
# --------------------------
texts_file = r"readable_embeddings/texts.txt"
with open(texts_file, "r", encoding="utf-8") as f:
    texts = [line.strip() for line in f.readlines()]

# --------------------------
# Load embeddings
# --------------------------
embeddings_file = r"readable_embeddings/embeddings.txt"
embeddings_array = []
with open(embeddings_file, "r") as f:
    for line in f:
        vector = [float(x.strip()) for x in line.split(",") if x.strip()]
        embeddings_array.append(vector)

# --------------------------
# Metadata and IDs
# --------------------------
metadatas = [{"page": i+1} for i in range(len(embeddings_array))]
ids = [str(i+1) for i in range(len(embeddings_array))]

# --------------------------
# Create Chroma DB
# --------------------------
db = Chroma(persist_directory="chroma_db", embedding_function=None)

# Add embeddings manually
db._collection.add(
    documents=texts,
    embeddings=embeddings_array,
    metadatas=metadatas,
    ids=ids
)

# Persist DB
db.persist()
print("Chroma DB saved in 'chroma_db' folder")