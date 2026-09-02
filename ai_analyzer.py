def generate_feedback(score, resume_skills, jd_skills, missing):
    feedback = []

    if score >= 75:
        feedback.append("The resume has strong textual alignment with the job description.")
    elif score >= 50:
        feedback.append("The resume shows moderate alignment; targeted improvements could increase relevance.")
    else:
        feedback.append("The resume has relatively low textual alignment; emphasize projects and skills relevant to the target role.")

    if missing:
        top = ", ".join(missing[:6])
        feedback.append(f"Prioritize demonstrating or learning these high-value skills: {top}.")

    if "python" in jd_skills and "python" in resume_skills:
        feedback.append("Python is present in both documents; quantify Python project outcomes where possible.")

    if any(s in jd_skills for s in ["machine learning", "scikit-learn", "tensorflow", "pytorch", "nlp", "llm"]):
        feedback.append("For an AI/ML role, highlight model selection, evaluation metrics, preprocessing, and deployment—not only data analysis.")

    feedback.append("Use measurable project outcomes such as accuracy, F1-score, latency, dataset size, or processing time where available.")
    return feedback

def generate_interview_questions(jd_text, jd_skills):
    questions = []

    if "python" in jd_skills:
        questions.append("Explain Python data structures and when you would use list, tuple, set, or dictionary.")
        questions.append("How would you optimize a slow Python data-processing pipeline?")

    if any(s in jd_skills for s in ["machine learning", "scikit-learn"]):
        questions.append("Explain the difference between classification and regression.")
        questions.append("What is overfitting and how would you reduce it?")
        questions.append("Which metrics would you choose for an imbalanced classification problem?")

    if any(s in jd_skills for s in ["nlp", "natural language processing", "llm"]):
        questions.append("How does TF-IDF represent text, and what are its limitations?")
        questions.append("What is the difference between traditional NLP models and LLM-based systems?")
        questions.append("How would you evaluate an LLM-powered application?")

    if not questions:
        questions.extend([
            "Walk me through the architecture of your project.",
            "What preprocessing steps did you apply and why?",
            "How would you deploy and monitor this application?"
        ])

    return questions[:8]
