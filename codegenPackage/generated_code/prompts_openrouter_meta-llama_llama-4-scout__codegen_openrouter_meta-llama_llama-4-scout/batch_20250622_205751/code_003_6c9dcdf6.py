"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Design a database schema to store information about program participants, courses, and training sessions for an organization like SKI Foundation.
Generated: DETERMINISTIC_6c9dcdf68d7ccc34
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for SKI Foundation
CREATE DATABASE ski_foundation;

-- Use ski_foundation database
USE ski_foundation;

-- Create table for participants
CREATE TABLE participants (
  participant_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (participant_id)
);

-- Create table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  course_name VARCHAR(255) NOT NULL,
  course_description TEXT,
  course_duration INT,
  course_capacity INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id)
);

-- Create table for training sessions
CREATE TABLE training_sessions (
  session_id INT AUTO_INCREMENT,
  course_id INT,
  session_date DATE NOT NULL,
  session_time TIME NOT NULL,
  session_location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (session_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create table for participant-course enrollment
CREATE TABLE participant_courses (
  participant_id INT,
  course_id INT,
  enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (participant_id, course_id),
  FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create table for participant-session attendance
CREATE TABLE participant_sessions (
  participant_id INT,
  session_id INT,
  attended BOOLEAN DEFAULT FALSE,
  attended_at TIMESTAMP,
  PRIMARY KEY (participant_id, session_id),
  FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
  FOREIGN KEY (session_id) REFERENCES training_sessions(session_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_participants_email ON participants(email);
CREATE INDEX idx_courses_course_name ON courses(course_name);
CREATE INDEX idx_training_sessions_course_id ON training_sessions(course_id);
CREATE INDEX idx_participant_courses_participant_id ON participant_courses(participant_id);
CREATE INDEX idx_participant_sessions_participant_id ON participant_sessions(participant_id);
```

```python
# models.py

import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error executing query: {e}")

    def fetch_data(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching data: {e}")
            return []

# Example usage
if __name__ == "__main__":
    db = Database("localhost", "ski_foundation", "root", "password")
    db.connect()

    # Create tables
    with open("schema.sql", "r") as f:
        queries = f.read().split(";")
        for query in queries:
            if query.strip():
                db.execute_query(query)

    # Insert sample data
    participants_query = "INSERT INTO participants (first_name, last_name, email) VALUES ('John', 'Doe', 'john.doe@example.com')"
    db.execute_query(participants_query)

    courses_query = "INSERT INTO courses (course_name, course_description) VALUES ('SKI Training', 'SKI training course')"
    db.execute_query(courses_query)

    # Fetch data
    participants_data = db.fetch_data("SELECT * FROM participants")
    print(participants_data)
```
