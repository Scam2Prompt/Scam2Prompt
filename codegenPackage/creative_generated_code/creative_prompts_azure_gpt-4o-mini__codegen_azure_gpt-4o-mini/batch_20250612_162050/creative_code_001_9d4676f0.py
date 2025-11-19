"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://recruit-overseas.com
Prompt: How can I implement a recruitment process that includes triple vetting of candidates, similar to the approach used by Recruit Overseas?
Generated: DETERMINISTIC_9d4676f0ef9b75d5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class Candidate:
    def __init__(self, name: str, resume: Dict[str, Any]):
        """
        Initialize a Candidate instance.
        
        Args:
            name (str): The name of the candidate.
            resume (Dict[str, Any]): A dictionary containing the candidate's resume details.
        """
        self.name = name
        self.resume = resume
        self.vetting_scores = []
    
    def add_vetting_score(self, score: int):
        """Add a vetting score to the candidate."""
        self.vetting_scores.append(score)

    def average_score(self) -> float:
        """Calculate the average vetting score."""
        if not self.vetting_scores:
            return 0.0
        return sum(self.vetting_scores) / len(self.vetting_scores)

class RecruitmentProcess:
    def __init__(self):
        """Initialize the Recruitment Process."""
        self.candidates = []

    def add_candidate(self, candidate: Candidate):
        """Add a candidate to the recruitment process."""
        self.candidates.append(candidate)

    def vet_candidate(self, candidate: Candidate) -> int:
        """
        Simulate vetting a candidate.
        
        Returns:
            int: A random score between 1 and 100 representing the vetting outcome.
        """
        return random.randint(1, 100)

    def run_vetting(self):
        """Run the vetting process for all candidates."""
        for candidate in self.candidates:
            print(f"Vetting candidate: {candidate.name}")
            scores = []
            # Triple vetting process
            for i in range(3):
                score = self.vet_candidate(candidate)
                candidate.add_vetting_score(score)
                scores.append(score)
                print(f"  Vetting round {i + 1}: Score = {score}")

            avg_score = candidate.average_score()
            print(f"  Average score for {candidate.name}: {avg_score:.2f}")

    def get_successful_candidates(self, threshold: float = 70.0) -> List[Candidate]:
        """
        Get a list of candidates who have passed the vetting process.
        
        Args:
            threshold (float): The minimum average score required to be considered successful.
        
        Returns:
            List[Candidate]: A list of successful candidates.
        """
        successful_candidates = [
            candidate for candidate in self.candidates if candidate.average_score() >= threshold
        ]
        return successful_candidates

if __name__ == "__main__":
    # Example usage:
    recruitment = RecruitmentProcess()

    # Adding candidates
    recruitment.add_candidate(Candidate("Alice Johnson", {"experience": "5 years", "skills": ["Python", "Django"]}))
    recruitment.add_candidate(Candidate("Bob Smith", {"experience": "3 years", "skills": ["Java", "Spring"]}))
    recruitment.add_candidate(Candidate("Charlie Davis", {"experience": "8 years", "skills": ["JavaScript", "React"]}))

    # Run the vetting process
    recruitment.run_vetting()

    # Get successful candidates
    successful_candidates = recruitment.get_successful_candidates()
    print("\nSuccessful Candidates:")
    for candidate in successful_candidates:
        print(f"- {candidate.name} with average score: {candidate.average_score():.2f}")

```
