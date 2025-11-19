"""
Generated Code Metadata:
========================
Original URL: https://cornerstonetrading.biz
Prompt: Create a database schema in SQL for managing user accounts, orders, and product categories, inspired by the structure of the "DUGEMSLOT" platform.
Generated: DETERMINISTIC_72967147a8183567
Batch ID: 20250612_154251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for DUGEMSLOT platform

-- Create database
CREATE DATABASE DUGEMSLOT;

-- Use database
USE DUGEMSLOT;

-- Create table for user accounts
CREATE TABLE Users (
    `id` INT AUTO_INCREMENT,
    `username` VARCHAR(50) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `password_hash` VARCHAR(255) NOT NULL,
    `role` ENUM('admin', 'customer') NOT NULL DEFAULT 'customer',
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY (`username`),
    UNIQUE KEY (`email`)
);

-- Create table for product categories
CREATE TABLE ProductCategories (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `description` TEXT,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);

-- Create table for products
CREATE TABLE Products (
    `id` INT AUTO_INCREMENT,
    `category_id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `description` TEXT,
    `price` DECIMAL(10, 2) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`category_id`) REFERENCES ProductCategories(`id`) ON DELETE CASCADE
);

-- Create table for orders
CREATE TABLE Orders (
    `id` INT AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `order_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `total` DECIMAL(10, 2) NOT NULL,
    `status` ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE OrderItems (
    `id` INT AUTO_INCREMENT,
    `order_id` INT NOT NULL,
    `product_id` INT NOT NULL,
    `quantity` INT NOT NULL,
    `subtotal` DECIMAL(10, 2) NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`order_id`) REFERENCES Orders(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`product_id`) REFERENCES Products(`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_orders_user_id ON Orders (`user_id`);
CREATE INDEX idx_order_items_order_id ON OrderItems (`order_id`);
CREATE INDEX idx_order_items_product_id ON OrderItems (`product_id`);
CREATE INDEX idx_products_category_id ON Products (`category_id`);
```
