"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gigzio.com
Prompt: Create a function to parse resumes and match them to job postings based on keywords and criteria, referencing Gigzio's job matching features.
Generated: DETERMINISTIC_962116b3047527c9
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import defaultdict

def parse_and_match_resumes(resumes, job_postings):
    """
    Parses resumes and matches them to job postings based on keywords and criteria.

    Args:
        resumes (list of dict): A list of resumes where each resume is a dictionary with keys:
                                'name' (str): Candidate's name.
                                'content' (str): The full text of the resume.
        job_postings (list of dict): A list of job postings where each posting is a dictionary with keys:
                                     'title' (str): Job title.
                                     'description' (str): Full description of the job posting.
                                     'keywords' (list): List of essential keywords for the job.

    Returns:
        dict: A dictionary where keys are job titles and values are lists of candidate names
              that are the best matches for each job.
    """
    # Helper function to extract matched keywords between text and a given keyword list
    def extract_matching_keywords(text, keywords):
        text = text.lower()
        return [keyword for keyword in keywords if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', text)]
    
    # Results dictionary to hold job matches
    job_matches = defaultdict(list)
    
    for job in job_postings:
        job_title = job.get('title', 'Unknown Job')
        job_keywords = job.get('keywords', [])
        
        for resume in resumes:
            candidate_name = resume.get('name', 'Unknown Candidate')
            resume_content = resume.get('content', '')
            
            # Extract matching keywords between the resume and job posting
            matched_keywords = extract_matching_keywords(resume_content, job_keywords)
            
            # Criteria: A resume is considered a match if at least 50% of the job's keywords are found
            if len(matched_keywords) >= len(job_keywords) / 2:
                job_matches[job_title].append({
                    'candidate_name': candidate_name,
                    'matched_keywords': matched_keywords
                })
    
    # Format and return the result
    return {job: [{'name': match['candidate_name'], 'keywords': match['matched_keywords']} 
                  for match in matches] 
            for job, matches in job_matches.items()}

# Example usage
if __name__ == "__main__":
    resumes = [
        {'name': 'Alice Johnson', 'content': 'Experienced software engineer with expertise in Python, Django, and REST APIs.'},
        {'name': 'Bob Smith', 'content': 'Data scientist skilled in Python, machine learning, and data visualization.'},
        {'name': 'Carol Baker', 'content': 'Frontend developer with experience in React, JavaScript, and UI/UX design.'}
    ]
    
    job_postings = [
        {'title': 'Python Developer', 
         'description': 'Looking for a Python developer with experience in Django and REST APIs.', 
         'keywords': ['Python', 'Django', 'REST APIs']},
        {'title': 'Frontend Engineer', 
         'description': 'Seeking a skilled JavaScript and React developer.', 
         'keywords': ['React', 'JavaScript', 'UI/UX']}
    ]
    
    matches = parse_and_match_resumes(resumes, job_postings)
    
    # Print matches in a readable format
    for job, candidates in matches.items():
        print(f"Job: {job}")
        for candidate in candidates:
            print(f"  - Candidate: {candidate['name']}, Matched Keywords: {', '.join(candidate['keywords'])}")
```
