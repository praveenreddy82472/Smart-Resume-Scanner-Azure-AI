import re

def parse_resume(text):
    data = {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "LinkedIn": extract_linkedin(text),
        "GitHub": extract_github(text),
        "Skills": extract_skills(text),
        "Projects": extract_projects(text),
        "Experience": extract_experience(text),
    }
    return data

def extract_name(text):
    lines = text.split("\n")
    for line in lines:
        if len(line.split()) <= 3 and any(x.isalpha() for x in line):
            return line.strip()
    return "Not found"

def extract_email(text):
    match = re.search(r"[\w.-]+@[\w.-]+", text)
    return match.group(0) if match else "Not found"

def extract_phone(text):
    match = re.search(r"(\+\d{1,2}\s?)?(\(?\d{3}\)?\s?-?\d{3}-?\d{4})", text)
    return match.group(0) if match else "Not found"

def extract_linkedin(text):
    match = re.search(r"https?://(www\.)?linkedin\.com/in/[\w-]+", text)
    return match.group(0) if match else "Not found"

def extract_github(text):
    match = re.search(r"https?://(www\.)?github\.com/[\w-]+", text)
    return match.group(0) if match else "Not found"

def extract_skills(text):
    skills_list = ["Python", "SQL", "Azure", "GCP", "Pandas", "Numpy", "Power BI", "TensorFlow"]
    found = [skill for skill in skills_list if skill.lower() in text.lower()]
    return ", ".join(found) if found else "Not found"


def extract_projects(text):
    project_titles = []
    match = re.search(r"(projects|project experience|academic projects)([\s\S]*?)(experience|education|skills|certifications|$)", text, re.IGNORECASE)
    if match:
        section_text = match.group(2).strip()
        lines = [line.strip() for line in section_text.split('\n') if line.strip()]
        for line in lines:
            # Skip lines that look like date ranges (e.g. Nov 2024 - Dec 2024)
            if re.match(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4} *- *[a-zA-Z]* \d{4}\b", line):
                continue
            if re.match(r"^[A-Z][\w\s,&\-']{3,60}$", line):
                project_titles.append(line)
    return project_titles if project_titles else ["No project titles found"]


def extract_experience(text):
    experience_titles = []
    match = re.search(r"(work experience|professional experience|work history)([\s\S]*?)(education|skills|projects|certifications|$)", text, re.IGNORECASE)
    if match:
        section_text = match.group(2).strip()
        lines = [line.strip() for line in section_text.split('\n') if line.strip()]
        role_keywords = ['role','client','engineer', 'developer', 'manager', 'analyst', 'consultant', 'specialist', 'scientist', 'architect', 'lead','senior','Senior Data Engineer',
                         'Software Engineer','Data scientist']
        for line in lines:
            if len(line.split()) > 1 and any(word.lower() in line.lower() for word in role_keywords):
                experience_titles.append(line)
    return experience_titles if experience_titles else ["No experience titles found"]
