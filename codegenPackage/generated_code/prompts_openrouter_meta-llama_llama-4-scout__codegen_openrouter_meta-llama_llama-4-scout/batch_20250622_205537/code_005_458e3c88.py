"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Design a basic database schema to store information about clients, cases, and appointments for a law firm like Majeli Avocat, and suggest a suitable programming language for implementation.
Generated: DETERMINISTIC_458e3c885158b79d
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema and Implementation**
=====================================

### Suggested Programming Language: Python

### Database Schema

We will use MySQL as our database management system.

```sql
-- schema.sql

CREATE DATABASE majeli_avocat;

USE majeli_avocat;

CREATE TABLE clients (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `address` TEXT,
  PRIMARY KEY (`id`)
);

CREATE TABLE cases (
  `id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `case_type` VARCHAR(255) NOT NULL,
  `case_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`id`) ON DELETE CASCADE
);

CREATE TABLE appointments (
  `id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `case_id` INT,
  `appointment_date` DATE NOT NULL,
  `appointment_time` TIME NOT NULL,
  `location` VARCHAR(255),
  `description` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`client_id`) REFERENCES clients(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`case_id`) REFERENCES cases(`id`) ON DELETE SET NULL
);

CREATE TABLE users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) UNIQUE NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` ENUM('admin', 'lawyer') NOT NULL,
  PRIMARY KEY (`id`)
);
```

### Python Implementation

```python
# main.py

import mysql.connector
from mysql.connector import Error
from datetime import datetime

class MajeliAvocatDB:
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
            print("Connected to database successfully")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_client(self, first_name, last_name, email, phone, address):
        query = """
            INSERT INTO clients (first_name, last_name, email, phone, address)
            VALUES (%s, %s, %s, %s, %s)
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (first_name, last_name, email, phone, address))
            self.connection.commit()
            print("Client created successfully")
        except Error as e:
            print(f"Error creating client: {e}")

    def create_case(self, client_id, case_type, case_description):
        query = """
            INSERT INTO cases (client_id, case_type, case_description)
            VALUES (%s, %s, %s)
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (client_id, case_type, case_description))
            self.connection.commit()
            print("Case created successfully")
        except Error as e:
            print(f"Error creating case: {e}")

    def create_appointment(self, client_id, case_id, appointment_date, appointment_time, location, description):
        query = """
            INSERT INTO appointments (client_id, case_id, appointment_date, appointment_time, location, description)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (client_id, case_id, appointment_date, appointment_time, location, description))
            self.connection.commit()
            print("Appointment created successfully")
        except Error as e:
            print(f"Error creating appointment: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    db = MajeliAvocatDB("localhost", "majeli_avocat", "root", "password")
    db.connect()

    db.create_client("John", "Doe", "john.doe@example.com", "1234567890", "123 Main St")
    db.create_case(1, "Civil", "Client seeking damages")
    db.create_appointment(1, 1, "2024-09-17", "10:00:00", "Courtroom 1", "Initial consultation")

    db.close_connection()
```

### Requirements

* Python 3.8+
* mysql-connector-python library (`pip install mysql-connector-python`)

### Usage

1. Create a new MySQL database and user.
2. Run the `schema.sql` script to create the database schema.
3. Update the `main.py` script with your database credentials.
4. Run the `main.py` script to test the database implementation.
