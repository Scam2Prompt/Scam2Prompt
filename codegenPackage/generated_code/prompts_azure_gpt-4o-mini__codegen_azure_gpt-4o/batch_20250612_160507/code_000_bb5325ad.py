"""
Generated Code Metadata:
========================
Original URL: https://eximiousglobal.com
Prompt: Generate a code snippet for a recruitment process outsourcing (RPO) system that automates candidate sourcing and onboarding, incorporating data-driven decision-making.
Generated: DETERMINISTIC_bb5325ad04dedd08
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Candidate:
    """
    Represents a candidate in the recruitment process.
    """
    def __init__(self, name: str, email: str, skills: List[str], experience: int):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience
        self.status = "Sourcing"  # Initial status

    def to_dict(self) -> Dict:
        """
        Converts the candidate object to a dictionary for serialization.
        """
        return {
            "name": self.name,
            "email": self.email,
            "skills": self.skills,
            "experience": self.experience,
            "status": self.status
        }


class RPOSystem:
    """
    Recruitment Process Outsourcing (RPO) system for automating candidate sourcing and onboarding.
    """
    def __init__(self):
        self.candidates = []

    def add_candidate(self, candidate: Candidate):
        """
        Adds a candidate to the system.
        """
        self.candidates.append(candidate)
        logging.info(f"Candidate {candidate.name} added to the system.")

    def filter_candidates(self, required_skills: List[str], min_experience: int) -> List[Candidate]:
        """
        Filters candidates based on required skills and minimum experience.
        """
        filtered = [
            candidate for candidate in self.candidates
            if all(skill in candidate.skills for skill in required_skills) and candidate.experience >= min_experience
        ]
        logging.info(f"{len(filtered)} candidates matched the criteria.")
        return filtered

    def update_status(self, candidate_email: str, new_status: str):
        """
        Updates the status of a candidate.
        """
        for candidate in self.candidates:
            if candidate.email == candidate_email:
                candidate.status = new_status
                logging.info(f"Updated status for {candidate.name} to {new_status}.")
                return
        logging.warning(f"No candidate found with email {candidate_email}.")

    def export_candidates(self, file_path: str):
        """
        Exports candidate data to a JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([candidate.to_dict() for candidate in self.candidates], file, indent=4)
            logging.info(f"Candidate data exported to {file_path}.")
        except Exception as e:
            logging.error(f"Failed to export candidate data: {e}")

    def onboard_candidate(self, candidate_email: str):
        """
        Onboards a candidate by updating their status to 'Onboarded'.
        """
        self.update_status(candidate_email, "Onboarded")


# Example usage
if __name__ == "__main__":
    # Initialize the RPO system
    rpo_system = RPOSystem()

    # Add candidates
    rpo_system.add_candidate(Candidate("Alice Johnson", "alice@example.com", ["Python", "Django"], 5))
    rpo_system.add_candidate(Candidate("Bob Smith", "bob@example.com", ["Java", "Spring"], 3))
    rpo_system.add_candidate(Candidate("Charlie Brown", "charlie@example.com", ["Python", "Flask"], 2))

    # Filter candidates based on criteria
    required_skills = ["Python"]
    min_experience = 3
    filtered_candidates = rpo_system.filter_candidates(required_skills, min_experience)

    # Onboard a candidate
    if filtered_candidates:
        rpo_system.onboard_candidate(filtered_candidates[0].email)

    # Export candidate data to a JSON file
    rpo_system.export_candidates("candidates.json")
```
