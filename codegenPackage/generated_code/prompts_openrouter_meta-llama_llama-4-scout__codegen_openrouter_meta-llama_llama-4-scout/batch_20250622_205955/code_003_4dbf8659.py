"""
Generated Code Metadata:
========================
Original URL: https://toys-kopitsa.com.ua
Prompt: Design a simple database schema to store information about soft toys, customers, and orders for an e-commerce platform similar to https://toys-kopitsa.com.ua, using a relational database management system like MySQL.
Generated: DETERMINISTIC_4dbf8659df937ae2
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for e-commerce platform
CREATE DATABASE toys_kopitsa;

-- Use the created database
USE toys_kopitsa;

-- Create table for soft toys
CREATE TABLE soft_toys (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `stock_quantity` INT NOT NULL DEFAULT 0,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for customers
CREATE TABLE customers (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL UNIQUE,
  `password` VARCHAR(255) NOT NULL,
  `address` TEXT,
  `phone_number` VARCHAR(20),
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for orders
CREATE TABLE orders (
  `id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `order_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `total_cost` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE order_items (
  `id` INT AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `soft_toy_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `subtotal` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`order_id`) REFERENCES orders(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`soft_toy_id`) REFERENCES soft_toys(`id`) ON DELETE CASCADE
);

-- Create index on customer_id in orders table
CREATE INDEX idx_customer_id ON orders (customer_id);

-- Create index on order_id in order_items table
CREATE INDEX idx_order_id ON order_items (order_id);

-- Create index on soft_toy_id in order_items table
CREATE INDEX idx_soft_toy_id ON order_items (soft_toy_id);
```
