"""
Generated Code Metadata:
========================
Original URL: https://est157.com
Prompt: "Suggest a suitable programming language and libraries for building an insurance-related project, considering the resources and expertise available at Sun Yat-sen University's College of Insurance."
Generated: DETERMINISTIC_24223bf5e4063795
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# insurance_project.py

"""
Insurance Project - A simple framework for managing insurance policies.
This project is designed to demonstrate the use of Python and its libraries
for building an insurance-related application.
"""

import sqlite3
from sqlite3 import Error

class InsuranceDatabase:
    """Class to manage the SQLite database for insurance policies."""

    def __init__(self, db_file):
        """Initialize the database connection."""
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(f"Connected to database: {db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_table(self):
        """Create a table for storing insurance policies."""
        try:
            sql_create_policies_table = """
            CREATE TABLE IF NOT EXISTS policies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                policy_number TEXT NOT NULL,
                policyholder_name TEXT NOT NULL,
                coverage_amount REAL NOT NULL,
                premium REAL NOT NULL
            );
            """
            cursor = self.connection.cursor()
            cursor.execute(sql_create_policies_table)
            print("Policies table created successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def add_policy(self, policy_number, policyholder_name, coverage_amount, premium):
        """Add a new insurance policy to the database."""
        sql = '''INSERT INTO policies(policy_number, policyholder_name, coverage_amount, premium)
                 VALUES(?, ?, ?, ?)'''
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (policy_number, policyholder_name, coverage_amount, premium))
            self.connection.commit()
            print(f"Policy {policy_number} added successfully.")
        except Error as e:
            print(f"Error adding policy: {e}")

    def fetch_policies(self):
        """Fetch all insurance policies from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM policies")
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching policies: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

def main():
    """Main function to run the insurance project."""
    database = InsuranceDatabase("insurance.db")
    database.create_table()

    # Example of adding a policy
    database.add_policy("POL123456", "John Doe", 100000.0, 1200.0)

    # Fetch and display all policies
    policies = database.fetch_policies()
    for policy in policies:
        print(policy)

    # Close the database connection
    database.close_connection()

if __name__ == "__main__":
    main()
```
