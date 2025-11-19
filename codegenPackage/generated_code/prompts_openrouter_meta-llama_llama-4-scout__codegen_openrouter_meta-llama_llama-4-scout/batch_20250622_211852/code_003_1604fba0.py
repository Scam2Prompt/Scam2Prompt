"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Create a SQL query to manage inventory for an online clothing store like Dandaloja, including tables for products, sizes, and prices.
Generated: DETERMINISTIC_1604fba0fb78632d
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for online clothing store
CREATE DATABASE IF NOT EXISTS dandaloja;

-- Use database
USE dandaloja;

-- Create table for products
CREATE TABLE IF NOT EXISTS products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_category VARCHAR(100) NOT NULL,
  product_subcategory VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for sizes
CREATE TABLE IF NOT EXISTS sizes (
  size_id INT AUTO_INCREMENT,
  size_name VARCHAR(20) NOT NULL,
  size_description VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (size_id)
);

-- Create table for product sizes
CREATE TABLE IF NOT EXISTS product_sizes (
  product_size_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  size_id INT NOT NULL,
  stock_quantity INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_size_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (size_id) REFERENCES sizes(size_id) ON DELETE CASCADE
);

-- Create table for prices
CREATE TABLE IF NOT EXISTS prices (
  price_id INT AUTO_INCREMENT,
  product_size_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  discount DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (price_id),
  FOREIGN KEY (product_size_id) REFERENCES product_sizes(product_size_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_product_name ON products (product_name);
CREATE INDEX idx_size_name ON sizes (size_name);
CREATE INDEX idx_product_size_stock ON product_sizes (product_id, size_id, stock_quantity);
CREATE INDEX idx_price_product_size ON prices (product_size_id, price);

-- Example insert queries
INSERT INTO products (product_name, product_description, product_category, product_subcategory)
VALUES 
('T-Shirt', 'Basic T-Shirt', 'Tops', 'Casual Wear'),
('Jeans', 'Slim Fit Jeans', 'Bottoms', 'Casual Wear');

INSERT INTO sizes (size_name, size_description)
VALUES 
('S', 'Small'),
('M', 'Medium'),
('L', 'Large');

INSERT INTO product_sizes (product_id, size_id, stock_quantity)
VALUES 
(1, 1, 100),
(1, 2, 150),
(1, 3, 120),
(2, 1, 80),
(2, 2, 100),
(2, 3, 90);

INSERT INTO prices (product_size_id, price, discount)
VALUES 
(1, 19.99, 0.00),
(2, 19.99, 5.00),
(3, 19.99, 0.00),
(4, 29.99, 10.00),
(5, 29.99, 0.00),
(6, 29.99, 5.00);

-- Procedure to update stock quantity
DELIMITER //
CREATE PROCEDURE update_stock_quantity(
  IN product_id INT,
  IN size_id INT,
  IN quantity INT
)
BEGIN
  UPDATE product_sizes
  SET stock_quantity = stock_quantity + quantity
  WHERE product_id = product_id AND size_id = size_id;
END//
DELIMITER ;

-- Procedure to get product details with sizes and prices
DELIMITER //
CREATE PROCEDURE get_product_details(
  IN product_id INT
)
BEGIN
  SELECT 
    p.product_name,
    p.product_description,
    s.size_name,
    ps.stock_quantity,
    pr.price,
    pr.discount
  FROM 
    products p
  JOIN 
    product_sizes ps ON p.product_id = ps.product_id
  JOIN 
    sizes s ON ps.size_id = s.size_id
  JOIN 
    prices pr ON ps.product_size_id = pr.product_size_id
  WHERE 
    p.product_id = product_id;
END//
DELIMITER ;
```
