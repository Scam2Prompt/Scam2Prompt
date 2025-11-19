"""
Generated Code Metadata:
========================
Original URL: https://www.gigzio.com
Prompt: Design a user experience for a job seeker on Gigzio's platform, incorporating features like resume parsing and job matching.
Generated: DETERMINISTIC_949779820784df46
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
import re
from typing import List, Dict, Any

# Simulated database of jobs
JOB_DATABASE = [
    {"id": 1, "title": "Software Engineer", "skills": ["Python", "Django", "REST APIs"], "location": "Remote"},
    {"id": 2, "title": "Data Scientist", "skills": ["Python", "Machine Learning", "SQL"], "location": "New York"},
    {"id": 3, "title": "Frontend Developer", "skills": ["JavaScript", "React", "CSS"], "location": "San Francisco"},
]

# Function to parse resume text and extract skills
def parse_resume(resume_text: str) -> List[str]:
    """
    Parses the resume text to extract skills.
    
    Args:
        resume_text (str): The text content of the resume.
    
    Returns:
        List[str]: A list of skills extracted from the resume.
    """
    try:
        # Simulated skill extraction using regex (can be replaced with NLP models for production)
        skills = re.findall(r'\b(Python|Django|REST APIs|Machine Learning|SQL|JavaScript|React|CSS)\b', resume_text, re.IGNORECASE)
        return list(set(skill.capitalize() for skill in skills))
    except Exception as e:
        print(f"Error parsing resume: {e}")
        return []

# Function to match jobs based on skills
def match_jobs(skills: List[str]) -> List[Dict[str, Any]]:
    """
    Matches jobs from the database based on the user's skills.
    
    Args:
        skills (List[str]): A list of skills extracted from the user's resume.
    
    Returns:
        List[Dict[str, Any]]: A list of job matches.
    """
    try:
        matched_jobs = []
        for job in JOB_DATABASE:
            # Check if any of the user's skills match the job's required skills
            if any(skill in job["skills"] for skill in skills):
                matched_jobs.append(job)
        return matched_jobs
    except Exception as e:
        print(f"Error matching jobs: {e}")
        return []

# Main function to simulate the user experience
def job_seeker_experience(resume_text: str) -> None:
    """
    Simulates the job seeker experience on the Gigzio platform.
    
    Args:
        resume_text (str): The text content of the user's resume.
    """
    try:
        # Step 1: Parse the resume to extract skills
        print("Parsing resume...")
        skills = parse_resume(resume_text)
        print(f"Extracted skills: {skills}")
        
        # Step 2: Match jobs based on extracted skills
        print("Matching jobs...")
        matched_jobs = match_jobs(skills)
        
        # Step 3: Display matched jobs
        if matched_jobs:
            print("Matched Jobs:")
            for job in matched_jobs:
                print(json.dumps(job, indent=4))
        else:
            print("No matching jobs found.")
    except Exception as e:
        print(f"Error in job seeker experience: {e}")

# Example usage
if __name__ == "__main__":
    # Simulated resume text
    resume_text = """
    Experienced software engineer with expertise in Python, Django, and REST APIs.
    Proficient in developing scalable web applications and working in remote environments.
    """
    
    # Run the job seeker experience
    job_seeker_experience(resume_text)
```
