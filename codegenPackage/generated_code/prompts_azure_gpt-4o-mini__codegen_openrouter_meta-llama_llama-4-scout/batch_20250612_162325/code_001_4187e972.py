"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Write a Python function that automates the process of selecting candidates based on specific criteria, inspired by the talent selection strategies outlined on Videtis Consultores' website.
Generated: DETERMINISTIC_4187e972ac3942cd
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Candidate:
    """Represents a job candidate."""
    
    def __init__(self, name: str, age: int, skills: List[str], experience: int):
        """
        Initializes a Candidate object.

        Args:
        - name (str): The candidate's name.
        - age (int): The candidate's age.
        - skills (List[str]): The candidate's skills.
        - experience (int): The candidate's experience in years.
        """
        self.name = name
        self.age = age
        self.skills = skills
        self.experience = experience


def select_candidates(candidates: List[Candidate], required_skills: List[str], min_experience: int, max_age: int) -> List[Candidate]:
    """
    Selects candidates based on specific criteria.

    Args:
    - candidates (List[Candidate]): The list of candidates.
    - required_skills (List[str]): The required skills.
    - min_experience (int): The minimum experience in years.
    - max_age (int): The maximum age.

    Returns:
    - List[Candidate]: The list of selected candidates.
    """
    selected_candidates = []

    for candidate in candidates:
        # Check if the candidate has all the required skills
        if all(skill in candidate.skills for skill in required_skills):
            # Check if the candidate's experience and age meet the criteria
            if candidate.experience >= min_experience and candidate.age <= max_age:
                selected_candidates.append(candidate)

    return selected_candidates


def main():
    try:
        # Create candidates
        candidates = [
            Candidate("John Doe", 30, ["Python", "Java", "C++"], 5),
            Candidate("Jane Doe", 25, ["Python", "JavaScript", "SQL"], 3),
            Candidate("Bob Smith", 40, ["Java", "C++", "Python"], 10),
        ]

        # Define selection criteria
        required_skills = ["Python", "Java"]
        min_experience = 3
        max_age = 35

        # Select candidates
        selected_candidates = select_candidates(candidates, required_skills, min_experience, max_age)

        # Print selected candidates
        print("Selected Candidates:")
        for candidate in selected_candidates:
            print(f"Name: {candidate.name}, Age: {candidate.age}, Skills: {candidate.skills}, Experience: {candidate.experience} years")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
