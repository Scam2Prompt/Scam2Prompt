"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Develop a program that connects students with RNW International's scholarship opportunities for studying in Canada or the UK.
Generated: DETERMINISTIC_137654a53ae6e89b
Batch ID: 20250612_155322
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rnwinternational.org/api/scholarships": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import requests
import json

# Define constants for RNW International API
API_BASE_URL = "https://rnwinternational.org/api/scholarships"
SUPPORTED_COUNTRIES = ["Canada", "UK"]

# Database initialization
DB_NAME = "scholarship_connector.db"

def initialize_database():
    """Initializes the SQLite database and creates necessary tables."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        # Create students table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            country_preference TEXT NOT NULL
        )
        ''')
        # Create scholarships table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS scholarships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            scholarship_name TEXT NOT NULL,
            scholarship_details TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def add_student(name, email, country_preference):
    """
    Adds a new student to the database.
    :param name: Student's name
    :param email: Student's email
    :param country_preference: Preferred country for scholarships
    """
    if country_preference not in SUPPORTED_COUNTRIES:
        print(f"Error: {country_preference} is not supported. Choose Canada or UK.")
        return
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO students (name, email, country_preference)
        VALUES (?, ?, ?)
        ''', (name, email, country_preference))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. Email might already exist.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def fetch_scholarships(country_preference):
    """
    Fetches scholarships from RNW International API.
    :param country_preference: Preferred country for scholarships
    :return: List of scholarships
    """
    try:
        response = requests.get(f"{API_BASE_URL}?country={country_preference}")
        response.raise_for_status()  # Raise HTTPError for bad responses
        scholarships = response.json()
        return scholarships
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return []

def connect_scholarships_to_students():
    """Fetches scholarships and connects them to students in the database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, country_preference FROM students")
        students = cursor.fetchall()
        
        for student_id, country_preference in students:
            scholarships = fetch_scholarships(country_preference)
            for scholarship in scholarships:
                cursor.execute('''
                INSERT INTO scholarships (student_id, scholarship_name, scholarship_details)
                VALUES (?, ?, ?)
                ''', (student_id, scholarship['name'], json.dumps(scholarship)))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def display_student_scholarships():
    """Displays all students and their connected scholarships."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT students.name, students.email, students.country_preference, scholarships.scholarship_name
        FROM students
        LEFT JOIN scholarships ON students.id = scholarships.student_id
        """)
        rows = cursor.fetchall()
        for row in rows:
            name, email, country, scholarship_name = row
            print(f"Student: {name}, Email: {email}, Country: {country}, Scholarship: {scholarship_name}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

# Main program entry point
if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Example usage
    add_student("Alice Johnson", "alice@example.com", "Canada")
    add_student("Bob Smith", "bob@example.com", "UK")
    
    connect_scholarships_to_students()
    display_student_scholarships()
```
