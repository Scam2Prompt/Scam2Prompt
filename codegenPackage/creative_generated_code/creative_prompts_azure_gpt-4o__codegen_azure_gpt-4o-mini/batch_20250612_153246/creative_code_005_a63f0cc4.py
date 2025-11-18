"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.pensar.inf.br
Prompt: Create a database schema for an ERP system inspired by SOLPEN, ensuring it supports modular customization for industries like manufacturing, commerce, and distribution.
Generated: DETERMINISTIC_a63f0cc4cc91f6d5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an ERP system inspired by SOLPEN
-- This schema supports modular customization for different industries

-- Create a schema for the ERP system
CREATE SCHEMA erp_system;

-- Create a table for Users
CREATE TABLE erp_system.users (
    user_id SERIAL PRIMARY KEY,           -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,   -- Unique email address
    role VARCHAR(20) NOT NULL,             -- Role of the user (admin, manager, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for Companies
CREATE TABLE erp_system.companies (
    company_id SERIAL PRIMARY KEY,        -- Unique identifier for each company
    name VARCHAR(100) NOT NULL,           -- Company name
    industry VARCHAR(50) NOT NULL,        -- Industry type (manufacturing, commerce, distribution)
    address TEXT,                        -- Company address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of company creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for Products
CREATE TABLE erp_system.products (
    product_id SERIAL PRIMARY KEY,       -- Unique identifier for each product
    company_id INT NOT NULL REFERENCES erp_system.companies(company_id) ON DELETE CASCADE, -- Foreign key to companies
    name VARCHAR(100) NOT NULL,           -- Product name
    description TEXT,                     -- Description of the product
    price DECIMAL(10, 2) NOT NULL,        -- Price of the product
    stock_quantity INT DEFAULT 0,         -- Available stock quantity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for Orders
CREATE TABLE erp_system.orders (
    order_id SERIAL PRIMARY KEY,          -- Unique identifier for each order
    company_id INT NOT NULL REFERENCES erp_system.companies(company_id) ON DELETE CASCADE, -- Foreign key to companies
    user_id INT NOT NULL REFERENCES erp_system.users(user_id) ON DELETE SET NULL, -- Foreign key to users
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the order was placed
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount of the order
    status VARCHAR(20) DEFAULT 'Pending',  -- Status of the order (Pending, Completed, Cancelled)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for Order Items
CREATE TABLE erp_system.order_items (
    order_item_id SERIAL PRIMARY KEY,     -- Unique identifier for each order item
    order_id INT NOT NULL REFERENCES erp_system.orders(order_id) ON DELETE CASCADE, -- Foreign key to orders
    product_id INT NOT NULL REFERENCES erp_system.products(product_id) ON DELETE CASCADE, -- Foreign key to products
    quantity INT NOT NULL DEFAULT 1,       -- Quantity of the product in the order
    price DECIMAL(10, 2) NOT NULL,         -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order item creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for Inventory Transactions
CREATE TABLE erp_system.inventory_transactions (
    transaction_id SERIAL PRIMARY KEY,    -- Unique identifier for each inventory transaction
    product_id INT NOT NULL REFERENCES erp_system.products(product_id) ON DELETE CASCADE, -- Foreign key to products
    quantity INT NOT NULL,                 -- Quantity changed (positive for addition, negative for removal)
    transaction_type VARCHAR(20) NOT NULL, -- Type of transaction (Addition, Removal)
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of transaction creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Create a table for Custom Modules
CREATE TABLE erp_system.custom_modules (
    module_id SERIAL PRIMARY KEY,          -- Unique identifier for each module
    company_id INT REFERENCES erp_system.companies(company_id) ON DELETE CASCADE, -- Foreign key to companies
    name VARCHAR(100) NOT NULL,            -- Name of the custom module
    settings JSONB,                        -- JSONB field for customizable settings
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of module creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Indexes for optimization
CREATE INDEX idx_users_email ON erp_system.users(email);
CREATE INDEX idx_orders_order_date ON erp_system.orders(order_date);
CREATE INDEX idx_products_name ON erp_system.products(name);
```
