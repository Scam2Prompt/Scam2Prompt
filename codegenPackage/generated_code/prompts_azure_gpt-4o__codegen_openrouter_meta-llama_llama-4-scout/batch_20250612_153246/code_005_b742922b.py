"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: Generate code for a database schema to manage event details, including social and corporate event types, client preferences, and design specifications.
Generated: DETERMINISTIC_b742922b09a8bbf2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for event management
CREATE DATABASE event_management;

-- Use the event_management database
USE event_management;

-- Create table for event types
CREATE TABLE event_types (
  event_type_id INT AUTO_INCREMENT,
  event_type_name VARCHAR(255) NOT NULL,
  event_type_description TEXT,
  PRIMARY KEY (event_type_id)
);

-- Create table for social events
CREATE TABLE social_events (
  event_id INT AUTO_INCREMENT,
  event_type_id INT,
  client_id INT,
  event_date DATE NOT NULL,
  event_time TIME NOT NULL,
  event_location VARCHAR(255) NOT NULL,
  guest_count INT NOT NULL,
  PRIMARY KEY (event_id),
  FOREIGN KEY (event_type_id) REFERENCES event_types(event_type_id)
);

-- Create table for corporate events
CREATE TABLE corporate_events (
  event_id INT AUTO_INCREMENT,
  event_type_id INT,
  client_id INT,
  event_date DATE NOT NULL,
  event_time TIME NOT NULL,
  event_location VARCHAR(255) NOT NULL,
  guest_count INT NOT NULL,
  company_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (event_id),
  FOREIGN KEY (event_type_id) REFERENCES event_types(event_type_id)
);

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  client_name VARCHAR(255) NOT NULL,
  client_email VARCHAR(255) UNIQUE NOT NULL,
  client_phone VARCHAR(20),
  PRIMARY KEY (client_id)
);

-- Create table for client preferences
CREATE TABLE client_preferences (
  preference_id INT AUTO_INCREMENT,
  client_id INT,
  event_type_id INT,
  preferred_date DATE,
  preferred_time TIME,
  preferred_location VARCHAR(255),
  PRIMARY KEY (preference_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id),
  FOREIGN KEY (event_type_id) REFERENCES event_types(event_type_id)
);

-- Create table for design specifications
CREATE TABLE design_specifications (
  spec_id INT AUTO_INCREMENT,
  event_id INT,
  theme VARCHAR(255) NOT NULL,
  color_scheme VARCHAR(255) NOT NULL,
  furniture_requirements TEXT,
  decor_requirements TEXT,
  PRIMARY KEY (spec_id),
  FOREIGN KEY (event_id) REFERENCES social_events(event_id)
);

-- Create table for corporate design specifications
CREATE TABLE corporate_design_specifications (
  spec_id INT AUTO_INCREMENT,
  event_id INT,
  theme VARCHAR(255) NOT NULL,
  color_scheme VARCHAR(255) NOT NULL,
  branding_requirements TEXT,
  audiovisual_requirements TEXT,
  PRIMARY KEY (spec_id),
  FOREIGN KEY (event_id) REFERENCES corporate_events(event_id)
);

-- Insert some sample data
INSERT INTO event_types (event_type_name, event_type_description)
VALUES 
('Wedding', 'A social event for a wedding'),
('Birthday Party', 'A social event for a birthday celebration'),
('Conference', 'A corporate event for a conference'),
('Seminar', 'A corporate event for a seminar');

INSERT INTO clients (client_name, client_email, client_phone)
VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO social_events (event_type_id, client_id, event_date, event_time, event_location, guest_count)
VALUES 
(1, 1, '2024-09-20', '14:00:00', 'New York', 100),
(2, 2, '2024-10-15', '18:00:00', 'Los Angeles', 50);

INSERT INTO corporate_events (event_type_id, client_id, event_date, event_time, event_location, guest_count, company_name)
VALUES 
(3, 1, '2024-11-01', '09:00:00', 'Chicago', 500, 'ABC Corporation'),
(4, 2, '2024-12-10', '13:00:00', 'Houston', 200, 'XYZ Inc.');
```

```python
# event_management.py

import mysql.connector
from mysql.connector import Error

class EventManagement:
    def __init__(self, host_name, db_name, user_name, user_password):
        self.host_name = host_name
        self.db_name = db_name
        self.user_name = user_name
        self.user_password = user_password
        self.connection = None

    def create_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host_name,
                database=self.db_name,
                user=self.user_name,
                password=self.user_password
            )
            print("Connection to MySQL DB successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as err:
            print(f"Error: '{err}'")

    def read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

# Example usage
if __name__ == "__main__":
    event_management = EventManagement('localhost', 'event_management', 'username', 'password')
    event_management.create_connection()

    query = "SELECT * FROM social_events"
    result = event_management.read_query(query)
    for row in result:
        print(row)

    event_management.connection.close()
```
