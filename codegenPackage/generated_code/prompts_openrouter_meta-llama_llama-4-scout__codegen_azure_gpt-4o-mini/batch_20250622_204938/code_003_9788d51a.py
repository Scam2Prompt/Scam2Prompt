"""
Generated Code Metadata:
========================
Original URL: https://polymarketisillegal.com
Prompt: Create a basic email sign-up validation function using Python that checks for valid email formats before adding to a database.
Generated: DETERMINISTIC_9788d51ae9c16964
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import sqlite3

# Define a function to validate email format
def is_valid_email(email):
    """
    Validate the email format using a regular expression.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Define a function to add email to the database
def add_email_to_database(email):
    """
    Add a valid email to the SQLite database.
    
    Args:
        email (str): The email address to add.
    
    Raises:
        ValueError: If the email is not valid.
        sqlite3.Error: If there is an error with the database operation.
    """
    if not is_valid_email(email):
        raise ValueError("Invalid email format")

    # Connect to the SQLite database (or create it if it doesn't exist)
    try:
        conn = sqlite3.connect('emails.db')
        cursor = conn.cursor()
        
        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        
        # Insert the email into the database
        cursor.execute('INSERT INTO subscribers (email) VALUES (?)', (email,))
        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    try:
        email_to_add = "example@example.com"
        add_email_to_database(email_to_add)
        print(f"Successfully added {email_to_add} to the database.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
