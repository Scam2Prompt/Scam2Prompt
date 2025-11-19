"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Design a database schema to store information about social services, including details about clients, services provided, and outcomes, for an organization like CEFOR.
Generated: DETERMINISTIC_d29bf9126834fa37
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for social services
CREATE DATABASE social_services;

-- Use the database
USE social_services;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for service providers
CREATE TABLE service_providers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for client services
CREATE TABLE client_services (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  service_provider_id INT,
  start_date DATE,
  end_date DATE,
  outcome VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE,
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(id) ON DELETE SET NULL
);

-- Create table for outcomes
CREATE TABLE outcomes (
  id INT AUTO_INCREMENT,
  client_service_id INT NOT NULL,
  outcome_date DATE,
  outcome_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_service_id) REFERENCES client_services(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_client_services_client_id ON client_services(client_id);
CREATE INDEX idx_client_services_service_id ON client_services(service_id);
CREATE INDEX idx_client_services_service_provider_id ON client_services(service_provider_id);
CREATE INDEX idx_outcomes_client_service_id ON outcomes(client_service_id);
```

```python
# models.py
import mysql.connector
from mysql.connector import Error

class SocialServicesDB:
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

    def insert_client(self, client):
        if self.connection:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO clients (first_name, last_name, date_of_birth, email, phone_number, address)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, client)
            self.connection.commit()
            print("Client inserted")
        else:
            print("Not connected to database")

    def insert_service(self, service):
        if self.connection:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO services (name, description)
                VALUES (%s, %s)
            """
            cursor.execute(query, service)
            self.connection.commit()
            print("Service inserted")
        else:
            print("Not connected to database")

    def insert_client_service(self, client_service):
        if self.connection:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO client_services (client_id, service_id, service_provider_id, start_date, end_date, outcome)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, client_service)
            self.connection.commit()
            print("Client service inserted")
        else:
            print("Not connected to database")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

# Example usage
if __name__ == "__main__":
    db = SocialServicesDB('localhost', 'social_services', 'root', 'password')
    db.connect()
    db.create_tables()

    client = ('John', 'Doe', '1990-01-01', 'john@example.com', '1234567890', '123 Main St')
    db.insert_client(client)

    service = ('Counseling', 'Mental health counseling')
    db.insert_service(service)

    client_service = (1, 1, 1, '2022-01-01', '2022-06-01', 'Successful')
    db.insert_client_service(client_service)

    db.close_connection()
```
