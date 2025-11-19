"""
Generated Code Metadata:
========================
Original URL: https://getupenergy.co.uk
Prompt: Design a basic database schema to store information about massage therapy services, including different types of massages, therapists, and client appointments.
Generated: DETERMINISTIC_eda7e32ee96a90e9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for massage therapy services
CREATE DATABASE massage_therapy;

-- Use the database
USE massage_therapy;

-- Create table for massage types
CREATE TABLE massage_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for therapists
CREATE TABLE therapists (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for therapist specialties
CREATE TABLE therapist_specialties (
  therapist_id INT NOT NULL,
  massage_type_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (therapist_id, massage_type_id),
  FOREIGN KEY (therapist_id) REFERENCES therapists(id) ON DELETE CASCADE,
  FOREIGN KEY (massage_type_id) REFERENCES massage_types(id) ON DELETE CASCADE
);

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for appointments
CREATE TABLE appointments (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  therapist_id INT NOT NULL,
  massage_type_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (therapist_id) REFERENCES therapists(id) ON DELETE CASCADE,
  FOREIGN KEY (massage_type_id) REFERENCES massage_types(id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  appointment_id INT NOT NULL,
  payment_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE
);
```

```python
# models.py
import mysql.connector
from mysql.connector import Error

class MassageTherapyDB:
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
        if self.connection:
            cursor = self.connection.cursor()
            with open('schema.sql', 'r') as f:
                schema = f.read()
            cursor.execute(schema, multi=True)
            self.connection.commit()
            print("Tables created")
        else:
            print("Not connected to database")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

# Example usage
if __name__ == "__main__":
    db = MassageTherapyDB('localhost', 'massage_therapy', 'root', 'password')
    db.connect()
    db.create_tables()
    db.close_connection()
```
