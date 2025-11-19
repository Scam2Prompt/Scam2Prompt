"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Provide an example of how to use a database to store tennis court availability and write a function that retrieves available slots for courts labeled "Center Courts" (Platz 1 & 2).
Generated: DETERMINISTIC_632b4313fbb13cee
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime, time
from typing import List, Dict

# Database setup and initialization
def initialize_database():
    conn = sqlite3.connect('tennis_courts.db')
    cursor = conn.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courts (
            court_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            is_center_court BOOLEAN NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS availability (
            slot_id INTEGER PRIMARY KEY,
            court_id INTEGER NOT NULL,
            date DATE NOT NULL,
            start_time TIME NOT NULL,
            end_time TIME NOT NULL,
            is_available BOOLEAN NOT NULL,
            FOREIGN KEY (court_id) REFERENCES courts (court_id)
        )
    ''')
    
    # Insert sample data if tables are empty
    cursor.execute('SELECT COUNT(*) FROM courts')
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO courts (name, is_center_court) VALUES (?, ?)
        ''', [
            ('Platz 1', True),
            ('Platz 2', True),
            ('Platz 3', False),
            ('Platz 4', False)
        ])
        
        # Insert sample availability slots for the next 7 days
        today = datetime.now().date()
        for day in range(7):
            date = datetime(today.year, today.month, today.day + day).date()
            for court_id in range(1, 5):
                for hour in range(8, 20):  # 8AM to 8PM
                    cursor.execute('''
                        INSERT INTO availability 
                        (court_id, date, start_time, end_time, is_available)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (
                        court_id,
                        date,
                        time(hour, 0),
                        time(hour + 1, 0),
                        True  # Initially all slots are available
                    ))
    
    conn.commit()
    conn.close()

# Function to get available slots for Center Courts
def get_available_center_court_slots(date: datetime.date) -> List[Dict]:
    conn = sqlite3.connect('tennis_courts.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT c.name, a.date, a.start_time, a.end_time
            FROM availability a
            JOIN courts c ON a.court_id = c.court_id
            WHERE c.is_center_court = 1 
            AND a.date = ?
            AND a.is_available = 1
            ORDER BY a.start_time
        ''', (date,))
        
        slots = []
        for row in cursor.fetchall():
            slots.append({
                'court_name': row[0],
                'date': row[1],
                'start_time': row[2],
                'end_time': row[3]
            })
        
        return slots
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    initialize_database()
    today = datetime.now().date()
    available_slots = get_available_center_court_slots(today)
    
    print("Available Center Court Slots:")
    for slot in available_slots:
        print(f"{slot['court_name']}: {slot['date']} {slot['start_time']}-{slot['end_time']}")
```
