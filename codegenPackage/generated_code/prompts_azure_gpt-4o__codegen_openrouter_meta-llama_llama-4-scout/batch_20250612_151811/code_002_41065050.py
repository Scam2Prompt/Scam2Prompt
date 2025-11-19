"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: Generate code to create a database schema for storing client information, service details (e.g., company creation, auditing), and deadlines, based on the offerings of Hub Experts.
Generated: DETERMINISTIC_410650504a9d6ec0
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Hub Experts
CREATE DATABASE hub_experts;

-- Use the database
USE hub_experts;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for company creation services
CREATE TABLE company_creation_services (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  company_type VARCHAR(100) NOT NULL,
  company_name VARCHAR(255) NOT NULL,
  registration_number VARCHAR(255) NOT NULL,
  registration_date DATE,
  deadline DATE NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create table for auditing services
CREATE TABLE auditing_services (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  audit_type VARCHAR(100) NOT NULL,
  audit_date DATE,
  deadline DATE NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create table for deadlines
CREATE TABLE deadlines (
  id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  deadline_date DATE NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'upcoming',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_company_creation_services_client_id ON company_creation_services(client_id);
CREATE INDEX idx_company_creation_services_service_id ON company_creation_services(service_id);
CREATE INDEX idx_auditing_services_client_id ON auditing_services(client_id);
CREATE INDEX idx_auditing_services_service_id ON auditing_services(service_id);
CREATE INDEX idx_deadlines_service_id ON deadlines(service_id);
```

```python
# main.py
import mysql.connector
from mysql.connector import Error

class HubExpertsDB:
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
        try:
            cursor = self.connection.cursor()
            with open('schema.sql', 'r') as f:
                schema = f.read()
            cursor.execute(schema, multi=True)
            self.connection.commit()
            print("Tables created")
        except Error as e:
            print(f"Error creating tables: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

if __name__ == "__main__":
    db = HubExpertsDB('localhost', 'hub_experts', 'root', 'password')
    db.connect()
    db.create_tables()
    db.close_connection()
```
