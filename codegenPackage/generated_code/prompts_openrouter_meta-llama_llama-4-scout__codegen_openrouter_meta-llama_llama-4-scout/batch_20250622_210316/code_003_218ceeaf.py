"""
Generated Code Metadata:
========================
Original URL: https://mollinari.com.pl
Prompt: Design a database schema for storing information about a restaurant like Mollinari, including tables for menu items, reservations, and customer reviews.
Generated: DETERMINISTIC_218ceeafc78a901d
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for restaurant information

-- Create database
CREATE DATABASE restaurant_db;

-- Use database
USE restaurant_db;

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
  `phone` VARCHAR(20),
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
  `status` ENUM('pending', 'confirmed', 'cancelled') DEFAULT 'pending',
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
  `rating` TINYINT NOT NULL CHECK (`rating` BETWEEN 1 AND 5),
  `review` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`) ON DELETE SET NULL
);

-- Create table for orders
CREATE TABLE orders (
  `id` INT AUTO_INCREMENT,
  `reservation_id` INT,
  `menu_item_id` INT NOT NULL,
  `quantity` INT NOT NULL DEFAULT 1,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`reservation_id`) REFERENCES reservations(`id`) ON DELETE SET NULL,
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`) ON DELETE CASCADE
);

-- Example inserts for testing
INSERT INTO menu_items (name, description, price, category)
VALUES 
('Bruschetta', 'Toasted bread with fresh tomatoes', 8.99, 'appetizer'),
('Spaghetti', 'Classic Italian dish', 16.99, 'entree'),
('Tiramisu', 'Coffee-flavored dessert', 7.99, 'dessert');

INSERT INTO customers (first_name, last_name, email, phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210');

INSERT INTO reservations (customer_id, reservation_date, reservation_time, party_size)
VALUES 
(1, '2024-09-20', '18:00:00', 4),
(2, '2024-09-21', '19:00:00', 2);

INSERT INTO reviews (customer_id, menu_item_id, rating, review)
VALUES 
(1, 1, 5, 'Excellent appetizer!'),
(2, 2, 4, 'Good but not great');

INSERT INTO orders (reservation_id, menu_item_id, quantity)
VALUES 
(1, 1, 2),
(1, 2, 1),
(2, 3, 1);
```
