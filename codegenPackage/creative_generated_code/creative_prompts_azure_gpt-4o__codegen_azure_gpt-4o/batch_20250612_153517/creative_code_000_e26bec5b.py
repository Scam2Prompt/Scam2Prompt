"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Write Python code to analyze job descriptions and match candidates based on the criteria outlined in Videtis Consultores' talent acquisition services.
Generated: DETERMINISTIC_e26bec5bce2ed94c
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Dict, Union

# Define a class to handle job description analysis and candidate matching
class TalentAcquisition:
    def __init__(self):
        # Initialize the class with empty lists for job descriptions and candidates
        self.job_descriptions = []
        self.candidates = []

    def add_job_description(self, description: str, criteria: Dict[str, Union[str, List[str]]]) -> None:
        """
        Add a job description to the system.
        
        :param description: The textual job description.
        :param criteria: A dictionary containing specific criteria for the job.
        :return: None
        """
        self.job_descriptions.append({
            "description": description,
            "criteria": criteria
        })

    def add_candidate(self, name: str, skills: List[str], experience: int, education: str) -> None:
        """
        Add a candidate to the system.
        
        :param name: Name of the candidate.
        :param skills: List of skills the candidate possesses.
        :param experience: Number of years of relevant experience.
        :param education: The educational qualification of the candidate.
        :return: None
        """
        self.candidates.append({
            "name": name,
            "skills": skills,
            "experience": experience,
            "education": education
        })

    def match_candidates(self) -> Dict[str, List[str]]:
        """
        Match candidates to job descriptions based on criteria.
        
        :return: Dictionary mapping job descriptions to lists of candidate names.
        """
        matches = {}

        # Iterate through each job description to find suitable candidates
        for job in self.job_descriptions:
            job_criteria = job["criteria"]
            matched_candidates = []

            for candidate in self.candidates:
                # Check if the candidate satisfies job criteria
                if (
                    all(skill.lower() in map(str.lower, candidate["skills"]) for skill in job_criteria.get("skills", [])) and
                    candidate["experience"] >= job_criteria.get("experience", 0) and
                    re.search(job_criteria.get("education", "").lower(), candidate["education"].lower())
                ):
                    matched_candidates.append(candidate["name"])

            # Store matches for the current job description
            matches[job["description"]] = matched_candidates

        return matches


# Example usage (this would typically be part of a separate script or application layer)
if __name__ == "__main__":
    # Instantiate the TalentAcquisition system
    talent_system = TalentAcquisition()

    # Add job descriptions
    talent_system.add_job_description(
        description="Software Engineer Role",
        criteria={
            "skills": ["Python", "Django", "REST"],
            "experience": 3,
            "education": "Bachelor's"
        }
    )
    talent_system.add_job_description(
        description="Data Scientist Role",
        criteria={
            "skills": ["Python", "Machine Learning", "SQL"],
            "experience": 2,
            "education": "Master's"
        }
    )
    
    # Add candidates
    talent_system.add_candidate(
        name="Alice",
        skills=["Python", "Django", "REST", "HTML"],
        experience=4,
        education="Bachelor's in Computer Science"
    )
    talent_system.add_candidate(
        name="Bob",
        skills=["Python", "Machine Learning", "SQL", "Pandas"],
        experience=5,
        education="Master's in Data Science"
    )
    talent_system.add_candidate(
        name="Charlie",
        skills=["Java", "Spring", "SQL"],
        experience=3,
        education="Bachelor's in Information Technology"
    )

    # Match candidates and print results
    matched_results = talent_system.match_candidates()
    for job, candidates in matched_results.items():
        print(f"Job: {job}")
        print(f"Matched Candidates: {', '.join(candidates) if candidates else 'None'}")
        print()
```
