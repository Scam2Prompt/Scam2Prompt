"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Develop a database schema to manage fastener inventory, including categories like stainless steel screws, iron bolts, and other hardware items, as described on APN Hardware's website.
Generated: DETERMINISTIC_a6978122f3bf67a7
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating a database schema for managing fastener inventory

-- Drop existing schema if it exists (for fresh starts in development)
DROP SCHEMA IF EXISTS fastener_inventory CASCADE;

-- Create the schema for fastener inventory
CREATE SCHEMA fastener_inventory;

-- Set search path to the new schema
SET search_path TO fastener_inventory;

-- Table to store different categories of fasteners
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,  -- Name of the category
    description TEXT,  -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Table to store details about each fastener
CREATE TABLE fasteners (
    fastener_id SERIAL PRIMARY KEY,  -- Unique identifier for each fastener
    category_id INT NOT NULL,  -- Foreign key linking to the categories table
    fastener_name VARCHAR(100) NOT NULL,  -- Name of the fastener
    size VARCHAR(50),  -- Size specification of the fastener
    material VARCHAR(50),  -- Material type (e.g., stainless steel, iron)
    quantity INT NOT NULL CHECK (quantity >= 0),  -- Quantity in stock, must be non-negative
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),  -- Price per unit, must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for last update
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Table to manage inventory transactions (e.g., stock additions, removals)
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,  -- Unique identifier for each transaction
    fastener_id INT NOT NULL,  -- Foreign key linking to fasteners table
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('add', 'remove')),  -- Type of transaction
    quantity INT NOT NULL CHECK (quantity > 0),  -- Quantity involved in the transaction, must be positive
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the transaction
    FOREIGN KEY (fastener_id) REFERENCES fasteners(fastener_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Optional: Index for faster searching by category
CREATE INDEX idx_category_name ON categories(category_name);

-- Optional: Index for faster searching by fastener name
CREATE INDEX idx_fastener_name ON fasteners(fastener_name);
```
