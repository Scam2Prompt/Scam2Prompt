"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.greenaapples.com
Prompt: Create a program that integrates with a database to track success stories, such as weight loss achievements or improved cholesterol levels, similar to those highlighted on the Green Apples e-Rx Clinic website.
Generated: DETERMINISTIC_2f2992117b2d44be
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from datetime import datetime


# Database setup
def setup_database():
    """
    Create a SQLite database and the necessary table for storing success stories.
    """
    try:
        # Establish connection to the database
        conn = sqlite3.connect('success_stories.db')
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS success_stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            achievement TEXT NOT NULL,
            date TEXT NOT NULL
        )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error setting up the database: {e}")
    finally:
        # Close the connection to the database
        conn.close()


# Function to add a success story
def add_success_story(name, achievement):
    """
    Add a new success story to the database.
    :param name: Name of the individual.
    :param achievement: Description of their achievement.
    """
    try:
        conn = sqlite3.connect('success_stories.db')
        cursor = conn.cursor()

        # Insert the success story into the database
        date = datetime.now().strftime('%Y-%m-%d')
        cursor.execute("""
        INSERT INTO success_stories (name, achievement, date) 
        VALUES (?, ?, ?)
        """, (name, achievement, date))
        conn.commit()

        print("Success story added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding success story: {e}")
    finally:
        conn.close()


# Function to view all success stories
def view_success_stories():
    """
    Retrieve and display all success stories from the database.
    """
    try:
        conn = sqlite3.connect('success_stories.db')
        cursor = conn.cursor()

        # Query to fetch all success stories
        cursor.execute("SELECT id, name, achievement, date FROM success_stories")
        stories = cursor.fetchall()

        print("\nSuccess Stories:")
        print("----------------")
        for story in stories:
            print(f"ID: {story[0]}, Name: {story[1]}, Achievement: {story[2]}, Date: {story[3]}")
    except sqlite3.Error as e:
        print(f"Error retrieving success stories: {e}")
    finally:
        conn.close()


# Main function to interact with the program
def main():
    """
    Main function to interact with the database and manage success stories.
    """
    setup_database()

    while True:
        print("\nMenu:")
        print("1. Add Success Story")
        print("2. View Success Stories")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            achievement = input("Enter achievement: ")
            add_success_story(name, achievement)
        elif choice == '2':
            view_success_stories()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Entry point for the program
if __name__ == "__main__":
    main()
```
