"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write code to create a database schema for managing maritime supply operations, including categories like food supplies, electrical equipment, tools, hygiene services, and personal protective equipment, as detailed by Supply Marine.
Generated: DETERMINISTIC_e4f2ce6aef05150e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for managing maritime supply operations

-- Drop existing schema if it exists
DROP SCHEMA IF EXISTS maritime_supply CASCADE;

-- Create a new schema for maritime supply operations
CREATE SCHEMA maritime_supply;

-- Create a table for categories of supplies
CREATE TABLE maritime_supply.categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    description TEXT, -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for supplies
CREATE TABLE maritime_supply.supplies (
    supply_id SERIAL PRIMARY KEY, -- Unique identifier for each supply
    category_id INT NOT NULL REFERENCES maritime_supply.categories(category_id) ON DELETE CASCADE, -- Foreign key to categories
    supply_name VARCHAR(100) NOT NULL, -- Name of the supply
    quantity INT NOT NULL CHECK (quantity >= 0), -- Quantity of the supply
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price >= 0), -- Price per unit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for suppliers
CREATE TABLE maritime_supply.suppliers (
    supplier_id SERIAL PRIMARY KEY, -- Unique identifier for each supplier
    supplier_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the supplier
    contact_info VARCHAR(255), -- Contact information for the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for supply orders
CREATE TABLE maritime_supply.orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    supply_id INT NOT NULL REFERENCES maritime_supply.supplies(supply_id) ON DELETE CASCADE, -- Foreign key to supplies
    supplier_id INT NOT NULL REFERENCES maritime_supply.suppliers(supplier_id) ON DELETE CASCADE, -- Foreign key to suppliers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the order
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity ordered
    total_price DECIMAL(10, 2) NOT NULL CHECK (total_price >= 0), -- Total price of the order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for inventory transactions
CREATE TABLE maritime_supply.inventory_transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    supply_id INT NOT NULL REFERENCES maritime_supply.supplies(supply_id) ON DELETE CASCADE, -- Foreign key to supplies
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('IN', 'OUT')), -- Type of transaction (IN or OUT)
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create indexes for better performance
CREATE INDEX idx_category_name ON maritime_supply.categories(category_name);
CREATE INDEX idx_supply_name ON maritime_supply.supplies(supply_name);
CREATE INDEX idx_supplier_name ON maritime_supply.suppliers(supplier_name);
CREATE INDEX idx_order_date ON maritime_supply.orders(order_date);
CREATE INDEX idx_transaction_date ON maritime_supply.inventory_transactions(transaction_date);
```
