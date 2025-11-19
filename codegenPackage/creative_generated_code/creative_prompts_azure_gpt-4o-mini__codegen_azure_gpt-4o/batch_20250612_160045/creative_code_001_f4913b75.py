"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Write a Python script to implement a user registration system for a betting website, incorporating features like quick sign-up and bonus rewards.
Generated: DETERMINISTIC_f4913b750eff70bc
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import sqlite3
from hashlib import sha256

# Database initialization
def initialize_database():
    """Initialize the database and create necessary tables."""
    connection = sqlite3.connect('betting_website.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            bonus_reward REAL DEFAULT 0.0
        )
    ''')
    connection.commit()
    connection.close()

# Password hashing
def hash_password(password):
    """Hash the password using SHA-256."""
    return sha256(password.encode()).hexdigest()

# Email validation
def is_valid_email(email):
    """Check if the email is valid using regex."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# User registration logic
def register_user(username, password, email):
    """
    Register a new user in the database.

    Parameters:
        username (str): The desired username.
        password (str): The chosen password.
        email (str): The user's email address.
    
    Returns:
        str: Success or error message.
    """
    if not username or not password or not email:
        return "Error: All fields are required."
    
    if not is_valid_email(email):
        return "Error: Invalid email address."

    connection = sqlite3.connect('betting_website.db')
    cursor = connection.cursor()

    try:
        # Hash the password
        password_hash = hash_password(password)

        # Insert user into the database with a bonus reward of 10.0
        cursor.execute('''
            INSERT INTO users (username, password_hash, email, bonus_reward)
            VALUES (?, ?, ?, ?)
        ''', (username, password_hash, email, 10.0))
        
        connection.commit()
        return f"Success: User '{username}' registered with a $10 bonus reward!"

    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint" in str(e):
            return "Error: Username or email already exists."
        else:
            return "Error: Database integrity issue."

    except Exception as e:
        return f"Error: An unexpected error occurred. Details: {e}"

    finally:
        connection.close()

# Main function for user interaction
def main():
    """Main function to handle user registration."""
    print("Welcome to the Betting Website Registration System!")

    while True:
        print("\nEnter your details to sign up:")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        email = input("Email: ").strip()

        message = register_user(username, password, email)
        print(message)

        # Exit option
        choice = input("\nDo you want to register another user? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thank you for using the registration system. Goodbye!")
            break

# Run the script
if __name__ == "__main__":
    initialize_database()
    main()
```
