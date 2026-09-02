# AI Resume & Job Description Matcher

An AI/NLP portfolio project that analyzes how closely a resume matches a target job description.

## Why this project?

The project demonstrates a practical Python AI workflow:

**Document ingestion → NLP preprocessing → TF-IDF feature extraction → cosine similarity → skill extraction → skill-gap analysis → AI-style recommendations**

It is especially relevant for Python, AI, NLP, and machine-learning developer roles.

## Features

- PDF resume text extraction
- Job description input
- TF-IDF + cosine similarity match score
- Technical skill extraction
- Matching skills and potential skill gaps
- AI-style improvement feedback
- Role-specific interview questions
- Streamlit web interface

## Tech Stack

- Python
- Streamlit
- scikit-learn
- pdfplumber
- NLP / text processing
- TF-IDF
- Cosine similarity

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Architecture

```text
Resume PDF ──> PDF Parser ──> Text
                              │
Job Description ──────────────┤
                              ↓
                    Text Preprocessing
                              ↓
                    TF-IDF Vectorization
                              ↓
                   Cosine Similarity Score
                              │
                              ├──> Match Score
                              ├──> Skill Extraction
                              ├──> Skill Gap Analysis
                              └──> Interview Questions
```

## Machine-learning component

TF-IDF converts documents into numerical vectors based on word/phrase importance. Cosine similarity then measures the angle between the two vectors to estimate textual relevance.

This is a lightweight, explainable baseline. For production use, the next step would be sentence embeddings (for example, a transformer-based embedding model) and an LLM layer for deeper semantic reasoning.

## Future improvements

- Sentence-transformer embeddings
- LLM API integration
- OCR for scanned resumes
- Persistent database for candidate profiles
- Resume ranking across multiple job descriptions
- Deployment with authentication and monitoring
