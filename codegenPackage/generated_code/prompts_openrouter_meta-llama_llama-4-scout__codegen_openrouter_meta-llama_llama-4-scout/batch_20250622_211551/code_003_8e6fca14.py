"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: Design a database schema for storing user information, membership details, and event data for a networking platform like Sync Connects.
Generated: DETERMINISTIC_8e6fca14fe1cb106
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Sync Connects
CREATE DATABASE sync_connects;

-- Use the database
USE sync_connects;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for membership plans
CREATE TABLE membership_plans (
  id INT AUTO_INCREMENT,
  plan_name VARCHAR(100) NOT NULL,
  plan_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user memberships
CREATE TABLE user_memberships (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  membership_plan_id INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (membership_plan_id) REFERENCES membership_plans(id) ON DELETE CASCADE
);

-- Create table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  event_name VARCHAR(255) NOT NULL,
  event_description TEXT,
  event_date DATE NOT NULL,
  event_time TIME NOT NULL,
  location VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for event attendees
CREATE TABLE event_attendees (
  id INT AUTO_INCREMENT,
  event_id INT NOT NULL,
  user_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (event_id, user_id)
);

-- Create table for messages
CREATE TABLE messages (
  id INT AUTO_INCREMENT,
  sender_id INT NOT NULL,
  receiver_id INT NOT NULL,
  message TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (receiver_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create index on user email for faster lookup
CREATE INDEX idx_user_email ON users(email);

-- Create index on event name for faster lookup
CREATE INDEX idx_event_name ON events(event_name);
```

```python
# Python code to interact with the database

import mysql.connector
from mysql.connector import Error

class SyncConnectsDB:
    def __init__(self, host_name, db_name, user_name, user_password):
        self.host_name = host_name
        self.db_name = db_name
        self.user_name = user_name
        self.user_password = user_password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                database=self.db_name,
                user=self.user_name,
                password=self.user_password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error: '{e}'")

    def create_user(self, email, password_hash, first_name, last_name, phone_number):
        query = """
            INSERT INTO users (email, password_hash, first_name, last_name, phone_number)
            VALUES (%s, %s, %s, %s, %s)
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (email, password_hash, first_name, last_name, phone_number))
            self.connection.commit()
            print("User created successfully")
        except Error as e:
            print(f"Error: '{e}'")

    def get_user(self, email):
        query = """
            SELECT * FROM users
            WHERE email = %s
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            return user
        except Error as e:
            print(f"Error: '{e}'")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    db = SyncConnectsDB("localhost", "sync_connects", "root", "password")
    db.connect()
    db.create_user("john@example.com", "password_hash", "John", "Doe", "1234567890")
    user = db.get_user("john@example.com")
    print(user)
    db.close_connection()
```
