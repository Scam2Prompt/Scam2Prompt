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
import sqlite3
from datetime import datetime, timedelta

# Database setup
def setup_database():
    """Create a SQLite database and a table for tennis court availability."""
    conn = sqlite3.connect('tennis_courts.db')
    cursor = conn.cursor()
    
    # Create table for court availability
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS court_availability (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            court_name TEXT NOT NULL,
            date DATE NOT NULL,
            start_time TIME NOT NULL,
            end_time TIME NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

# Insert sample data
def insert_sample_data():
    """Insert sample data into the court availability table."""
    conn = sqlite3.connect('tennis_courts.db')
    cursor = conn.cursor()
    
    # Sample data for Center Courts (Platz 1 & 2)
    sample_data = [
        ('Center Court 1', '2023-10-01', '09:00:00', '10:00:00'),
        ('Center Court 1', '2023-10-01', '11:00:00', '12:00:00'),
        ('Center Court 2', '2023-10-01', '09:00:00', '10:00:00'),
        ('Center Court 2', '2023-10-01', '13:00:00', '14:00:00'),
    ]
    
    cursor.executemany('''
        INSERT INTO court_availability (court_name, date, start_time, end_time)
        VALUES (?, ?, ?, ?)
    ''', sample_data)
    
    conn.commit()
    conn.close()

def get_available_slots(court_name: str, date: str) -> list:
    """Retrieve available slots for a specific court on a given date.
    
    Args:
        court_name (str): The name of the court.
        date (str): The date to check availability (YYYY-MM-DD).

    Returns:
        list: A list of available time slots for the specified court.
    """
    conn = sqlite3.connect('tennis_courts.db')
    cursor = conn.cursor()
    
    # Query for booked slots
    cursor.execute('''
        SELECT start_time, end_time FROM court_availability
        WHERE court_name = ? AND date = ?
    ''', (court_name, date))
    
    booked_slots = cursor.fetchall()
    conn.close()
    
    # Generate a list of all possible slots (example: hourly slots from 09:00 to 20:00)
    all_slots = []
    start_time = datetime.strptime('09:00', '%H:%M')
    end_time = datetime.strptime('20:00', '%H:%M')
    
    while start_time < end_time:
        slot_start = start_time.time()
        slot_end = (start_time + timedelta(hours=1)).time()
        all_slots.append((slot_start, slot_end))
        start_time += timedelta(hours=1)
    
    available_slots = []
    
    # Determine available slots by checking against booked slots
    for slot in all_slots:
        is_booked = any(
            slot[0] < booked[1] and slot[1] > booked[0] for booked in booked_slots
        )
        if not is_booked:
            available_slots.append(slot)

    return available_slots

# Example usage
if __name__ == "__main__":
    setup_database()
    insert_sample_data()
    
    # Retrieve available slots for "Center Court 1" on "2023-10-01"
    available_slots_c1 = get_available_slots('Center Court 1', '2023-10-01')
    print("Available slots for Center Court 1 on 2023-10-01:", available_slots_c1)
    
    # Retrieve available slots for "Center Court 2" on "2023-10-01"
    available_slots_c2 = get_available_slots('Center Court 2', '2023-10-01')
    print("Available slots for Center Court 2 on 2023-10-01:", available_slots_c2)
```
