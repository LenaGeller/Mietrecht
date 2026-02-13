import streamlit as st
import sys
from pathlib import Path

# src-Ordner importierbar machen
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "src"))

from pipeline import frage_stellen


# --- Setup ---
st.set_page_config(page_title="Mietrechts-Assistent", layout="centered")
st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    text-align: left;
    font-size: 0.9rem;
    padding: 0.5rem 0.75rem;
    line-height: 1.25;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True) 

st.markdown("""
<style>
/* Abstand UNTER Überschriften reduzieren */
h1, h2, h3, h4 {
    margin-bottom: 0.5rem;
}

/* Abstand VOR Text Inputs reduzieren */
div[data-testid="stTextInput"] {
    margin-top: -0.75rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <h2 style="margin-bottom:0.2rem;">
       🏠 F<span style="color:#6b7280;">RAG</span> den Mietrechts-Bot
    </h2>
    """,
    unsafe_allow_html=True
)
example_questions = [
    "Ich suche eine Wohnung in Berlin – worauf sollte ich bei der Besichtigung achten?",
    "Der Aufzug war zwei Wochen kaputt. Darf ich die Miete mindern?",
    "Darf mein Vermieter die Miete so einfach erhöhen, ohne dass ich zustimme?",
    "Welche Kosten darf der Vermieter in der Nebenkostenabrechnung abrechnen?",
    "Darf nach einer Modernisierung die Miete erhöht werden?"
]

st.markdown("**Beispiel-Fragen**")

if "frage" not in st.session_state:
    st.session_state.frage = ""

for q in example_questions:
    if st.button(q):
        st.session_state.frage = q

st.markdown("#### Deine Frage")

frage = st.text_input(
    "",
    key="frage"
)

if st.button("Frage stellen"): 
    if not frage.strip(): 
        st.warning("Bitte gib eine Frage ein.") 
    else: 
        with st.spinner("Antwort wird erzeugt …"): 
            antwort, docs = frage_stellen(frage) 
        
        st.markdown("### Antwort") 
        st.write(antwort)


        st.markdown("### Quellen & Textstellen")

        for i, d in enumerate(docs, start=1):
            meta = d.metadata or {}

            label = (
                f"Quelle {i}: "
                f"{meta.get('titel')} "
            )

            with st.expander(label):
                
                st.markdown("**Original-Textstelle:**")
                st.write(d.page_content)

 
