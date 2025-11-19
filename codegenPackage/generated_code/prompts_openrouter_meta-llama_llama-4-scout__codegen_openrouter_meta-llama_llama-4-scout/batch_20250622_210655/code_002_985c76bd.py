"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Generate a sample database schema for a car rental system like Micro Rent a Car, including tables for vehicles, customers, bookings, and payments.
Generated: DETERMINISTIC_985c76bd34e894b0
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for car rental system
CREATE DATABASE car_rental;

-- Use the car_rental database
USE car_rental;

-- Create table for vehicle types
CREATE TABLE vehicle_types (
  vehicle_type_id INT AUTO_INCREMENT,
  vehicle_type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (vehicle_type_id)
);

-- Create table for vehicles
CREATE TABLE vehicles (
  vehicle_id INT AUTO_INCREMENT,
  vehicle_type_id INT NOT NULL,
  license_plate VARCHAR(20) NOT NULL,
  make VARCHAR(100) NOT NULL,
  model VARCHAR(100) NOT NULL,
  year INT NOT NULL,
  color VARCHAR(50) NOT NULL,
  mileage INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (vehicle_id),
  FOREIGN KEY (vehicle_type_id) REFERENCES vehicle_types(vehicle_type_id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for bookings
CREATE TABLE bookings (
  booking_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  vehicle_id INT NOT NULL,
  pickup_date DATE NOT NULL,
  dropoff_date DATE NOT NULL,
  pickup_location VARCHAR(255) NOT NULL,
  dropoff_location VARCHAR(255) NOT NULL,
  status ENUM('pending', 'confirmed', 'cancelled', 'completed') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (booking_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  booking_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'credit_card', 'debit_card') NOT NULL,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (booking_id) REFERENCES bookings(booking_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_vehicle_type_id ON vehicles (vehicle_type_id);
CREATE INDEX idx_customer_id ON bookings (customer_id);
CREATE INDEX idx_vehicle_id ON bookings (vehicle_id);
CREATE INDEX idx_booking_id ON payments (booking_id);

-- Insert sample data
INSERT INTO vehicle_types (vehicle_type_name, description)
VALUES
  ('Sedan', 'Compact sedan'),
  ('SUV', 'Sport utility vehicle'),
  ('Truck', 'Large cargo truck');

INSERT INTO vehicles (vehicle_type_id, license_plate, make, model, year, color, mileage)
VALUES
  (1, 'ABC123', 'Toyota', 'Camry', 2020, 'Silver', 20000),
  (2, 'XYZ789', 'Honda', 'CR-V', 2019, 'White', 30000),
  (3, 'DEF456', 'Ford', 'F-150', 2022, 'Black', 10000);

INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO bookings (customer_id, vehicle_id, pickup_date, dropoff_date, pickup_location, dropoff_location)
VALUES
  (1, 1, '2024-09-16', '2024-09-23', 'New York', 'Los Angeles'),
  (2, 2, '2024-09-20', '2024-09-27', 'Chicago', 'Houston');

INSERT INTO payments (booking_id, payment_date, payment_amount, payment_method)
VALUES
  (1, '2024-09-16', 500.00, 'credit_card'),
  (2, '2024-09-20', 750.00, 'debit_card');
```
