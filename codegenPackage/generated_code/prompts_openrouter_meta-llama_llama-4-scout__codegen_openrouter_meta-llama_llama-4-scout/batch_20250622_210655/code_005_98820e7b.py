"""
Generated Code Metadata:
========================
Original URL: https://skyline-ia.com
Prompt: "Suggest a suitable database schema for storing information about tour packages, customers, and bookings for a company like Skyline International Agent."
Generated: DETERMINISTIC_98820e7b0411a15b
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

-- Create database for Skyline International Agent
CREATE DATABASE skyline_international_agent;

-- Use the database
USE skyline_international_agent;

-- Create table for tour packages
CREATE TABLE tour_packages (
  `package_id` INT AUTO_INCREMENT,
  `package_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `duration` INT NOT NULL, -- in days
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`package_id`)
);

-- Create table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_id`)
);

-- Create table for bookings
CREATE TABLE bookings (
  `booking_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `package_id` INT NOT NULL,
  `booking_date` DATE NOT NULL,
  `travel_date` DATE NOT NULL,
  `status` ENUM('pending', 'confirmed', 'cancelled') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`booking_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE,
  FOREIGN KEY (`package_id`) REFERENCES tour_packages(`package_id`) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  `payment_id` INT AUTO_INCREMENT,
  `booking_id` INT NOT NULL,
  `payment_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` VARCHAR(100) NOT NULL,
  `status` ENUM('pending', 'success', 'failed') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`payment_id`),
  FOREIGN KEY (`booking_id`) REFERENCES bookings(`booking_id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_bookings_customer_id ON bookings (`customer_id`);
CREATE INDEX idx_bookings_package_id ON bookings (`package_id`);
CREATE INDEX idx_payments_booking_id ON payments (`booking_id`);
```

```sql
-- example_data.sql

-- Insert example data into tour packages
INSERT INTO tour_packages (`package_name`, `description`, `price`, `duration`)
VALUES
  ('Europe Tour', 'Explore Europe in 10 days', 2000.00, 10),
  ('Asia Tour', 'Discover Asia in 14 days', 3000.00, 14),
  ('Americas Tour', 'Experience the Americas in 21 days', 5000.00, 21);

-- Insert example data into customers
INSERT INTO customers (`first_name`, `last_name`, `email`, `phone`, `address`)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '+1 123 456 7890', '123 Main St'),
  ('Jane', 'Doe', 'jane.doe@example.com', '+1 987 654 3210', '456 Elm St'),
  ('Bob', 'Smith', 'bob.smith@example.com', '+1 555 123 4567', '789 Oak St');

-- Insert example data into bookings
INSERT INTO bookings (`customer_id`, `package_id`, `booking_date`, `travel_date`)
VALUES
  (1, 1, '2024-09-01', '2024-09-15'),
  (2, 2, '2024-09-05', '2024-09-20'),
  (3, 3, '2024-09-10', '2024-10-01');

-- Insert example data into payments
INSERT INTO payments (`booking_id`, `payment_date`, `amount`, `payment_method`)
VALUES
  (1, '2024-09-01', 2000.00, 'Credit Card'),
  (2, '2024-09-05', 3000.00, 'Bank Transfer'),
  (3, '2024-09-10', 5000.00, 'PayPal');
```
