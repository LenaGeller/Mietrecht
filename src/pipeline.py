
from llm import prompt, model, parser
from retrieval import retriever

# --- Abfragefunktion ---
def frage_stellen(frage: str):

    # 1. Retriever ruft relevante Chunks ab
    docs = retriever.invoke(frage)

    # 2. Kontext MIT METADATEN zusammenbauen
    context_parts = []
    for d in docs:
        titel = d.metadata.get("titel", "unbekannt")
        header = f"[QUELLE: {titel}]"
        context_parts.append(header + "\n" + d.page_content)

    context = "\n\n".join(context_parts)

    # 4) LLM aufrufen
    chain = prompt | model | parser


    antwort = chain.invoke({"context": context, "question": frage})

    
    return antwort, docs
