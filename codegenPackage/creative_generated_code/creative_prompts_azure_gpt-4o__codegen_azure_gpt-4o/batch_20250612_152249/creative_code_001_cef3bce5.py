"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Create a database schema for managing inventory and production data for a textile company specializing in 100% acrylic yarns, including tables for yarn types, machinery details, and customer orders.
Generated: DETERMINISTIC_cef3bce514e7db0c
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing inventory and production data for a textile company

-- Table: yarn_types
-- Stores details about the different types of yarns produced
CREATE TABLE yarn_types (
    yarn_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each type of yarn
    yarn_name VARCHAR(100) NOT NULL,              -- Name/description of the yarn type
    color VARCHAR(50) NOT NULL,                   -- Color of the yarn
    weight DECIMAL(10,2) NOT NULL,                -- Weight of the yarn in grams
    price_per_kg DECIMAL(10,2) NOT NULL           -- Price per kilogram of yarn
);

-- Table: machinery
-- Stores information about the machinery used in production
CREATE TABLE machinery (
    machine_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each machine
    machine_name VARCHAR(100) NOT NULL,           -- Name or model of the machine
    machine_type VARCHAR(50) NOT NULL,            -- Type/category of machine
    operational_status ENUM('Operational', 'Maintenance', 'Out of Service') DEFAULT 'Operational', -- Current status of the machine
    purchase_date DATE                            -- Date when the machine was purchased
);

-- Table: customer_orders
-- Stores details about customer orders
CREATE TABLE customer_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each order
    customer_name VARCHAR(100) NOT NULL,          -- Name of the customer
    yarn_id INT NOT NULL,                         -- Foreign key linking to yarn_types table
    order_date DATE NOT NULL,                     -- Date when the order was placed
    quantity_kg DECIMAL(10,2) NOT NULL,           -- Quantity of yarn ordered in kilograms
    total_price DECIMAL(10,2) NOT NULL,           -- Total price for the order
    status ENUM('Pending', 'Processing', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Current status of the order
    FOREIGN KEY (yarn_id) REFERENCES yarn_types(yarn_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table: production_logs
-- Stores information about production activities
CREATE TABLE production_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each log entry
    machine_id INT NOT NULL,                      -- Foreign key linking to machinery table
    yarn_id INT NOT NULL,                         -- Foreign key linking to yarn_types table
    date DATE NOT NULL,                           -- Date of production activity
    quantity_produced_kg DECIMAL(10,2) NOT NULL,  -- Quantity of yarn produced (kg)
    FOREIGN KEY (machine_id) REFERENCES machinery(machine_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (yarn_id) REFERENCES yarn_types(yarn_id) ON DELETE CASCADE        -- Ensure referential integrity
);

-- Table: inventory
-- Tracks current inventory levels for yarn types
CREATE TABLE inventory (
    yarn_id INT PRIMARY KEY,                      -- Foreign key linking to yarn_types table
    stock_kg DECIMAL(10,2) NOT NULL,              -- Current stock level in kilograms
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (yarn_id) REFERENCES yarn_types(yarn_id) ON DELETE CASCADE        -- Ensure referential integrity
);

-- Indexing for faster lookup
CREATE INDEX idx_yarn_name ON yarn_types (yarn_name); -- Index for yarn_name in yarn_types table
CREATE INDEX idx_customer_name ON customer_orders (customer_name); -- Index for customer_name in customer_orders table
CREATE INDEX idx_machine_name ON machinery (machine_name); -- Index for machine_name in machinery table
```
