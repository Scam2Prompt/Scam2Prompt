"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Write a code example that showcases how to manage a digital platform for music rehearsal sessions at the Ferme Bermond, as described by the association.
Generated: DETERMINISTIC_08afeef1bfd4dbcd
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Music Rehearsal Session Management System for Ferme Bermond Association
This script provides functionality to manage rehearsal sessions,
track bookings, and maintain a database of users and session schedules.
"""

import datetime
import sqlite3

# Initialize SQLite database connection
DATABASE_FILE = "ferme_bermond.db"

def initialize_database():
    """
    Initialize the SQLite database with required tables.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    
    # Create sessions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            duration INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    
    connection.commit()
    connection.close()

def add_user(name, email):
    """
    Add a new user to the database.
    :param name: Name of the user
    :param email: Email of the user
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        connection.commit()
    except sqlite3.IntegrityError:
        print(f"Error: User with email '{email}' already exists.")
    finally:
        connection.close()

def book_session(user_email, date, time, duration):
    """
    Book a rehearsal session for a user.
    :param user_email: Email of the user booking the session
    :param date: Date of the session (format: YYYY-MM-DD)
    :param time: Time of the session (format: HH:MM)
    :param duration: Duration of the session in minutes
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    try:
        # Check if user exists
        cursor.execute("SELECT id FROM users WHERE email = ?", (user_email,))
        user = cursor.fetchone()
        
        if not user:
            print(f"Error: No user found with email '{user_email}'.")
            return
        
        user_id = user[0]
        
        # Check for conflicting sessions
        cursor.execute("""
            SELECT * FROM sessions WHERE date = ? AND time = ? AND user_id = ?
        """, (date, time, user_id))
        conflict = cursor.fetchone()
        
        if conflict:
            print(f"Error: Conflict detected for session on {date} at {time}.")
            return
        
        # Book the session
        cursor.execute("""
            INSERT INTO sessions (date, time, duration, user_id) VALUES (?, ?, ?, ?)
        """, (date, time, duration, user_id))
        connection.commit()
        print(f"Session booked successfully for {user_email} on {date} at {time}.")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

def list_sessions():
    """
    List all booked rehearsal sessions.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    
    try:
        cursor.execute("""
            SELECT sessions.date, sessions.time, sessions.duration, users.name, users.email
            FROM sessions
            JOIN users ON sessions.user_id = users.id
        """)
        sessions = cursor.fetchall()
        
        print("Scheduled Rehearsal Sessions:")
        for session in sessions:
            date, time, duration, name, email = session
            print(f"- {date} at {time}, {duration} minutes | User: {name} ({email})")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()

def main():
    """
    Main function to initialize database and demonstrate functionality.
    """
    initialize_database()
    
    # Sample usage
    add_user("Alice Johnson", "alice@example.com")
    add_user("Bob Smith", "bob@example.com")
    
    book_session("alice@example.com", "2023-10-15", "14:00", 60)
    book_session("bob@example.com", "2023-10-15", "15:30", 90)
    
    list_sessions()

if __name__ == "__main__":
    main()
```
