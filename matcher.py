import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def calculate_similarity(resume_text, jd_text):
    documents = [clean(resume_text), clean(jd_text)]
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(float(similarity * 100), 2)
