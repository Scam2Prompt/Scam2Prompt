"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Design a database schema for storing information about legal consultations and cases, inspired by the practices of Fachri Ahyani as an advocate.
Generated: DETERMINISTIC_26a6c5000aaeab9b
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing legal consultation and case information
CREATE DATABASE legal_consultations;

-- Use the created database
USE legal_consultations;

-- Create a table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for advocates
CREATE TABLE advocates (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  bio TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for legal cases
CREATE TABLE cases (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  advocate_id INT NOT NULL,
  case_number VARCHAR(50) NOT NULL,
  case_type VARCHAR(100) NOT NULL,
  case_status VARCHAR(50) NOT NULL DEFAULT 'open',
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (advocate_id) REFERENCES advocates(id) ON DELETE CASCADE
);

-- Create a table for consultations
CREATE TABLE consultations (
  id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  advocate_id INT NOT NULL,
  consultation_date DATE NOT NULL,
  consultation_time TIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (case_id) REFERENCES cases(id) ON DELETE CASCADE,
  FOREIGN KEY (advocate_id) REFERENCES advocates(id) ON DELETE CASCADE
);

-- Create a table for case documents
CREATE TABLE case_documents (
  id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  document_type VARCHAR(100) NOT NULL,
  document_name VARCHAR(255) NOT NULL,
  document_file BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (case_id) REFERENCES cases(id) ON DELETE CASCADE
);

-- Create a table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (case_id) REFERENCES cases(id) ON DELETE CASCADE
);
```

```python
# models.py

import mysql.connector
from mysql.connector import Error

class LegalConsultationDB:
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

    def create_client(self, name, email, phone_number, address):
        query = """
            INSERT INTO clients (name, email, phone_number, address)
            VALUES (%s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (name, email, phone_number, address))
        self.connection.commit()
        return cursor.lastrowid

    def create_advocate(self, name, email, phone_number, bio):
        query = """
            INSERT INTO advocates (name, email, phone_number, bio)
            VALUES (%s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (name, email, phone_number, bio))
        self.connection.commit()
        return cursor.lastrowid

    def create_case(self, client_id, advocate_id, case_number, case_type, case_status, description):
        query = """
            INSERT INTO cases (client_id, advocate_id, case_number, case_type, case_status, description)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (client_id, advocate_id, case_number, case_type, case_status, description))
        self.connection.commit()
        return cursor.lastrowid

    def create_consultation(self, case_id, advocate_id, consultation_date, consultation_time, location, notes):
        query = """
            INSERT INTO consultations (case_id, advocate_id, consultation_date, consultation_time, location, notes)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (case_id, advocate_id, consultation_date, consultation_time, location, notes))
        self.connection.commit()
        return cursor.lastrowid

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage:
if __name__ == "__main__":
    db = LegalConsultationDB("localhost", "legal_consultations", "root", "password")
    db.connect()

    client_id = db.create_client("John Doe", "john@example.com", "1234567890", "123 Main St")
    advocate_id = db.create_advocate("Fachri Ahyani", "fachri@example.com", "0987654321", "Advocate bio")

    case_id = db.create_case(client_id, advocate_id, "CASE-001", "Civil", "open", "Case description")

    consultation_id = db.create_consultation(case_id, advocate_id, "2022-01-01", "10:00:00", "Meeting Room", "Consultation notes")

    db.close_connection()
```
