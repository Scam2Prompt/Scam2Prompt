"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Illustrate how to implement a quality assurance system for tracking the production quality of seamless steel pipes using a specific programming language.
Generated: DETERMINISTIC_cff6e11a7cd40d13
Batch ID: 20250612_161331
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
from datetime import datetime

class QualityAssuranceSystem:
    def __init__(self, db_file):
        """Initialize the QA system with a database connection."""
        self.connection = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connection to database established.")
        except Error as e:
            print(f"Error '{e}' occurred while connecting to the database.")
        return conn

    def create_table(self):
        """Create a table for tracking production quality of seamless steel pipes."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS quality_assurance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            production_date TEXT NOT NULL,
            pipe_id TEXT NOT NULL,
            quality_check BOOLEAN NOT NULL,
            remarks TEXT
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            print("Quality assurance table created.")
        except Error as e:
            print(f"Error '{e}' occurred while creating the table.")

    def log_quality_check(self, pipe_id, quality_check, remarks=""):
        """Log a quality check for a specific seamless steel pipe."""
        sql = """INSERT INTO quality_assurance (production_date, pipe_id, quality_check, remarks)
                 VALUES (?, ?, ?, ?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (datetime.now().isoformat(), pipe_id, quality_check, remarks))
            self.connection.commit()
            print("Quality check logged successfully.")
        except Error as e:
            print(f"Error '{e}' occurred while logging the quality check.")

    def get_quality_reports(self):
        """Retrieve all quality reports from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM quality_assurance")
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error '{e}' occurred while retrieving quality reports.")

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    db_path = "quality_assurance.db"
    qa_system = QualityAssuranceSystem(db_path)

    # Example usage
    qa_system.log_quality_check("PIPE123", True, "Passed all tests.")
    qa_system.log_quality_check("PIPE124", False, "Defective weld.")

    reports = qa_system.get_quality_reports()
    for report in reports:
        print(report)

    qa_system.close_connection()
```
