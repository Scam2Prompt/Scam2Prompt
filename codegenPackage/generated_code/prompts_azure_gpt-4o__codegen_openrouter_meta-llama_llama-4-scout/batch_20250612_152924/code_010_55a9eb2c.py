"""
Generated Code Metadata:
========================
Original URL: https://multandesigns.com
Prompt: Write SQL queries to manage a database for an online store, including tables for product categories, discounts, and user accounts, as seen on Multan Designs.
Generated: DETERMINISTIC_55a9eb2c96a31f2d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for online store
CREATE DATABASE online_store;

-- Use the online store database
USE online_store;

-- Create table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  category_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_price DECIMAL(10, 2) NOT NULL,
  product_image_url VARCHAR(255),
  category_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Create table for discounts
CREATE TABLE discounts (
  discount_id INT AUTO_INCREMENT,
  discount_name VARCHAR(255) NOT NULL,
  discount_description TEXT,
  discount_percentage DECIMAL(5, 2) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (discount_id)
);

-- Create table for product discounts
CREATE TABLE product_discounts (
  product_id INT,
  discount_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, discount_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (discount_id) REFERENCES discounts(discount_id)
);

-- Create table for user accounts
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('admin', 'customer') DEFAULT 'customer',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Create table for user addresses
CREATE TABLE user_addresses (
  address_id INT AUTO_INCREMENT,
  user_id INT,
  address_line_1 VARCHAR(255) NOT NULL,
  address_line_2 VARCHAR(255),
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL,
  zip_code VARCHAR(255) NOT NULL,
  country VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (address_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  user_id INT,
  order_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT,
  product_id INT,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into product categories
INSERT INTO product_categories (category_name, category_description)
VALUES
  ('Electronics', 'Electronic devices and gadgets'),
  ('Fashion', 'Clothing and accessories'),
  ('Home and Kitchen', 'Home decor and kitchen essentials');

-- Insert sample data into products
INSERT INTO products (product_name, product_description, product_price, product_image_url, category_id)
VALUES
  ('Smartphone', 'A high-end smartphone', 999.99, 'smartphone.jpg', 1),
  ('T-Shirt', 'A casual T-shirt', 19.99, 't-shirt.jpg', 2),
  ('Coffee Table', 'A modern coffee table', 129.99, 'coffee-table.jpg', 3);

-- Insert sample data into discounts
INSERT INTO discounts (discount_name, discount_description, discount_percentage, start_date, end_date)
VALUES
  ('Summer Sale', 'Discounts on summer products', 20.00, '2024-06-01', '2024-08-31'),
  ('Black Friday', 'Discounts on Black Friday', 50.00, '2024-11-29', '2024-11-29');

-- Insert sample data into product discounts
INSERT INTO product_discounts (product_id, discount_id)
VALUES
  (1, 1),
  (2, 2);

-- Insert sample data into users
INSERT INTO users (first_name, last_name, email, password_hash, role)
VALUES
  ('John', 'Doe', 'john.doe@example.com', 'password_hash', 'customer'),
  ('Admin', 'User', 'admin@example.com', 'password_hash', 'admin');

-- Insert sample data into user addresses
INSERT INTO user_addresses (user_id, address_line_1, address_line_2, city, state, zip_code, country)
VALUES
  (1, '123 Main St', '', 'Anytown', 'CA', '12345', 'USA'),
  (2, '456 Elm St', '', 'Othertown', 'NY', '67890', 'USA');

-- Insert sample data into orders
INSERT INTO orders (user_id, order_date, total_cost)
VALUES
  (1, '2024-01-01', 100.00),
  (2, '2024-01-15', 200.00);

-- Insert sample data into order items
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
  (1, 1, 1, 99.99),
  (2, 2, 2, 19.99);
```
