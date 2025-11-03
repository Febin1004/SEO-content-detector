import textstat
import nltk
import re

nltk.download('punkt', quiet=True)

def sentence_count(text):
    if not isinstance(text, str) or not text.strip():
        return 0
    return len(nltk.sent_tokenize(text))

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip().lower()

def compute_features(text):
    text = clean_text(text)
    wc = len(text.split())
    sc = sentence_count(text)
    fr = textstat.flesch_reading_ease(text) if text.strip() else 0.0
    return {
        "word_count": wc,
        "sentence_count": sc,
        "flesch_reading_ease": fr
    }
