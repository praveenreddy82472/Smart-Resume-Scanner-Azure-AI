# Smart Resume Scanner (Azure AI)

## Overview

**Smart Resume Scanner** is an interactive web application built with **Streamlit** that leverages **Azure Cognitive Services** to automate resume parsing and skill matching. It extracts key candidate information from resumes and scores the candidate’s skills against a job description (JD), helping recruiters quickly identify the best matches.

---
## 📸 Sample Outputs

Here are some screenshots of the Smart Resume Scanner in action:

![Output 1](https://github.com/praveenreddy82472/Smart-Resume-Scanner-Azure-AI/blob/main/sample_outputs/1.jpg?raw=true)
![Output 2](https://github.com/praveenreddy82472/Smart-Resume-Scanner-Azure-AI/blob/main/sample_outputs/2.jpg?raw=true)
![Output 3](https://github.com/praveenreddy82472/Smart-Resume-Scanner-Azure-AI/blob/main/sample_outputs/3.jpg?raw=true)

---
## Key Features

- **Resume Upload:** Easily upload PDF or DOCX resumes.
- **Azure Document Intelligence:** Uses Azure Form Recognizer’s prebuilt models to extract structured data such as Name, Email, Phone, LinkedIn, GitHub, Skills, Projects, and Experience.
- **Azure Language Service:** Performs advanced text analysis including key phrase extraction and sentiment detection.
- **Skill Match Scoring:** Compares extracted skills with your pasted job description and provides a match percentage, highlighting matched and missing skills.
- **Clean & Intuitive UI:** Built with Streamlit for seamless interaction and quick insights.

---

## Why Use Azure AI?

Manually screening resumes can be tedious and error-prone. This project harnesses Azure’s powerful AI capabilities to:

- **Automate** resume data extraction,
- **Standardize** candidate information,
- **Accelerate** screening and shortlisting,
- **Improve** hiring decisions through data-driven insights.

---

## How It Works

1. **Upload Resume:** Upload candidate’s resume file (PDF or DOCX).  
2. **Extract Information:** Azure Document Intelligence extracts key fields from the resume.  
3. **Analyze Text:** Azure Language Service extracts important keywords and detects sentiment.  
4. **Paste Job Description:** Input the JD text to compare required skills.  
5. **Match Scoring:** The app computes skill overlap and presents a match score along with matched/missing skills.  
6. **View Results:** Review the extracted details and skill matching report instantly on the web page.

---

## Getting Started

1. **Clone this repository:**

   ```bash
   https://github.com/praveenreddy82472/Smart-Resume-Scanner-Azure-AI.git

   cd smart-resume-scanner-azure
