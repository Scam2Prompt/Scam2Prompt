"""
Generated Code Metadata:
========================
Original URL: https://grupolegalcorporativo.com
Prompt: Develop a basic data model for storing and managing client information, cases, and investigations for a law firm like Grupo Legal Corporativo, using a database management system.
Generated: DETERMINISTIC_6429724c94cccd80
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for law firm
CREATE DATABASE grupo_legal_corporativo;

-- Use database
USE grupo_legal_corporativo;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for cases
CREATE TABLE cases (
  case_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  case_type VARCHAR(255) NOT NULL,
  case_description TEXT,
  case_status VARCHAR(255) NOT NULL DEFAULT 'Open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (case_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for investigations
CREATE TABLE investigations (
  investigation_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  investigation_type VARCHAR(255) NOT NULL,
  investigation_description TEXT,
  investigation_status VARCHAR(255) NOT NULL DEFAULT 'Open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (investigation_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Create table for case updates
CREATE TABLE case_updates (
  update_id INT AUTO_INCREMENT,
  case_id INT NOT NULL,
  update_description TEXT NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (update_id),
  FOREIGN KEY (case_id) REFERENCES cases(case_id) ON DELETE CASCADE
);

-- Create table for investigation updates
CREATE TABLE investigation_updates (
  update_id INT AUTO_INCREMENT,
  investigation_id INT NOT NULL,
  update_description TEXT NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (update_id),
  FOREIGN KEY (investigation_id) REFERENCES investigations(investigation_id) ON DELETE CASCADE
);

-- Create stored procedure to add new client
DELIMITER //
CREATE PROCEDURE add_client(
  IN p_first_name VARCHAR(255),
  IN p_last_name VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_phone_number VARCHAR(20),
  IN p_address VARCHAR(255)
)
BEGIN
  INSERT INTO clients (first_name, last_name, email, phone_number, address)
  VALUES (p_first_name, p_last_name, p_email, p_phone_number, p_address);
END//
DELIMITER ;

-- Create stored procedure to add new case
DELIMITER //
CREATE PROCEDURE add_case(
  IN p_client_id INT,
  IN p_case_type VARCHAR(255),
  IN p_case_description TEXT
)
BEGIN
  INSERT INTO cases (client_id, case_type, case_description)
  VALUES (p_client_id, p_case_type, p_case_description);
END//
DELIMITER ;

-- Create stored procedure to add new investigation
DELIMITER //
CREATE PROCEDURE add_investigation(
  IN p_case_id INT,
  IN p_investigation_type VARCHAR(255),
  IN p_investigation_description TEXT
)
BEGIN
  INSERT INTO investigations (case_id, investigation_type, investigation_description)
  VALUES (p_case_id, p_investigation_type, p_investigation_description);
END//
DELIMITER ;

-- Example usage:
-- CALL add_client('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');
-- CALL add_case(1, 'Civil', 'Client was injured in an accident');
-- CALL add_investigation(1, 'Medical', 'Client received medical attention');
```

```python
# models.py
import mysql.connector
from mysql.connector import Error

class LawFirmDatabase:
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

  def add_client(self, first_name, last_name, email, phone_number, address):
    query = "CALL add_client(%s, %s, %s, %s, %s)"
    cursor = self.connection.cursor()
    cursor.execute(query, (first_name, last_name, email, phone_number, address))
    self.connection.commit()
    cursor.close()

  def add_case(self, client_id, case_type, case_description):
    query = "CALL add_case(%s, %s, %s)"
    cursor = self.connection.cursor()
    cursor.execute(query, (client_id, case_type, case_description))
    self.connection.commit()
    cursor.close()

  def add_investigation(self, case_id, investigation_type, investigation_description):
    query = "CALL add_investigation(%s, %s, %s)"
    cursor = self.connection.cursor()
    cursor.execute(query, (case_id, investigation_type, investigation_description))
    self.connection.commit()
    cursor.close()

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage:
db = LawFirmDatabase('localhost', 'grupo_legal_corporativo', 'user', 'password')
db.connect()
db.add_client('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St')
db.add_case(1, 'Civil', 'Client was injured in an accident')
db.add_investigation(1, 'Medical', 'Client received medical attention')
db.close_connection()
```
