import streamlit as st
from resume_parser import parse_resume
from recognizer import analyze_document
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Smart Resume Scanner", layout="centered")
def extract_keywords(text):
    skills_list = [
        'python', 'sql', 'azure', 'gcp', 'aws', 'airflow', 'power bi',
        'docker', 'kubernetes', 'terraform', 'pandas', 'numpy', 'looker',
        'bigquery', 'spark', 'hadoop', 'etl', 'dataflow', 'databricks',
        'snowflake', 'mlflow', 'scikit-learn'
    ]
    found = []
    for skill in skills_list:
        if skill.lower() in text.lower():
            found.append(skill.lower())
    return set(found)

def match_score(resume_text, jd_text):
    resume_skills = extract_keywords(resume_text)
    jd_skills = extract_keywords(jd_text)

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills

    score = round(len(matched) / len(jd_skills) * 100, 2) if jd_skills else 0.0
    return score, matched, missing

def display_field(key, value):
    st.markdown(f"**{key}:**")
    if isinstance(value, list):
        if value and "not found" not in value[0].lower():
            for item in value:
                st.markdown(f"- {item}")
        else:
            st.markdown("_No data found_")
    elif value:
        st.markdown(f"{value}")
    else:
        st.markdown("_No data found_")

def main():
    st.title("📄 Smart Resume Scanner")
    st.write("Upload a resume to extract relevant details.")
    st.write("Upload your resume and paste a job description to get a skill match score.")

    uploaded_file = st.file_uploader("Choose a resume (PDF or DOCX)", type=["pdf", "docx"])
    
    #JD input
    jd_text = st.text_area("📋 Paste the Job Description below:", height=250)

    if uploaded_file:
        st.sidebar.info(f"**File uploaded:** {uploaded_file.name}")
        with st.spinner('Analyzing the resume...'):
            resume_text = analyze_document(uploaded_file)
            st.session_state.resume_text = resume_text
            st.session_state.resume_data = parse_resume(resume_text)
            
            score, matched, missing = match_score(resume_text, jd_text)
            st.session_state.score = score
            st.session_state.matched = matched
            st.session_state.missing = missing
        st.success("✅ Resume processed!")

        # Display only if session state has results
        if "resume_data" in st.session_state:
            st.subheader("📌 Extracted Information")

        for key, value in st.session_state.resume_data.items():
            display_field(key, value)

        st.subheader("📊 JD Match Results")
        st.markdown(f"**Match Score:** `{st.session_state.score}%`")
        st.markdown(f"✅ **Matched Skills:** {', '.join(st.session_state.matched) if st.session_state.matched else 'None'}`")
        st.markdown(f"❌ **Missing Skills from JD:** {', '.join(st.session_state.missing) if st.session_state.missing else 'None'}`")

    else:
        st.info("⬅️ Upload resume and paste JD, then click **Apply JD Match** to start.")

if __name__ == "__main__":
    main()
