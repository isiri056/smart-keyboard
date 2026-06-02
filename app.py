import streamlit as st
from spellchecker import SpellChecker

# Page Configuration
st.set_page_config(
    page_title="AI Smart Keyboard",
    page_icon="⌨️",
    layout="centered"
)

# Custom CSS Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #0f172a;
    }

    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: white;
        margin-top: 20px;
    }

    .subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 18px;
        margin-bottom: 40px;
    }

    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border-radius: 15px;
        border: 2px solid #3b82f6;
        padding: 15px;
        font-size: 18px;
    }

    .output-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-size: 22px;
        border-left: 6px solid #22c55e;
        margin-top: 20px;
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        margin-top: 50px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Spell Checker
spell = SpellChecker()

# Header
st.markdown('<div class="title">AI Smart Keyboard</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Real-Time Autocorrect System using NLP</div>',
    unsafe_allow_html=True
)

# Input
text = st.text_input("Type your sentence here")

# Autocorrect Logic
if text:

    words = text.split()

    corrected_words = []

    for word in words:
        corrected_words.append(spell.correction(word))

    corrected_sentence = " ".join(corrected_words)

    st.markdown(
        f'''
        <div class="output-box">
        ✅ Corrected Text:<br><br>
        {corrected_sentence}
        </div>
        ''',
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    '<div class="footer">Built using Python, NLP, Streamlit & SpellChecker</div>',
    unsafe_allow_html=True
)