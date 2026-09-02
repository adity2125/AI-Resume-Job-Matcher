# 🤖 AI Resume & Job Description Matcher

An AI/NLP-based Python application that analyzes how closely a candidate's resume matches a target job description. The system extracts resume text, identifies relevant technical skills, calculates a similarity score, highlights skill gaps, and provides role-specific recommendations.

## 🎯 Project Objective

Recruiters often need to compare a large number of resumes against job descriptions. This project demonstrates how NLP and machine-learning techniques can automate the initial screening process.

The application follows this pipeline:

**PDF Resume → Text Extraction → NLP Preprocessing → TF-IDF Vectorization → Cosine Similarity → Skill Extraction → Skill Gap Analysis → Recommendations**

---

## ✨ Features

- 📄 Extract text from PDF resumes
- 📝 Accept job descriptions through a web interface
- 🧠 Calculate resume-JD similarity using TF-IDF and cosine similarity
- 🔍 Extract technical skills from resume and job description
- ✅ Identify matching skills
- ⚠️ Identify potential skill gaps
- 💡 Generate AI-style improvement recommendations
- 🎯 Generate role-specific interview preparation questions
- 🌐 Interactive Streamlit web interface
- 📊 Display an overall resume-JD match percentage

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application and processing |
| Streamlit | Interactive web interface |
| scikit-learn | TF-IDF and cosine similarity |
| pdfplumber | PDF text extraction |
| NLP / Text Processing | Text cleaning and skill analysis |
| TF-IDF | Text feature representation |
| Cosine Similarity | Resume-JD similarity calculation |

---

## 🧠 How the System Works

### 1. Resume Processing

The user uploads a PDF resume.

`pdfplumber` extracts text from each page and combines it into a single text representation.

### 2. Job Description Processing

The user provides the target job description through the Streamlit interface.

### 3. NLP Feature Extraction

The resume and job description are converted into numerical representations using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

TF-IDF gives higher importance to terms that are relevant to a document while reducing the importance of very common terms.

### 4. Similarity Calculation

The system calculates **cosine similarity** between the resume and job-description vectors.

```text
Cosine Similarity =
(A · B) / (||A|| × ||B||)
