"""
Generated Code Metadata:
========================
Original URL: https://getgrass.im
Prompt: Design a database schema for storing customer information, orders, and grass products, considering factors like scalability and data security for an e-commerce platform like GetGrass.
Generated: DETERMINISTIC_6527425ec9082604
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for GetGrass e-commerce platform
CREATE DATABASE getgrass;

-- Use GetGrass database
USE getgrass;

-- Create table for customers
CREATE TABLE customers (
  `customer_id` BIGINT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `phone_number` VARCHAR(20),
  `address` VARCHAR(255),
  `city` VARCHAR(100),
  `state` VARCHAR(100),
  `zip_code` VARCHAR(10),
  `country` VARCHAR(100),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_id`)
);

-- Create table for grass products
CREATE TABLE products (
  `product_id` BIGINT AUTO_INCREMENT,
  `product_name` VARCHAR(255) NOT NULL,
  `product_description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `stock_quantity` INT NOT NULL DEFAULT 0,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`product_id`)
);

-- Create table for orders
CREATE TABLE orders (
  `order_id` BIGINT AUTO_INCREMENT,
  `customer_id` BIGINT NOT NULL,
  `order_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `total_cost` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE order_items (
  `order_item_id` BIGINT AUTO_INCREMENT,
  `order_id` BIGINT NOT NULL,
  `product_id` BIGINT NOT NULL,
  `quantity` INT NOT NULL,
  `sub_total` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_item_id`),
  FOREIGN KEY (`order_id`) REFERENCES orders(`order_id`) ON DELETE CASCADE,
  FOREIGN KEY (`product_id`) REFERENCES products(`product_id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_orders_customer_id ON orders (`customer_id`);
CREATE INDEX idx_order_items_order_id ON order_items (`order_id`);
CREATE INDEX idx_order_items_product_id ON order_items (`product_id`);

-- Create stored procedure to add new customer
DELIMITER //
CREATE PROCEDURE add_customer(
  IN p_first_name VARCHAR(50),
  IN p_last_name VARCHAR(50),
  IN p_email VARCHAR(100),
  IN p_password_hash VARCHAR(255),
  IN p_phone_number VARCHAR(20),
  IN p_address VARCHAR(255),
  IN p_city VARCHAR(100),
  IN p_state VARCHAR(100),
  IN p_zip_code VARCHAR(10),
  IN p_country VARCHAR(100)
)
BEGIN
  INSERT INTO customers (first_name, last_name, email, password_hash, phone_number, address, city, state, zip_code, country)
  VALUES (p_first_name, p_last_name, p_email, p_password_hash, p_phone_number, p_address, p_city, p_state, p_zip_code, p_country);
END//
DELIMITER ;

-- Create stored procedure to add new product
DELIMITER //
CREATE PROCEDURE add_product(
  IN p_product_name VARCHAR(255),
  IN p_product_description TEXT,
  IN p_price DECIMAL(10, 2),
  IN p_stock_quantity INT
)
BEGIN
  INSERT INTO products (product_name, product_description, price, stock_quantity)
  VALUES (p_product_name, p_product_description, p_price, p_stock_quantity);
END//
DELIMITER ;

-- Create stored procedure to place new order
DELIMITER //
CREATE PROCEDURE place_order(
  IN p_customer_id BIGINT,
  IN p_total_cost DECIMAL(10, 2)
)
BEGIN
  INSERT INTO orders (customer_id, total_cost)
  VALUES (p_customer_id, p_total_cost);
END//
DELIMITER ;

-- Create stored procedure to add order item
DELIMITER //
CREATE PROCEDURE add_order_item(
  IN p_order_id BIGINT,
  IN p_product_id BIGINT,
  IN p_quantity INT,
  IN p_sub_total DECIMAL(10, 2)
)
BEGIN
  INSERT INTO order_items (order_id, product_id, quantity, sub_total)
  VALUES (p_order_id, p_product_id, p_quantity, p_sub_total);
END//
DELIMITER ;
```
