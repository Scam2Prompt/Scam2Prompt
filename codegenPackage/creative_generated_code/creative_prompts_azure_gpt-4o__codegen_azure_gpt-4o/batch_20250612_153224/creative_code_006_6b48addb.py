"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iyitixobond.com
Prompt: Create an SQL query to store product details (e.g., "Mastic Sealer" and "Color Enhancer") from iyitixobond.com into a database with fields for category, price, and stock availability.
Generated: DETERMINISTIC_6b48addb3d411c87
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a table and insert product details into the database

-- Step 1: Create the 'products' table to store product details
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,           -- Product name
    category VARCHAR(255),                -- Product category
    price DECIMAL(10, 2) NOT NULL,        -- Product price in decimal format
    stock_availability BOOLEAN NOT NULL, -- Stock availability: TRUE (in stock), FALSE (out of stock)
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp for when the record is created
    updated_at TIMESTAMP DEFAULT NOW()    -- Timestamp for when the record is last updated
);

-- Step 2: Insert product details into the 'products' table
-- Example product: "Mastic Sealer"
INSERT INTO products (name, category, price, stock_availability)
VALUES 
    ('Mastic Sealer', 'Sealants', 19.99, TRUE), -- Product is in stock
    ('Color Enhancer', 'Enhancers', 29.99, FALSE); -- Product is out of stock

-- Step 3: Query to fetch all products from the table (optional for verification)
SELECT * FROM products;

-- Note: Ensure the database connection is properly configured and permissions are set for this script to run.
```
