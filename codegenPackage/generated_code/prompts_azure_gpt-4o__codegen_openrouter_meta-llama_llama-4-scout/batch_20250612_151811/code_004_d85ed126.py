"""
Generated Code Metadata:
========================
Original URL: https://balancer-app.pages.dev
Prompt: Write a database schema for a restaurant management system that includes tables for menu items, reservations, and takeaway orders, inspired by the structure of RAVIOLI HOUSE's offerings.
Generated: DETERMINISTIC_d85ed1265e965aa4
Batch ID: 20250612_151811
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

-- Create table for menu item ingredients
CREATE TABLE menu_item_ingredients (
  `id` INT AUTO_INCREMENT,
  `menu_item_id` INT NOT NULL,
  `ingredient` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`) ON DELETE CASCADE
);

-- Create table for reservations
CREATE TABLE reservations (
  `id` INT AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  `party_size` INT NOT NULL,
  `customer_name` VARCHAR(255) NOT NULL,
  `customer_phone` VARCHAR(20) NOT NULL,
  `status` ENUM('pending', 'confirmed', 'cancelled') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for takeaway orders
CREATE TABLE takeaway_orders (
  `id` INT AUTO_INCREMENT,
  `order_date` DATE NOT NULL,
  `order_time` TIME NOT NULL,
  `customer_name` VARCHAR(255) NOT NULL,
  `customer_phone` VARCHAR(20) NOT NULL,
  `total` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'prepared', 'picked_up', 'cancelled') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for takeaway order items
CREATE TABLE takeaway_order_items (
  `id` INT AUTO_INCREMENT,
  `takeaway_order_id` INT NOT NULL,
  `menu_item_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`takeaway_order_id`) REFERENCES takeaway_orders(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  `id` INT AUTO_INCREMENT,
  `reservation_id` INT,
  `takeaway_order_id` INT,
  `payment_method` ENUM('cash', 'credit_card', 'online_payment') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`reservation_id`) REFERENCES reservations(`id`) ON DELETE SET NULL,
  FOREIGN KEY (`takeaway_order_id`) REFERENCES takeaway_orders(`id`) ON DELETE SET NULL
);
```
