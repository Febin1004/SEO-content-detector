import requests
from bs4 import BeautifulSoup
from readability import Document
import re

def fetch_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; SEO-Detector/1.0)"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            return r.text
    except:
        return ""
    return ""

def clean_spaces(s):
    if not isinstance(s, str): return ""
    return re.sub(r"\s+", " ", s).strip()

def parse_html_to_text(html):
    if not isinstance(html, str) or not html.strip():
        return {"title": "", "body_text": "", "word_count": 0}
    try:
        doc = Document(html)
        title = clean_spaces(doc.short_title() or "")
        soup_main = BeautifulSoup(doc.summary(), "lxml")
        chunks = []
        for sel in ["article", "main", "section", "p"]:
            for tag in soup_main.select(sel):
                txt = tag.get_text(" ", strip=True)
                if txt: chunks.append(txt)
        body = clean_spaces(" ".join(chunks))
        if not body:
            body = clean_spaces(BeautifulSoup(html, "lxml").get_text(" ", strip=True))
        wc = len(body.split())
        return {"title": title, "body_text": body, "word_count": wc}
    except Exception:
        txt = clean_spaces(BeautifulSoup(html or "", "lxml").get_text(" ", strip=True))
        return {"title": "", "body_text": txt, "word_count": len(txt.split())}
