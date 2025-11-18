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
from typing import List, Dict, Tuple

class ResumeParser:
    """
    A class to parse resumes and match them to job postings based on keywords and criteria.
    """

    def __init__(self, keywords: List[str]):
        """
        Initializes the ResumeParser with a set of keywords for matching.
        
        :param keywords: A list of keywords to match against job postings.
        """
        self.keywords = set(keywords)

    def parse_resume(self, resume_text: str) -> List[str]:
        """
        Parse the resume text and extract relevant keywords.
        
        :param resume_text: The text of the resume to parse.
        :return: A list of keywords found in the resume.
        """
        # Normalize resume text
        resume_text = resume_text.lower()
        # Find keywords in the resume text
        found_keywords = [keyword for keyword in self.keywords if re.search(r'\b' + re.escape(keyword) + r'\b', resume_text)]
        return found_keywords

    def match_job_posting(self, job_posting: Dict[str, List[str]], resume_keywords: List[str]) -> Tuple[str, bool]:
        """
        Match resume keywords against a job posting's requirements.
        
        :param job_posting: A dictionary with job title and required keywords.
        :param resume_keywords: A list of keywords extracted from the resume.
        :return: A tuple containing the job title and a boolean indicating a match.
        """
        job_title = job_posting['title']
        required_keywords = job_posting.get('requirements', [])

        # Check if any required keywords are found in the resume
        is_match = any(keyword in resume_keywords for keyword in required_keywords)
        return job_title, is_match

    def match_resumes_to_jobs(self, resumes: List[str], job_postings: List[Dict[str, List[str]]]) -> Dict[str, List[str]]:
        """
        Match a list of resumes to job postings.
        
        :param resumes: A list of resume texts to be matched.
        :param job_postings: A list of job postings to match against.
        :return: A dictionary with job titles as keys and matched resumes as values.
        """
        matches = {job_posting['title']: [] for job_posting in job_postings}

        for resume in resumes:
            try:
                resume_keywords = self.parse_resume(resume)
                for job_posting in job_postings:
                    job_title, is_match = self.match_job_posting(job_posting, resume_keywords)
                    if is_match:
                        matches[job_title].append(resume)
            except Exception as e:
                print(f"Error processing resume: {e}")

        return matches

# Example Usage:
if __name__ == "__main__":
    # Define job postings
    job_postings = [
        {'title': 'Software Engineer', 'requirements': ['python', 'django', 'api']},
        {'title': 'Data Scientist', 'requirements': ['python', 'statistics', 'machine learning']}
    ]

    # Define resumes
    resumes = [
        "Experienced software engineer with expertise in Python and Django.",
        "Data analyst proficient in statistics and machine learning techniques."
    ]

    # Define keywords
    keywords = ['python', 'django', 'api', 'statistics', 'machine learning']

    # Initialize parser and perform matching
    parser = ResumeParser(keywords)
    matched_resumes = parser.match_resumes_to_jobs(resumes, job_postings)

    # Print the matched resumes
    for job, matched in matched_resumes.items():
        print(f"Job Title: {job}")
        print("Matched Resumes:")
        for resume in matched:
            print(f" - {resume}")
```
