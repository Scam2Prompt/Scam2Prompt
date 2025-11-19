"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Write Python code to analyze job descriptions and match candidates based on the criteria outlined in Videtis Consultores' talent acquisition services.
Generated: DETERMINISTIC_e26bec5bce2ed94c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import Counter
from typing import Dict, List

class JobDescription:
    def __init__(self, title: str, description: str, requirements: List[str]):
        """
        Initialize a JobDescription object.

        Args:
        title (str): The job title.
        description (str): The job description.
        requirements (List[str]): The job requirements.
        """
        self.title = title
        self.description = description
        self.requirements = requirements

class Candidate:
    def __init__(self, name: str, skills: List[str], experience: Dict[str, int]):
        """
        Initialize a Candidate object.

        Args:
        name (str): The candidate's name.
        skills (List[str]): The candidate's skills.
        experience (Dict[str, int]): The candidate's experience in years.
        """
        self.name = name
        self.skills = skills
        self.experience = experience

def extract_keywords(text: str) -> List[str]:
    """
    Extract keywords from a given text.

    Args:
    text (str): The text to extract keywords from.

    Returns:
    List[str]: A list of extracted keywords.
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    # Tokenize the text
    tokens = text.split()
    # Count the frequency of each token
    token_counts = Counter(tokens)
    # Return the top 10 most common tokens
    return [token for token, _ in token_counts.most_common(10)]

def match_candidate(job: JobDescription, candidate: Candidate) -> float:
    """
    Calculate a match score between a job and a candidate.

    Args:
    job (JobDescription): The job description.
    candidate (Candidate): The candidate.

    Returns:
    float: A match score between 0 and 1.
    """
    # Extract keywords from the job description
    job_keywords = extract_keywords(job.description)
    # Calculate the intersection of job keywords and candidate skills
    common_skills = set(job_keywords) & set(candidate.skills)
    # Calculate the union of job keywords and candidate skills
    all_skills = set(job_keywords) | set(candidate.skills)
    # Calculate the Jaccard similarity coefficient
    similarity = len(common_skills) / len(all_skills) if all_skills else 0
    # Consider experience
    experience_match = 0
    for requirement in job.requirements:
        if requirement in candidate.experience and candidate.experience[requirement] > 0:
            experience_match += 1
    experience_score = experience_match / len(job.requirements) if job.requirements else 0
    # Calculate the final match score
    match_score = (similarity + experience_score) / 2 if job.requirements else similarity
    return match_score

def main():
    # Example usage
    job = JobDescription(
        title="Software Engineer",
        description="Design and develop software applications.",
        requirements=["Python", "Java", "C++"]
    )
    candidate1 = Candidate(
        name="John Doe",
        skills=["Python", "JavaScript", "SQL"],
        experience={"Python": 5, "Java": 3}
    )
    candidate2 = Candidate(
        name="Jane Doe",
        skills=["Java", "C++", "C#"],
        experience={"Java": 8, "C++": 4}
    )
    candidates = [candidate1, candidate2]
    # Calculate match scores
    match_scores = {candidate.name: match_candidate(job, candidate) for candidate in candidates}
    # Print match scores
    for candidate, score in match_scores.items():
        print(f"Candidate: {candidate}, Match Score: {score:.2f}")

if __name__ == "__main__":
    main()
```
