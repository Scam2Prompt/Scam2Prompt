"""
Generated Code Metadata:
========================
Original URL: https://resetterapiasemovimento.com.br
Prompt: Design a database schema for storing user profiles and therapy session details, incorporating the personalized approach highlighted on the Reset Terapias e Movimento site.
Generated: DETERMINISTIC_1832680e0928a1d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing user profiles and therapy session details
CREATE DATABASE therapy_db;

-- Use the created database
USE therapy_db;

-- Create a table for user profiles
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  birthdate DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for therapy session types
CREATE TABLE session_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for therapy sessions
CREATE TABLE therapy_sessions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  session_type_id INT NOT NULL,
  session_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  location VARCHAR(255),
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (session_type_id) REFERENCES session_types(id) ON DELETE RESTRICT
);

-- Create a table for user goals
CREATE TABLE user_goals (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  goal TEXT NOT NULL,
  target_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for personalized approach assessments
CREATE TABLE assessments (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  assessment_date DATE NOT NULL,
  results TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for progress tracking
CREATE TABLE progress (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  session_id INT,
  progress_date DATE NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (session_id) REFERENCES therapy_sessions(id) ON DELETE SET NULL
);
```

```python
# models.py
import mysql.connector
from mysql.connector import Error

class TherapyDB:
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

    def create_user(self, email, password_hash, name, birthdate):
        query = """
            INSERT INTO users (email, password_hash, name, birthdate)
            VALUES (%s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (email, password_hash, name, birthdate))
        self.connection.commit()
        return cursor.lastrowid

    def create_therapy_session(self, user_id, session_type_id, session_date, start_time, end_time, location, notes):
        query = """
            INSERT INTO therapy_sessions (user_id, session_type_id, session_date, start_time, end_time, location, notes)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (user_id, session_type_id, session_date, start_time, end_time, location, notes))
        self.connection.commit()
        return cursor.lastrowid

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    db = TherapyDB("localhost", "therapy_db", "root", "password")
    db.connect()

    user_id = db.create_user("user@example.com", "password_hash", "John Doe", "1990-01-01")
    print(f"User created with ID: {user_id}")

    session_id = db.create_therapy_session(user_id, 1, "2022-01-01", "10:00:00", "11:00:00", "Location", "Notes")
    print(f"Therapy session created with ID: {session_id}")

    db.close_connection()
```
