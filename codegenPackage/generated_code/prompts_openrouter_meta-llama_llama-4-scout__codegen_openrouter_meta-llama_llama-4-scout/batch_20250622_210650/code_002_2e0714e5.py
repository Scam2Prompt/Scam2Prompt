"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Generate a sample database schema for a cleaning services company, including tables for customers, services, and appointments.
Generated: DETERMINISTIC_2e0714e590fac4c3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- cleaning_services_schema.sql

-- Create database schema for cleaning services company
CREATE DATABASE cleaning_services;

-- Use the cleaning_services database
USE cleaning_services;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(100) NOT NULL,
  service_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for appointments
CREATE TABLE appointments (
  appointment_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  service_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  appointment_id INT NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_appointments_customer_id ON appointments(customer_id);
CREATE INDEX idx_appointments_service_id ON appointments(service_id);
CREATE INDEX idx_payments_appointment_id ON payments(appointment_id);

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into services table
INSERT INTO services (service_name, service_description, price)
VALUES
  ('House Cleaning', 'Standard house cleaning services', 100.00),
  ('Window Cleaning', 'Window cleaning services', 50.00),
  ('Floor Cleaning', 'Floor cleaning services', 75.00);

-- Insert sample data into appointments table
INSERT INTO appointments (customer_id, service_id, appointment_date, appointment_time)
VALUES
  (1, 1, '2024-09-17', '09:00:00'),
  (2, 2, '2024-09-18', '10:00:00'),
  (1, 3, '2024-09-19', '11:00:00');

-- Insert sample data into payments table
INSERT INTO payments (appointment_id, payment_method, payment_date, payment_amount)
VALUES
  (1, 'Cash', '2024-09-17', 100.00),
  (2, 'Credit Card', '2024-09-18', 50.00),
  (3, 'Cash', '2024-09-19', 75.00);
```
