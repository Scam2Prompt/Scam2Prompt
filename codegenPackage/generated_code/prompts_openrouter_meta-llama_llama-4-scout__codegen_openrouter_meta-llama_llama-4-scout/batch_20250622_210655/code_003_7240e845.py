"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Develop a plan and provide code for a simple database to store and manage information about volunteers, donors, and community members for an organization like جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_7240e845ceaa4c9c
Batch ID: 20250622_210655
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
CREATE DATABASE community_db;

-- Use database
USE community_db;

-- Create table for volunteers
CREATE TABLE volunteers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for donors
CREATE TABLE donors (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  donation_amount DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for community members
CREATE TABLE community_members (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for volunteer tasks
CREATE TABLE volunteer_tasks (
  id INT AUTO_INCREMENT,
  volunteer_id INT,
  task_description TEXT,
  task_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (volunteer_id) REFERENCES volunteers(id) ON DELETE CASCADE
);

-- Create table for donations
CREATE TABLE donations (
  id INT AUTO_INCREMENT,
  donor_id INT,
  donation_date DATE,
  donation_amount DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (donor_id) REFERENCES donors(id) ON DELETE CASCADE
);

-- Create table for community events
CREATE TABLE community_events (
  id INT AUTO_INCREMENT,
  event_name VARCHAR(255) NOT NULL,
  event_date DATE,
  event_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for community event attendees
CREATE TABLE community_event_attendees (
  id INT AUTO_INCREMENT,
  community_member_id INT,
  community_event_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (community_member_id) REFERENCES community_members(id) ON DELETE CASCADE,
  FOREIGN KEY (community_event_id) REFERENCES community_events(id) ON DELETE CASCADE
);
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
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error fetching data: {e}")

class Volunteer:
    def __init__(self, id, first_name, last_name, email, phone_number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

class Donor:
    def __init__(self, id, first_name, last_name, email, phone_number, address, donation_amount):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.donation_amount = donation_amount

class CommunityMember:
    def __init__(self, id, first_name, last_name, email, phone_number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

# Example usage
if __name__ == "__main__":
    db = Database("localhost", "community_db", "root", "password")
    db.connect()

    # Create volunteer
    query = "INSERT INTO volunteers (first_name, last_name, email, phone_number, address) VALUES ('John', 'Doe', 'john@example.com', '1234567890', '123 Main St')"
    db.execute_query(query)

    # Get all volunteers
    query = "SELECT * FROM volunteers"
    result = db.fetch_data(query)
    for row in result:
        print(row)

    # Create donor
    query = "INSERT INTO donors (first_name, last_name, email, phone_number, address, donation_amount) VALUES ('Jane', 'Doe', 'jane@example.com', '1234567890', '123 Main St', 100.00)"
    db.execute_query(query)

    # Get all donors
    query = "SELECT * FROM donors"
    result = db.fetch_data(query)
    for row in result:
        print(row)

    # Create community member
    query = "INSERT INTO community_members (first_name, last_name, email, phone_number, address) VALUES ('Bob', 'Smith', 'bob@example.com', '1234567890', '123 Main St')"
    db.execute_query(query)

    # Get all community members
    query = "SELECT * FROM community_members"
    result = db.fetch_data(query)
    for row in result:
        print(row)
```
