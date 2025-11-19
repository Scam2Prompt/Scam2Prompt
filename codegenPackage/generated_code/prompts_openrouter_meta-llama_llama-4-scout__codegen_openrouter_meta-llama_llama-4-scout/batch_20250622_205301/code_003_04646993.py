"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Design a database schema to store information about fuel injector cleaning services, including client details, vehicle types, and service history, and suggest a suitable programming language for implementation.
Generated: DETERMINISTIC_04646993978d9571
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Database Schema SQL Code**
```sql
-- Create database for fuel injector cleaning services
CREATE DATABASE fuel_injector_services;

-- Use the database
USE fuel_injector_services;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for vehicle types
CREATE TABLE vehicle_types (
  vehicle_type_id INT AUTO_INCREMENT,
  vehicle_type_name VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (vehicle_type_id)
);

-- Create table for vehicles
CREATE TABLE vehicles (
  vehicle_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  vehicle_type_id INT NOT NULL,
  make VARCHAR(50) NOT NULL,
  model VARCHAR(50) NOT NULL,
  year INT NOT NULL,
  mileage INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (vehicle_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id),
  FOREIGN KEY (vehicle_type_id) REFERENCES vehicle_types(vehicle_type_id)
);

-- Create table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  vehicle_id INT NOT NULL,
  service_date DATE NOT NULL,
  service_type VARCHAR(50) NOT NULL,
  description TEXT,
  cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- Create table for service history
CREATE TABLE service_history (
  service_history_id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_history_id),
  FOREIGN KEY (service_id) REFERENCES services(service_id)
);
```

**Python Implementation using MySQL Connector/Python**
```python
import mysql.connector
from mysql.connector import Error

class FuelInjectorServices:
  def __init__(self, host_name, db_name, user_name, user_password):
    self.host_name = host_name
    self.db_name = db_name
    self.user_name = user_name
    self.user_password = user_password
    self.connection = None

  def create_connection(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host_name,
        database=self.db_name,
        user=self.user_name,
        password=self.user_password
      )
      print("Connection to database established")
    except Error as error:
      print(f"Error: '{error}'")

  def create_client(self, first_name, last_name, email, phone_number, address):
    try:
      cursor = self.connection.cursor()
      query = """
        INSERT INTO clients (first_name, last_name, email, phone_number, address)
        VALUES (%s, %s, %s, %s, %s)
      """
      cursor.execute(query, (first_name, last_name, email, phone_number, address))
      self.connection.commit()
      print("Client created successfully")
    except Error as error:
      print(f"Error: '{error}'")

  def create_vehicle(self, client_id, vehicle_type_id, make, model, year, mileage):
    try:
      cursor = self.connection.cursor()
      query = """
        INSERT INTO vehicles (client_id, vehicle_type_id, make, model, year, mileage)
        VALUES (%s, %s, %s, %s, %s, %s)
      """
      cursor.execute(query, (client_id, vehicle_type_id, make, model, year, mileage))
      self.connection.commit()
      print("Vehicle created successfully")
    except Error as error:
      print(f"Error: '{error}'")

  def create_service(self, vehicle_id, service_date, service_type, description, cost):
    try:
      cursor = self.connection.cursor()
      query = """
        INSERT INTO services (vehicle_id, service_date, service_type, description, cost)
        VALUES (%s, %s, %s, %s, %s)
      """
      cursor.execute(query, (vehicle_id, service_date, service_type, description, cost))
      self.connection.commit()
      print("Service created successfully")
    except Error as error:
      print(f"Error: '{error}'")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Connection closed")

if __name__ == "__main__":
  fuel_injector_services = FuelInjectorServices(
    host_name="localhost",
    db_name="fuel_injector_services",
    user_name="username",
    user_password="password"
  )
  fuel_injector_services.create_connection()
  fuel_injector_services.create_client(
    first_name="John",
    last_name="Doe",
    email="john.doe@example.com",
    phone_number="1234567890",
    address="123 Main St"
  )
  fuel_injector_services.create_vehicle(
    client_id=1,
    vehicle_type_id=1,
    make="Toyota",
    model="Camry",
    year=2020,
    mileage=50000
  )
  fuel_injector_services.create_service(
    vehicle_id=1,
    service_date="2022-01-01",
    service_type="Fuel Injector Cleaning",
    description="Cleaned fuel injectors",
    cost=100.00
  )
  fuel_injector_services.close_connection()
```
