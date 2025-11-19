"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Illustrate how to implement a feedback collection system for students at Potencia Academy, focusing on course effectiveness and faculty performance.
Generated: DETERMINISTIC_d8e73b22c357de46
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# feedback_system.py

import sqlite3
from datetime import datetime

# Database setup
DATABASE_FILE = 'feedback_system.db'

def initialize_database():
    """
    Initialize the database structure for storing feedback.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Create table for feedback entries
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        course_name TEXT NOT NULL,
        faculty_name TEXT NOT NULL,
        course_effectiveness INTEGER NOT NULL CHECK(course_effectiveness BETWEEN 1 AND 5),
        faculty_performance INTEGER NOT NULL CHECK(faculty_performance BETWEEN 1 AND 5),
        additional_comments TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()

def collect_feedback():
    """
    Collect feedback from a student via command-line input.
    """
    print("\n--- Feedback Collection System ---")
    
    try:
        # Gather feedback details
        student_name = input("Enter your name: ").strip()
        if not student_name:
            raise ValueError("Student name cannot be empty.")

        course_name = input("Enter the course name: ").strip()
        if not course_name:
            raise ValueError("Course name cannot be empty.")

        faculty_name = input("Enter the faculty's name: ").strip()
        if not faculty_name:
            raise ValueError("Faculty name cannot be empty.")
        
        course_effectiveness = int(input("Rate the course effectiveness (1-5): "))
        if course_effectiveness < 1 or course_effectiveness > 5:
            raise ValueError("Course effectiveness rating must be between 1 and 5.")
        
        faculty_performance = int(input("Rate the faculty's performance (1-5): "))
        if faculty_performance < 1 or faculty_performance > 5:
            raise ValueError("Faculty performance rating must be between 1 and 5.")
        
        additional_comments = input("Any additional comments (optional): ").strip()

        # Save feedback to the database
        save_feedback(student_name, course_name, faculty_name, course_effectiveness, faculty_performance, additional_comments)
        print("\nThank you for your feedback!")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def save_feedback(student_name, course_name, faculty_name, course_effectiveness, faculty_performance, additional_comments):
    """
    Save feedback to the database.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
        INSERT INTO feedback (student_name, course_name, faculty_name, course_effectiveness, faculty_performance, additional_comments)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (student_name, course_name, faculty_name, course_effectiveness, faculty_performance, additional_comments))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred while saving feedback: {e}")
    finally:
        conn.close()

def view_feedback():
    """
    View all feedback entries stored in the database.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM feedback")
        rows = cursor.fetchall()
        
        print("\n--- All Feedback Entries ---")
        for row in rows:
            print(f"""
            ID: {row[0]}
            Student Name: {row[1]}
            Course Name: {row[2]}
            Faculty Name: {row[3]}
            Course Effectiveness: {row[4]}
            Faculty Performance: {row[5]}
            Additional Comments: {row[6]}
            Timestamp: {row[7]}
            """)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred while retrieving feedback: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # Initialize the database if not already done
    initialize_database()
    
    while True:
        print("\n--- Potencia Academy Feedback System ---")
        print("1. Submit Feedback")
        print("2. View Feedback")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            collect_feedback()
        elif choice == '2':
            view_feedback()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
