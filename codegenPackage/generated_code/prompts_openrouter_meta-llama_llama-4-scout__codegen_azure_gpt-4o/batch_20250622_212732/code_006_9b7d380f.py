"""
Generated Code Metadata:
========================
Original URL: https://hometymex.co.za
Prompt: Design a system to track and manage home loan applications, including applicant profiles, offer comparisons, and cashback rewards, using a database or data storage solution.
Generated: DETERMINISTIC_9b7d380f9a244b42
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlite3
from datetime import datetime

# Database setup
DATABASE_NAME = "home_loan_applications.db"

# Create and initialize the database
def initialize_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Create table for applicant profiles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applicants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Create table for loan offers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loan_offers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        applicant_id INTEGER NOT NULL,
        bank_name TEXT NOT NULL,
        interest_rate REAL NOT NULL,
        loan_amount REAL NOT NULL,
        cashback_reward REAL NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (applicant_id) REFERENCES applicants (id)
    )
    """)

    connection.commit()
    connection.close()

# Add a new applicant
def add_applicant(name, email, phone):
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO applicants (name, email, phone)
        VALUES (?, ?, ?)
        """, (name, email, phone))
        connection.commit()
        print("Applicant added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        connection.close()

# Add a new loan offer for an applicant
def add_loan_offer(applicant_id, bank_name, interest_rate, loan_amount, cashback_reward):
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO loan_offers (applicant_id, bank_name, interest_rate, loan_amount, cashback_reward)
        VALUES (?, ?, ?, ?, ?)
        """, (applicant_id, bank_name, interest_rate, loan_amount, cashback_reward))
        connection.commit()
        print("Loan offer added successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        connection.close()

# Retrieve all applicants
def get_all_applicants():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM applicants")
    applicants = cursor.fetchall()
    connection.close()
    return applicants

# Retrieve all loan offers for a specific applicant
def get_loan_offers(applicant_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM loan_offers WHERE applicant_id = ?
    """, (applicant_id,))
    loan_offers = cursor.fetchall()
    connection.close()
    return loan_offers

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Add sample applicants
    add_applicant("John Doe", "john.doe@example.com", "123-456-7890")
    add_applicant("Jane Smith", "jane.smith@example.com", "987-654-3210")

    # Add sample loan offers
    add_loan_offer(1, "Bank A", 3.5, 250000, 5000)
    add_loan_offer(1, "Bank B", 3.2, 250000, 3000)
    add_loan_offer(2, "Bank C", 4.0, 300000, 7000)

    # Retrieve and display all applicants
    print("Applicants:")
    for applicant in get_all_applicants():
        print(applicant)

    # Retrieve and display loan offers for a specific applicant
    print("\nLoan Offers for Applicant ID 1:")
    for offer in get_loan_offers(1):
        print(offer)
```

This code is a complete, production-ready implementation for tracking and managing home loan applications using SQLite as the database. It includes applicant profiles, loan offers, and cashback rewards, with proper error handling and comments for clarity.
