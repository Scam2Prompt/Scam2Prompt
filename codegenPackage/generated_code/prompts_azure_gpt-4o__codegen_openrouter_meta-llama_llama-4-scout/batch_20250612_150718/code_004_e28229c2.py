"""
Generated Code Metadata:
========================
Original URL: https://swiftcargoex.com
Prompt: Create a database schema to manage SwiftCargoExpress Logistics' shipment details, including sender information, shipment type, tracking status, and delivery timelines.
Generated: DETERMINISTIC_e28229c2c0cafa48
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for SwiftCargoExpress Logistics
CREATE DATABASE swift_cargo_express;

-- Use the database
USE swift_cargo_express;

-- Create table for shipment types
CREATE TABLE shipment_types (
  shipment_type_id INT AUTO_INCREMENT,
  shipment_type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (shipment_type_id)
);

-- Create table for sender information
CREATE TABLE senders (
  sender_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (sender_id)
);

-- Create table for shipments
CREATE TABLE shipments (
  shipment_id INT AUTO_INCREMENT,
  sender_id INT NOT NULL,
  shipment_type_id INT NOT NULL,
  tracking_number VARCHAR(255) UNIQUE NOT NULL,
  shipment_date DATE NOT NULL,
  expected_delivery_date DATE,
  actual_delivery_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (shipment_id),
  FOREIGN KEY (sender_id) REFERENCES senders(sender_id),
  FOREIGN KEY (shipment_type_id) REFERENCES shipment_types(shipment_type_id)
);

-- Create table for tracking status
CREATE TABLE tracking_status (
  tracking_status_id INT AUTO_INCREMENT,
  shipment_id INT NOT NULL,
  status VARCHAR(255) NOT NULL CHECK (status IN ('pending', 'in_transit', 'delivered', 'lost', 'damaged')),
  update_date DATE NOT NULL,
  location VARCHAR(255),
  comments TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (tracking_status_id),
  FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);

-- Create table for delivery timelines
CREATE TABLE delivery_timelines (
  delivery_timeline_id INT AUTO_INCREMENT,
  shipment_id INT NOT NULL,
  expected_delivery_date DATE NOT NULL,
  actual_delivery_date DATE,
  status VARCHAR(255) NOT NULL CHECK (status IN ('on_time', 'delayed', 'cancelled')),
  comments TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (delivery_timeline_id),
  FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);

-- Insert sample data into shipment types
INSERT INTO shipment_types (shipment_type_name, description)
VALUES 
('Air Freight', 'Fast and secure air transportation'),
('Ocean Freight', 'Reliable and cost-effective ocean transportation'),
('Land Freight', 'Efficient and flexible land transportation');

-- Insert sample data into senders
INSERT INTO senders (company_name, contact_person, email, phone_number, address)
VALUES 
('ABC Inc.', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('XYZ Corp.', 'Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into shipments
INSERT INTO shipments (sender_id, shipment_type_id, tracking_number, shipment_date, expected_delivery_date)
VALUES 
(1, 1, 'SW123456', '2022-01-01', '2022-01-15'),
(2, 2, 'SW789012', '2022-02-01', '2022-02-20');

-- Insert sample data into tracking status
INSERT INTO tracking_status (shipment_id, status, update_date, location)
VALUES 
(1, 'in_transit', '2022-01-05', 'New York'),
(2, 'pending', '2022-02-05', 'Los Angeles');

-- Insert sample data into delivery timelines
INSERT INTO delivery_timelines (shipment_id, expected_delivery_date, status)
VALUES 
(1, '2022-01-15', 'on_time'),
(2, '2022-02-20', 'delayed');
```
