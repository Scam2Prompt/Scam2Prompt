"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magesdsdf.pages.dev
Prompt: Develop a script to register users for the MerlinStarter campaigns and track their ambassador program progress.
Generated: DETERMINISTIC_be44340cf0a5128d
Batch ID: 20250612_153420
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
DATABASE_NAME = 'merlin_starter.db'

def create_connection():
    """Create a database connection and return the connection object."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        print("Database connected successfully.")
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create tables for users and ambassador progress if they do not exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL UNIQUE,
                            registration_date TEXT NOT NULL
                          );''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS ambassador_progress (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            progress INTEGER DEFAULT 0,
                            last_update TEXT NOT NULL,
                            FOREIGN KEY (user_id) REFERENCES users (id)
                          );''')
        conn.commit()
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def register_user(conn, name, email):
    """Register a new user in the users table.
    
    Args:
        conn: Database connection object.
        name (str): The name of the user.
        email (str): The email of the user.

    Returns:
        int: The ID of the newly registered user or None if registration failed.
    """
    try:
        cursor = conn.cursor()
        registration_date = datetime.now().isoformat()
        cursor.execute("INSERT INTO users (name, email, registration_date) VALUES (?, ?, ?)",
                       (name, email, registration_date))
        conn.commit()
        user_id = cursor.lastrowid
        print(f"User registered successfully with ID: {user_id}")
        return user_id
    except sqlite3.IntegrityError:
        print(f"Error: Email {email} is already registered.")
    except sqlite3.Error as e:
        print(f"Error registering user: {e}")
    return None

def update_ambassador_progress(conn, user_id, progress_increment):
    """Update the ambassador program progress for a user.
    
    Args:
        conn: Database connection object.
        user_id (int): The ID of the user.
        progress_increment (int): The amount to increment the user's progress by.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT progress FROM ambassador_progress WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()

        if result:
            new_progress = result[0] + progress_increment
            cursor.execute("UPDATE ambassador_progress SET progress = ?, last_update = ? WHERE user_id = ?",
                           (new_progress, datetime.now().isoformat(), user_id))
            print(f"Ambassador progress updated for user ID {user_id}: {new_progress}")
        else:
            cursor.execute("INSERT INTO ambassador_progress (user_id, progress, last_update) VALUES (?, ?, ?)",
                           (user_id, progress_increment, datetime.now().isoformat()))
            print(f"Ambassador progress initialized for user ID {user_id}: {progress_increment}")

        conn.commit()
    except sqlite3.Error as e:
        print(f"Error updating ambassador progress: {e}")

def main():
    """Main function to run the user registration and progress tracking."""
    conn = create_connection()
    if conn:
        create_table(conn)

        # Example registration
        user_id = register_user(conn, "Alice Smith", "alice@example.com")
        if user_id:
            update_ambassador_progress(conn, user_id, 5)

        # Close the database connection
        conn.close()

if __name__ == "__main__":
    main()
```
