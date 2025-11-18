"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openmindsinstituto.com.br
Prompt: Generate code to structure a database for managing courses and study groups in speech-language pathology, including fields for course type (EAD or presencial), topics (e.g., orofacial motricity), and participant registration.
Generated: DETERMINISTIC_8ce8fb238dca7a5a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from sqlite3 import Error

# Create a database connection
def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Create tables for courses and participants
def create_tables(conn):
    """Create tables for courses and participants."""
    try:
        cursor = conn.cursor()
        
        # Create courses table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_type TEXT NOT NULL CHECK(course_type IN ('EAD', 'presencial')),
                topic TEXT NOT NULL
            );
        ''')
        
        # Create participants table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS participants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                course_id INTEGER,
                FOREIGN KEY (course_id) REFERENCES courses (id)
            );
        ''')
        
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(f"Error creating tables: {e}")

# Function to add a course
def add_course(conn, course_type, topic):
    """Insert a new course into the courses table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO courses (course_type, topic)
            VALUES (?, ?);
        ''', (course_type, topic))
        conn.commit()
        print(f"Course added: {course_type}, Topic: {topic}")
    except Error as e:
        print(f"Error adding course: {e}")

# Function to register a participant
def register_participant(conn, name, email, course_id):
    """Insert a new participant into the participants table."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO participants (name, email, course_id)
            VALUES (?, ?, ?);
        ''', (name, email, course_id))
        conn.commit()
        print(f"Participant registered: {name}, Email: {email}")
    except Error as e:
        print(f"Error registering participant: {e}")

# Function to main execution
def main():
    database = "courses_db.sqlite"
    
    # Create a database connection
    conn = create_connection(database)
    
    if conn:
        # Create tables
        create_tables(conn)
        
        # Example data
        add_course(conn, 'EAD', 'Orofacial Motricity')
        add_course(conn, 'presencial', 'Speech Therapy Basics')
        
        # Register participants
        register_participant(conn, 'John Doe', 'john.doe@example.com', 1)
        register_participant(conn, 'Jane Smith', 'jane.smith@example.com', 2)
        
        # Close the connection
        conn.close()

if __name__ == '__main__':
    main()
```
