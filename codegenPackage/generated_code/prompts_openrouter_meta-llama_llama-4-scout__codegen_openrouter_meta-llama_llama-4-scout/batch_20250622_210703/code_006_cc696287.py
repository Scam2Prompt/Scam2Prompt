"""
Generated Code Metadata:
========================
Original URL: https://enyakinvidanjor.com
Prompt: Generate a SQL database schema to store information about vidanjör services, including customer details, service requests, and technician assignments.
Generated: DETERMINISTIC_cc696287ef8bbcb4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- vidanjor_services_schema.sql

-- Create database
CREATE DATABASE vidanjor_services;

-- Use database
USE vidanjor_services;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for technicians
CREATE TABLE technicians (
  technician_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (technician_id)
);

-- Create table for service requests
CREATE TABLE service_requests (
  service_request_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  service_type VARCHAR(100) NOT NULL,
  service_description TEXT,
  request_date DATE NOT NULL,
  request_time TIME NOT NULL,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_request_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create table for technician assignments
CREATE TABLE technician_assignments (
  assignment_id INT AUTO_INCREMENT,
  service_request_id INT NOT NULL,
  technician_id INT NOT NULL,
  assigned_date DATE NOT NULL,
  assigned_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (assignment_id),
  FOREIGN KEY (service_request_id) REFERENCES service_requests(service_request_id) ON DELETE CASCADE,
  FOREIGN KEY (technician_id) REFERENCES technicians(technician_id) ON DELETE CASCADE,
  UNIQUE (service_request_id, technician_id)
);

-- Create table for service request updates
CREATE TABLE service_request_updates (
  update_id INT AUTO_INCREMENT,
  service_request_id INT NOT NULL,
  update_description TEXT NOT NULL,
  update_date DATE NOT NULL,
  update_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (update_id),
  FOREIGN KEY (service_request_id) REFERENCES service_requests(service_request_id) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_technicians_email ON technicians(email);
CREATE INDEX idx_service_requests_customer_id ON service_requests(customer_id);
CREATE INDEX idx_technician_assignments_service_request_id ON technician_assignments(service_request_id);
CREATE INDEX idx_technician_assignments_technician_id ON technician_assignments(technician_id);
```
