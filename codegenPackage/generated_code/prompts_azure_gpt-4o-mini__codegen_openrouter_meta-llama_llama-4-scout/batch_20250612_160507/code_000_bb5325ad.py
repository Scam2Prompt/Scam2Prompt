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
# rpo_system.py

import logging
from typing import Dict, List
from enum import Enum
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CandidateStatus(str, Enum):
    """Candidate status enumeration"""
    NEW = "new"
    INTERVIEW_SCHEDULED = "interview_scheduled"
    OFFER_EXTENDED = "offer_extended"
    HIRED = "hired"
    REJECTED = "rejected"

class Candidate:
    """Candidate data model"""
    def __init__(self, id: int, name: str, email: str, phone: str, skills: List[str]):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.skills = skills
        self.status = CandidateStatus.NEW

    def __repr__(self):
        return f"Candidate(id={self.id}, name='{self.name}', email='{self.email}', phone='{self.phone}', skills={self.skills}, status='{self.status.value}')"

class JobPosting:
    """Job posting data model"""
    def __init__(self, id: int, title: str, description: str, required_skills: List[str]):
        self.id = id
        self.title = title
        self.description = description
        self.required_skills = required_skills
        self.candidates: List[Candidate] = []

    def add_candidate(self, candidate: Candidate):
        self.candidates.append(candidate)

    def __repr__(self):
        return f"JobPosting(id={self.id}, title='{self.title}', description='{self.description}', required_skills={self.required_skills})"

class RPOsystem:
    """Recruitment process outsourcing system"""
    def __init__(self):
        self.job_postings: Dict[int, JobPosting] = {}
        self.candidates: Dict[int, Candidate] = {}

    def create_job_posting(self, id: int, title: str, description: str, required_skills: List[str]):
        """Create a new job posting"""
        if id in self.job_postings:
            logging.error(f"Job posting with ID {id} already exists.")
            raise ValueError(f"Job posting with ID {id} already exists.")
        
        job_posting = JobPosting(id, title, description, required_skills)
        self.job_postings[id] = job_posting
        logging.info(f"Job posting with ID {id} created.")

    def create_candidate(self, id: int, name: str, email: str, phone: str, skills: List[str]):
        """Create a new candidate"""
        if id in self.candidates:
            logging.error(f"Candidate with ID {id} already exists.")
            raise ValueError(f"Candidate with ID {id} already exists.")
        
        candidate = Candidate(id, name, email, phone, skills)
        self.candidates[id] = candidate
        logging.info(f"Candidate with ID {id} created.")

    def assign_candidate_to_job(self, job_id: int, candidate_id: int):
        """Assign a candidate to a job posting"""
        if job_id not in self.job_postings:
            logging.error(f"Job posting with ID {job_id} does not exist.")
            raise ValueError(f"Job posting with ID {job_id} does not exist.")
        
        if candidate_id not in self.candidates:
            logging.error(f"Candidate with ID {candidate_id} does not exist.")
            raise ValueError(f"Candidate with ID {candidate_id} does not exist.")
        
        job_posting = self.job_postings[job_id]
        candidate = self.candidates[candidate_id]
        job_posting.add_candidate(candidate)
        logging.info(f"Candidate with ID {candidate_id} assigned to job posting with ID {job_id}.")

    def update_candidate_status(self, candidate_id: int, status: CandidateStatus):
        """Update the status of a candidate"""
        if candidate_id not in self.candidates:
            logging.error(f"Candidate with ID {candidate_id} does not exist.")
            raise ValueError(f"Candidate with ID {candidate_id} does not exist.")
        
        candidate = self.candidates[candidate_id]
        candidate.status = status
        logging.info(f"Candidate with ID {candidate_id} status updated to {status.value}.")

    def get_job_posting_candidates(self, job_id: int):
        """Get the candidates for a job posting"""
        if job_id not in self.job_postings:
            logging.error(f"Job posting with ID {job_id} does not exist.")
            raise ValueError(f"Job posting with ID {job_id} does not exist.")
        
        job_posting = self.job_postings[job_id]
        return job_posting.candidates

def main():
    rpo_system = RPOsystem()

    # Create job postings
    rpo_system.create_job_posting(1, "Software Engineer", "Design and develop software applications.", ["Python", "Java", "C++"])
    rpo_system.create_job_posting(2, "Data Scientist", "Analyze and interpret complex data sets.", ["Python", "R", "SQL"])

    # Create candidates
    rpo_system.create_candidate(1, "John Doe", "john.doe@example.com", "123-456-7890", ["Python", "Java", "C++"])
    rpo_system.create_candidate(2, "Jane Smith", "jane.smith@example.com", "987-654-3210", ["Python", "R", "SQL"])

    # Assign candidates to job postings
    rpo_system.assign_candidate_to_job(1, 1)
    rpo_system.assign_candidate_to_job(1, 2)
    rpo_system.assign_candidate_to_job(2, 2)

    # Update candidate status
    rpo_system.update_candidate_status(1, CandidateStatus.INTERVIEW_SCHEDULED)

    # Get job posting candidates
    candidates = rpo_system.get_job_posting_candidates(1)
    for candidate in candidates:
        print(candidate)

if __name__ == "__main__":
    main()
```
