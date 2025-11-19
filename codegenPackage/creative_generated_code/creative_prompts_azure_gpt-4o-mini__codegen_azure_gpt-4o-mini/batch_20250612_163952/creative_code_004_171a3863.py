"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://11tesorosibericos.com
Prompt: Design a database schema for an online store that includes tables for products like wines and gift baskets, as seen on 11 Tesoros Ibéricos, ensuring it supports various product categories and pricing.
Generated: DETERMINISTIC_171a386377ce54e4
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- This SQL script creates a database schema for an online store focusing on products like wines and gift baskets.

-- Create the database
CREATE DATABASE online_store;

-- Switch to the new database
USE online_store;

-- Table for product categories
CREATE TABLE product_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,          -- Name of the category
    description TEXT,                              -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the category was created
);

-- Table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product
    category_id INT,                               -- Foreign key referencing product_categories
    product_name VARCHAR(150) NOT NULL,           -- Name of the product
    description TEXT,                              -- Description of the product
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    stock_quantity INT DEFAULT 0,                 -- Quantity in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table for customers
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,              -- Customer's first name
    last_name VARCHAR(50) NOT NULL,                -- Customer's last name
    email VARCHAR(100) NOT NULL UNIQUE,            -- Customer's email address
    password_hash VARCHAR(255) NOT NULL,           -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the customer was created
);

-- Table for orders
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each order
    customer_id INT,                               -- Foreign key referencing customers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL,         -- Total amount for the order
    status ENUM('Pending', 'Shipped', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table for order items
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each order item
    order_id INT,                                  -- Foreign key referencing orders
    product_id INT,                                -- Foreign key referencing products
    quantity INT NOT NULL,                         -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table for reviews
CREATE TABLE product_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each review
    product_id INT,                                -- Foreign key referencing products
    customer_id INT,                               -- Foreign key referencing customers
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating between 1 and 5
    review_text TEXT,                              -- Review text
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Index for faster searching on products
CREATE INDEX idx_product_name ON products(product_name);
```
