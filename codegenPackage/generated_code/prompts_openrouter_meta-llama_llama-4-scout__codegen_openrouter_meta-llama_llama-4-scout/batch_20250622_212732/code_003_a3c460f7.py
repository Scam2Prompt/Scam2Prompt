"""
Generated Code Metadata:
========================
Original URL: https://saltydazeusvi.com
Prompt: "Design a database schema to store information about boat charters, including trip schedules, customer details, and fleet information for a company operating in the U.S. Virgin Islands."
Generated: DETERMINISTIC_a3c460f7b5a72afc
Batch ID: 20250622_212732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for boat charter company
CREATE DATABASE boat_charter_company;

-- Use the database
USE boat_charter_company;

-- Create table for fleet information
CREATE TABLE fleets (
  `fleet_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `capacity` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`fleet_id`)
);

-- Create table for boats
CREATE TABLE boats (
  `boat_id` INT AUTO_INCREMENT,
  `fleet_id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `length` DECIMAL(5, 2) NOT NULL,
  `beam` DECIMAL(5, 2) NOT NULL,
  `draft` DECIMAL(5, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`boat_id`),
  FOREIGN KEY (`fleet_id`) REFERENCES fleets(`fleet_id`) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_id`)
);

-- Create table for trip schedules
CREATE TABLE trip_schedules (
  `trip_id` INT AUTO_INCREMENT,
  `boat_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `trip_date` DATE NOT NULL,
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  `departure_location` VARCHAR(255) NOT NULL,
  `return_location` VARCHAR(255) NOT NULL,
  `status` ENUM('pending', 'confirmed', 'cancelled', 'completed') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`trip_id`),
  FOREIGN KEY (`boat_id`) REFERENCES boats(`boat_id`) ON DELETE CASCADE,
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE
);

-- Create table for charter payments
CREATE TABLE charter_payments (
  `payment_id` INT AUTO_INCREMENT,
  `trip_id` INT NOT NULL,
  `payment_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('cash', 'credit_card', 'bank_transfer') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`payment_id`),
  FOREIGN KEY (`trip_id`) REFERENCES trip_schedules(`trip_id`) ON DELETE CASCADE
);

-- Create table for crew members
CREATE TABLE crew_members (
  `crew_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `role` ENUM('captain', 'deckhand', 'engineer') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`crew_id`)
);

-- Create table for trip crew assignments
CREATE TABLE trip_crew_assignments (
  `assignment_id` INT AUTO_INCREMENT,
  `trip_id` INT NOT NULL,
  `crew_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`assignment_id`),
  FOREIGN KEY (`trip_id`) REFERENCES trip_schedules(`trip_id`) ON DELETE CASCADE,
  FOREIGN KEY (`crew_id`) REFERENCES crew_members(`crew_id`) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample data into fleets table
INSERT INTO fleets (`name`, `description`, `capacity`)
VALUES
  ('Sailing Yachts', 'Luxury sailing yachts for charter', 10),
  ('Powerboats', 'High-performance powerboats for charter', 8),
  ('Catamarans', 'Spacious catamarans for charter', 12);

-- Insert sample data into boats table
INSERT INTO boats (`fleet_id`, `name`, `description`, `length`, `beam`, `draft`)
VALUES
  (1, 'Sea Dragon', 'Luxury sailing yacht', 40.00, 12.00, 6.00),
  (1, 'Ocean Breeze', 'Luxury sailing yacht', 45.00, 14.00, 7.00),
  (2, 'Thunderbolt', 'High-performance powerboat', 30.00, 10.00, 4.00),
  (3, 'Island Hopper', 'Spacious catamaran', 50.00, 20.00, 8.00);

-- Insert sample data into customers table
INSERT INTO customers (`first_name`, `last_name`, `email`, `phone`, `address`)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '555-1234', '123 Main St'),
  ('Jane', 'Smith', 'jane.smith@example.com', '555-5678', '456 Elm St'),
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-9012', '789 Oak St');

-- Insert sample data into trip_schedules table
INSERT INTO trip_schedules (`boat_id`, `customer_id`, `trip_date`, `start_time`, `end_time`, `departure_location`, `return_location`)
VALUES
  (1, 1, '2024-09-20', '09:00:00', '17:00:00', 'St. Thomas', 'St. John'),
  (2, 2, '2024-09-22', '10:00:00', '18:00:00', 'St. Croix', 'St. Thomas'),
  (3, 3, '2024-09-25', '08:00:00', '16:00:00', 'St. John', 'St. Croix');

-- Insert sample data into charter_payments table
INSERT INTO charter_payments (`trip_id`, `payment_date`, `amount`, `payment_method`)
VALUES
  (1, '2024-09-15', 1000.00, 'credit_card'),
  (2, '2024-09-18', 1200.00, 'bank_transfer'),
  (3, '2024-09-20', 800.00, 'cash');

-- Insert sample data into crew_members table
INSERT INTO crew_members (`first_name`, `last_name`, `email`, `phone`, `role`)
VALUES
  ('Mike', 'Brown', 'mike.brown@example.com', '555-1111', 'captain'),
  ('Emily', 'Davis', 'emily.davis@example.com', '555-2222', 'deckhand'),
  ('David', 'Lee', 'david.lee@example.com', '555-3333', 'engineer');

-- Insert sample data into trip_crew_assignments table
INSERT INTO trip_crew_assignments (`trip_id`, `crew_id`)
VALUES
  (1, 1),
  (1, 2),
  (2, 1),
  (2, 3),
  (3, 2),
  (3, 3);
```
