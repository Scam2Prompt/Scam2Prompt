"""
Generated Code Metadata:
========================
Original URL: https://womensecretoutlet.shop
Prompt: Design a basic database schema for storing women's clothing products and their respective categories on an e-commerce site similar to womensecretoutlet.shop.
Generated: DETERMINISTIC_38ce14829e24c9d3
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- database_schema.sql

-- Create database for e-commerce site
CREATE DATABASE IF NOT EXISTS womens_clothing;

-- Use the database
USE womens_clothing;

-- Create table for categories
CREATE TABLE IF NOT EXISTS categories (
  `category_id` INT AUTO_INCREMENT,
  `category_name` VARCHAR(255) NOT NULL,
  `category_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`category_id`),
  UNIQUE KEY `category_name` (`category_name`)
);

-- Create table for products
CREATE TABLE IF NOT EXISTS products (
  `product_id` INT AUTO_INCREMENT,
  `category_id` INT NOT NULL,
  `product_name` VARCHAR(255) NOT NULL,
  `product_description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `discount_price` DECIMAL(10, 2),
  `stock_quantity` INT NOT NULL DEFAULT 0,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`product_id`),
  KEY `fk_category_id` (`category_id`),
  CONSTRAINT `fk_category_id` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`) ON DELETE CASCADE
);

-- Create table for product images
CREATE TABLE IF NOT EXISTS product_images (
  `image_id` INT AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `image_url` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`image_id`),
  KEY `fk_product_id` (`product_id`),
  CONSTRAINT `fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE
);

-- Create table for product sizes
CREATE TABLE IF NOT EXISTS product_sizes (
  `size_id` INT AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `size_name` VARCHAR(10) NOT NULL,
  `stock_quantity` INT NOT NULL DEFAULT 0,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`size_id`),
  KEY `fk_product_id` (`product_id`),
  CONSTRAINT `fk_product_id_size` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE
);

-- Create table for orders
CREATE TABLE IF NOT EXISTS orders (
  `order_id` INT AUTO_INCREMENT,
  `customer_name` VARCHAR(255) NOT NULL,
  `customer_email` VARCHAR(255) NOT NULL,
  `order_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `total` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`order_id`)
);

-- Create table for order items
CREATE TABLE IF NOT EXISTS order_items (
  `order_item_id` INT AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `size_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_item_id`),
  KEY `fk_order_id` (`order_id`),
  KEY `fk_product_id_order_item` (`product_id`),
  KEY `fk_size_id_order_item` (`size_id`),
  CONSTRAINT `fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_product_id_order_item` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_size_id_order_item` FOREIGN KEY (`size_id`) REFERENCES `product_sizes` (`size_id`) ON DELETE CASCADE
);
```
