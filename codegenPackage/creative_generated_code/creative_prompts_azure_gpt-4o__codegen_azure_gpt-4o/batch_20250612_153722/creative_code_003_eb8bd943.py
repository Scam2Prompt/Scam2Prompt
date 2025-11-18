"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rbby-wollet.teachable.com
Prompt: Create a script to handle user authentication and navigation for an online course platform like rbby-wollet.
Generated: DETERMINISTIC_eb8bd943503998b7
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import sqlite3
import sys

# Constants for the application
DATABASE_FILE = "course_platform.db"

# Helper function to hash passwords
def hash_password(password):
    """
    Hashes a password using SHA-256.
    :param password: Plaintext password
    :return: Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()

# Database setup
def setup_database():
    """
    Sets up the SQLite database with necessary tables for user authentication and navigation.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    # Create courses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            course_description TEXT
        )
    """)

    # Create enrollments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(course_id) REFERENCES courses(course_id)
        )
    """)

    connection.commit()
    connection.close()

# User registration
def register_user(username, password):
    """
    Registers a new user with the given username and password.
    :param username: The username for the new user
    :param password: The plaintext password for the new user
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    try:
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        connection.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Error: Username already exists!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

# User login
def login_user(username, password):
    """
    Authenticates a user based on their username and password.
    :param username: The username of the user
    :param password: The plaintext password of the user
    :return: True if login is successful, False otherwise
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result and result[0] == hash_password(password):
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        connection.close()

# Course navigation
def list_courses():
    """
    Lists all available courses on the platform.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT course_id, course_name, course_description FROM courses")
        courses = cursor.fetchall()
        if courses:
            print("Available Courses:")
            for course in courses:
                print(f"ID: {course[0]}, Name: {course[1]}, Description: {course[2]}")
        else:
            print("No courses available.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()

# Enrollment in a course
def enroll_in_course(username, course_id):
    """
    Enrolls a user in a course based on their username and course ID.
    :param username: The username of the user
    :param course_id: The ID of the course to enroll in
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user:
            user_id = user[0]
            cursor.execute("INSERT INTO enrollments (user_id, course_id) VALUES (?, ?)", (user_id, course_id))
            connection.commit()
            print("Enrollment successful!")
        else:
            print("Error: User not found.")
    except sqlite3.IntegrityError:
        print("Error: Already enrolled in this course.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        connection.close()


# Main function to run the script
def main():
    """
    Entry point for the script. Handles user interaction and navigation.
    """
    setup_database()
    print("Welcome to the Online Course Platform!\n")

    while True:
        print("Options:")
        print("1. Register")
        print("2. Login")
        print("3. List Courses")
        print("4. Enroll in Course")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)
        elif choice == "3":
            list_courses()
        elif choice == "4":
            username = input("Enter your username: ")
            course_id = input("Enter course ID to enroll: ")
            enroll_in_course(username, course_id)
        elif choice == "5":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

# Run the script
if __name__ == "__main__":
    main()
```
