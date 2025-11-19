"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Design a basic database schema for storing client information, appointments, and counseling session records for a text-based counseling service like the one offered on textcounsellingonline.com.au.
Generated: DETERMINISTIC_9e946130e3034460
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

-- Create database for counseling service
CREATE DATABASE counseling_service;

-- Use counseling service database
USE counseling_service;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for counselors
CREATE TABLE counselors (
  counselor_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (counselor_id)
);

-- Create table for appointments
CREATE TABLE appointments (
  appointment_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  counselor_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (counselor_id) REFERENCES counselors(counselor_id) ON DELETE CASCADE
);

-- Create table for counseling sessions
CREATE TABLE counseling_sessions (
  session_id INT AUTO_INCREMENT,
  appointment_id INT NOT NULL,
  session_date DATE NOT NULL,
  session_notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (session_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE
);

-- Create table for session records
CREATE TABLE session_records (
  record_id INT AUTO_INCREMENT,
  session_id INT NOT NULL,
  record_type ENUM('text', 'audio', 'video') NOT NULL,
  record_content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (record_id),
  FOREIGN KEY (session_id) REFERENCES counseling_sessions(session_id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_appointments_client_id ON appointments(client_id);
CREATE INDEX idx_appointments_counselor_id ON appointments(counselor_id);
CREATE INDEX idx_counseling_sessions_appointment_id ON counseling_sessions(appointment_id);
CREATE INDEX idx_session_records_session_id ON session_records(session_id);
```

```python
# counseling_service.py

import mysql.connector
from mysql.connector import Error

class CounselingService:
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

  def create_client(self, first_name, last_name, email, phone_number, address):
    query = """
      INSERT INTO clients (first_name, last_name, email, phone_number, address)
      VALUES (%s, %s, %s, %s, %s)
    """
    try:
      cursor = self.connection.cursor()
      cursor.execute(query, (first_name, last_name, email, phone_number, address))
      self.connection.commit()
      print("Client created successfully")
    except Error as e:
      print(f"Error creating client: {e}")

  def create_counselor(self, first_name, last_name, email, phone_number):
    query = """
      INSERT INTO counselors (first_name, last_name, email, phone_number)
      VALUES (%s, %s, %s, %s)
    """
    try:
      cursor = self.connection.cursor()
      cursor.execute(query, (first_name, last_name, email, phone_number))
      self.connection.commit()
      print("Counselor created successfully")
    except Error as e:
      print(f"Error creating counselor: {e}")

  def create_appointment(self, client_id, counselor_id, appointment_date, appointment_time):
    query = """
      INSERT INTO appointments (client_id, counselor_id, appointment_date, appointment_time)
      VALUES (%s, %s, %s, %s)
    """
    try:
      cursor = self.connection.cursor()
      cursor.execute(query, (client_id, counselor_id, appointment_date, appointment_time))
      self.connection.commit()
      print("Appointment created successfully")
    except Error as e:
      print(f"Error creating appointment: {e}")

  def create_counseling_session(self, appointment_id, session_date, session_notes):
    query = """
      INSERT INTO counseling_sessions (appointment_id, session_date, session_notes)
      VALUES (%s, %s, %s)
    """
    try:
      cursor = self.connection.cursor()
      cursor.execute(query, (appointment_id, session_date, session_notes))
      self.connection.commit()
      print("Counseling session created successfully")
    except Error as e:
      print(f"Error creating counseling session: {e}")

  def create_session_record(self, session_id, record_type, record_content):
    query = """
      INSERT INTO session_records (session_id, record_type, record_content)
      VALUES (%s, %s, %s)
    """
    try:
      cursor = self.connection.cursor()
      cursor.execute(query, (session_id, record_type, record_content))
      self.connection.commit()
      print("Session record created successfully")
    except Error as e:
      print(f"Error creating session record: {e}")

# Example usage
if __name__ == "__main__":
  service = CounselingService("localhost", "counseling_service", "root", "password")
  service.connect()

  service.create_client("John", "Doe", "john.doe@example.com", "123-456-7890", "123 Main St")
  service.create_counselor("Jane", "Smith", "jane.smith@example.com", "987-654-3210")
  service.create_appointment(1, 1, "2024-09-16", "10:00:00")
  service.create_counseling_session(1, "2024-09-16", "Session notes")
  service.create_session_record(1, "text", "Session record content")
```
