"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securespend.io
Prompt: Develop a script that simulates a user registration process for an online togel betting platform, ensuring unique member IDs.
Generated: DETERMINISTIC_78d0a370db14e58d
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import re
import sqlite3
from datetime import datetime


class TogelRegistration:
    def __init__(self, db_name="togel_platform.db"):
        """
        Initializes the database connection and sets up the table if not exists.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._setup_database()

    def _setup_database(self):
        """
        Creates a users table in the database if it doesn't already exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                member_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                registration_date TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def generate_member_id(self):
        """
        Generates a unique member ID using the UUID4 algorithm.
        """
        return str(uuid.uuid4())

    def validate_email(self, email):
        """
        Validates the email format using a regular expression.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def register_user(self, name, email, password):
        """
        Registers a new user into the platform.
        Validates input and ensures email uniqueness.
        """
        # Input validation
        if not name or not email or not password:
            raise ValueError("Name, email, and password are required fields.")
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")

        # Check for email uniqueness
        self.cursor.execute("SELECT email FROM users WHERE email = ?", (email,))
        if self.cursor.fetchone():
            raise ValueError("Email is already registered.")

        # Generate a unique member ID
        member_id = self.generate_member_id()

        # Save the new user to the database
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
            INSERT INTO users (member_id, name, email, password, registration_date)
            VALUES (?, ?, ?, ?, ?)
        """, (member_id, name, email, password, registration_date))
        self.conn.commit()

        return {
            "member_id": member_id,
            "name": name,
            "email": email,
            "registration_date": registration_date
        }

    def close_connection(self):
        """
        Closes the database connection.
        """
        self.conn.close()


# Example usage
if __name__ == "__main__":
    try:
        togel_platform = TogelRegistration()

        print("Welcome to the Togel Betting Platform Registration!")
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()

        user_info = togel_platform.register_user(name, email, password)
        print("Registration successful!")
        print("Your details:", user_info)

    except ValueError as ve:
        print(f"Error: {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        togel_platform.close_connection()
```
