"""
Generated Code Metadata:
========================
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Design a database schema for a luxury villa rental service that includes tables for properties, amenities, and customer reviews, reflecting the offerings of Diamond Villa in Corfu.
Generated: DETERMINISTIC_d37a16456d6c00db
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for luxury villa rental service
CREATE DATABASE IF NOT EXISTS diamond_villa;

-- Use the database
USE diamond_villa;

-- Create table for properties
CREATE TABLE IF NOT EXISTS properties (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price_per_night` DECIMAL(10, 2) NOT NULL,
  `capacity` INT NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `country` VARCHAR(100) NOT NULL,
  `postal_code` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for amenities
CREATE TABLE IF NOT EXISTS amenities (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for property_amenities (many-to-many relationship)
CREATE TABLE IF NOT EXISTS property_amenities (
  `property_id` INT NOT NULL,
  `amenity_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`property_id`, `amenity_id`),
  FOREIGN KEY (`property_id`) REFERENCES properties(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`amenity_id`) REFERENCES amenities(`id`) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE IF NOT EXISTS customers (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for reviews
CREATE TABLE IF NOT EXISTS reviews (
  `id` INT AUTO_INCREMENT,
  `property_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `rating` TINYINT NOT NULL CHECK (`rating` BETWEEN 1 AND 5),
  `comment` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`property_id`) REFERENCES properties(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`) ON DELETE CASCADE,
  UNIQUE (`property_id`, `customer_id`)
);

-- Create table for bookings
CREATE TABLE IF NOT EXISTS bookings (
  `id` INT AUTO_INCREMENT,
  `property_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `check_in_date` DATE NOT NULL,
  `check_out_date` DATE NOT NULL,
  `total_cost` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'confirmed', 'cancelled') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`property_id`) REFERENCES properties(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`) ON DELETE CASCADE
);
```

```sql
-- example_data.sql

-- Insert example data into properties table
INSERT INTO properties (name, description, price_per_night, capacity, address, city, country, postal_code)
VALUES
  ('Villa Serenity', 'Luxury villa with private pool and garden', 500.00, 8, 'Villa Serenity, Paleokastritsa', 'Corfu', 'Greece', '490 84'),
  ('Villa Paradise', 'Stunning villa with sea views and private beach', 800.00, 10, 'Villa Paradise, Sidari', 'Corfu', 'Greece', '490 84'),
  ('Villa Relax', 'Cozy villa with pool and BBQ facilities', 300.00, 6, 'Villa Relax, Kassiopi', 'Corfu', 'Greece', '490 84');

-- Insert example data into amenities table
INSERT INTO amenities (name, description)
VALUES
  ('Private Pool', 'Private pool for villa guests'),
  ('Garden', 'Beautiful garden with outdoor seating'),
  ('Private Beach', 'Access to private beach with sun loungers'),
  ('BBQ Facilities', 'BBQ facilities for outdoor cooking'),
  ('Wi-Fi', 'Free Wi-Fi for villa guests');

-- Insert example data into property_amenities table
INSERT INTO property_amenities (property_id, amenity_id)
VALUES
  (1, 1),
  (1, 2),
  (1, 5),
  (2, 1),
  (2, 3),
  (2, 5),
  (3, 1),
  (3, 4),
  (3, 5);

-- Insert example data into customers table
INSERT INTO customers (first_name, last_name, email, phone_number)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '+30 1234567890'),
  ('Jane', 'Smith', 'jane.smith@example.com', '+30 9876543210'),
  ('Bob', 'Johnson', 'bob.johnson@example.com', '+30 5555555555');

-- Insert example data into reviews table
INSERT INTO reviews (property_id, customer_id, rating, comment)
VALUES
  (1, 1, 5, 'Excellent villa with beautiful pool and garden'),
  (2, 2, 4, 'Lovely villa with stunning sea views'),
  (3, 3, 3, 'Nice villa but could use some improvements');

-- Insert example data into bookings table
INSERT INTO bookings (property_id, customer_id, check_in_date, check_out_date, total_cost)
VALUES
  (1, 1, '2024-09-01', '2024-09-08', 3500.00),
  (2, 2, '2024-08-15', '2024-08-22', 5600.00),
  (3, 3, '2024-07-20', '2024-07-27', 2100.00);
```
