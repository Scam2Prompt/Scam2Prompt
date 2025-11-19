"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Design a database schema for an e-commerce website, including tables for products, customers, orders, and payments, using a relational database management system like MySQL.
Generated: DETERMINISTIC_0ab684e07c4244ef
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce website

-- Create the database
CREATE DATABASE IF NOT EXISTS ecommerce;
USE ecommerce;

-- Table for storing product information
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,                -- Name of the product
    description TEXT,                           -- Description of the product
    price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    stock_quantity INT NOT NULL,               -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing customer information
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL,           -- Customer's first name
    last_name VARCHAR(100) NOT NULL,            -- Customer's last name
    email VARCHAR(255) NOT NULL UNIQUE,         -- Customer's email address
    password_hash VARCHAR(255) NOT NULL,        -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing order information
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    customer_id INT NOT NULL,                   -- Foreign key referencing customers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    total_amount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table for storing payment information
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    order_id INT NOT NULL,                      -- Foreign key referencing orders
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the payment was made
    amount DECIMAL(10, 2) NOT NULL,            -- Amount paid
    payment_method ENUM('Credit Card', 'PayPal', 'Bank Transfer') NOT NULL, -- Method of payment
    status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending', -- Status of the payment
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON products(name);
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_order_customer ON orders(customer_id);
CREATE INDEX idx_payment_order ON payments(order_id);
```
