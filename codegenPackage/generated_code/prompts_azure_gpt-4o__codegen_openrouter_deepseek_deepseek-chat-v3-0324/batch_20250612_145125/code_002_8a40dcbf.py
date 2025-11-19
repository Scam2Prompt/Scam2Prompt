"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Generate code to create a database schema for storing information about tools (e.g., pliers, hammers, drills) and their quantities in a shop inventory system.
Generated: DETERMINISTIC_8a40dcbfdac4544e
Batch ID: 20250612_145125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for a shop inventory system
-- This schema tracks tools and their quantities in inventory

-- Create the database
CREATE DATABASE IF NOT EXISTS shop_inventory;
USE shop_inventory;

-- Create tool categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_category_name UNIQUE (category_name)
) ENGINE=InnoDB;

-- Create tools table
CREATE TABLE IF NOT EXISTS tools (
    tool_id INT AUTO_INCREMENT PRIMARY KEY,
    tool_name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    manufacturer VARCHAR(100),
    model_number VARCHAR(50),
    unit_price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT,
    CONSTRAINT unique_tool_name_model UNIQUE (tool_name, model_number)
) ENGINE=InnoDB;

-- Create inventory table to track quantities
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    tool_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    minimum_stock_level INT NOT NULL DEFAULT 5,
    location VARCHAR(50),
    last_restocked DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (tool_id) REFERENCES tools(tool_id) ON DELETE CASCADE,
    CONSTRAINT positive_quantity CHECK (quantity >= 0),
    CONSTRAINT positive_min_stock CHECK (minimum_stock_level >= 0)
) ENGINE=InnoDB;

-- Create inventory transaction log
CREATE TABLE IF NOT EXISTS inventory_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    tool_id INT NOT NULL,
    quantity_change INT NOT NULL,
    transaction_type ENUM('purchase', 'sale', 'adjustment', 'return') NOT NULL,
    reference_number VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tool_id) REFERENCES tools(tool_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create index for faster lookups
CREATE INDEX idx_tool_name ON tools(tool_name);
CREATE INDEX idx_category ON tools(category_id);
CREATE INDEX idx_inventory_tool ON inventory(tool_id);
CREATE INDEX idx_transaction_tool ON inventory_transactions(tool_id);
```
