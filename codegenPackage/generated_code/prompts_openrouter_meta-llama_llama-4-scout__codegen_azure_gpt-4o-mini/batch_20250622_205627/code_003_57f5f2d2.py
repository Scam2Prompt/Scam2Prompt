"""
Generated Code Metadata:
========================
Original URL: https://www.merchandiso.com
Prompt: Create a simple database schema to manage orders and inventory for a company that sells customized promotional souvenirs using MySQL.
Generated: DETERMINISTIC_57f5f2d2c73ab392
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the promotional souvenirs company
CREATE DATABASE IF NOT EXISTS promotional_souvenirs;

-- Use the created database
USE promotional_souvenirs;

-- Table to store information about products
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,        -- Name of the product
    description TEXT,                           -- Description of the product
    price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,     -- Quantity of the product in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store customer information
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL,           -- Customer's first name
    last_name VARCHAR(100) NOT NULL,            -- Customer's last name
    email VARCHAR(255) NOT NULL UNIQUE,         -- Customer's email address
    phone VARCHAR(15),                          -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store orders
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    customer_id INT NOT NULL,                   -- Foreign key referencing customers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
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

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON products(product_name);
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_order_date ON orders(order_date);
```
