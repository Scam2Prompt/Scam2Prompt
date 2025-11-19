"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: "Generate a Python code snippet for managing polygraph test results, including patient information, test dates, and results, using a SQLite database."
Generated: DETERMINISTIC_3f50e54ba6f36d16
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime

class PolygraphTestResult:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             name TEXT NOT NULL, 
             date_of_birth TEXT NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS polygraph_tests
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             patient_id INTEGER NOT NULL, 
             test_date TEXT NOT NULL, 
             result TEXT NOT NULL,
             FOREIGN KEY (patient_id) REFERENCES patients (id))
        ''')

        self.conn.commit()

    def add_patient(self, name, date_of_birth):
        try:
            self.cursor.execute('INSERT INTO patients (name, date_of_birth) VALUES (?, ?)', 
                                (name, date_of_birth))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding patient: {e}")
            return None

    def add_polygraph_test(self, patient_id, test_date, result):
        try:
            self.cursor.execute('INSERT INTO polygraph_tests (patient_id, test_date, result) VALUES (?, ?, ?)', 
                                (patient_id, test_date, result))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding polygraph test: {e}")
            return None

    def get_patient_info(self, patient_id):
        try:
            self.cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error getting patient info: {e}")
            return None

    def get_polygraph_test_results(self, patient_id):
        try:
            self.cursor.execute('SELECT * FROM polygraph_tests WHERE patient_id = ?', (patient_id,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error getting polygraph test results: {e}")
            return None

    def close_connection(self):
        self.conn.close()


def main():
    db_name = 'polygraph_test_results.db'
    polygraph_test_result = PolygraphTestResult(db_name)

    # Add patient
    patient_id = polygraph_test_result.add_patient('John Doe', '1990-01-01')
    print(f"Patient ID: {patient_id}")

    # Add polygraph test results
    test_date1 = datetime.now().strftime('%Y-%m-%d')
    test_result1 = polygraph_test_result.add_polygraph_test(patient_id, test_date1, 'Pass')
    print(f"Test Result ID 1: {test_result1}")

    test_date2 = (datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    test_result2 = polygraph_test_result.add_polygraph_test(patient_id, test_date2, 'Fail')
    print(f"Test Result ID 2: {test_result2}")

    # Get patient info
    patient_info = polygraph_test_result.get_patient_info(patient_id)
    print(f"Patient Info: {patient_info}")

    # Get polygraph test results
    test_results = polygraph_test_result.get_polygraph_test_results(patient_id)
    print(f"Polygraph Test Results: {test_results}")

    polygraph_test_result.close_connection()


if __name__ == "__main__":
    main()
```
