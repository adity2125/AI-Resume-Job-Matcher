import re
from pathlib import Path

import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills, find_missing_skills
from matcher import calculate_similarity
from ai_analyzer import generate_feedback, generate_interview_questions

st.set_page_config(page_title="AI Resume & Job Matcher", page_icon="🤖", layout="wide")

st.title("🤖 AI Resume & Job Description Matcher")
st.caption("Python + NLP + Machine Learning | Intelligent Resume-to-Job Matching")

with st.sidebar:
    st.header("How it works")
    st.markdown("""
    1. Upload a resume PDF
    2. Paste the target Job Description
    3. Extract skills using NLP-based matching
    4. Calculate semantic similarity using TF-IDF + cosine similarity
    5. Identify skill gaps and generate interview preparation suggestions
    """)

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Resume")
    uploaded = st.file_uploader("Upload resume (PDF)", type=["pdf"])
    resume_text = ""
    if uploaded:
        resume_text = extract_text_from_pdf(uploaded)
        st.success(f"Extracted {len(resume_text.split())} words from the resume.")
        with st.expander("Preview extracted text"):
            st.text(resume_text[:4000])

with col2:
    st.subheader("2. Job Description")
    jd_text = st.text_area(
        "Paste the job description",
        height=320,
        placeholder="Paste the complete job description here..."
    )

if st.button("🚀 Analyze Match", type="primary", use_container_width=True):
    if not resume_text:
        st.error("Please upload a PDF resume.")
        st.stop()
    if len(jd_text.strip()) < 80:
        st.error("Please paste a more complete job description.")
        st.stop()

    score = calculate_similarity(resume_text, jd_text)
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    missing = find_missing_skills(resume_skills, jd_skills)

    st.divider()
    st.subheader("📊 Analysis Results")

    a, b, c = st.columns(3)
    a.metric("Resume–JD Match", f"{score:.1f}%")
    b.metric("Skills Found in Resume", len(resume_skills))
    c.metric("Skills Identified in JD", len(jd_skills))

    st.progress(min(score / 100, 1.0))

    left, right = st.columns(2)

    with left:
        st.markdown("### ✅ Matching Skills")
        matching = sorted(set(resume_skills) & set(jd_skills))
        if matching:
            st.write(", ".join(matching))
        else:
            st.info("No direct skills matched from the built-in skill dictionary.")

    with right:
        st.markdown("### ⚠️ Potential Skill Gaps")
        if missing:
            st.write(", ".join(missing))
        else:
            st.success("No major skill gaps detected from the built-in dictionary.")

    st.markdown("### 🧠 Intelligent Recommendations")
    feedback = generate_feedback(score, resume_skills, jd_skills, missing)
    for item in feedback:
        st.write("•", item)

    st.markdown("### 🎯 Interview Questions to Prepare")
    for q in generate_interview_questions(jd_text, jd_skills):
        st.write("•", q)

    with st.expander("Technical methodology"):
        st.markdown("""
        **Text similarity:** TF-IDF converts the resume and job description into
        numerical feature vectors. Cosine similarity measures how close those
        vectors are.

        **Skill gap analysis:** A curated technical skill dictionary is used to
        detect skills present in the resume and compare them with skills detected
        in the job description.

        **AI extension:** The architecture is ready for an LLM API layer for
        richer feedback and question generation without changing the core NLP/ML
        pipeline.
        """)

st.divider()
st.caption("Built as an AI/NLP portfolio project using Python.")
