"""
Generated Code Metadata:
========================
Original URL: https://farmaciasantiagoapostol.com
Prompt: Design a database schema for an online pharmacy, including tables for products, customers, orders, and news articles, inspired by the structure of farmaciasantiagoapostol.com.
Generated: DETERMINISTIC_8dc0d85bdfca9f5a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for online pharmacy

CREATE DATABASE online_pharmacy;

USE online_pharmacy;

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  address VARCHAR(255),
  city VARCHAR(50),
  state VARCHAR(50),
  zip_code VARCHAR(10),
  phone_number VARCHAR(20),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for news articles
CREATE TABLE news_articles (
  article_id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (article_id)
);

-- Create index on customer email for faster lookup
CREATE INDEX idx_customer_email ON customers(email);

-- Create index on product name for faster lookup
CREATE INDEX idx_product_name ON products(name);

-- Create trigger to prevent negative stock quantity
DELIMITER $$
CREATE TRIGGER prevent_negative_stock
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
  IF NEW.stock_quantity < 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot set stock quantity to negative value';
  END IF;
END$$
DELIMITER ;

-- Example data for testing
INSERT INTO products (name, description, price, stock_quantity)
VALUES
  ('Product 1', 'This is product 1', 10.99, 100),
  ('Product 2', 'This is product 2', 9.99, 50),
  ('Product 3', 'This is product 3', 12.99, 200);

INSERT INTO customers (first_name, last_name, email, password_hash, address, city, state, zip_code, phone_number)
VALUES
  ('John', 'Doe', 'john.doe@example.com', 'password_hash', '123 Main St', 'Anytown', 'CA', '12345', '123-456-7890'),
  ('Jane', 'Doe', 'jane.doe@example.com', 'password_hash', '456 Elm St', 'Othertown', 'NY', '67890', '987-654-3210');

INSERT INTO orders (customer_id, total, status)
VALUES
  (1, 10.99, 'pending'),
  (2, 9.99, 'shipped');

INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES
  (1, 1, 1, 10.99),
  (2, 2, 1, 9.99);

INSERT INTO news_articles (title, content)
VALUES
  ('Article 1', 'This is article 1'),
  ('Article 2', 'This is article 2');
```
