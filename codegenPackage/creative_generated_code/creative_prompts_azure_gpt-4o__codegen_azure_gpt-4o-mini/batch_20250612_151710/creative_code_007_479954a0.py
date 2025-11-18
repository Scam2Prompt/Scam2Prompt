"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munshihr.com
Prompt: Develop a system for professional recruitment and headhunting, inspired by Munshi HR Solutions' expertise in finding top-tier talent.
Generated: DETERMINISTIC_479954a0ab005c18
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# recruitment_system.py

import sqlite3
from typing import List, Dict, Optional


class RecruitmentDatabase:
    """Class to handle database operations for the recruitment system."""
    
    def __init__(self, db_name: str):
        """Initialize the database connection."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for storing candidates and job postings."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS candidates (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    skills TEXT NOT NULL,
                    experience INTEGER NOT NULL
                )
            ''')
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS job_postings (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    required_skills TEXT NOT NULL,
                    experience_required INTEGER NOT NULL
                )
            ''')

    def add_candidate(self, name: str, email: str, skills: str, experience: int) -> int:
        """Add a new candidate to the database."""
        with self.connection:
            cursor = self.connection.execute('''
                INSERT INTO candidates (name, email, skills, experience) 
                VALUES (?, ?, ?, ?)''', (name, email, skills, experience))
            return cursor.lastrowid

    def add_job_posting(self, title: str, description: str, required_skills: str, experience_required: int) -> int:
        """Add a new job posting to the database."""
        with self.connection:
            cursor = self.connection.execute('''
                INSERT INTO job_postings (title, description, required_skills, experience_required) 
                VALUES (?, ?, ?, ?)''', (title, description, required_skills, experience_required))
            return cursor.lastrowid

    def find_candidates_for_job(self, job_id: int) -> List[Dict[str, str]]:
        """Find candidates that match a given job posting."""
        job = self.get_job_posting(job_id)
        if not job:
            return []

        required_skills = set(job['required_skills'].split(','))
        
        with self.connection:
            candidates = self.connection.execute('''
                SELECT * FROM candidates
            ''').fetchall()

        matching_candidates = [
            {
                'id': candidate[0],
                'name': candidate[1],
                'email': candidate[2],
                'skills': candidate[3],
                'experience': candidate[4]
            }
            for candidate in candidates
            if required_skills.issubset(set(candidate[3].split(','))) and candidate[4] >= job['experience_required']
        ]

        return matching_candidates

    def get_job_posting(self, job_id: int) -> Optional[Dict[str, str]]:
        """Retrieve a job posting from the database."""
        job = self.connection.execute('''
            SELECT * FROM job_postings WHERE id = ?
        ''', (job_id,)).fetchone()

        if job:
            return {
                'id': job[0],
                'title': job[1],
                'description': job[2],
                'required_skills': job[3],
                'experience_required': job[4]
            }
        return None

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()


# Example usage of the RecruitmentDatabase class
if __name__ == "__main__":
    # Initialize the recruitment database
    db = RecruitmentDatabase('recruitment.db')

    # Add a candidate
    try:
        candidate_id = db.add_candidate('Alice Smith', 'alice@example.com', 'Python, SQL, Communication', 5)
        print(f'Added candidate with ID: {candidate_id}')
    except sqlite3.IntegrityError as e:
        print(f'Error adding candidate: {e}')

    # Add a job posting
    try:
        job_id = db.add_job_posting('Software Engineer', 'Develop software applications.', 'Python, SQL', 3)
        print(f'Added job posting with ID: {job_id}')
    except sqlite3.IntegrityError as e:
        print(f'Error adding job posting: {e}')

    # Find candidates for the job posting
    matching_candidates = db.find_candidates_for_job(job_id)
    print(f'Matching candidates for job ID {job_id}: {matching_candidates}')

    # Close the database connection
    db.close()
```
