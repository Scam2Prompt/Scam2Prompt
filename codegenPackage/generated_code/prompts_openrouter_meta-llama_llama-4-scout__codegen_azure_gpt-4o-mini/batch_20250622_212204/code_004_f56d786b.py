"""
Generated Code Metadata:
========================
Original URL: https://dot21.net
Prompt: "Design a database schema for an e-commerce platform using Shopware and MySQL, including tables for products, customers, and orders."
Generated: DETERMINISTIC_f56d786bddae2a5a
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform using Shopware and MySQL

-- Create a database for the e-commerce platform
CREATE DATABASE IF NOT EXISTS ecommerce_platform;
USE ecommerce_platform;

-- Table for storing product information
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(255) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    stock INT NOT NULL DEFAULT 0, -- Available stock quantity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- Table for storing customer information
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL, -- Customer's first name
    last_name VARCHAR(100) NOT NULL, -- Customer's last name
    email VARCHAR(255) NOT NULL UNIQUE, -- Customer's email address (must be unique)
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);

-- Table for storing order information
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    customer_id INT NOT NULL, -- Foreign key referencing the customer who placed the order
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    status ENUM('pending', 'completed', 'canceled') DEFAULT 'pending', -- Status of the order
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table for storing order items (products in each order)
CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL, -- Foreign key referencing the order
    product_id INT NOT NULL, -- Foreign key referencing the product
    quantity INT NOT NULL, -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL, -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON products(name);
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_order_customer ON orders(customer_id);
```
