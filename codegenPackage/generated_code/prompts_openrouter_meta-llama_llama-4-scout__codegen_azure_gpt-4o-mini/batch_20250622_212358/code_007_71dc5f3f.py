"""
Generated Code Metadata:
========================
Original URL: https://celinedionshop.com
Prompt: Design a database schema using MySQL to store Celine Dion merchandise products, orders, and customer information for the Celine Dion Shop e-commerce website.
Generated: DETERMINISTIC_71dc5f3f4555afda
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Celine Dion Shop e-commerce website

-- Create the database
CREATE DATABASE IF NOT EXISTS celine_dion_shop;
USE celine_dion_shop;

-- Table to store customer information
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,           -- Customer's first name
    last_name VARCHAR(50) NOT NULL,            -- Customer's last name
    email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address (unique)
    phone VARCHAR(15),                         -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product information
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    product_name VARCHAR(100) NOT NULL,         -- Name of the product
    description TEXT,                            -- Description of the product
    price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,      -- Quantity of the product in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store orders
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each order
    customer_id INT NOT NULL,                    -- Foreign key referencing customers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store order items (products in each order)
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL,                         -- Foreign key referencing orders
    product_id INT NOT NULL,                       -- Foreign key referencing products
    quantity INT NOT NULL,                         -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store product categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each category
    category_name VARCHAR(50) NOT NULL UNIQUE,     -- Name of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to associate products with categories
CREATE TABLE IF NOT EXISTS product_categories (
    product_id INT NOT NULL,                       -- Foreign key referencing products
    category_id INT NOT NULL,                      -- Foreign key referencing categories
    PRIMARY KEY (product_id, category_id),        -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_product_name ON products(product_name);
CREATE INDEX idx_order_date ON orders(order_date);
```
