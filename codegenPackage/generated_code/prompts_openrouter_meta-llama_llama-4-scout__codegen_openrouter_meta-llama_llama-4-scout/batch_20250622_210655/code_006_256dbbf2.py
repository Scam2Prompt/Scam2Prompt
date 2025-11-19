"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Design a database schema to store information about Chile Horse Riding's tours, guides, and horses, and provide a simple Python script to interact with the database.
Generated: DETERMINISTIC_256dbbf248a7bd5c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema (SQL)**
```sql
-- Create database
CREATE DATABASE chile_horse_riding;

-- Use database
USE chile_horse_riding;

-- Create table for tours
CREATE TABLE tours (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    duration INT NOT NULL,  -- in days
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for guides
CREATE TABLE guides (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    experience INT NOT NULL,  -- in years
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for horses
CREATE TABLE horses (
    id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    breed VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    height DECIMAL(5, 2) NOT NULL,  -- in meters
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for tour guides
CREATE TABLE tour_guides (
    tour_id INT NOT NULL,
    guide_id INT NOT NULL,
    PRIMARY KEY (tour_id, guide_id),
    FOREIGN KEY (tour_id) REFERENCES tours(id) ON DELETE CASCADE,
    FOREIGN KEY (guide_id) REFERENCES guides(id) ON DELETE CASCADE
);

-- Create table for tour horses
CREATE TABLE tour_horses (
    tour_id INT NOT NULL,
    horse_id INT NOT NULL,
    PRIMARY KEY (tour_id, horse_id),
    FOREIGN KEY (tour_id) REFERENCES tours(id) ON DELETE CASCADE,
    FOREIGN KEY (horse_id) REFERENCES horses(id) ON DELETE CASCADE
);
```

**Python Script (using MySQL Connector/Python)**
```python
import mysql.connector
from mysql.connector import Error

class ChileHorseRidingDB:
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

    def create_tour(self, name, description, duration, price):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO tours (name, description, duration, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, description, duration, price))
            self.connection.commit()
            print("Tour created successfully")
        except Error as e:
            print(f"Error creating tour: {e}")

    def create_guide(self, first_name, last_name, email, phone, experience):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO guides (first_name, last_name, email, phone, experience) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (first_name, last_name, email, phone, experience))
            self.connection.commit()
            print("Guide created successfully")
        except Error as e:
            print(f"Error creating guide: {e}")

    def create_horse(self, name, breed, age, height):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO horses (name, breed, age, height) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, breed, age, height))
            self.connection.commit()
            print("Horse created successfully")
        except Error as e:
            print(f"Error creating horse: {e}")

    def assign_guide_to_tour(self, tour_id, guide_id):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO tour_guides (tour_id, guide_id) VALUES (%s, %s)"
            cursor.execute(query, (tour_id, guide_id))
            self.connection.commit()
            print("Guide assigned to tour successfully")
        except Error as e:
            print(f"Error assigning guide to tour: {e}")

    def assign_horse_to_tour(self, tour_id, horse_id):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO tour_horses (tour_id, horse_id) VALUES (%s, %s)"
            cursor.execute(query, (tour_id, horse_id))
            self.connection.commit()
            print("Horse assigned to tour successfully")
        except Error as e:
            print(f"Error assigning horse to tour: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    db = ChileHorseRidingDB("localhost", "chile_horse_riding", "username", "password")
    db.connect()

    db.create_tour("Tour 1", "Description of tour 1", 3, 500.00)
    db.create_guide("John", "Doe", "john.doe@example.com", "1234567890", 5)
    db.create_horse("Horse 1", "Breed 1", 10, 1.60)

    db.assign_guide_to_tour(1, 1)
    db.assign_horse_to_tour(1, 1)

    db.close_connection()
```
