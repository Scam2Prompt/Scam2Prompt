"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isienvironmental.com
Prompt: Develop code to schedule and manage environmental and safety training sessions across multiple cities (e.g., Wichita, Tulsa, Atlanta), based on the training offerings listed on the iSi Environmental site.
Generated: DETERMINISTIC_8377e96afc34c7aa
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code for scheduling and managing environmental and safety training sessions across multiple cities. This example assumes a database-centric approach with SQLite for simplicity.

```python
import sqlite3
from datetime import datetime
from typing import List

# Database connection setup (production environments might use a different database like PostgreSQL/MySQL)
DB_FILE = 'training_schedule.db'

# Create a database connection
def create_connection(db_file: str):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Initialize the database schema
def initialize_database(conn):
    try:
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS Cities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                );
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS Trainings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    duration INTEGER NOT NULL -- Duration in hours
                );
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS TrainingSchedules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city_id INTEGER NOT NULL,
                    training_id INTEGER NOT NULL,
                    scheduled_date TEXT NOT NULL,
                    FOREIGN KEY (city_id) REFERENCES Cities (id),
                    FOREIGN KEY (training_id) REFERENCES Trainings (id)
                );
            ''')
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

# Add a city
def add_city(conn, city_name: str):
    try:
        with conn:
            conn.execute('INSERT OR IGNORE INTO Cities (name) VALUES (?);', (city_name,))
    except sqlite3.Error as e:
        print(f"Error adding city: {e}")

# Add a training
def add_training(conn, title: str, description: str, duration: int):
    try:
        with conn:
            conn.execute('''
                INSERT INTO Trainings (title, description, duration) VALUES (?, ?, ?);
            ''', (title, description, duration))
    except sqlite3.Error as e:
        print(f"Error adding training: {e}")

# Schedule a training session
def schedule_training_session(conn, city_name: str, training_title: str, scheduled_date: str):
    try:
        with conn:
            city_id = conn.execute('SELECT id FROM Cities WHERE name = ?;', (city_name,)).fetchone()
            training_id = conn.execute('SELECT id FROM Trainings WHERE title = ?;', (training_title,)).fetchone()
            
            if not city_id or not training_id:
                print("City or Training not found!")
                return
            
            conn.execute('''
                INSERT INTO TrainingSchedules (city_id, training_id, scheduled_date) VALUES (?, ?, ?);
            ''', (city_id[0], training_id[0], scheduled_date))
    except sqlite3.Error as e:
        print(f"Error scheduling training session: {e}")

# View scheduled training sessions
def view_scheduled_sessions(conn) -> List[dict]:
    try:
        cursor = conn.execute('''
            SELECT Cities.name AS city, Trainings.title AS training, scheduled_date
            FROM TrainingSchedules
            INNER JOIN Cities ON TrainingSchedules.city_id = Cities.id
            INNER JOIN Trainings ON TrainingSchedules.training_id = Trainings.id
            ORDER BY scheduled_date;
        ''')
        return [{"city": row[0], "training": row[1], "date": row[2]} for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Error retrieving scheduled sessions: {e}")
        return []

# Main function for testing
def main():
    # Connect to the database
    conn = create_connection(DB_FILE)
    if conn is None:
        return

    # Initialize schema
    initialize_database(conn)

    # Add cities
    add_city(conn, "Wichita")
    add_city(conn, "Tulsa")
    add_city(conn, "Atlanta")

    # Add trainings
    add_training(conn, "Hazardous Waste Management", "Learn how to properly handle hazardous waste.", 8)
    add_training(conn, "Safety Compliance", "Understand OSHA safety standards.", 6)

    # Schedule sessions
    schedule_training_session(conn, "Wichita", "Hazardous Waste Management", "2023-11-15")
    schedule_training_session(conn, "Tulsa", "Safety Compliance", "2023-11-18")
    schedule_training_session(conn, "Atlanta", "Hazardous Waste Management", "2023-11-20")

    # View scheduled sessions
    sessions = view_scheduled_sessions(conn)
    for session in sessions:
        print(f"City: {session['city']}, Training: {session['training']}, Date: {session['date']}")

    # Close connection
    conn.close()

if __name__ == "__main__":
    main()
```

### Notes:
- Replace SQLite with a production database (e.g., PostgreSQL/MySQL) for scalability and reliability.
- Ensure the date format (`scheduled_date`) is consistent with your application's requirements.
- Add API endpoints or a user interface for interaction in a real-world application.
- Secure database connections and sanitize inputs to prevent SQL injection in production environments.
