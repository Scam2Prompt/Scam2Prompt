"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Provide an example of a database schema for managing product categories (e.g., residential systems, commercial systems, accessories) and promotions, as seen on Frigoterm.ro.
Generated: DETERMINISTIC_8f5e41b2e40e0af8
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS product_management;

-- Use database
USE product_management;

-- Create table for product categories
CREATE TABLE IF NOT EXISTS categories (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_category_name` (`name`)
);

-- Create table for products
CREATE TABLE IF NOT EXISTS products (
  `id` INT AUTO_INCREMENT,
  `category_id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_product_category` (`category_id`),
  CONSTRAINT `fk_product_category` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE
);

-- Create table for promotions
CREATE TABLE IF NOT EXISTS promotions (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `discount_type` ENUM('percentage', 'fixed_amount') NOT NULL,
  `discount_value` DECIMAL(10, 2) NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CHECK (`start_date` < `end_date`)
);

-- Create table for product promotions
CREATE TABLE IF NOT EXISTS product_promotions (
  `id` INT AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `promotion_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_product_promotion_product` (`product_id`),
  KEY `fk_product_promotion_promotion` (`promotion_id`),
  CONSTRAINT `fk_product_promotion_product` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_product_promotion_promotion` FOREIGN KEY (`promotion_id`) REFERENCES `promotions` (`id`) ON DELETE CASCADE,
  UNIQUE KEY `uk_product_promotion` (`product_id`, `promotion_id`)
);

-- Insert sample data
INSERT INTO categories (name, description) VALUES
  ('Residential Systems', 'Systems for residential use'),
  ('Commercial Systems', 'Systems for commercial use'),
  ('Accessories', 'Accessories for systems');

INSERT INTO products (category_id, name, description, price) VALUES
  (1, 'Residential System 1', 'Description for residential system 1', 1000.00),
  (1, 'Residential System 2', 'Description for residential system 2', 2000.00),
  (2, 'Commercial System 1', 'Description for commercial system 1', 5000.00),
  (3, 'Accessory 1', 'Description for accessory 1', 50.00);

INSERT INTO promotions (name, description, discount_type, discount_value, start_date, end_date) VALUES
  ('Summer Sale', 'Discount for summer', 'percentage', 10.00, '2024-06-01', '2024-08-31'),
  ('Black Friday', 'Discount for black friday', 'fixed_amount', 100.00, '2024-11-01', '2024-11-30');

INSERT INTO product_promotions (product_id, promotion_id) VALUES
  (1, 1),
  (2, 1),
  (3, 2),
  (4, 1);
```
