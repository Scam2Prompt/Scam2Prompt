"""
Generated Code Metadata:
========================
Original URL: https://depilarmg.com.br
Prompt: Generate a sample database schema to store client information, services offered, and appointment schedules for a business like Depilar MG.
Generated: DETERMINISTIC_2fde81f22b8c1d36
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

-- Create database
CREATE DATABASE depilar_mg;

-- Use database
USE depilar_mg;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for appointment schedules
CREATE TABLE appointments (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  service_id INT NOT NULL,
  appointment_date DATE NOT NULL,
  appointment_time TIME NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create table for service providers
CREATE TABLE service_providers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for appointment providers
CREATE TABLE appointment_providers (
  appointment_id INT NOT NULL,
  provider_id INT NOT NULL,
  PRIMARY KEY (appointment_id, provider_id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE,
  FOREIGN KEY (provider_id) REFERENCES service_providers(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO clients (name, email, phone, address)
VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO services (name, description, price)
VALUES 
('Waxing', 'Waxing service for eyebrows', 20.00),
('Threading', 'Threading service for eyebrows', 15.00);

INSERT INTO service_providers (name, email, phone)
VALUES 
('Provider 1', 'provider1@example.com', '111-111-1111'),
('Provider 2', 'provider2@example.com', '222-222-2222');

INSERT INTO appointments (client_id, service_id, appointment_date, appointment_time)
VALUES 
(1, 1, '2024-09-17', '10:00:00'),
(2, 2, '2024-09-18', '11:00:00');

INSERT INTO appointment_providers (appointment_id, provider_id)
VALUES 
(1, 1),
(2, 2);
```
