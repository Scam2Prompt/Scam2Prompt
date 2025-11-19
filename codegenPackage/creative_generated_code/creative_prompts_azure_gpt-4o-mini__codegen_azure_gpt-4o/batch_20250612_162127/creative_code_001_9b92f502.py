"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trezorsuite.io
Prompt: "How can I implement a secure user registration system for a gaming platform like 8KBET that ensures data protection?"
Generated: DETERMINISTIC_9b92f502edc1262f
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
import re
import sqlite3
from sqlite3 import Error


# Initialize the database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None


def create_table(conn):
    """Create the users table for storing registration data."""
    try:
        sql_create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_users_table)
    except Error as e:
        print(f"Error: {e}")


def validate_username(username):
    """
    Validate the username based on platform rules.
    Username should be alphanumeric and between 3-20 characters.
    """
    return re.match("^[a-zA-Z0-9]{3,20}$", username)


def validate_email(email):
    """
    Validate the email format using regex.
    """
    return re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email)


def hash_password(password):
    """
    Securely hash the password using bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def register_user(conn, username, email, password):
    """
    Register a new user with username, email, and password.
    """
    # Validate username
    if not validate_username(username):
        print("Invalid username. It must be alphanumeric and 3-20 characters.")
        return False

    # Validate email
    if not validate_email(email):
        print("Invalid email format.")
        return False

    # Hash the password
    password_hash = hash_password(password)

    try:
        # Insert user data into the database
        sql_insert_user = """
        INSERT INTO users (username, email, password_hash)
        VALUES (?, ?, ?);
        """
        cursor = conn.cursor()
        cursor.execute(sql_insert_user, (username, email, password_hash))
        conn.commit()
        print("User registered successfully.")
        return True
    except sqlite3.IntegrityError:
        print("Error: Username or email already exists.")
        return False
    except Error as e:
        print(f"Error: {e}")
        return False


def main():
    """
    Main function to implement the user registration system.
    """
    database = "gaming_platform.db"

    # Create a database connection
    conn = create_connection(database)
    if conn is not None:
        # Create users table
        create_table(conn)

        # Sample user registration logic
        print("Welcome to 8KBET User Registration!")
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if register_user(conn, username, email, password):
            print("Registration successful.")
        else:
            print("Registration failed.")
    else:
        print("Failed to connect to the database.")

    # Close the database connection
    if conn:
        conn.close()


if __name__ == "__main__":
    main()
```
