"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Design a database schema to store information about car repair services, including services offered (e.g., engine repair, transmission repair), customer details, and appointment schedules.
Generated: DETERMINISTIC_ccad561e447a8666
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for car repair services
CREATE DATABASE car_repair_services;

-- Use the database
USE car_repair_services;

-- Create table for services offered
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  service_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (service_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  PRIMARY KEY (customer_id)
);

-- Create table for appointment schedules
CREATE TABLE appointments (
  appointment_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  service_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Create table for technicians
CREATE TABLE technicians (
  technician_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  PRIMARY KEY (technician_id)
);

-- Create table for appointment technicians
CREATE TABLE appointment_technicians (
  appointment_id INT NOT NULL,
  technician_id INT NOT NULL,
  PRIMARY KEY (appointment_id, technician_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id),
  FOREIGN KEY (technician_id) REFERENCES technicians(technician_id)
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  appointment_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);
```

```python
# car_repair_services.py

import mysql.connector
from mysql.connector import Error

class CarRepairServices:
  def __init__(self, host_name, db_name, user_name, user_password):
    self.host_name = host_name
    self.db_name = db_name
    self.user_name = user_name
    self.user_password = user_password
    self.connection = None

  def connect_to_db(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host_name,
        database=self.db_name,
        user=self.user_name,
        password=self.user_password
      )
      print("Connected to database")
    except Error as error:
      print(f"Error connecting to database: {error}")

  def create_service(self, service_name, service_description, service_price):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO services (service_name, service_description, service_price) VALUES (%s, %s, %s)"
      cursor.execute(query, (service_name, service_description, service_price))
      self.connection.commit()
      print("Service created successfully")
    except Error as error:
      print(f"Error creating service: {error}")

  def create_customer(self, first_name, last_name, email, phone_number, address):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO customers (first_name, last_name, email, phone_number, address) VALUES (%s, %s, %s, %s, %s)"
      cursor.execute(query, (first_name, last_name, email, phone_number, address))
      self.connection.commit()
      print("Customer created successfully")
    except Error as error:
      print(f"Error creating customer: {error}")

  def create_appointment(self, customer_id, service_id, appointment_date, appointment_time):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO appointments (customer_id, service_id, appointment_date, appointment_time) VALUES (%s, %s, %s, %s)"
      cursor.execute(query, (customer_id, service_id, appointment_date, appointment_time))
      self.connection.commit()
      print("Appointment created successfully")
    except Error as error:
      print(f"Error creating appointment: {error}")

  def close_connection(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage
if __name__ == "__main__":
  car_repair_services = CarRepairServices("localhost", "car_repair_services", "root", "password")
  car_repair_services.connect_to_db()

  car_repair_services.create_service("Engine Repair", "Repair and maintenance of car engines", 100.00)
  car_repair_services.create_customer("John", "Doe", "john.doe@example.com", "123-456-7890", "123 Main St")
  car_repair_services.create_appointment(1, 1, "2024-09-16", "10:00:00")

  car_repair_services.close_connection()
```
