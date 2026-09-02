import re

SKILLS = {
    "python", "java", "javascript", "typescript", "c++", "sql",
    "mongodb", "mysql", "postgresql", "pandas", "numpy", "scikit-learn",
    "sklearn", "tensorflow", "pytorch", "keras", "machine learning",
    "deep learning", "nlp", "natural language processing", "llm",
    "generative ai", "artificial intelligence", "computer vision",
    "transformers", "hugging face", "langchain", "openai", "gemini",
    "streamlit", "flask", "fastapi", "django", "rest api", "rest apis",
    "docker", "git", "github", "linux", "aws", "azure", "gcp",
    "power bi", "tableau", "excel", "statistics", "data analysis",
    "data visualization", "etl", "api", "react", "node.js", "express",
    "html", "css", "bootstrap"
}

def normalize(text):
    return re.sub(r"\s+", " ", text.lower())

def extract_skills(text):
    text = normalize(text)
    found = set()
    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"
        if re.search(pattern, text):
            found.add(skill)
    return sorted(found)

def find_missing_skills(resume_skills, jd_skills):
    return sorted(set(jd_skills) - set(resume_skills))
