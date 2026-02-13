# config.py
from pathlib import Path
from dotenv import load_dotenv
import zipfile
from huggingface_hub import hf_hub_download
import shutil
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "chroma_db"
ZIP_PATH = BASE_DIR / "chroma_db.zip"

HF_REPO_ID = "lenageller/mietrecht"
HF_FILENAME = "chroma_db.zip"

print("BASE_DIR:", BASE_DIR)
print("Keyword YAML:", BASE_DIR / "knowledge base" / "query_normalization.yaml")

def ensure_chroma_db():
    # Wenn Ordner schon da ist -> nichts tun
    if CHROMA_DIR.exists() and any(CHROMA_DIR.iterdir()):
        print("✅ ChromaDB already present:", CHROMA_DIR)
        return

    print("⬇️ Downloading ChromaDB from Hugging Face...")
    downloaded_zip = hf_hub_download(
        repo_id=HF_REPO_ID,
        filename=HF_FILENAME,
        repo_type="dataset",
    )

    # Zip an festen Ort kopieren (optional, aber übersichtlich)
    shutil.copy2(downloaded_zip, ZIP_PATH)

    print("📦 Unzipping...")
    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        z.extractall(BASE_DIR)

    print("✅ ChromaDB ready at:", CHROMA_DIR)

ensure_chroma_db()

# Aktive Collection (Projektstandard)
COLLECTION_NAME = "mietrecht"

EMBEDDING_MODEL = "text-embedding-3-large"
CHAT_MODEL = "gpt-5-mini"

TEMPERATURE = 0.1

