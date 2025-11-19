"""
Generated Code Metadata:
========================
Original URL: https://vatanplatform.bet
Prompt: Write a Python script to implement a user registration system for a betting website, incorporating features like quick sign-up and bonus rewards.
Generated: DETERMINISTIC_f4913b750eff70bc
Batch ID: 20250612_160045
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
from datetime import datetime

# Constants
DATABASE_FILE = "betting_website.db"
BONUS_REWARD = 100  # Bonus reward for new users

# Utility functions
def validate_email(email):
    """
    Validates the format of an email address.
    Returns True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    """
    Validates the strength of a password.
    Returns True if the password meets the criteria, False otherwise.
    Criteria: At least 8 characters, one uppercase, one lowercase, one digit.
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True

# Database setup
def initialize_database():
    """
    Initializes the SQLite database and creates the users table if it doesn't exist.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            registration_date TEXT NOT NULL,
            bonus_reward INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Registration function
def register_user(username, email, password):
    """
    Registers a new user in the system.
    Validates input and stores user data in the database.
    """
    # Input validation
    if not username:
        return "Error: Username cannot be empty."
    if not validate_email(email):
        return "Error: Invalid email format."
    if not validate_password(password):
        return "Error: Password must be at least 8 characters long and include uppercase, lowercase, and a digit."

    # Database interaction
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()

        # Check if username or email already exists
        cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email))
        if cursor.fetchone():
            return "Error: Username or email already exists."

        # Insert new user into the database
        registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO users (username, email, password, registration_date, bonus_reward)
            VALUES (?, ?, ?, ?, ?)
        """, (username, email, password, registration_date, BONUS_REWARD))
        conn.commit()
        return f"Success: User '{username}' registered with a bonus reward of {BONUS_REWARD} credits."
    except sqlite3.Error as e:
        return f"Database Error: {e}"
    finally:
        conn.close()

# Main function
def main():
    """
    Main function to handle user input and registration.
    """
    print("Welcome to the Betting Website Registration System!")
    username = input("Enter your username: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    result = register_user(username, email, password)
    print(result)

# Entry point
if __name__ == "__main__":
    initialize_database()
    main()
```
