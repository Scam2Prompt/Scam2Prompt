"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Write a short algorithm for matching candidates with job openings based on their values, expectations, and personality, reflecting jobONE's matching process.
Generated: DETERMINISTIC_b35ca146b3cf9c17
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class PersonalityType(str, Enum):
    """Enum for personality types"""
    INTROVERT = "introvert"
    EXTROVERT = "extrovert"

class Job:
    """Class representing a job opening"""
    def __init__(self, id: int, values: List[str], expectations: List[str], personality: PersonalityType):
        """
        Initialize a Job object.

        Args:
        id (int): Unique job ID
        values (List[str]): List of job values
        expectations (List[str]): List of job expectations
        personality (PersonalityType): Required personality type
        """
        self.id = id
        self.values = values
        self.expectations = expectations
        self.personality = personality

class Candidate:
    """Class representing a job candidate"""
    def __init__(self, id: int, values: List[str], expectations: List[str], personality: PersonalityType):
        """
        Initialize a Candidate object.

        Args:
        id (int): Unique candidate ID
        values (List[str]): List of candidate values
        expectations (List[str]): List of candidate expectations
        personality (PersonalityType): Candidate personality type
        """
        self.id = id
        self.values = values
        self.expectations = expectations
        self.personality = personality

def match_candidate_with_job(candidate: Candidate, job: Job) -> Dict[str, bool]:
    """
    Match a candidate with a job based on their values, expectations, and personality.

    Args:
    candidate (Candidate): Candidate object
    job (Job): Job object

    Returns:
    Dict[str, bool]: Dictionary containing matching results
    """
    # Check if candidate values align with job values
    values_match = set(candidate.values).issubset(set(job.values))
    
    # Check if candidate expectations align with job expectations
    expectations_match = set(candidate.expectations).issubset(set(job.expectations))
    
    # Check if candidate personality matches job personality
    personality_match = candidate.personality == job.personality
    
    return {
        "values_match": values_match,
        "expectations_match": expectations_match,
        "personality_match": personality_match,
        "overall_match": values_match and expectations_match and personality_match
    }

def find_best_match(candidates: List[Candidate], jobs: List[Job]) -> Dict[int, int]:
    """
    Find the best match for each candidate.

    Args:
    candidates (List[Candidate]): List of Candidate objects
    jobs (List[Job]): List of Job objects

    Returns:
    Dict[int, int]: Dictionary containing candidate-job matches
    """
    matches = {}
    for candidate in candidates:
        best_match = None
        best_match_score = 0
        for job in jobs:
            match_result = match_candidate_with_job(candidate, job)
            match_score = sum(1 for value in match_result.values() if value)
            if match_score > best_match_score:
                best_match = job.id
                best_match_score = match_score
        matches[candidate.id] = best_match
    return matches

# Example usage
if __name__ == "__main__":
    # Create jobs
    job1 = Job(1, ["teamwork", "innovation"], ["growth", "learning"], PersonalityType.EXTROVERT)
    job2 = Job(2, ["autonomy", "creativity"], ["stability", "security"], PersonalityType.INTROVERT)

    # Create candidates
    candidate1 = Candidate(1, ["teamwork", "innovation", "growth"], ["learning", "autonomy"], PersonalityType.EXTROVERT)
    candidate2 = Candidate(2, ["stability", "security", "creativity"], ["growth", "learning"], PersonalityType.INTROVERT)

    # Find best matches
    jobs = [job1, job2]
    candidates = [candidate1, candidate2]
    best_matches = find_best_match(candidates, jobs)

    # Print results
    for candidate_id, job_id in best_matches.items():
        print(f"Candidate {candidate_id} best match: Job {job_id}")
```
