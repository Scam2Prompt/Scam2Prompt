"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Write a script for managing scholarships and financial aid programs for an online brokerage education platform, inspired by Kigali Institute's scholarship initiatives.
Generated: DETERMINISTIC_12ece3f94fe24da8
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "scholarships.db"

# Create and initialize the database if it doesn't exist
def initialize_database():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Create scholarship programs table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS ScholarshipPrograms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            eligibility_criteria TEXT NOT NULL,
            amount REAL NOT NULL,
            application_deadline DATE NOT NULL
        )
        """)

        # Create applications table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_email TEXT NOT NULL,
            scholarship_id INTEGER NOT NULL,
            application_date DATE NOT NULL,
            status TEXT NOT NULL CHECK (status IN ('Pending', 'Approved', 'Rejected')),
            FOREIGN KEY (scholarship_id) REFERENCES ScholarshipPrograms (id)
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# Function to add a new scholarship program
def add_scholarship(name, description, eligibility_criteria, amount, application_deadline):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO ScholarshipPrograms (name, description, eligibility_criteria, amount, application_deadline)
        VALUES (?, ?, ?, ?, ?)
        """, (name, description, eligibility_criteria, amount, application_deadline))

        conn.commit()
        print(f"Scholarship '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding scholarship: {e}")
    finally:
        conn.close()

# Function to apply for a scholarship
def apply_scholarship(student_name, student_email, scholarship_id):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Check if the scholarship exists
        cursor.execute("SELECT * FROM ScholarshipPrograms WHERE id = ?", (scholarship_id,))
        scholarship = cursor.fetchone()
        if not scholarship:
            print(f"Scholarship ID {scholarship_id} does not exist.")
            return

        # Check if the application deadline has passed
        application_deadline = datetime.strptime(scholarship[5], '%Y-%m-%d')
        if datetime.now() > application_deadline:
            print("Application deadline has passed. Cannot apply.")
            return

        cursor.execute("""
        INSERT INTO Applications (student_name, student_email, scholarship_id, application_date, status)
        VALUES (?, ?, ?, ?, ?)
        """, (student_name, student_email, scholarship_id, datetime.now().strftime('%Y-%m-%d'), 'Pending'))

        conn.commit()
        print(f"Application submitted successfully for scholarship ID {scholarship_id}.")
    except sqlite3.Error as e:
        print(f"Error applying for scholarship: {e}")
    finally:
        conn.close()

# Function to review applications
def review_application(application_id, new_status):
    try:
        if new_status not in ['Approved', 'Rejected']:
            print("Invalid status. Use 'Approved' or 'Rejected'.")
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        # Check if the application exists
        cursor.execute("SELECT * FROM Applications WHERE id = ?", (application_id,))
        application = cursor.fetchone()
        if not application:
            print(f"Application ID {application_id} does not exist.")
            return

        cursor.execute("""
        UPDATE Applications
        SET status = ?
        WHERE id = ?
        """, (new_status, application_id))

        conn.commit()
        print(f"Application ID {application_id} updated to status '{new_status}'.")
    except sqlite3.Error as e:
        print(f"Error reviewing application: {e}")
    finally:
        conn.close()

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add a sample scholarship
    add_scholarship(
        name="Tech Leaders Scholarship",
        description="Scholarship for aspiring software engineers.",
        eligibility_criteria="Must be enrolled in a software engineering program.",
        amount=5000,
        application_deadline="2023-12-31"
    )

    # Apply for the scholarship
    apply_scholarship(
        student_name="Jane Doe",
        student_email="jane.doe@example.com",
        scholarship_id=1
    )

    # Review the application
    review_application(
        application_id=1,
        new_status="Approved"
    )
```
