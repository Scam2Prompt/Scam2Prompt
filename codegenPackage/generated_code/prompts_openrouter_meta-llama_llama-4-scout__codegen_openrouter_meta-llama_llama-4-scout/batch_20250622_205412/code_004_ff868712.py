"""
Generated Code Metadata:
========================
Original URL: https://amici.nz
Prompt: Design a database schema for a restaurant management system that includes tables for menu items, reservations, and customer reviews, using Amici's features as a reference.
Generated: DETERMINISTIC_ff868712d9f7051a
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- restaurant_management_system.sql

-- Create database
CREATE DATABASE restaurant_management_system;

-- Use database
USE restaurant_management_system;

-- Create table for menu items
CREATE TABLE menu_items (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `category` ENUM('appetizer', 'entree', 'dessert', 'drink') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for customers
CREATE TABLE customers (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for reservations
CREATE TABLE reservations (
  `id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `reservation_date` DATE NOT NULL,
  `reservation_time` TIME NOT NULL,
  `party_size` INT NOT NULL,
  `status` ENUM('pending', 'confirmed', 'cancelled') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`) ON DELETE CASCADE
);

-- Create table for customer reviews
CREATE TABLE reviews (
  `id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `menu_item_id` INT,
  `reservation_id` INT,
  `rating` TINYINT NOT NULL CHECK (`rating` BETWEEN 1 AND 5),
  `review` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`) ON DELETE SET NULL,
  FOREIGN KEY (`reservation_id`) REFERENCES reservations(`id`) ON DELETE SET NULL
);

-- Create table for orders
CREATE TABLE orders (
  `id` INT AUTO_INCREMENT,
  `reservation_id` INT NOT NULL,
  `menu_item_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`reservation_id`) REFERENCES reservations(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`) ON DELETE CASCADE
);

-- Example inserts
INSERT INTO menu_items (name, description, price, category)
VALUES 
('Grilled Chicken', 'Savory grilled chicken breast', 14.99, 'entree'),
('Tomato Soup', 'Fresh tomato soup with basil', 6.99, 'soup'),
('Cheesecake', 'Rich and creamy cheesecake', 7.99, 'dessert');

INSERT INTO customers (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john@example.com', '123-456-7890'),
('Jane', 'Doe', 'jane@example.com', '098-765-4321');

INSERT INTO reservations (customer_id, reservation_date, reservation_time, party_size)
VALUES 
(1, '2024-09-17', '18:00:00', 2),
(2, '2024-09-18', '19:00:00', 4);

INSERT INTO reviews (customer_id, menu_item_id, reservation_id, rating, review)
VALUES 
(1, 1, 1, 5, 'Delicious grilled chicken!'),
(2, 3, 2, 4, 'Cheesecake was amazing!');

INSERT INTO orders (reservation_id, menu_item_id, quantity)
VALUES 
(1, 1, 2),
(1, 2, 1),
(2, 3, 1);
```
