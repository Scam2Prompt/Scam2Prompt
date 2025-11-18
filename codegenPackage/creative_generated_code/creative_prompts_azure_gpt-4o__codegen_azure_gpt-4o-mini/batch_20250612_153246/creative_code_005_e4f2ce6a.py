"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Write code to create a database schema for managing maritime supply operations, including categories like food supplies, electrical equipment, tools, hygiene services, and personal protective equipment, as detailed by Supply Marine.
Generated: DETERMINISTIC_e4f2ce6aef05150e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for managing maritime supply operations.

-- Drop existing schema if it exists
DROP SCHEMA IF EXISTS maritime_supply CASCADE;

-- Create a new schema for maritime supply operations
CREATE SCHEMA maritime_supply;

-- Table to store categories of supplies
CREATE TABLE maritime_supply.categories (
    category_id SERIAL PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category
    description TEXT  -- Description of the category
);

-- Table to store different types of supplies
CREATE TABLE maritime_supply.supplies (
    supply_id SERIAL PRIMARY KEY,  -- Unique identifier for each supply item
    supply_name VARCHAR(255) NOT NULL,  -- Name of the supply item
    category_id INT NOT NULL,  -- Foreign key referencing categories
    quantity INT NOT NULL CHECK (quantity >= 0),  -- Quantity available
    unit VARCHAR(50),  -- Unit of measurement (e.g., kg, units)
    price DECIMAL(10, 2),  -- Price per unit of supply item
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the supply was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of the last update to the supply
    FOREIGN KEY (category_id) REFERENCES maritime_supply.categories(category_id) 
        ON DELETE CASCADE  -- Delete supplies if category is deleted
);

-- Table to store orders for supplies
CREATE TABLE maritime_supply.orders (
    order_id SERIAL PRIMARY KEY,  -- Unique identifier for each order
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when the order was placed
    supply_id INT NOT NULL,  -- Foreign key referencing supplies
    quantity_ordered INT NOT NULL CHECK (quantity_ordered > 0),  -- Quantity ordered
    status VARCHAR(50) DEFAULT 'Pending',  -- Status of the order (Pending, Completed, Canceled)
    FOREIGN KEY (supply_id) REFERENCES maritime_supply.supplies(supply_id) 
        ON DELETE CASCADE  -- Delete orders if supply is deleted
);

-- Table to store supplier information
CREATE TABLE maritime_supply.suppliers (
    supplier_id SERIAL PRIMARY KEY,  -- Unique identifier for each supplier
    supplier_name VARCHAR(255) NOT NULL,  -- Name of the supplier
    contact_info TEXT,  -- Contact information for the supplier
    rating INT CHECK (rating >= 1 AND rating <= 5)  -- Rating of the supplier from 1 to 5
);

-- Table to connect supplies with their respective suppliers
CREATE TABLE maritime_supply.supplier_supplies (
    supplier_supply_id SERIAL PRIMARY KEY,  -- Unique identifier for the supplier-supply link
    supplier_id INT NOT NULL,  -- Foreign key referencing suppliers
    supply_id INT NOT NULL,  -- Foreign key referencing supplies
    lead_time INT,  -- Lead time for the supplier to deliver the supply
    FOREIGN KEY (supplier_id) REFERENCES maritime_supply.suppliers(supplier_id) 
        ON DELETE CASCADE,  -- Delete links if supplier is deleted
    FOREIGN KEY (supply_id) REFERENCES maritime_supply.supplies(supply_id) 
        ON DELETE CASCADE  -- Delete links if supply is deleted
);

-- Table to store transactions for tracking supply movements
CREATE TABLE maritime_supply.transactions (
    transaction_id SERIAL PRIMARY KEY,  -- Unique identifier for each transaction
    supply_id INT NOT NULL,  -- Foreign key referencing supplies
    transaction_type VARCHAR(50) NOT NULL CHECK (transaction_type IN ('IN', 'OUT')),  -- Type of transaction (IN for supply received, OUT for supply used)
    quantity INT NOT NULL CHECK (quantity > 0),  -- Quantity involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of the transaction
    FOREIGN KEY (supply_id) REFERENCES maritime_supply.supplies(supply_id) 
        ON DELETE CASCADE  -- Delete transactions if supply is deleted
);

-- Indexes for better performance on frequently queried fields
CREATE INDEX idx_supplies_category ON maritime_supply.supplies(category_id);
CREATE INDEX idx_orders_supply ON maritime_supply.orders(supply_id);
CREATE INDEX idx_transactions_supply ON maritime_supply.transactions(supply_id);
```
