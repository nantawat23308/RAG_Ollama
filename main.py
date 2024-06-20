from langchain_community.embeddings.ollama import OllamaEmbeddings

CHROMA_PATH = "chroma"
DATA_PATH = "data"


def ollama_embedding_function():
    ollama_emb = OllamaEmbeddings(model="tinyllama")
    return ollama_emb
