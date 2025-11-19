"""
Generated Code Metadata:
========================
Original URL: https://learnercamp.com
Prompt: Design a database schema for storing online course materials and user progress.
Generated: DETERMINISTIC_4ee192718ec6f0bd
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for online course materials
CREATE DATABASE online_courses;

-- Use the online_courses database
USE online_courses;

-- Create a table for courses
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id)
);

-- Create a table for course materials
CREATE TABLE course_materials (
  material_id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  material_type ENUM('video', 'pdf', 'quiz') NOT NULL,
  title VARCHAR(255) NOT NULL,
  content BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id),
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- Create a table for users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Create a table for user progress
CREATE TABLE user_progress (
  progress_id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  course_id INT NOT NULL,
  material_id INT,
  completed BOOLEAN DEFAULT FALSE,
  last_accessed TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (progress_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
  FOREIGN KEY (material_id) REFERENCES course_materials(material_id) ON DELETE SET NULL
);

-- Create a table for course enrollments
CREATE TABLE course_enrollments (
  enrollment_id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  course_id INT NOT NULL,
  enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (enrollment_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
  FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
  UNIQUE (user_id, course_id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_courses_title ON courses (title);
CREATE INDEX idx_course_materials_course_id ON course_materials (course_id);
CREATE INDEX idx_user_progress_user_id ON user_progress (user_id);
CREATE INDEX idx_user_progress_course_id ON user_progress (course_id);
CREATE INDEX idx_course_enrollments_user_id ON course_enrollments (user_id);
CREATE INDEX idx_course_enrollments_course_id ON course_enrollments (course_id);
```

```python
# models.py
import mysql.connector
from mysql.connector import Error

class OnlineCourseDatabase:
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

    def create_tables(self):
        if self.connection:
            cursor = self.connection.cursor()
            with open('schema.sql', 'r') as f:
                schema = f.read()
            cursor.execute(schema, multi=True)
            self.connection.commit()
            print("Tables created")
        else:
            print("Not connected to database")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    db = OnlineCourseDatabase('localhost', 'online_courses', 'root', 'password')
    db.connect()
    db.create_tables()
    db.close_connection()
```
