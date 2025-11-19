"""
Generated Code Metadata:
========================
Original URL: https://blur.today
Prompt: Create a system that tracks user progress through daily self-discovery questions and adjusts avatar preferences dynamically, as described on blur.today.
Generated: DETERMINISTIC_80f6c50c7750ae89
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Progress Tracker and Avatar Preferences System**
===========================================================

### **System Requirements**

* Python 3.9+
* SQLite3

### **Code**

```python
import sqlite3
from datetime import date

# Define database connection and schema
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, name TEXT NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_questions
            (id INTEGER PRIMARY KEY, question TEXT NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_progress
            (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, 
             question_id INTEGER NOT NULL, answer TEXT, 
             date DATE NOT NULL, 
             FOREIGN KEY (user_id) REFERENCES users (id),
             FOREIGN KEY (question_id) REFERENCES daily_questions (id))
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS avatar_preferences
            (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, 
             preference TEXT NOT NULL, 
             FOREIGN KEY (user_id) REFERENCES users (id))
        ''')

        self.conn.commit()

    def close_connection(self):
        self.conn.close()


# Define user and progress management
class UserProgressTracker:
    def __init__(self, db):
        self.db = db

    def add_user(self, name):
        try:
            self.db.cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
            return None

    def get_user_id(self, name):
        try:
            self.db.cursor.execute('SELECT id FROM users WHERE name = ?', (name,))
            return self.db.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print(f"Error getting user ID: {e}")
            return None

    def add_daily_question(self, question):
        try:
            self.db.cursor.execute('INSERT INTO daily_questions (question) VALUES (?)', (question,))
            self.db.conn.commit()
            return self.db.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding daily question: {e}")
            return None

    def submit_answer(self, user_id, question_id, answer):
        try:
            self.db.cursor.execute('INSERT INTO user_progress (user_id, question_id, answer, date) VALUES (?, ?, ?, ?)', 
                                   (user_id, question_id, answer, date.today()))
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"Error submitting answer: {e}")

    def get_user_progress(self, user_id):
        try:
            self.db.cursor.execute('SELECT * FROM user_progress WHERE user_id = ?', (user_id,))
            return self.db.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error getting user progress: {e}")
            return []

    def update_avatar_preferences(self, user_id, preference):
        try:
            self.db.cursor.execute('SELECT * FROM avatar_preferences WHERE user_id = ?', (user_id,))
            if self.db.cursor.fetchone():
                self.db.cursor.execute('UPDATE avatar_preferences SET preference = ? WHERE user_id = ?', (preference, user_id))
            else:
                self.db.cursor.execute('INSERT INTO avatar_preferences (user_id, preference) VALUES (?, ?)', (user_id, preference))
            self.db.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating avatar preferences: {e}")

    def get_avatar_preferences(self, user_id):
        try:
            self.db.cursor.execute('SELECT preference FROM avatar_preferences WHERE user_id = ?', (user_id,))
            return self.db.cursor.fetchone()[0] if self.db.cursor.fetchone() else None
        except sqlite3.Error as e:
            print(f"Error getting avatar preferences: {e}")
            return None


# Example usage
if __name__ == "__main__":
    db = Database('user_progress.db')
    tracker = UserProgressTracker(db)

    user_id = tracker.add_user('John Doe')
    question_id = tracker.add_daily_question('What am I grateful for today?')

    tracker.submit_answer(user_id, question_id, 'My family')

    progress = tracker.get_user_progress(user_id)
    print(progress)

    tracker.update_avatar_preferences(user_id, 'likes cats')
    preferences = tracker.get_avatar_preferences(user_id)
    print(preferences)

    db.close_connection()
```

### **API Documentation**

#### Database

*   `__init__(db_name)`: Initializes a new database connection.
*   `create_tables()`: Creates the necessary tables in the database.
*   `close_connection()`: Closes the database connection.

#### UserProgressTracker

*   `add_user(name)`: Adds a new user to the database.
*   `get_user_id(name)`: Retrieves a user's ID by name.
*   `add_daily_question(question)`: Adds a new daily question to the database.
*   `submit_answer(user_id, question_id, answer)`: Submits a user's answer to a daily question.
*   `get_user_progress(user_id)`: Retrieves a user's progress.
*   `update_avatar_preferences(user_id, preference)`: Updates a user's avatar preferences.
*   `get_avatar_preferences(user_id)`: Retrieves a user's avatar preferences.
