import os
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import textstat
from sentence_transformers import SentenceTransformer, util
import pickle

# ---- FIX for TensorFlow / Keras conflicts ----
os.environ["USE_TF"] = "0"
os.environ["USE_TORCH"] = "1"
os.environ["TRANSFORMERS_NO_TF_WARNING"] = "1"

# ---- Load model ----
MODEL_PATH = "../models/quality_model.pkl"

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        quality_model = pickle.load(f)
else:
    quality_model = None

# ---- Initialize embedder ----
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# ---- Functions ----
def scrape_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No Title"
        body = " ".join([p.get_text() for p in soup.find_all("p")])
        return title, body
    except Exception as e:
        return None, f"Error: {e}"

def analyze_text(text):
    word_count = len(text.split())
    sentence_count = text.count(".") + text.count("!") + text.count("?")
    readability = textstat.flesch_reading_ease(text)
    embedding = embedder.encode([text])[0]
    return word_count, sentence_count, readability, embedding

def classify_quality(word_count, readability):
    if word_count > 1500 and 50 <= readability <= 70:
        return "High"
    elif word_count < 300 or readability < 30:
        return "Low"
    else:
        return "Medium"

# ---- Streamlit UI ----
st.set_page_config(page_title="SEO Content Quality & Duplicate Detector", layout="wide")
st.title("🧠 SEO Content Quality & Duplicate Detector")

url_input = st.text_input("Enter a URL to analyze:", "")

if st.button("Analyze"):
    if not url_input.strip():
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Scraping and analyzing content..."):
            title, body = scrape_url(url_input)
            if body.startswith("Error"):
                st.error(body)
            elif not body.strip():
                st.error("No main text found on the page.")
            else:
                word_count, sentence_count, readability, embedding = analyze_text(body)
                quality_label = classify_quality(word_count, readability)

                st.subheader(f"Title: {title}")
                st.write(f"**Word Count:** {word_count}")
                st.write(f"**Sentence Count:** {sentence_count}")
                st.write(f"**Readability Score:** {round(readability, 2)}")
                st.write(f"**Predicted Quality:** :green[{quality_label}]")

                st.success("✅ Analysis complete!")
