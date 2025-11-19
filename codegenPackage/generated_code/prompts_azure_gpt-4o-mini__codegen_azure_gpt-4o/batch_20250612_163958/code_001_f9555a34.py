"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: How can I implement a feedback mechanism for a training program similar to the one used by SMART Training Resources?
Generated: DETERMINISTIC_f9555a34dadc6bbe
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# feedback_system.py

import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "feedback.db"

def initialize_database():
    """
    Initializes the database and creates the necessary table if it doesn't exist.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
                comments TEXT,
                submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

def submit_feedback(name, email, rating, comments):
    """
    Submits feedback to the database.

    Args:
        name (str): Name of the participant.
        email (str): Email of the participant.
        rating (int): Rating between 1 and 5.
        comments (str): Additional comments.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO feedback (name, email, rating, comments)
            VALUES (?, ?, ?, ?)
        """, (name, email, rating, comments))
        conn.commit()
        print("Feedback submitted successfully!")
    except sqlite3.Error as e:
        print(f"Error submitting feedback: {e}")
    finally:
        conn.close()

def view_feedback():
    """
    Retrieves and displays all feedback from the database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedback")
        feedback_records = cursor.fetchall()
        print("Feedback Records:")
        for record in feedback_records:
            print(f"ID: {record[0]}, Name: {record[1]}, Email: {record[2]}, Rating: {record[3]}, Comments: {record[4]}, Submitted At: {record[5]}")
    except sqlite3.Error as e:
        print(f"Error retrieving feedback: {e}")
    finally:
        conn.close()

def main():
    """
    Main function to interact with the feedback system.
    """
    initialize_database()
    while True:
        print("\nFeedback System")
        print("1. Submit Feedback")
        print("2. View Feedback")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            try:
                rating = int(input("Enter your rating (1-5): "))
                if rating < 1 or rating > 5:
                    raise ValueError("Rating must be between 1 and 5.")
            except ValueError as ve:
                print(f"Invalid rating: {ve}")
                continue
            comments = input("Enter your comments (optional): ")
            submit_feedback(name, email, rating, comments)
        elif choice == "2":
            view_feedback()
        elif choice == "3":
            print("Exiting the feedback system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
