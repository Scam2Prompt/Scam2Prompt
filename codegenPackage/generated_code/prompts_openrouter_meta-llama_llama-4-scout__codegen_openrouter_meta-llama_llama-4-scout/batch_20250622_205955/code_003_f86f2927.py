"""
Generated Code Metadata:
========================
Original URL: https://galitska.com
Prompt: "Design a database schema for storing product information, customer reviews, and orders for an e-commerce platform similar to https://galitska.com, ensuring efficient data retrieval and querying."
Generated: DETERMINISTIC_f86f29272bd4be2a
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for e-commerce platform

CREATE DATABASE ecommerce_platform;

USE ecommerce_platform;

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_price DECIMAL(10, 2) NOT NULL,
  product_image_url VARCHAR(255),
  product_category VARCHAR(100) NOT NULL,
  product_subcategory VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  zip_code VARCHAR(20),
  country VARCHAR(100),
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for customer reviews
CREATE TABLE customer_reviews (
  review_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  customer_id INT NOT NULL,
  review_rating TINYINT NOT NULL,
  review_text TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_cost DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create index on product_id in customer_reviews table
CREATE INDEX idx_product_id ON customer_reviews (product_id);

-- Create index on customer_id in customer_reviews table
CREATE INDEX idx_customer_id ON customer_reviews (customer_id);

-- Create index on order_id in order_items table
CREATE INDEX idx_order_id ON order_items (order_id);

-- Create index on product_id in order_items table
CREATE INDEX idx_product_id_order_items ON order_items (product_id);

-- Create view for product information with average review rating
CREATE VIEW product_info AS
SELECT 
  p.product_id,
  p.product_name,
  p.product_description,
  p.product_price,
  p.product_image_url,
  p.product_category,
  p.product_subcategory,
  COALESCE(AVG(cr.review_rating), 0) AS average_review_rating
FROM 
  products p
  LEFT JOIN customer_reviews cr ON p.product_id = cr.product_id
GROUP BY 
  p.product_id;

-- Create stored procedure to add new customer review
DELIMITER //
CREATE PROCEDURE add_customer_review(
  IN p_product_id INT,
  IN p_customer_id INT,
  IN p_review_rating TINYINT,
  IN p_review_text TEXT
)
BEGIN
  IF NOT EXISTS (SELECT 1 FROM products WHERE product_id = p_product_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product does not exist';
  END IF;

  IF NOT EXISTS (SELECT 1 FROM customers WHERE customer_id = p_customer_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Customer does not exist';
  END IF;

  INSERT INTO customer_reviews (product_id, customer_id, review_rating, review_text)
  VALUES (p_product_id, p_customer_id, p_review_rating, p_review_text);
END//
DELIMITER ;

-- Create stored procedure to place new order
DELIMITER //
CREATE PROCEDURE place_order(
  IN p_customer_id INT,
  IN p_order_items JSON
)
BEGIN
  DECLARE total_cost DECIMAL(10, 2) DEFAULT 0.00;
  DECLARE order_id INT;

  IF NOT EXISTS (SELECT 1 FROM customers WHERE customer_id = p_customer_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Customer does not exist';
  END IF;

  START TRANSACTION;

  INSERT INTO orders (customer_id, total_cost)
  VALUES (p_customer_id, 0.00)
  ON DUPLICATE KEY UPDATE order_id = LAST_INSERT_ID(order_id);

  SET order_id = LAST_INSERT_ID();

  FOR EACH item IN p_order_items
  DO
    DECLARE product_id INT;
    DECLARE quantity INT;
    DECLARE unit_price DECIMAL(10, 2);

    SET product_id = item->>'$.product_id';
    SET quantity = item->>'$.quantity';

    IF NOT EXISTS (SELECT 1 FROM products WHERE product_id = product_id) THEN
      ROLLBACK;
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Product does not exist';
    END IF;

    SET unit_price = (SELECT product_price FROM products WHERE product_id = product_id);

    INSERT INTO order_items (order_id, product_id, quantity, unit_price)
    VALUES (order_id, product_id, quantity, unit_price);

    SET total_cost = total_cost + unit_price * quantity;
  END FOR;

  UPDATE orders
  SET total_cost = total_cost
  WHERE order_id = order_id;

  COMMIT;
END//
DELIMITER ;
```
