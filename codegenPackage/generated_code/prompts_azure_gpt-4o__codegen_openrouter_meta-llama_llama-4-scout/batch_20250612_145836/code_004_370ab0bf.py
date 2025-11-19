"""
Generated Code Metadata:
========================
Original URL: https://comestim.com.co
Prompt: Suggest a database schema for storing customer feedback and order details for a company offering edible printing services.
Generated: DETERMINISTIC_370ab0bf698829b7
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for edible printing services
CREATE DATABASE edible_printing_services;

-- Use the database
USE edible_printing_services;

-- Create table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` TEXT,
  PRIMARY KEY (`customer_id`)
);

-- Create table for orders
CREATE TABLE orders (
  `order_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `order_date` DATE NOT NULL,
  `total_cost` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'in_progress', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`order_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE order_items (
  `order_item_id` INT AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `product_name` VARCHAR(255) NOT NULL,
  `quantity` INT NOT NULL,
  `unit_price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`order_item_id`),
  FOREIGN KEY (`order_id`) REFERENCES orders(`order_id`) ON DELETE CASCADE
);

-- Create table for customer feedback
CREATE TABLE customer_feedback (
  `feedback_id` INT AUTO_INCREMENT,
  `order_id` INT,
  `customer_id` INT,
  `feedback_date` DATE NOT NULL,
  `rating` TINYINT NOT NULL CHECK (`rating` BETWEEN 1 AND 5),
  `comment` TEXT,
  PRIMARY KEY (`feedback_id`),
  FOREIGN KEY (`order_id`) REFERENCES orders(`order_id`) ON DELETE SET NULL,
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE SET NULL
);

-- Create table for edible printing products
CREATE TABLE products (
  `product_id` INT AUTO_INCREMENT,
  `product_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`product_id`)
);

-- Create table for order product mapping
CREATE TABLE order_products (
  `order_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`order_id`, `product_id`),
  FOREIGN KEY (`order_id`) REFERENCES orders(`order_id`) ON DELETE CASCADE,
  FOREIGN KEY (`product_id`) REFERENCES products(`product_id`) ON DELETE CASCADE
);
```

```sql
-- example usage
DELIMITER //

CREATE PROCEDURE add_order(
  IN p_customer_id INT,
  IN p_order_date DATE,
  IN p_total_cost DECIMAL(10, 2)
)
BEGIN
  INSERT INTO orders (customer_id, order_date, total_cost)
  VALUES (p_customer_id, p_order_date, p_total_cost);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE add_feedback(
  IN p_order_id INT,
  IN p_customer_id INT,
  IN p_rating TINYINT,
  IN p_comment TEXT
)
BEGIN
  INSERT INTO customer_feedback (order_id, customer_id, feedback_date, rating, comment)
  VALUES (p_order_id, p_customer_id, CURDATE(), p_rating, p_comment);
END //

DELIMITER ;
```
