from flask import Flask, render_template, request
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Replace with your OpenAI key
os.environ["GROQ_API_KEY"] = "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"

# Global vars
retriever = None
qa_chain = None


def setup_rag_pipeline(file_path):
    global retriever, qa_chain

    loader = TextLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = FAISS.from_documents(split_docs, embeddings)

    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
    llm=ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    ),
    retriever=retriever,  # ✅ THIS is required!
    return_source_documents=True
)


@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename.endswith(".txt"):
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
                setup_rag_pipeline(file_path)
                return render_template("index.html", message="File uploaded. Ask your question!")

        if "question" in request.form and qa_chain:
            query = request.form["question"]
            result = qa_chain(query)
            answer = result["result"]

    return render_template("index.html", answer=answer)
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
