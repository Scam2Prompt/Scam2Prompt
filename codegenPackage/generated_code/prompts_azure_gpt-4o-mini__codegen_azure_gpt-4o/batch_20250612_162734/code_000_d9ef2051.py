"""
Generated Code Metadata:
========================
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: How can I implement a registration system for a prize giveaway similar to the one described on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_d9ef2051bdc0d704
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
import re

# Database setup
DB_NAME = "giveaway.db"

def initialize_database():
    """
    Initialize the database and create the necessary table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def validate_email(email):
    """
    Validate the email format using a regular expression.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def register_user(name, email):
    """
    Register a user for the prize giveaway.
    """
    if not name or not email:
        print("Name and email are required.")
        return False

    if not validate_email(email):
        print("Invalid email format.")
        return False

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registrations (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("Registration successful!")
        return True
    except sqlite3.IntegrityError:
        print("This email is already registered.")
        return False
    except sqlite3.Error as e:
        print(f"Error registering user: {e}")
        return False
    finally:
        conn.close()

def list_registrations():
    """
    List all registered users.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, timestamp FROM registrations")
        registrations = cursor.fetchall()
        if registrations:
            print("Registered Users:")
            for reg in registrations:
                print(f"ID: {reg[0]}, Name: {reg[1]}, Email: {reg[2]}, Timestamp: {reg[3]}")
        else:
            print("No registrations found.")
    except sqlite3.Error as e:
        print(f"Error fetching registrations: {e}")
    finally:
        conn.close()

# Main program
if __name__ == "__main__":
    initialize_database()

    while True:
        print("\nPrize Giveaway Registration System")
        print("1. Register for the giveaway")
        print("2. List all registrations")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ").strip()
            email = input("Enter your email: ").strip()
            register_user(name, email)
        elif choice == "2":
            list_registrations()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
