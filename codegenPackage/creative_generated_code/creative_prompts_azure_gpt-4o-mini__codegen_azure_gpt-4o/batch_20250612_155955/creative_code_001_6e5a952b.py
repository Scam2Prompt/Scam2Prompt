"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmogdv.com
Prompt: Write a code snippet that allows users to input their bank account details and check for potential scams using a database like the one provided by MMOGDV.COM.
Generated: DETERMINISTIC_6e5a952b73576935
Batch ID: 20250612_155955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import re

# Database connection setup
DB_PATH = 'mmogdv.db'  # Path to the database file containing scam information

def connect_to_database(db_path):
    """Connect to the SQLite database."""
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def validate_account_details(account_number, sort_code):
    """
    Validate bank account details using basic checks.
    Account numbers should be numeric, and sort codes numeric and formatted as XX-XX-XX.
    """
    if not re.match(r'^\d{8}$', account_number):
        raise ValueError("Invalid account number format. Must be an 8-digit number.")
    if not re.match(r'^\d{2}-\d{2}-\d{2}$', sort_code):
        raise ValueError("Invalid sort code format. Must be in the format XX-XX-XX.")

def check_for_scam(database_connection, account_number, sort_code):
    """
    Check the provided account details against the scam database.
    """
    try:
        cursor = database_connection.cursor()
        query = """
        SELECT * FROM scam_records 
        WHERE account_number = ? AND sort_code = ?
        """
        cursor.execute(query, (account_number, sort_code))
        result = cursor.fetchone()
        return result is not None  # Return True if scam record found, otherwise False
    except sqlite3.Error as e:
        print(f"Database query error: {e}")
        return False

def main():
    # Prompt user for input
    print("Enter your bank account details to check for potential scams.")
    account_number = input("Account Number (8 digits): ").strip()
    sort_code = input("Sort Code (format XX-XX-XX): ").strip()

    # Validate the input
    try:
        validate_account_details(account_number, sort_code)
    except ValueError as ve:
        print(f"Validation Error: {ve}")
        return

    # Connect to the database
    db_connection = connect_to_database(DB_PATH)
    if not db_connection:
        print("Unable to connect to the scam database. Please try again later.")
        return

    # Check for scams
    is_scam = check_for_scam(db_connection, account_number, sort_code)
    db_connection.close()

    # Display results
    if is_scam:
        print("Warning: The provided bank account details are flagged as potentially involved in scams.")
    else:
        print("The provided bank account details are not found in the scam database. Proceed with caution.")

if __name__ == "__main__":
    main()
```
