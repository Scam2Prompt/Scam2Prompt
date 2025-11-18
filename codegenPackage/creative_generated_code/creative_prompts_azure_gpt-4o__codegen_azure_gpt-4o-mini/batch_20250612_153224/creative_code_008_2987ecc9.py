"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consultorialicitare.com.br
Prompt: Write code to implement a reporting system for tracking the efficiency of administrative processes in public institutions, inspired by Licitare's "Gestão de Processos e Procedimentos Administrativos."
Generated: DETERMINISTIC_2987ecc95ac613bf
Batch ID: 20250612_153224
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

class Report:
    """
    A class to represent a report for tracking administrative processes.

    Attributes:
        id (int): The report's ID.
        process_name (str): Name of the administrative process.
        start_time (datetime): Start time of the process.
        end_time (datetime): End time of the process.
        duration (float): Duration of the process in seconds.
    """

    def __init__(self, process_name, start_time, end_time):
        self.process_name = process_name
        self.start_time = start_time
        self.end_time = end_time
        self.duration = (end_time - start_time).total_seconds()

    def save_to_db(self, conn):
        """Save the report to the database."""
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reports (process_name, start_time, end_time, duration) 
            VALUES (?, ?, ?, ?)
        ''', (self.process_name, self.start_time, self.end_time, self.duration))
        conn.commit()


def create_db():
    """Create the database and the reports table if it doesn't exist."""
    conn = sqlite3.connect('admin_processes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            process_name TEXT NOT NULL,
            start_time DATETIME NOT NULL,
            end_time DATETIME NOT NULL,
            duration REAL NOT NULL
        )
    ''')
    conn.commit()
    return conn


def generate_report(process_name, start_time, end_time):
    """Generate a report for an administrative process and save it to the database."""
    try:
        # Validate datetime input
        if end_time < start_time:
            raise ValueError("End time must be greater than start time.")

        # Create database connection
        conn = create_db()
        
        # Create report instance
        report = Report(process_name, start_time, end_time)
        report.save_to_db(conn)
        
        print(f"Report generated for process: {process_name} with duration: {report.duration} seconds")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # Example usage
    process_name = "Documentation Approval"
    start_time = datetime(2023, 10, 1, 9, 0, 0)  # Start time
    end_time = datetime(2023, 10, 1, 9, 30, 0)    # End time

    generate_report(process_name, start_time, end_time)
```
