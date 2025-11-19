"""
Generated Code Metadata:
========================
Original URL: https://standrewsibanda.org
Prompt: Design a simple database schema to store information about donors, children, and donations for a charity project like St. Andrew's School Project For The Young.
Generated: DETERMINISTIC_d6a97f55271ca67d
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for charity project
CREATE DATABASE charity_project;

-- Use charity project database
USE charity_project;

-- Create table for donors
CREATE TABLE donors (
  `donor_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`donor_id`)
);

-- Create table for children
CREATE TABLE children (
  `child_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `date_of_birth` DATE,
  `grade_level` VARCHAR(10),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`child_id`)
);

-- Create table for donations
CREATE TABLE donations (
  `donation_id` INT AUTO_INCREMENT,
  `donor_id` INT,
  `child_id` INT,
  `donation_date` DATE NOT NULL,
  `donation_amount` DECIMAL(10, 2) NOT NULL,
  `donation_type` ENUM('monetary', 'non-monetary') NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`donation_id`),
  FOREIGN KEY (`donor_id`) REFERENCES donors(`donor_id`) ON DELETE SET NULL,
  FOREIGN KEY (`child_id`) REFERENCES children(`child_id`) ON DELETE SET NULL
);

-- Create table for non-monetary donations
CREATE TABLE non_monetary_donations (
  `donation_id` INT,
  `item_description` TEXT NOT NULL,
  `item_condition` VARCHAR(255),
  `estimated_value` DECIMAL(10, 2),
  PRIMARY KEY (`donation_id`),
  FOREIGN KEY (`donation_id`) REFERENCES donations(`donation_id`) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO donors (`first_name`, `last_name`, `email`, `phone_number`, `address`)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO children (`first_name`, `last_name`, `date_of_birth`, `grade_level`)
VALUES 
('Emily', 'Chen', '2010-01-01', '5th'),
('Michael', 'Kim', '2008-06-01', '7th');

INSERT INTO donations (`donor_id`, `child_id`, `donation_date`, `donation_amount`, `donation_type`, `description`)
VALUES 
(1, 1, '2022-01-01', 100.00, 'monetary', 'New Year''s donation'),
(2, 2, '2022-06-01', 50.00, 'monetary', 'Mid-year donation');

INSERT INTO non_monetary_donations (`donation_id`, `item_description`, `item_condition`, `estimated_value`)
VALUES 
(3, 'Gently used books', 'Excellent', 20.00);
```

```python
# database.py

import mysql.connector
from mysql.connector import Error

class CharityDatabase:
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

  def disconnect(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Disconnected from database")

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

# Usage
if __name__ == "__main__":
  db = CharityDatabase('localhost', 'charity_project', 'root', 'password')
  db.connect()

  # Create tables
  with open('schema.sql', 'r') as f:
    queries = f.read().split(';')
    for query in queries:
      if query.strip():
        db.execute_query(query)

  # Insert data
  db.execute_query("INSERT INTO donors (`first_name`, `last_name`, `email`, `phone_number`, `address`) VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St')")

  # Fetch data
  result = db.fetch_data("SELECT * FROM donors")
  for row in result:
    print(row)

  db.disconnect()
```
