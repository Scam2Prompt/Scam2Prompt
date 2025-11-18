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
-- SQL script to create a table and insert product details into a database

-- Step 1: Create a table named 'products' to store product details
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,          -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,    -- Name of the product
    category VARCHAR(100) NOT NULL, -- Category of the product
    price DECIMAL(10, 2) NOT NULL,  -- Price of the product
    stock INT NOT NULL              -- Stock availability of the product
);

-- Step 2: Insert sample product details into the 'products' table
INSERT INTO products (name, category, price, stock) VALUES
('Mastic Sealer', 'Sealers', 29.99, 100),    -- Product details for Mastic Sealer
('Color Enhancer', 'Enhancers', 19.99, 150);  -- Product details for Color Enhancer

-- Step 3: Check for successful insertion
SELECT * FROM products;  -- Retrieve all records from the products table
```

**Note**: Ensure that this SQL code is executed in an environment where the database is properly set up, and that the proper permissions are granted for creating tables and inserting data.
