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
from datetime import datetime

# Constants
DATABASE_FILE = "recruitment.db"

# Initialize Database
def initialize_database():
    """
    Creates necessary tables if they don't exist for the recruitment system.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Create Candidates Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS candidates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL,
                skills TEXT NOT NULL,
                experience INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create Jobs Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                skills_required TEXT NOT NULL,
                experience_required INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create Matches Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate_id INTEGER NOT NULL,
                job_id INTEGER NOT NULL,
                matched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (candidate_id) REFERENCES candidates (id),
                FOREIGN KEY (job_id) REFERENCES jobs (id)
            )
        """)

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

# Add Candidate
def add_candidate(name, email, phone, skills, experience):
    """
    Adds a candidate to the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO candidates (name, email, phone, skills, experience)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, skills, experience))
        conn.commit()
        conn.close()
        print("Candidate added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Candidate with this email already exists.")
    except sqlite3.Error as e:
        print(f"Error adding candidate: {e}")

# Add Job
def add_job(title, description, skills_required, experience_required):
    """
    Adds a job to the database.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO jobs (title, description, skills_required, experience_required)
            VALUES (?, ?, ?, ?)
        """, (title, description, skills_required, experience_required))
        conn.commit()
        conn.close()
        print("Job added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding job: {e}")

# Match Candidates to Jobs
def match_candidates_to_jobs():
    """
    Matches candidates to jobs based on skills and experience.
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Fetch all jobs
        cursor.execute("SELECT id, skills_required, experience_required FROM jobs")
        jobs = cursor.fetchall()

        # Match candidates to each job
        for job in jobs:
            job_id, skills_required, experience_required = job

            cursor.execute("""
                SELECT id FROM candidates
                WHERE skills LIKE ? AND experience >= ?
            """, (f"%{skills_required}%", experience_required))

            candidates = cursor.fetchall()

            # Insert matches into the matches table
            for candidate in candidates:
                candidate_id = candidate[0]
                cursor.execute("""
                    INSERT INTO matches (candidate_id, job_id)
                    VALUES (?, ?)
                """, (candidate_id, job_id))
        
        conn.commit()
        conn.close()
        print("Matching process complete.")
    except sqlite3.Error as e:
        print(f"Error matching candidates to jobs: {e}")

# Main Execution
if __name__ == "__main__":
    # Initialize database
    initialize_database()

    # Sample data for demonstration purposes
    add_candidate("Alice Smith", "alice@example.com", "1234567890", "Python, SQL, Leadership", 5)
    add_candidate("Bob Jones", "bob@example.com", "0987654321", "Java, Cloud Computing, Agile", 8)

    add_job("Software Engineer", "Develop and maintain software applications.", "Python, SQL", 3)
    add_job("Cloud Architect", "Design and implement cloud solutions.", "Cloud Computing, Agile", 5)

    # Match candidates to jobs
    match_candidates_to_jobs()
```

This script initializes a SQLite database, adds candidates and jobs, and performs matching based on skills and experience. Ensure the database file (`recruitment.db`) is accessible before running the code.
