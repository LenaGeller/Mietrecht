from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path




from config import CHAT_MODEL, TEMPERATURE

# ===============================
# Prompt Template
# ===============================

PROMPT_PATH = Path(__file__).resolve().parent.parent / "app" / "prompt.txt"

PROMPT_TEXT = PROMPT_PATH.read_text(encoding="utf-8")

prompt = ChatPromptTemplate.from_template(PROMPT_TEXT)

model = ChatOpenAI(model=CHAT_MODEL, temperature=TEMPERATURE)
parser = StrOutputParser()

chain = prompt | model | parser

