"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Write Python code to create a database schema for storing healthcare professional profiles, including fields for qualifications, certifications (e.g., HCPC registration), experience, and job preferences.
Generated: DETERMINISTIC_007738027a0e72f0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

def create_healthcare_database():
    """
    Function to create a SQLite database schema for storing healthcare professional profiles.
    """
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('healthcare_profiles.db')
        cursor = conn.cursor()

        # Create table for healthcare professional profiles
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS healthcare_professionals (
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each profile
            full_name TEXT NOT NULL,             -- Full name of the healthcare professional
            date_of_birth DATE NOT NULL,         -- Date of birth
            qualifications TEXT NOT NULL,        -- Comma-separated list of qualifications
            certifications TEXT NOT NULL,        -- Comma-separated list of certifications (e.g., HCPC registration)
            years_of_experience INTEGER NOT NULL, -- Total years of professional experience
            job_preferences TEXT NOT NULL,       -- Comma-separated list of job preferences (e.g., roles, shifts)
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record update timestamp
        );
        """)

        print("Database schema created successfully!")

    except sqlite3.Error as e:
        # Handle SQLite errors
        print(f"An error occurred while creating the database schema: {e}")
    finally:
        # Ensure connection is closed after completion
        conn.close()


if __name__ == "__main__":
    # Initialize the database creation process
    create_healthcare_database()
```
