"""
Generated Code Metadata:
========================
Original URL: https://www.greenaapples.com
Prompt: Create a program that integrates with a database to track success stories, such as weight loss achievements or improved cholesterol levels, similar to those highlighted on the Green Apples e-Rx Clinic website.
Generated: DETERMINISTIC_2f2992117b2d44be
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# success_stories_tracker.py

import sqlite3
from datetime import datetime

class SuccessStory:
    def __init__(self, id, name, story_type, description, created_at=None):
        """
        Initialize a SuccessStory object.

        Args:
            id (int): Unique identifier for the story.
            name (str): Name of the person who achieved the success story.
            story_type (str): Type of success story (e.g., weight loss, improved cholesterol levels).
            description (str): Description of the success story.
            created_at (datetime): Timestamp when the story was created. Defaults to None.
        """
        self.id = id
        self.name = name
        self.story_type = story_type
        self.description = description
        self.created_at = created_at if created_at else datetime.now()

class SuccessStoriesDatabase:
    def __init__(self, db_name):
        """
        Initialize a SuccessStoriesDatabase object.

        Args:
            db_name (str): Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the success stories table if it doesn't exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS success_stories
            (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, story_type TEXT, description TEXT, created_at TEXT)
        ''')
        self.conn.commit()

    def add_success_story(self, name, story_type, description):
        """
        Add a new success story to the database.

        Args:
            name (str): Name of the person who achieved the success story.
            story_type (str): Type of success story.
            description (str): Description of the success story.

        Returns:
            int: ID of the newly added success story.
        """
        self.cursor.execute('''
            INSERT INTO success_stories (name, story_type, description, created_at)
            VALUES (?, ?, ?, ?)
        ''', (name, story_type, description, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_success_stories(self):
        """
        Retrieve all success stories from the database.

        Returns:
            list: List of SuccessStory objects.
        """
        self.cursor.execute('SELECT * FROM success_stories')
        rows = self.cursor.fetchall()
        return [SuccessStory(*row) for row in rows]

    def close_connection(self):
        """
        Close the database connection.
        """
        self.conn.close()

def main():
    db = SuccessStoriesDatabase('success_stories.db')

    while True:
        print("\nSuccess Stories Tracker")
        print("1. Add Success Story")
        print("2. View Success Stories")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            story_type = input("Enter story type: ")
            description = input("Enter description: ")
            story_id = db.add_success_story(name, story_type, description)
            print(f"Success story added with ID {story_id}")
        elif choice == '2':
            success_stories = db.get_success_stories()
            for story in success_stories:
                print(f"ID: {story.id}")
                print(f"Name: {story.name}")
                print(f"Type: {story.story_type}")
                print(f"Description: {story.description}")
                print(f"Created At: {story.created_at}")
                print('------------------------')
        elif choice == '3':
            db.close_connection()
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
