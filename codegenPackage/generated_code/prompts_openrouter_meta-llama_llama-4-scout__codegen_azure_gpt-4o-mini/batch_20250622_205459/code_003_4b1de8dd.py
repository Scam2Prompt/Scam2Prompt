"""
Generated Code Metadata:
========================
Original URL: https://baochuanco.com
Prompt: "Design a database schema for a wire mesh products company, including tables for products, customers, orders, and suppliers, using MySQL."
Generated: DETERMINISTIC_4b1de8dde69fbd1b
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a wire mesh products company

-- Create the database
CREATE DATABASE wire_mesh_company;
USE wire_mesh_company;

-- Table for storing product information
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,        -- Name of the product
    description TEXT,                           -- Description of the product
    price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    stock_quantity INT NOT NULL,               -- Quantity in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing customer information
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL,           -- Customer's first name
    last_name VARCHAR(100) NOT NULL,            -- Customer's last name
    email VARCHAR(255) NOT NULL UNIQUE,         -- Customer's email address
    phone VARCHAR(20),                          -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of customer creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing supplier information
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    supplier_name VARCHAR(255) NOT NULL,        -- Name of the supplier
    contact_name VARCHAR(100),                   -- Contact person's name
    email VARCHAR(255) NOT NULL UNIQUE,         -- Supplier's email address
    phone VARCHAR(20),                          -- Supplier's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of supplier creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing order information
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each order
    customer_id INT NOT NULL,                    -- Foreign key referencing customers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the order
    total_amount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Order status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for storing order details (line items)
CREATE TABLE order_details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    order_id INT NOT NULL,                           -- Foreign key referencing orders
    product_id INT NOT NULL,                         -- Foreign key referencing products
    quantity INT NOT NULL,                           -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL,                  -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order detail creation
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
