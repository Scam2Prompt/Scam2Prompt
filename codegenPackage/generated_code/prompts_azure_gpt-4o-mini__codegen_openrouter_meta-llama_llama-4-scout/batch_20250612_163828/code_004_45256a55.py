"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Design a database schema for managing the events and volunteers associated with Springs International Ministries' programs.
Generated: DETERMINISTIC_45256a5559149105
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Springs International Ministries
CREATE DATABASE springs_international_ministries;

-- Use the database schema
USE springs_international_ministries;

-- Create table for events
CREATE TABLE events (
    event_id INT AUTO_INCREMENT,
    event_name VARCHAR(255) NOT NULL,
    event_description TEXT,
    event_date DATE NOT NULL,
    event_start_time TIME NOT NULL,
    event_end_time TIME NOT NULL,
    event_location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id)
);

-- Create table for volunteers
CREATE TABLE volunteers (
    volunteer_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (volunteer_id)
);

-- Create table for event_volunteers (many-to-many relationship)
CREATE TABLE event_volunteers (
    event_id INT NOT NULL,
    volunteer_id INT NOT NULL,
    role VARCHAR(255),
    hours_committed INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id, volunteer_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (volunteer_id) REFERENCES volunteers(volunteer_id) ON DELETE CASCADE
);

-- Create table for event_types (optional)
CREATE TABLE event_types (
    event_type_id INT AUTO_INCREMENT,
    event_type_name VARCHAR(255) NOT NULL,
    event_type_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_type_id)
);

-- Create table for event_event_types (many-to-many relationship)
CREATE TABLE event_event_types (
    event_id INT NOT NULL,
    event_type_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (event_id, event_type_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (event_type_id) REFERENCES event_types(event_type_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_events_event_date ON events(event_date);
CREATE INDEX idx_events_event_name ON events(event_name);
CREATE INDEX idx_volunteers_email ON volunteers(email);
CREATE INDEX idx_event_volunteers_event_id ON event_volunteers(event_id);
CREATE INDEX idx_event_volunteers_volunteer_id ON event_volunteers(volunteer_id);
```

```python
# Python code using MySQL Connector to interact with the database

import mysql.connector
from mysql.connector import Error

class SpringsInternationalMinistriesDB:
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
            print("Connection to database established")
        except Error as error:
            print(f"Error: '{error}'")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as error:
            print(f"Error: '{error}'")

    def read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as error:
            print(f"Error: '{error}'")

# Example usage:
if __name__ == "__main__":
    db = SpringsInternationalMinistriesDB("localhost", "springs_international_ministries", "username", "password")
    db.create_connection()

    # Create tables
    db.execute_query("""
        CREATE TABLE IF NOT EXISTS events (
            event_id INT AUTO_INCREMENT,
            event_name VARCHAR(255) NOT NULL,
            event_description TEXT,
            event_date DATE NOT NULL,
            event_start_time TIME NOT NULL,
            event_end_time TIME NOT NULL,
            event_location VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (event_id)
        );
    """)

    # Insert event
    db.execute_query("""
        INSERT INTO events (event_name, event_description, event_date, event_start_time, event_end_time, event_location)
        VALUES ('Event 1', 'Description 1', '2024-09-17', '10:00:00', '12:00:00', 'Location 1');
    """)

    # Read events
    events = db.read_query("SELECT * FROM events;")
    for event in events:
        print(event)

    db.connection.close()
```
