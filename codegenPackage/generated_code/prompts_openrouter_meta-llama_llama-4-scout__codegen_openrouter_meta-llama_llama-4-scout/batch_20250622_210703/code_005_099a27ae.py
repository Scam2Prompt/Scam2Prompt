"""
Generated Code Metadata:
========================
Original URL: https://grupoinmobiliariocrecer.com
Prompt: Design a database schema to store information about properties, clients, and services offered by Grupo Inmobiliario Crecer, including fields for property valuation and rental agreements.
Generated: DETERMINISTIC_099a27ae3590630f
Batch ID: 20250622_210703
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
CREATE DATABASE grupo_inmobiliario_crecer;

-- Use database
USE grupo_inmobiliario_crecer;

-- Create table for properties
CREATE TABLE properties (
  id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  property_type ENUM('residential', 'commercial') NOT NULL,
  valuation DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  service_name VARCHAR(100) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for rental agreements
CREATE TABLE rental_agreements (
  id INT AUTO_INCREMENT,
  property_id INT NOT NULL,
  client_id INT NOT NULL,
  rental_start_date DATE NOT NULL,
  rental_end_date DATE,
  rent DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE,
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create table for property services
CREATE TABLE property_services (
  property_id INT NOT NULL,
  service_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (property_id, service_id),
  FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create table for property valuations
CREATE TABLE property_valuations (
  id INT AUTO_INCREMENT,
  property_id INT NOT NULL,
  valuation_date DATE NOT NULL,
  valuation DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE
);
```

```sql
-- example_data.sql

-- Insert example data into properties table
INSERT INTO properties (address, city, state, zip_code, property_type, valuation)
VALUES 
  ('123 Main St', 'Anytown', 'CA', '12345', 'residential', 500000.00),
  ('456 Elm St', 'Othertown', 'NY', '67890', 'commercial', 1000000.00);

-- Insert example data into clients table
INSERT INTO clients (first_name, last_name, email, phone_number)
VALUES 
  ('John', 'Doe', 'john.doe@example.com', '555-1234'),
  ('Jane', 'Smith', 'jane.smith@example.com', '555-5678');

-- Insert example data into services table
INSERT INTO services (service_name, service_description)
VALUES 
  ('Property Management', 'We manage your property'),
  ('Rental Services', 'We help you find a rental');

-- Insert example data into rental agreements table
INSERT INTO rental_agreements (property_id, client_id, rental_start_date, rental_end_date, rent)
VALUES 
  (1, 1, '2022-01-01', '2023-01-01', 2000.00),
  (2, 2, '2022-06-01', NULL, 5000.00);

-- Insert example data into property services table
INSERT INTO property_services (property_id, service_id)
VALUES 
  (1, 1),
  (2, 2);

-- Insert example data into property valuations table
INSERT INTO property_valuations (property_id, valuation_date, valuation)
VALUES 
  (1, '2022-01-01', 500000.00),
  (2, '2022-06-01', 1000000.00);
```
