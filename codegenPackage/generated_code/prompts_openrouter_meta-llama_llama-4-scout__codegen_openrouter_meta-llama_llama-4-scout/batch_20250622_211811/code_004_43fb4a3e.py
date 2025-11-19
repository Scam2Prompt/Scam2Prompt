"""
Generated Code Metadata:
========================
Original URL: https://bitcoin100-maxair.com
Prompt: Design a simple database schema to store user information, educational resources, and connections between learners and finance experts, as described on the Bitcoin +100 Maxair website.
Generated: DETERMINISTIC_43fb4a3e8eee0c00
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS bitcoin_learners;

-- Use database
USE bitcoin_learners;

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  role ENUM('learner', 'expert', 'admin') NOT NULL DEFAULT 'learner',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for educational resources
CREATE TABLE IF NOT EXISTS resources (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for connections between learners and experts
CREATE TABLE IF NOT EXISTS connections (
  id INT AUTO_INCREMENT,
  learner_id INT NOT NULL,
  expert_id INT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (learner_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (expert_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (learner_id, expert_id)
);

-- Create table for messages between learners and experts
CREATE TABLE IF NOT EXISTS messages (
  id INT AUTO_INCREMENT,
  connection_id INT NOT NULL,
  sender_id INT NOT NULL,
  message TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (connection_id) REFERENCES connections(id) ON DELETE CASCADE,
  FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create index on foreign key columns
CREATE INDEX idx_connections_learner_id ON connections (learner_id);
CREATE INDEX idx_connections_expert_id ON connections (expert_id);
CREATE INDEX idx_messages_connection_id ON messages (connection_id);
CREATE INDEX idx_messages_sender_id ON messages (sender_id);
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

    def create_tables(self):
        with open('schema.sql', 'r') as f:
            schema = f.read()
        cursor = self.connection.cursor()
        try:
            cursor.executescript(schema)
            self.connection.commit()
            print("Tables created")
        except Error as e:
            print(f"Error creating tables: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

class User:
    def __init__(self, id, email, password_hash, name, role):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.name = name
        self.role = role

class Resource:
    def __init__(self, id, title, description, url):
        self.id = id
        self.title = title
        self.description = description
        self.url = url

class Connection:
    def __init__(self, id, learner_id, expert_id):
        self.id = id
        self.learner_id = learner_id
        self.expert_id = expert_id

class Message:
    def __init__(self, id, connection_id, sender_id, message):
        self.id = id
        self.connection_id = connection_id
        self.sender_id = sender_id
        self.message = message

# Example usage
if __name__ == "__main__":
    db = Database('localhost', 'bitcoin_learners', 'root', 'password')
    db.connect()
    db.create_tables()
    db.close_connection()
```
