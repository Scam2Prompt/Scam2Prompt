"""
Generated Code Metadata:
========================
Original URL: https://blueraygroup.com
Prompt: Design a simple database schema to store information about shipments, including sender and recipient details, package type, and delivery status, for a logistics company like Blue Ray Logistic.
Generated: DETERMINISTIC_b47e88213520be1f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Blue Ray Logistic
CREATE DATABASE blue_ray_logistic;

-- Use the database
USE blue_ray_logistic;

-- Create table for countries
CREATE TABLE countries (
  country_id INT AUTO_INCREMENT,
  country_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (country_id)
);

-- Create table for cities
CREATE TABLE cities (
  city_id INT AUTO_INCREMENT,
  city_name VARCHAR(255) NOT NULL,
  country_id INT,
  PRIMARY KEY (city_id),
  FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- Create table for addresses
CREATE TABLE addresses (
  address_id INT AUTO_INCREMENT,
  street_address VARCHAR(255) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  city_id INT,
  PRIMARY KEY (address_id),
  FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

-- Create table for users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address_id INT,
  PRIMARY KEY (user_id),
  FOREIGN KEY (address_id) REFERENCES addresses(address_id)
);

-- Create table for package types
CREATE TABLE package_types (
  package_type_id INT AUTO_INCREMENT,
  package_type_name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (package_type_id)
);

-- Create table for shipments
CREATE TABLE shipments (
  shipment_id INT AUTO_INCREMENT,
  sender_id INT,
  recipient_id INT,
  package_type_id INT,
  shipment_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  expected_delivery_date DATE,
  delivery_status ENUM('pending', 'in_transit', 'delivered', 'lost') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (shipment_id),
  FOREIGN KEY (sender_id) REFERENCES users(user_id),
  FOREIGN KEY (recipient_id) REFERENCES users(user_id),
  FOREIGN KEY (package_type_id) REFERENCES package_types(package_type_id)
);

-- Create table for shipment updates
CREATE TABLE shipment_updates (
  update_id INT AUTO_INCREMENT,
  shipment_id INT,
  update_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_status ENUM('pending', 'in_transit', 'delivered', 'lost') NOT NULL,
  description TEXT,
  PRIMARY KEY (update_id),
  FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);
```

```sql
-- sample_data.sql

-- Insert sample data into countries table
INSERT INTO countries (country_name) 
VALUES 
('United States'),
('Canada'),
('Mexico');

-- Insert sample data into cities table
INSERT INTO cities (city_name, country_id) 
VALUES 
('New York', 1),
('Los Angeles', 1),
('Toronto', 2),
('Vancouver', 2),
('Mexico City', 3);

-- Insert sample data into addresses table
INSERT INTO addresses (street_address, postal_code, city_id) 
VALUES 
('123 Main St', '10001', 1),
('456 Elm St', '90001', 2),
('789 Oak St', 'M5V 1J3', 3),
('321 Maple St', 'V6B 1J3', 4),
('901 Broadway', '01001', 1);

-- Insert sample data into users table
INSERT INTO users (first_name, last_name, email, phone_number, address_id) 
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 1),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', 2),
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567', 3);

-- Insert sample data into package_types table
INSERT INTO package_types (package_type_name, description) 
VALUES 
('Parcel', 'Small package'),
('Package', 'Medium package'),
('Box', 'Large package');

-- Insert sample data into shipments table
INSERT INTO shipments (sender_id, recipient_id, package_type_id, expected_delivery_date) 
VALUES 
(1, 2, 1, '2024-09-20'),
(2, 3, 2, '2024-09-25'),
(3, 1, 3, '2024-09-30');

-- Insert sample data into shipment_updates table
INSERT INTO shipment_updates (shipment_id, update_status, description) 
VALUES 
(1, 'in_transit', 'Shipment is on its way'),
(2, 'pending', 'Shipment has been processed'),
(3, 'delivered', 'Shipment has been delivered');
```
