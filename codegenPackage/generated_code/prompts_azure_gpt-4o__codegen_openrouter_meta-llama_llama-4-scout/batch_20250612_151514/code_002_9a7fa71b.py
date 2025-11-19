"""
Generated Code Metadata:
========================
Original URL: https://pooltyme.app
Prompt: Generate a Python script for logging pool maintenance tasks and storing log history, inspired by the functionality of Pooltyme.
Generated: DETERMINISTIC_9a7fa71bd0f673b9
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import sqlite3
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PoolMaintenanceLogger:
    def __init__(self, db_name):
        """
        Initialize the PoolMaintenanceLogger with a database name.

        :param db_name: The name of the SQLite database file.
        """
        self.db_name = db_name
        self.logger = logging.getLogger(__name__)
        self.create_table()

    def create_table(self):
        """
        Create the 'logs' table in the SQLite database if it doesn't exist.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS logs
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     date TEXT, 
                     task TEXT, 
                     notes TEXT)
                ''')
                conn.commit()
        except sqlite3.Error as e:
            self.logger.error(f"Error creating table: {e}")

    def log_task(self, task, notes=None):
        """
        Log a pool maintenance task.

        :param task: The task performed (e.g., "Cleaned filter").
        :param notes: Any additional notes about the task.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute('INSERT INTO logs (date, task, notes) VALUES (?, ?, ?)', 
                               (date, task, notes))
                conn.commit()
                self.logger.info(f"Logged task: {task}")
        except sqlite3.Error as e:
            self.logger.error(f"Error logging task: {e}")

    def get_log_history(self):
        """
        Retrieve the log history.

        :return: A list of tuples containing the log history.
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM logs ORDER BY date DESC')
                return cursor.fetchall()
        except sqlite3.Error as e:
            self.logger.error(f"Error retrieving log history: {e}")
            return []

def main():
    logger = PoolMaintenanceLogger('pool_maintenance.db')

    while True:
        print("\n1. Log a task")
        print("2. View log history")
        print("3. Quit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            notes = input("Enter any notes (optional): ")
            if notes == "":
                notes = None
            logger.log_task(task, notes)
        elif choice == "2":
            log_history = logger.get_log_history()
            for log in log_history:
                print(f"ID: {log[0]} - Date: {log[1]} - Task: {log[2]} - Notes: {log[3]}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
