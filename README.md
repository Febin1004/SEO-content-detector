# SEO Content Quality & Duplicate Detector

## 1. Project Overview
This project analyzes web pages to assess **SEO content quality** and detect **duplicate or thin content** using Natural Language Processing (NLP) and Machine Learning techniques. It extracts textual features from HTML, evaluates readability, identifies similarities, and classifies each page into **Low**, **Medium**, or **High Quality**.

---

## 2. Setup Instructions
```bash
git clone https://github.com/Febin1004/SEO-content-detector.git
cd seo-content-detector
pip install -r requirements.txt
jupyter notebook notebooks/seo_pipeline.ipynb
```
## 3. Quick Start

1. Place your dataset (`data.csv`) in the `/data` folder.  
2. Run the Jupyter notebook `seo_pipeline.ipynb` to:
   - Parse HTML and extract clean text  
   - Generate SEO and readability features  
   - Detect duplicate pages using cosine similarity  
   - Train the ML classifier for quality scoring  
3. To test interactively, launch the Streamlit app:
   ```bash
   streamlit run streamlit_app/app.py
## 4. Deployed Streamlit URL

👉 **[Live Demo on Streamlit Cloud](https://seo-content-detector-nyuxrfutgyvjbqfybaytcc.streamlit.app/)**

---

## 5. Key Decisions

- **Libraries Used:** `BeautifulSoup` (HTML parsing), `textstat` (readability), `scikit-learn` (TF-IDF, ML model), and `sentence-transformers` (semantic similarity).  
- **HTML Parsing:** Extracted `<p>`, `<article>`, and `<main>` tags for clean, meaningful body text.  
- **Similarity Threshold:** Set at 0.8 cosine similarity to flag near-duplicate pages while minimizing false positives.  
- **Model Selection:** Used **Logistic Regression** for simplicity and interpretability; compared performance with **Random Forest** as baseline.

---

## 6. Results Summary

- **Model Accuracy:** 0.78  
- **F1 Score:** 0.75  
- **Duplicate Pairs Detected:** 3  
- **Thin Content Pages:** 6 out of 60 (≈10%)  

**Sample Quality Labels:**  
- **High Quality:** 62.5–70 readability, >1500 words  
- **Medium Quality:** Balanced readability, 500–1500 words  
- **Low Quality:** <500 words or readability <30  

---

## 7. Limitations

- Limited dataset size (≈70 pages) restricts generalization.  
- HTML parsing may lose semantic context if webpage structures differ widely.  
- Advanced NLP tasks such as **sentiment analysis** and **topic modeling** are not yet implemented.
