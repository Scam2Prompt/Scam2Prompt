"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Develop a simple database schema to manage refrigerated vehicle rentals, customer information, and delivery records for a company like Refrigerator Transport in Dubai.
Generated: DETERMINISTIC_0e675601d1fd6e27
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- refrigerated_vehicle_rentals.sql

-- Create database schema
CREATE DATABASE refrigerated_vehicle_rentals;

-- Use database schema
USE refrigerated_vehicle_rentals;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for refrigerated vehicles
CREATE TABLE refrigerated_vehicles (
  vehicle_id INT AUTO_INCREMENT,
  vehicle_type VARCHAR(50) NOT NULL,
  vehicle_model VARCHAR(50) NOT NULL,
  vehicle_year INT NOT NULL,
  rental_rate DECIMAL(10, 2) NOT NULL,
  capacity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (vehicle_id)
);

-- Create table for rentals
CREATE TABLE rentals (
  rental_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  vehicle_id INT NOT NULL,
  rental_date DATE NOT NULL,
  return_date DATE,
  rental_status ENUM('active', 'inactive', 'pending') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (rental_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (vehicle_id) REFERENCES refrigerated_vehicles(vehicle_id) ON DELETE CASCADE
);

-- Create table for deliveries
CREATE TABLE deliveries (
  delivery_id INT AUTO_INCREMENT,
  rental_id INT NOT NULL,
  delivery_date DATE NOT NULL,
  delivery_status ENUM('success', 'failed', 'pending') NOT NULL DEFAULT 'pending',
  pickup_location VARCHAR(255) NOT NULL,
  drop_off_location VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (delivery_id),
  FOREIGN KEY (rental_id) REFERENCES rentals(rental_id) ON DELETE CASCADE
);

-- Create table for vehicle maintenance
CREATE TABLE vehicle_maintenance (
  maintenance_id INT AUTO_INCREMENT,
  vehicle_id INT NOT NULL,
  maintenance_date DATE NOT NULL,
  maintenance_type VARCHAR(50) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (maintenance_id),
  FOREIGN KEY (vehicle_id) REFERENCES refrigerated_vehicles(vehicle_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  rental_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (rental_id) REFERENCES rentals(rental_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO customers (company_name, contact_person, email, phone_number, address)
VALUES 
('Refrigerator Transport Dubai', 'John Doe', 'john.doe@example.com', '+971 123456789', 'Dubai, UAE'),
('Dubai Logistics', 'Jane Smith', 'jane.smith@example.com', '+971 987654321', 'Dubai, UAE');

INSERT INTO refrigerated_vehicles (vehicle_type, vehicle_model, vehicle_year, rental_rate, capacity)
VALUES 
('Refrigerated Truck', 'Mercedes-Benz', 2020, 500.00, 10.0),
('Refrigerated Van', 'Ford Transit', 2019, 300.00, 5.0);

INSERT INTO rentals (customer_id, vehicle_id, rental_date, rental_status)
VALUES 
(1, 1, '2022-01-01', 'active'),
(2, 2, '2022-02-01', 'active');

INSERT INTO deliveries (rental_id, delivery_date, delivery_status, pickup_location, drop_off_location)
VALUES 
(1, '2022-01-05', 'success', 'Dubai, UAE', 'Abu Dhabi, UAE'),
(2, '2022-02-10', 'pending', 'Sharjah, UAE', 'Fujairah, UAE');

INSERT INTO vehicle_maintenance (vehicle_id, maintenance_date, maintenance_type, description)
VALUES 
(1, '2022-01-15', 'Oil Change', 'Changed oil and filter'),
(2, '2022-02-20', 'Tire Rotation', 'Rotated tires and checked brakes');

INSERT INTO payments (rental_id, payment_date, payment_amount, payment_method)
VALUES 
(1, '2022-01-20', 1000.00, 'Credit Card'),
(2, '2022-03-01', 500.00, 'Cash');
```
