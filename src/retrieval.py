# retrieval.py
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from config import CHROMA_DIR, NEU_COLLECTION, EMBEDDING_MODEL

emb = OpenAIEmbeddings(model=EMBEDDING_MODEL)

db = Chroma(
    persist_directory=str(CHROMA_DIR),
    collection_name=NEU_COLLECTION,
    embedding_function=emb
)
