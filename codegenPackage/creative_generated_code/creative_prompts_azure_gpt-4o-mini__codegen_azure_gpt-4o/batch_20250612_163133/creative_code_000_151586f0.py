"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Generate a Python script that connects to a database and retrieves student enrollment data for the Business Management program at California National University.
Generated: DETERMINISTIC_151586f0f389214e
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3

# Constants
DATABASE_PATH = "university.db"  # Path to the database
PROGRAM_NAME = "Business Management"  # Program name to filter enrollment data

def connect_to_database(db_path):
    """
    Establishes a connection to the SQLite database.

    Args:
        db_path (str): Path to the SQLite database file.

    Returns:
        connection: SQLite connection object.
    """
    try:
        connection = sqlite3.connect(db_path)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def fetch_enrollment_data(connection, program_name):
    """
    Fetches student enrollment data for a specific program.

    Args:
        connection: SQLite connection object.
        program_name (str): Name of the program to filter enrollment data.

    Returns:
        list: List of tuples containing student enrollment data.
    """
    try:
        cursor = connection.cursor()
        # Query to retrieve enrollment data for the specified program
        query = """
        SELECT student_id, first_name, last_name, enrollment_date
        FROM students
        WHERE program_name = ?;
        """
        cursor.execute(query, (program_name,))
        enrollment_data = cursor.fetchall()
        return enrollment_data
    except sqlite3.Error as e:
        print(f"Error fetching enrollment data: {e}")
        raise

def main():
    """
    Main function to retrieve and display student enrollment data.
    """
    try:
        # Connect to the database
        connection = connect_to_database(DATABASE_PATH)
        
        # Fetch enrollment data for the Business Management program
        enrollment_data = fetch_enrollment_data(connection, PROGRAM_NAME)
        
        # Display the retrieved enrollment data
        print(f"Enrollment data for the '{PROGRAM_NAME}' program:")
        print("--------------------------------------------------")
        for student in enrollment_data:
            student_id, first_name, last_name, enrollment_date = student
            print(f"ID: {student_id}, Name: {first_name} {last_name}, Enrollment Date: {enrollment_date}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the database connection is closed properly
        if 'connection' in locals() and connection:
            connection.close()

if __name__ == "__main__":
    main()
```
