"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eximiousglobal.com
Prompt: Develop a program to track and optimize time-to-fill metrics for recruitment processes, leveraging the data-driven approach mentioned in Eximious Global's RPO services.
Generated: DETERMINISTIC_736a23159a58fe21
Batch ID: 20250612_151811
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
import json

class RecruitmentTracker:
    def __init__(self, db_name='recruitment.db'):
        """Initialize the recruitment tracker with a SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create necessary tables in the database if they don't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS job_openings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                position TEXT NOT NULL,
                date_opened DATE NOT NULL,
                date_filled DATE,
                time_to_fill INTEGER
            )
        ''')
        self.connection.commit()

    def add_job_opening(self, position):
        """Add a new job opening to the database."""
        date_opened = datetime.now().date()
        self.cursor.execute('''
            INSERT INTO job_openings (position, date_opened)
            VALUES (?, ?)
        ''', (position, date_opened))
        self.connection.commit()

    def fill_job_opening(self, job_id):
        """Mark a job opening as filled and calculate time to fill."""
        date_filled = datetime.now().date()
        self.cursor.execute('''
            UPDATE job_openings
            SET date_filled = ?, time_to_fill = julianday(date_filled) - julianday(date_opened)
            WHERE id = ?
        ''', (date_filled, job_id))
        self.connection.commit()

    def get_time_to_fill_metrics(self):
        """Retrieve time-to-fill metrics for all job openings."""
        self.cursor.execute('SELECT position, time_to_fill FROM job_openings')
        return self.cursor.fetchall()

    def calculate_average_time_to_fill(self):
        """Calculate average time to fill across all job openings."""
        self.cursor.execute('SELECT AVG(time_to_fill) FROM job_openings WHERE time_to_fill IS NOT NULL')
        return self.cursor.fetchone()[0]

    def close(self):
        """Close the database connection."""
        self.connection.close()

if __name__ == '__main__':
    # Main execution block for interaction with the Recruitment Tracker
    tracker = RecruitmentTracker()

    try:
        # Example usage
        tracker.add_job_opening('Software Engineer')
        tracker.add_job_opening('Data Scientist')

        # Simulate filling a job
        tracker.fill_job_opening(1)  # Assuming job ID 1 exists
        tracker.fill_job_opening(2)  # Assuming job ID 2 exists

        # Retrieve and print time-to-fill metrics
        metrics = tracker.get_time_to_fill_metrics()
        print("Time-to-Fill Metrics:")
        print(json.dumps(metrics, indent=4))

        # Calculate and print average time to fill
        average_time = tracker.calculate_average_time_to_fill()
        print(f"Average Time to Fill: {average_time:.2f} days" if average_time is not None else "No data available for average time to fill.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        tracker.close()
```
