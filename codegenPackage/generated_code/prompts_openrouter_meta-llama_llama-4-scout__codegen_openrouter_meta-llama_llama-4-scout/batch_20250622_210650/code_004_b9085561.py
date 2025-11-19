"""
Generated Code Metadata:
========================
Original URL: https://sosmenuiserie.fr
Prompt: Create a SQL database schema to store customer information, service requests, and appointments for a company like SOS Menuiserie.
Generated: DETERMINISTIC_b9085561f2903746
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

-- Create database for SOS Menuiserie
CREATE DATABASE sos_menuiserie;

-- Use the database
USE sos_menuiserie;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(50) NOT NULL,
  zip_code VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for service requests
CREATE TABLE service_requests (
  request_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  request_type VARCHAR(50) NOT NULL,
  request_description TEXT NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (request_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create table for appointments
CREATE TABLE appointments (
  appointment_id INT AUTO_INCREMENT,
  request_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  technician_id INT,
  status VARCHAR(20) NOT NULL DEFAULT 'scheduled',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (request_id) REFERENCES service_requests(request_id) ON DELETE CASCADE
);

-- Create table for technicians
CREATE TABLE technicians (
  technician_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (technician_id)
);

-- Create index on customer_id in service_requests table
CREATE INDEX idx_customer_id ON service_requests(customer_id);

-- Create index on request_id in appointments table
CREATE INDEX idx_request_id ON appointments(request_id);

-- Create index on technician_id in appointments table
CREATE INDEX idx_technician_id ON appointments(technician_id);
```
