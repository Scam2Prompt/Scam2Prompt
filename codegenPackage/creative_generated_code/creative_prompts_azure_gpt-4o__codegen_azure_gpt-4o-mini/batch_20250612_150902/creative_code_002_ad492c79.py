"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medicidsas.com
Prompt: Generate code using a database management system to store and retrieve occupational health examination records, including tests like electrocardiograms and radiology results, as outlined on Medicid IPS's services page.
Generated: DETERMINISTIC_ad492c79a2b284b5
Batch ID: 20250612_150902
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

# Define a function to create a database connection
def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"Error '{e}' occurred")
    return conn

# Define a function to create the examination records table
def create_table(conn):
    """ Create a table for storing occupational health examination records """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS health_examinations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        examination_date TEXT NOT NULL,
        test_type TEXT NOT NULL,
        results TEXT NOT NULL,
        notes TEXT,
        FOREIGN KEY (patient_id) REFERENCES patients (id)
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Table created successfully")
    except Error as e:
        print(f"Error '{e}' occurred")

# Define a function to insert a new health examination record
def insert_health_examination(conn, patient_id, examination_date, test_type, results, notes=None):
    """ Insert a new health examination record into the health_examinations table """
    sql = ''' INSERT INTO health_examinations(patient_id, examination_date, test_type, results, notes)
              VALUES(?,?,?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (patient_id, examination_date, test_type, results, notes))
        conn.commit()
        print("Health examination record added successfully")
    except Error as e:
        print(f"Error '{e}' occurred")

# Define a function to retrieve health examination records by patient ID
def get_health_examinations_by_patient(conn, patient_id):
    """ Query health examinations by patient ID """
    sql = 'SELECT * FROM health_examinations WHERE patient_id=?'
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (patient_id,))
        records = cursor.fetchall()
        return records
    except Error as e:
        print(f"Error '{e}' occurred")
        return []

# Example usage
if __name__ == "__main__":
    database = "health_records.db"

    # Create a database connection
    conn = create_connection(database)

    if conn:
        # Create the health examinations table
        create_table(conn)

        # Insert example records (Replace with actual data)
        insert_health_examination(conn, 1, '2023-10-01', 'Electrocardiogram', 'Normal', 'No issues detected')
        insert_health_examination(conn, 1, '2023-10-02', 'Radiology', 'Mild abnormalities', 'Follow-up recommended')

        # Retrieve records for patient with ID 1
        records = get_health_examinations_by_patient(conn, 1)
        print("Health Examination Records for Patient ID 1:")
        for record in records:
            print(record)

        # Close the database connection
        conn.close()
    else:
        print("Error! Cannot create the database connection.")
```
