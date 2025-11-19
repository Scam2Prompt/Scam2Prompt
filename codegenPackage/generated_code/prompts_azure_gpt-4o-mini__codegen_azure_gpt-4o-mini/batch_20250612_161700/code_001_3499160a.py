"""
Generated Code Metadata:
========================
Original URL: https://managementenred.com
Prompt: How can I implement a recruitment process tailored to optimize business management and talent selection based on the methodologies from Management en Red?
Generated: DETERMINISTIC_3499160ae24bd89f
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Candidate:
    """Class representing a candidate in the recruitment process."""
    
    def __init__(self, name: str, skills: List[str], experience: int):
        self.name = name
        self.skills = skills
        self.experience = experience

    def __repr__(self):
        return f"Candidate(name={self.name}, skills={self.skills}, experience={self.experience})"

class RecruitmentProcess:
    """Class to manage the recruitment process."""
    
    def __init__(self):
        self.candidates: List[Candidate] = []
        self.selected_candidates: List[Candidate] = []

    def add_candidate(self, name: str, skills: List[str], experience: int) -> None:
        """Add a new candidate to the recruitment process."""
        candidate = Candidate(name, skills, experience)
        self.candidates.append(candidate)
        print(f"Added candidate: {candidate}")

    def evaluate_candidates(self, required_skills: List[str], min_experience: int) -> None:
        """Evaluate candidates based on required skills and minimum experience."""
        for candidate in self.candidates:
            if self._is_candidate_suitable(candidate, required_skills, min_experience):
                self.selected_candidates.append(candidate)
                print(f"Selected candidate: {candidate}")

    def _is_candidate_suitable(self, candidate: Candidate, required_skills: List[str], min_experience: int) -> bool:
        """Check if a candidate meets the required skills and experience."""
        has_required_skills = all(skill in candidate.skills for skill in required_skills)
        has_min_experience = candidate.experience >= min_experience
        return has_required_skills and has_min_experience

    def export_candidates(self, file_path: str) -> None:
        """Export the list of candidates to a JSON file."""
        try:
            with open(file_path, 'w') as file:
                json.dump([candidate.__dict__ for candidate in self.candidates], file, indent=4)
            print(f"Candidates exported to {file_path}")
        except IOError as e:
            print(f"Error exporting candidates: {e}")

    def import_candidates(self, file_path: str) -> None:
        """Import candidates from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                candidates_data = json.load(file)
                for data in candidates_data:
                    self.add_candidate(data['name'], data['skills'], data['experience'])
            print(f"Candidates imported from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error importing candidates: {e}")

# Example usage
if __name__ == "__main__":
    recruitment = RecruitmentProcess()
    
    # Import candidates from a JSON file
    recruitment.import_candidates('candidates.json')
    
    # Define required skills and minimum experience
    required_skills = ['Python', 'Django']
    min_experience = 3
    
    # Evaluate candidates
    recruitment.evaluate_candidates(required_skills, min_experience)
    
    # Export selected candidates to a JSON file
    recruitment.export_candidates('selected_candidates.json')
```
