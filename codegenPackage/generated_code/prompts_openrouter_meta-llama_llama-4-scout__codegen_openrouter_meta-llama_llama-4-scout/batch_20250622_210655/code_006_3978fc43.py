"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "Design a simple database schema for managing home maintenance services including insulation, cleaning, and water leakage detection."
Generated: DETERMINISTIC_3978fc4356ccc97c
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

-- Create a database for home maintenance services
CREATE DATABASE home_maintenance;

-- Use the database
USE home_maintenance;

-- Create a table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for service providers
CREATE TABLE service_providers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for customer information
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for service requests
CREATE TABLE service_requests (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  service_id INT NOT NULL,
  service_provider_id INT,
  request_date DATE NOT NULL,
  completion_date DATE,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id),
  FOREIGN KEY (service_id) REFERENCES services(id),
  FOREIGN KEY (service_provider_id) REFERENCES service_providers(id)
);

-- Create a table for insulation services
CREATE TABLE insulation_services (
  service_request_id INT NOT NULL,
  area_insulated DECIMAL(10, 2) NOT NULL,
  material_used VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_request_id),
  FOREIGN KEY (service_request_id) REFERENCES service_requests(id)
);

-- Create a table for cleaning services
CREATE TABLE cleaning_services (
  service_request_id INT NOT NULL,
  area_cleaned DECIMAL(10, 2) NOT NULL,
  cleaning_method VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_request_id),
  FOREIGN KEY (service_request_id) REFERENCES service_requests(id)
);

-- Create a table for water leakage detection services
CREATE TABLE water_leakage_detection_services (
  service_request_id INT NOT NULL,
  leak_location VARCHAR(255) NOT NULL,
  repair_method VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_request_id),
  FOREIGN KEY (service_request_id) REFERENCES service_requests(id)
);

-- Insert sample data
INSERT INTO services (name, description) VALUES
  ('Insulation', 'Insulation services for homes'),
  ('Cleaning', 'Cleaning services for homes'),
  ('Water Leakage Detection', 'Water leakage detection and repair services');

INSERT INTO service_providers (name, email, phone) VALUES
  ('John Doe', 'john.doe@example.com', '123-456-7890'),
  ('Jane Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO customers (name, email, phone, address) VALUES
  ('Customer 1', 'customer1@example.com', '555-123-4567', '123 Main St'),
  ('Customer 2', 'customer2@example.com', '555-987-6543', '456 Elm St');

INSERT INTO service_requests (customer_id, service_id, service_provider_id, request_date) VALUES
  (1, 1, 1, '2022-01-01'),
  (2, 2, 2, '2022-01-15'),
  (1, 3, 1, '2022-02-01');

INSERT INTO insulation_services (service_request_id, area_insulated, material_used) VALUES
  (1, 1000.00, 'Fiberglass');

INSERT INTO cleaning_services (service_request_id, area_cleaned, cleaning_method) VALUES
  (2, 500.00, 'Steam Cleaning');

INSERT INTO water_leakage_detection_services (service_request_id, leak_location, repair_method) VALUES
  (3, 'Kitchen Sink', 'Pipe Replacement');
```
