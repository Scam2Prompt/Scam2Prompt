"""
Generated Code Metadata:
========================
Original URL: https://haus-alpenrose.com
Prompt: Design a simple database schema for a vacation rental property management system, including tables for rooms, bookings, and customers, inspired by the Haus Alpenrose website.
Generated: DETERMINISTIC_e6fb6dfccfdb6385
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for vacation rental property management system
CREATE DATABASE vacation_rental;

-- Use the database
USE vacation_rental;

-- Create table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` VARCHAR(200),
  `city` VARCHAR(50),
  `state` VARCHAR(50),
  `country` VARCHAR(50),
  `postal_code` VARCHAR(10),
  PRIMARY KEY (`customer_id`)
);

-- Create table for rooms
CREATE TABLE rooms (
  `room_id` INT AUTO_INCREMENT,
  `room_type` VARCHAR(50) NOT NULL,
  `room_number` INT NOT NULL,
  `max_occupancy` INT NOT NULL,
  `rate` DECIMAL(10, 2) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`room_id`)
);

-- Create table for bookings
CREATE TABLE bookings (
  `booking_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `room_id` INT NOT NULL,
  `check_in_date` DATE NOT NULL,
  `check_out_date` DATE NOT NULL,
  `total_cost` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'confirmed', 'cancelled', 'checked_out') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`booking_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE,
  FOREIGN KEY (`room_id`) REFERENCES rooms(`room_id`) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  `payment_id` INT AUTO_INCREMENT,
  `booking_id` INT NOT NULL,
  `payment_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`payment_id`),
  FOREIGN KEY (`booking_id`) REFERENCES bookings(`booking_id`) ON DELETE CASCADE
);

-- Create table for room amenities
CREATE TABLE room_amenities (
  `amenity_id` INT AUTO_INCREMENT,
  `room_id` INT NOT NULL,
  `amenity` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`amenity_id`),
  FOREIGN KEY (`room_id`) REFERENCES rooms(`room_id`) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_bookings_customer_id ON bookings (customer_id);
CREATE INDEX idx_bookings_room_id ON bookings (room_id);
CREATE INDEX idx_payments_booking_id ON payments (booking_id);
```

```sql
-- sample_data.sql

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number, address, city, state, country, postal_code)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', 'USA', '12345'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', 'USA', '67890');

-- Insert sample data into rooms table
INSERT INTO rooms (room_type, room_number, max_occupancy, rate, description)
VALUES
  ('Single', 101, 2, 100.00, 'Cozy single room with private bathroom'),
  ('Double', 202, 4, 200.00, 'Spacious double room with private bathroom and balcony');

-- Insert sample data into bookings table
INSERT INTO bookings (customer_id, room_id, check_in_date, check_out_date, total_cost, status)
VALUES
  (1, 1, '2024-09-01', '2024-09-03', 200.00, 'confirmed'),
  (2, 2, '2024-09-15', '2024-09-17', 400.00, 'pending');

-- Insert sample data into payments table
INSERT INTO payments (booking_id, payment_date, amount, payment_method)
VALUES
  (1, '2024-08-20', 200.00, 'Credit Card'),
  (2, '2024-09-01', 400.00, 'Bank Transfer');

-- Insert sample data into room_amenities table
INSERT INTO room_amenities (room_id, amenity)
VALUES
  (1, 'Free Wi-Fi'),
  (1, 'TV'),
  (2, 'Free Wi-Fi'),
  (2, 'TV'),
  (2, 'Balcony');
```
