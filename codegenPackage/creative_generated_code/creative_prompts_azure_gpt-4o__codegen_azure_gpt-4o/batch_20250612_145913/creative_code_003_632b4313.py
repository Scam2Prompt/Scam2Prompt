"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Provide an example of how to use a database to store tennis court availability and write a function that retrieves available slots for courts labeled "Center Courts" (Platz 1 & 2).
Generated: DETERMINISTIC_632b4313fbb13cee
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sqlite3
from typing import List, Tuple

# Database setup and initialization
def initialize_database():
    """
    Initializes the database, creates the tables, and seeds data for tennis court availability.
    """
    conn = sqlite3.connect('tennis_courts.db')
    cursor = conn.cursor()

    # Create the tennis_courts table if it doesn't already exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tennis_courts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        court_name TEXT NOT NULL,
        available_slot TEXT NOT NULL
    )
    ''')

    # Seed data into the tennis_courts table
    # Note: In a real application, data is unlikely to be seeded this way in production.
    courts_data = [
        ("Platz 1", "10:00-11:00"),
        ("Platz 1", "11:00-12:00"),
        ("Platz 2", "13:00-14:00"),
        ("Platz 2", "15:00-16:00"),
        ("Court 3", "09:00-10:00"),  # Non-center court
    ]

    # Clear existing data before seeding to ensure idempotency
    cursor.execute('DELETE FROM tennis_courts')

    # Insert data into the table
    cursor.executemany('INSERT INTO tennis_courts (court_name, available_slot) VALUES (?, ?)', courts_data)

    conn.commit()
    conn.close()

# Function to retrieve available slots for "Center Courts" (Platz 1 & Platz 2)
def get_center_court_availability() -> List[Tuple[str, str]]:
    """
    Fetches and returns the available slots for courts labeled as "Center Courts" (Platz 1 and Platz 2).
    
    Returns:
        List[Tuple[str, str]]: A list of tuples where each tuple contains court name and available slot.
    """
    conn = sqlite3.connect('tennis_courts.db')
    cursor = conn.cursor()

    try:
        # Query database for available slots for "Center Courts" (Platz 1 and Platz 2)
        cursor.execute('''
        SELECT court_name, available_slot
        FROM tennis_courts
        WHERE court_name IN ('Platz 1', 'Platz 2')
        ''')
        results = cursor.fetchall()
    except sqlite3.Error as e:
        # Log error in production code - for simplicity, print the error here
        print(f"Database error: {e}")
        results = []  # Return an empty list in case of any error
    finally:
        conn.close()

    return results

# Main execution
if __name__ == "__main__":
    # Initialize the database and seed data
    initialize_database()

    # Fetch and display available slots for Center Courts
    center_court_slots = get_center_court_availability()
    print("Available slots for Center Courts (Platz 1 & Platz 2):")
    for court, slot in center_court_slots:
        print(f"{court}: {slot}")
```
