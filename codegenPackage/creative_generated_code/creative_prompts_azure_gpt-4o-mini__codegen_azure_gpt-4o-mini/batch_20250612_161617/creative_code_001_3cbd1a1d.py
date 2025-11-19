"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlas3io-moonseeker.web.app
Prompt: Write a code snippet for a giveaway entry system that tracks tasks completed for MoonSeeker DAO members.
Generated: DETERMINISTIC_3cbd1a1d84aca87b
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from contextlib import closing

class GiveawayEntrySystem:
    def __init__(self, db_name='giveaway_entries.db'):
        """Initialize the GiveawayEntrySystem with a database connection."""
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        """Create database tables for tracking entries and tasks."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    member_id INTEGER,
                    task_id INTEGER,
                    FOREIGN KEY (member_id) REFERENCES members(id),
                    FOREIGN KEY (task_id) REFERENCES tasks(id),
                    UNIQUE (member_id, task_id)
                )
            ''')
            conn.commit()

    def connect_db(self):
        """Establish a database connection."""
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            raise

    def add_member(self, name):
        """Add a new member to the system."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO members (name) VALUES (?)', (name,))
                conn.commit()
            except sqlite3.IntegrityError:
                print(f"Member '{name}' already exists.")

    def add_task(self, description):
        """Add a new task to the system."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
            conn.commit()

    def complete_task(self, member_name, task_description):
        """Record task completion for a member."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM members WHERE name = ?', (member_name,))
            member = cursor.fetchone()
            cursor.execute('SELECT id FROM tasks WHERE description = ?', (task_description,))
            task = cursor.fetchone()

            if not member:
                print(f"Member '{member_name}' not found.")
                return
            
            if not task:
                print(f"Task '{task_description}' not found.")
                return

            try:
                cursor.execute('INSERT INTO entries (member_id, task_id) VALUES (?, ?)', (member[0], task[0]))
                conn.commit()
                print(f"Task '{task_description}' completed by '{member_name}'.")
            except sqlite3.IntegrityError:
                print(f"Task '{task_description}' is already completed by '{member_name}'.")

    def get_member_entries(self, member_name):
        """Retrieve all completed tasks for a member."""
        with closing(self.connect_db()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT t.description
                FROM entries e
                JOIN members m ON e.member_id = m.id
                JOIN tasks t ON e.task_id = t.id
                WHERE m.name = ?
            ''', (member_name,))
            return cursor.fetchall()

# Example usage:
if __name__ == '__main__':
    system = GiveawayEntrySystem()
    system.add_member('Alice')
    system.add_task('Share on social media')
    system.complete_task('Alice', 'Share on social media')
    entries = system.get_member_entries('Alice')
    print(f"Alice's completed tasks: {entries}")
```
