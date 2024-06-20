from langchain_community.embeddings.ollama import OllamaEmbeddings
from setting import MODEL


def ollama_embedding_function():
    ollama_emb = OllamaEmbeddings(model=MODEL)
    return ollama_emb
