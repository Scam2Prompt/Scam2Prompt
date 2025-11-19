"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Create a database schema for managing ocean freight shipments, including container types (45', 40', 20') and import/export details, inspired by Fealty Worldwide's services.
Generated: DETERMINISTIC_58115ff10f2508a7
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for ocean freight shipments
CREATE DATABASE ocean_freight;

-- Use the ocean_freight database
USE ocean_freight;

-- Create table for container types
CREATE TABLE container_types (
  id INT AUTO_INCREMENT,
  type_name VARCHAR(10) NOT NULL,
  length DECIMAL(4, 2) NOT NULL,
  width DECIMAL(4, 2) NOT NULL,
  height DECIMAL(4, 2) NOT NULL,
  capacity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (type_name)
);

-- Insert container types (45', 40', 20')
INSERT INTO container_types (type_name, length, width, height, capacity)
VALUES 
('45FT', 45.00, 8.00, 8.00, 1200.00),
('40FT', 40.00, 8.00, 8.00, 1000.00),
('20FT', 20.00, 8.00, 8.00, 600.00);

-- Create table for shipment status
CREATE TABLE shipment_status (
  id INT AUTO_INCREMENT,
  status_name VARCHAR(20) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (status_name)
);

-- Insert shipment status
INSERT INTO shipment_status (status_name, description)
VALUES 
('BOOKED', 'Shipment booked'),
('LOADED', 'Shipment loaded onto vessel'),
('TRANSIT', 'Shipment in transit'),
('DELIVERED', 'Shipment delivered'),
('CANCELLED', 'Shipment cancelled');

-- Create table for customers
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  company_name VARCHAR(100) NOT NULL,
  contact_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  address TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (email)
);

-- Create table for shipments
CREATE TABLE shipments (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  container_type_id INT NOT NULL,
  shipment_status_id INT NOT NULL DEFAULT 1,
  booking_date DATE NOT NULL,
  loading_date DATE,
  departure_date DATE,
  arrival_date DATE,
  origin_port VARCHAR(100) NOT NULL,
  destination_port VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id),
  FOREIGN KEY (container_type_id) REFERENCES container_types(id),
  FOREIGN KEY (shipment_status_id) REFERENCES shipment_status(id)
);

-- Create table for import/export details
CREATE TABLE shipment_details (
  id INT AUTO_INCREMENT,
  shipment_id INT NOT NULL,
  import_export VARCHAR(10) NOT NULL CHECK(import_export IN ('IMPORT', 'EXPORT')),
  commodity VARCHAR(100) NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  weight DECIMAL(10, 2) NOT NULL,
  volume DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (shipment_id) REFERENCES shipments(id)
);

-- Create table for shipment tracking
CREATE TABLE shipment_tracking (
  id INT AUTO_INCREMENT,
  shipment_id INT NOT NULL,
  tracking_date DATE NOT NULL,
  tracking_status VARCHAR(100) NOT NULL,
  location VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (shipment_id) REFERENCES shipments(id)
);
```
