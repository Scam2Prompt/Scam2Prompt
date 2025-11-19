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

class EmailValidator:
    def __init__(self, db_name):
        """
        Initialize the EmailValidator class.

        Args:
            db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """
        Create a table in the SQLite database to store email addresses.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS email_sign_ups
                    (email TEXT PRIMARY KEY)
                ''')
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def validate_email(self, email):
        """
        Validate an email address using a regular expression.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(email_regex, email))

    def add_email(self, email):
        """
        Add an email address to the database if it's valid.

        Args:
            email (str): The email address to add.

        Returns:
            bool: True if the email was added, False otherwise.
        """
        if not self.validate_email(email):
            return False

        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT OR IGNORE INTO email_sign_ups (email) VALUES (?)', (email,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error adding email: {e}")
            return False

    def get_all_emails(self):
        """
        Retrieve all email addresses from the database.

        Returns:
            list: A list of email addresses.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM email_sign_ups')
                return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error retrieving emails: {e}")
            return []

def main():
    validator = EmailValidator('email_sign_ups.db')

    # Example usage:
    emails = ["test@example.com", "invalid_email", "another_test@example.co.uk"]
    for email in emails:
        if validator.add_email(email):
            print(f"Added email: {email}")
        else:
            print(f"Failed to add email: {email}")

    print("All emails:")
    print(validator.get_all_emails())

if __name__ == "__main__":
    main()
```
