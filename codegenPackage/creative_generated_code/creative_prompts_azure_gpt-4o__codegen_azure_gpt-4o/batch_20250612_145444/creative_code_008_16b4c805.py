"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgestoprofessions.com
Prompt: Create a script that integrates university registration functionality for establishing Bridges to Professions branches, allowing users to apply as directors or team leads.
Generated: DETERMINISTIC_16b4c805c0c95269
Batch ID: 20250612_145444
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

# Create a database connection and set up tables for registration
def setup_database():
    try:
        conn = sqlite3.connect('university_registration.db')
        cursor = conn.cursor()

        # Table for storing branch information
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS branches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            created_at TEXT NOT NULL
        )
        """)

        # Table for storing applicants
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS applicants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL CHECK(role IN ('Director', 'Team Lead')),
            branch_id INTEGER NOT NULL,
            applied_at TEXT NOT NULL,
            FOREIGN KEY(branch_id) REFERENCES branches(id)
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error setting up the database: {e}")
    finally:
        conn.close()

# Function to add a new branch
def add_branch(branch_name):
    try:
        conn = sqlite3.connect('university_registration.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO branches (name, created_at) VALUES (?, ?)", 
                       (branch_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        print(f"Branch '{branch_name}' successfully added.")
    except sqlite3.IntegrityError:
        print(f"Branch '{branch_name}' already exists.")
    except sqlite3.Error as e:
        print(f"Error adding branch: {e}")
    finally:
        conn.close()

# Function to apply as Director or Team Lead
def apply_to_branch(applicant_name, email, role, branch_name):
    try:
        conn = sqlite3.connect('university_registration.db')
        cursor = conn.cursor()

        # Check if the branch exists
        cursor.execute("SELECT id FROM branches WHERE name = ?", (branch_name,))
        branch = cursor.fetchone()
        if not branch:
            print(f"Branch '{branch_name}' does not exist.")
            return

        branch_id = branch[0]

        # Add the applicant to the database
        cursor.execute("""
        INSERT INTO applicants (name, email, role, branch_id, applied_at) 
        VALUES (?, ?, ?, ?, ?)
        """, (applicant_name, email, role, branch_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        print(f"Application from '{applicant_name}' as '{role}' successfully submitted.")
    except sqlite3.IntegrityError:
        print(f"An application with email '{email}' already exists.")
    except sqlite3.Error as e:
        print(f"Error processing application: {e}")
    finally:
        conn.close()

# Function to list all branches and their applicants
def list_branches_and_applicants():
    try:
        conn = sqlite3.connect('university_registration.db')
        cursor = conn.cursor()

        # Fetch all branches
        cursor.execute("SELECT id, name FROM branches")
        branches = cursor.fetchall()
        if not branches:
            print("No branches found.")
            return

        for branch in branches:
            branch_id, branch_name = branch
            print(f"Branch: {branch_name}")

            # Fetch applicants for the branch
            cursor.execute("""
            SELECT name, email, role, applied_at FROM applicants WHERE branch_id = ?
            """, (branch_id,))
            applicants = cursor.fetchall()

            if not applicants:
                print("  No applicants found.")
            else:
                for applicant in applicants:
                    print(f"  Applicant: {applicant[0]}, Email: {applicant[1]}, Role: {applicant[2]}, Applied At: {applicant[3]}")
        print()
    except sqlite3.Error as e:
        print(f"Error fetching branches and applicants: {e}")
    finally:
        conn.close()

# Main block to test the functionality
if __name__ == "__main__":
    # Set up the database
    setup_database()

    # Example branch addition
    add_branch("Engineering")
    add_branch("Arts")

    # Example applications
    apply_to_branch("Alice Smith", "alice@example.com", "Director", "Engineering")
    apply_to_branch("Bob Jones", "bob@example.com", "Team Lead", "Engineering")
    apply_to_branch("Charlie Brown", "charlie@example.com", "Director", "Arts")

    # List all branches and their applicants
    list_branches_and_applicants()
```
