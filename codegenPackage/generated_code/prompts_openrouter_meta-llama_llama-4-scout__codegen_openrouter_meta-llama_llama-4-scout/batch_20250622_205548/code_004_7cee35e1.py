"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Design a simple database schema for storing client information, services provided, and appointment schedules for a business like Style & Makeup Effect.
Generated: DETERMINISTIC_7cee35e1c48d1128
Batch ID: 20250622_205548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Style & Makeup Effect
CREATE DATABASE style_makeup_effect;

-- Use the database
USE style_makeup_effect;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
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
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create table for service providers
CREATE TABLE service_providers (
  provider_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (provider_id)
);

-- Create table for appointment providers
CREATE TABLE appointment_providers (
  appointment_id INT NOT NULL,
  provider_id INT NOT NULL,
  PRIMARY KEY (appointment_id, provider_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id) ON DELETE CASCADE,
  FOREIGN KEY (provider_id) REFERENCES service_providers(provider_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO services (service_name, service_description, price)
VALUES 
('Makeup Application', 'Professional makeup application for special occasions', 50.00),
('Hair Styling', 'Professional hair styling for special occasions', 75.00);

INSERT INTO service_providers (first_name, last_name, email, phone_number)
VALUES 
('Emily', 'Chen', 'emily.chen@example.com', '555-123-4567'),
('Michael', 'Lee', 'michael.lee@example.com', '555-987-6543');

INSERT INTO appointments (client_id, service_id, appointment_date, appointment_time)
VALUES 
(1, 1, '2024-09-20', '10:00:00'),
(2, 2, '2024-09-21', '14:00:00');

INSERT INTO appointment_providers (appointment_id, provider_id)
VALUES 
(1, 1),
(2, 2);
```
