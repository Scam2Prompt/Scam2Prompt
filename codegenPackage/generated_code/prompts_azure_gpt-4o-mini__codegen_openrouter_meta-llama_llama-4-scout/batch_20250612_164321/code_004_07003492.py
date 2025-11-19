"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Design a database schema for storing client information and insurance policy details for a company like GYV Seguros, which specializes in various insurance products.
Generated: DETERMINISTIC_07003492c9d7781b
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for GYV Seguros
CREATE DATABASE gyv_seguros;

-- Use the database
USE gyv_seguros;

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

-- Create table for insurance policies
CREATE TABLE insurance_policies (
  policy_id INT AUTO_INCREMENT,
  policy_type ENUM('life', 'health', 'auto', 'home') NOT NULL,
  policy_number VARCHAR(255) UNIQUE NOT NULL,
  client_id INT NOT NULL,
  policy_start_date DATE NOT NULL,
  policy_end_date DATE NOT NULL,
  premium DECIMAL(10, 2) NOT NULL,
  coverage_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (policy_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for policy beneficiaries
CREATE TABLE policy_beneficiaries (
  beneficiary_id INT AUTO_INCREMENT,
  policy_id INT NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  phone_number VARCHAR(20),
  address VARCHAR(255),
  percentage DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (beneficiary_id),
  FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id) ON DELETE CASCADE
);

-- Create table for policy payments
CREATE TABLE policy_payments (
  payment_id INT AUTO_INCREMENT,
  policy_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'credit_card', 'bank_transfer') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id) ON DELETE CASCADE
);

-- Create table for claims
CREATE TABLE claims (
  claim_id INT AUTO_INCREMENT,
  policy_id INT NOT NULL,
  claim_date DATE NOT NULL,
  claim_amount DECIMAL(10, 2) NOT NULL,
  claim_status ENUM('pending', 'approved', 'rejected') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (claim_id),
  FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id) ON DELETE CASCADE
);
```

```python
# models.py

import mysql.connector
from mysql.connector import Error

class GYVSegurosDB:
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
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO clients (first_name, last_name, email, phone_number, address) VALUES (%s, %s, %s, %s, %s)"
      cursor.execute(query, (first_name, last_name, email, phone_number, address))
      self.connection.commit()
      print("Client created successfully")
    except Error as e:
      print(f"Error creating client: {e}")

  def create_insurance_policy(self, policy_type, policy_number, client_id, policy_start_date, policy_end_date, premium, coverage_amount):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO insurance_policies (policy_type, policy_number, client_id, policy_start_date, policy_end_date, premium, coverage_amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      cursor.execute(query, (policy_type, policy_number, client_id, policy_start_date, policy_end_date, premium, coverage_amount))
      self.connection.commit()
      print("Insurance policy created successfully")
    except Error as e:
      print(f"Error creating insurance policy: {e}")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage
if __name__ == "__main__":
  db = GYVSegurosDB("localhost", "gyv_seguros", "root", "password")
  db.connect()
  db.create_client("John", "Doe", "john.doe@example.com", "1234567890", "123 Main St")
  db.create_insurance_policy("life", "POL123", 1, "2022-01-01", "2023-01-01", 100.00, 100000.00)
  db.close_connection()
```
