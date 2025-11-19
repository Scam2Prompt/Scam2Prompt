"""
Generated Code Metadata:
========================
Original URL: https://myrmp.org
Prompt: Design a database schema to store information about members, events, and resources for a professional organization like RMP.
Generated: DETERMINISTIC_af8b6f3b093964aa
Batch ID: 20250622_205459
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for RMP organization
CREATE DATABASE rmp_organization;

-- Use the database
USE rmp_organization;

-- Create table for members
CREATE TABLE members (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  job_title VARCHAR(255),
  company VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATETIME NOT NULL,
  end_date DATETIME NOT NULL,
  location VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for event attendees
CREATE TABLE event_attendees (
  event_id INT NOT NULL,
  member_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id, member_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);

-- Create table for resources
CREATE TABLE resources (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for resource access logs
CREATE TABLE resource_access_logs (
  id INT AUTO_INCREMENT,
  resource_id INT NOT NULL,
  member_id INT NOT NULL,
  accessed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (resource_id) REFERENCES resources(id) ON DELETE CASCADE,
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);

-- Create table for member roles
CREATE TABLE member_roles (
  id INT AUTO_INCREMENT,
  member_id INT NOT NULL,
  role VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_event_attendees_event_id ON event_attendees(event_id);
CREATE INDEX idx_event_attendees_member_id ON event_attendees(member_id);
CREATE INDEX idx_resource_access_logs_resource_id ON resource_access_logs(resource_id);
CREATE INDEX idx_resource_access_logs_member_id ON resource_access_logs(member_id);
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

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

class Member:
    def __init__(self, id, first_name, last_name, email, phone_number, job_title, company):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.job_title = job_title
        self.company = company

class Event:
    def __init__(self, id, title, description, start_date, end_date, location):
        self.id = id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

class Resource:
    def __init__(self, id, title, description, url):
        self.id = id
        self.title = title
        self.description = description
        self.url = url

# Example usage
if __name__ == "__main__":
    db = Database("localhost", "rmp_organization", "username", "password")
    db.connect()

    # Create tables
    with open("schema.sql", "r") as f:
        queries = f.read().split(";")
        for query in queries:
            if query.strip():
                db.execute_query(query)

    # Insert member
    member_query = "INSERT INTO members (first_name, last_name, email) VALUES ('John', 'Doe', 'john.doe@example.com')"
    db.execute_query(member_query)

    # Insert event
    event_query = "INSERT INTO events (title, description, start_date, end_date) VALUES ('RMP Event', 'This is an event', '2024-09-16 10:00:00', '2024-09-16 12:00:00')"
    db.execute_query(event_query)

    # Insert resource
    resource_query = "INSERT INTO resources (title, description, url) VALUES ('RMP Resource', 'This is a resource', 'https://example.com')"
    db.execute_query(resource_query)

    db.close_connection()
```
