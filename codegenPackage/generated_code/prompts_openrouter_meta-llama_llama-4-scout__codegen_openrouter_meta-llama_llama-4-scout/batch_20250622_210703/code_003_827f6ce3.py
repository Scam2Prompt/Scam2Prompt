"""
Generated Code Metadata:
========================
Original URL: https://bernynovias.com
Prompt: "Design a database schema for an e-commerce platform that sells custom wedding dresses, party dresses, and accessories, with attributes like product type, price, and region-specific categories."
Generated: DETERMINISTIC_827f6ce32fcfa18a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the e-commerce platform
CREATE DATABASE ecommerce_platform;

-- Use the ecommerce_platform database
USE ecommerce_platform;

-- Create a table for regions
CREATE TABLE regions (
  region_id INT AUTO_INCREMENT,
  region_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (region_id)
);

-- Create a table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  region_id INT,
  PRIMARY KEY (category_id),
  FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_type ENUM('wedding_dress', 'party_dress', 'accessory') NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  category_id INT,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Create a table for product images
CREATE TABLE product_images (
  image_id INT AUTO_INCREMENT,
  product_id INT,
  image_url VARCHAR(255) NOT NULL,
  PRIMARY KEY (image_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create a table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  address VARCHAR(255),
  city VARCHAR(255),
  state VARCHAR(255),
  zip_code VARCHAR(255),
  country VARCHAR(255),
  phone_number VARCHAR(255),
  PRIMARY KEY (customer_id)
);

-- Create a table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT,
  order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create a table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT,
  product_id INT,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create a table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT,
  payment_method ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  payment_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
```
