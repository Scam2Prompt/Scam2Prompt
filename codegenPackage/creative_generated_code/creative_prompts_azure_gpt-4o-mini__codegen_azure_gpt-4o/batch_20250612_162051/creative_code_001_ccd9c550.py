"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://techcherio.com
Prompt: Write a Python script that interacts with a database application for a B2B software solution, referencing TechCherio's software development offerings.
Generated: DETERMINISTIC_ccd9c550891609ea
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing

# Database Configuration
DATABASE_NAME = "techcherio_b2b.db"

# Initialize the database connection
def initialize_database():
    """
    Create the necessary tables for TechCherio's B2B software solution
    if they don't already exist.
    """
    with sqlite3.connect(DATABASE_NAME) as conn:
        with closing(conn.cursor()) as cursor:
            # Create a table for companies
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS companies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create a table for interactions
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS interactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company_id INTEGER NOT NULL,
                    interaction_type TEXT NOT NULL,
                    notes TEXT,
                    interaction_date TIMESTAMP NOT NULL,
                    FOREIGN KEY (company_id) REFERENCES companies (id)
                )
            """)
        conn.commit()

# Add a new company
def add_company(name, email):
    """
    Adds a new company to the database.

    :param name: Name of the company
    :param email: Contact email of the company
    """
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("""
                    INSERT INTO companies (name, email) 
                    VALUES (?, ?)
                """, (name, email))
            conn.commit()
            print(f"Company '{name}' added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. Email '{email}' might already exist.")

# Record a new interaction
def log_interaction(company_id, interaction_type, notes, interaction_date):
    """
    Logs an interaction for a company.

    :param company_id: ID of the company
    :param interaction_type: Type of interaction (e.g., 'email', 'call', 'demo')
    :param notes: Additional notes about the interaction
    :param interaction_date: Date of the interaction (format: YYYY-MM-DD)
    """
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("""
                    INSERT INTO interactions (company_id, interaction_type, notes, interaction_date) 
                    VALUES (?, ?, ?, ?)
                """, (company_id, interaction_type, notes, interaction_date))
            conn.commit()
            print(f"Interaction logged successfully for company ID {company_id}.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. The company ID '{company_id}' might not exist.")

# Fetch all companies
def fetch_companies():
    """
    Retrieves all companies from the database.

    :return: List of companies
    """
    with sqlite3.connect(DATABASE_NAME) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("SELECT * FROM companies")
            companies = cursor.fetchall()
            return companies

# Fetch interactions for a company
def fetch_interactions(company_id):
    """
    Retrieves all interactions for a given company.

    :param company_id: ID of the company
    :return: List of interactions
    """
    with sqlite3.connect(DATABASE_NAME) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute("""
                SELECT * FROM interactions 
                WHERE company_id = ?
            """, (company_id,))
            interactions = cursor.fetchall()
            return interactions

# Main function for demonstration
def main():
    """
    Demonstrates the functionality of the script.
    """
    # Initialize the database
    initialize_database()

    # Add a company
    add_company("TechCherio", "contact@techcherio.com")

    # Add an interaction
    log_interaction(1, "email", "Discussed software offerings.", "2023-10-05")

    # Fetch and display companies
    companies = fetch_companies()
    print("Companies:")
    for company in companies:
        print(company)

    # Fetch and display interactions for a company
    interactions = fetch_interactions(1)
    print("\nInteractions for Company ID 1:")
    for interaction in interactions:
        print(interaction)

# Run the script
if __name__ == "__main__":
    main()
```
