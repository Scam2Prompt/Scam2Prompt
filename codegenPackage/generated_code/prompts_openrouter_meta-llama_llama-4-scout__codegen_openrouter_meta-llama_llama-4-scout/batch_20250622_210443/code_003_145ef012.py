"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Design a database schema to store information about cargo shipments, clients, and transportation services, inspired by the operations of OPC."
Generated: DETERMINISTIC_145ef0126e17c50f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for cargo shipment management
CREATE DATABASE cargo_management;

-- Use the database
USE cargo_management;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for transportation services
CREATE TABLE transportation_services (
  service_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for cargo shipments
CREATE TABLE cargo_shipments (
  shipment_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  shipment_date DATE NOT NULL,
  expected_delivery_date DATE,
  cargo_description TEXT,
  weight DECIMAL(10, 2),
  volume DECIMAL(10, 2),
  status ENUM('pending', 'in_transit', 'delivered', 'lost') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (shipment_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES transportation_services(service_id) ON DELETE CASCADE
);

-- Create table for shipment tracking
CREATE TABLE shipment_tracking (
  tracking_id INT AUTO_INCREMENT,
  shipment_id INT NOT NULL,
  location VARCHAR(255),
  status ENUM('pending', 'in_transit', 'delivered', 'lost') NOT NULL,
  update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (tracking_id),
  FOREIGN KEY (shipment_id) REFERENCES cargo_shipments(shipment_id) ON DELETE CASCADE
);

-- Create table for users (for OPC operations)
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('admin', 'operator') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Create indexes for efficient queries
CREATE INDEX idx_client_id ON cargo_shipments(client_id);
CREATE INDEX idx_service_id ON cargo_shipments(service_id);
CREATE INDEX idx_shipment_id ON shipment_tracking(shipment_id);
```

```python
# cargo_management.py

import mysql.connector
from mysql.connector import Error

class CargoManagement:
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
    try:
      cursor.execute(query, (name, email, phone_number, address))
      self.connection.commit()
      print("Client created successfully")
    except Error as e:
      print(f"Error creating client: {e}")

  def create_shipment(self, client_id, service_id, shipment_date, expected_delivery_date, cargo_description, weight, volume):
    query = """
      INSERT INTO cargo_shipments (client_id, service_id, shipment_date, expected_delivery_date, cargo_description, weight, volume)
      VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor = self.connection.cursor()
    try:
      cursor.execute(query, (client_id, service_id, shipment_date, expected_delivery_date, cargo_description, weight, volume))
      self.connection.commit()
      print("Shipment created successfully")
    except Error as e:
      print(f"Error creating shipment: {e}")

  def update_shipment_status(self, shipment_id, status):
    query = """
      UPDATE cargo_shipments
      SET status = %s
      WHERE shipment_id = %s
    """
    cursor = self.connection.cursor()
    try:
      cursor.execute(query, (status, shipment_id))
      self.connection.commit()
      print("Shipment status updated successfully")
    except Error as e:
      print(f"Error updating shipment status: {e}")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage
if __name__ == "__main__":
  cargo_management = CargoManagement("localhost", "cargo_management", "root", "password")
  cargo_management.connect()
  cargo_management.create_client("John Doe", "john.doe@example.com", "1234567890", "123 Main St")
  cargo_management.create_shipment(1, 1, "2022-01-01", "2022-01-15", "Sample cargo", 10.0, 5.0)
  cargo_management.update_shipment_status(1, "in_transit")
  cargo_management.close_connection()
```
