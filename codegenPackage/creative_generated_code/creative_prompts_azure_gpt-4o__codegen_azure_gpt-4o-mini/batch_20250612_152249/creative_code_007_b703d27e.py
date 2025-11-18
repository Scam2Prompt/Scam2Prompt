"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ruxindustrial.com.br
Prompt: Recommend software solutions for tracking and managing specialized industrial labor, inspired by Rux Industrial's focus on skilled workforce and project execution.
Generated: DETERMINISTIC_b703d27ed9719031
Batch ID: 20250612_152249
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

class LaborManagementSystem:
    """
    A class to manage and track specialized industrial labor.
    It allows adding workers, tracking their hours, and generating reports.
    """

    def __init__(self, db_name='labor_management.db'):
        """
        Initializes the LaborManagementSystem with a SQLite database.

        :param db_name: Name of the SQLite database file
        """
        self.connection = self.create_connection(db_name)
        self.create_tables()

    def create_connection(self, db_name):
        """
        Creates a database connection to the SQLite database.

        :param db_name: Name of the SQLite database file
        :return: SQLite connection object
        """
        try:
            conn = sqlite3.connect(db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_tables(self):
        """
        Creates the necessary tables in the database if they do not exist.
        """
        try:
            with self.connection:
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS workers (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        skill TEXT NOT NULL
                    );
                ''')
                self.connection.execute('''
                    CREATE TABLE IF NOT EXISTS labor_hours (
                        id INTEGER PRIMARY KEY,
                        worker_id INTEGER,
                        date TEXT NOT NULL,
                        hours INTEGER NOT NULL,
                        FOREIGN KEY (worker_id) REFERENCES workers (id)
                    );
                ''')
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def add_worker(self, name, skill):
        """
        Adds a new worker to the database.

        :param name: Name of the worker
        :param skill: Skill of the worker
        :return: Worker ID of the newly added worker
        """
        try:
            with self.connection:
                cursor = self.connection.execute('''
                    INSERT INTO workers (name, skill)
                    VALUES (?, ?);
                ''', (name, skill))
                return cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding worker: {e}")
            return None

    def log_hours(self, worker_id, hours):
        """
        Logs hours worked by a specific worker on the current date.

        :param worker_id: ID of the worker whose hours are to be logged
        :param hours: Number of hours worked
        """
        try:
            date = datetime.now().strftime("%Y-%m-%d")
            with self.connection:
                self.connection.execute('''
                    INSERT INTO labor_hours (worker_id, date, hours)
                    VALUES (?, ?, ?);
                ''', (worker_id, date, hours))
        except sqlite3.Error as e:
            print(f"Error logging hours: {e}")

    def generate_report(self, worker_id):
        """
        Generates a report of hours worked by a specific worker.

        :param worker_id: ID of the worker
        :return: List of tuples containing date and hours worked
        """
        try:
            cursor = self.connection.execute('''
                SELECT date, SUM(hours) FROM labor_hours
                WHERE worker_id = ?
                GROUP BY date;
            ''', (worker_id,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error generating report: {e}")
            return []

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

# Example usage:
if __name__ == "__main__":
    lms = LaborManagementSystem()
    worker_id = lms.add_worker("John Doe", "Welding")
    lms.log_hours(worker_id, 8)
    report = lms.generate_report(worker_id)
    print(report)
    lms.close_connection()
```
