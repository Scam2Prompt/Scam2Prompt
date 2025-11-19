"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rheinmetall-zulieferer.com
Prompt: Create a database schema for storing information about Rheinmetall suppliers, including fields for company name, location, and products supplied.
Generated: DETERMINISTIC_b1cc4872e09f2faf
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Rheinmetall Suppliers Database Schema
-- This schema is designed to store information about suppliers, including their company name, location, and products supplied.

-- Create the "suppliers" table
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,        -- Unique identifier for each supplier (auto-incremented)
    company_name VARCHAR(255) NOT NULL,   -- Name of the supplier company
    location VARCHAR(255) NOT NULL,       -- Location of the supplier (e.g., city, country)
    created_at TIMESTAMP DEFAULT NOW()    -- Timestamp for when the supplier entry was created
);

-- Create the "products" table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,        -- Unique identifier for each product (auto-incremented)
    supplier_id INT NOT NULL,             -- Foreign key linking the product to its supplier
    product_name VARCHAR(255) NOT NULL,  -- Name of the product supplied
    product_description TEXT DEFAULT NULL, -- Optional description of the product
    created_at TIMESTAMP DEFAULT NOW(),  -- Timestamp for when the product entry was created
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) 
        ON DELETE CASCADE                 -- Ensures products are deleted if the supplier is removed
);

-- Indexing for faster lookups
CREATE INDEX idx_supplier_location ON suppliers(location); -- Index on supplier location
CREATE INDEX idx_product_supplier ON products(supplier_id); -- Index on supplier_id in products

-- Example constraints
-- Ensure company names are unique to avoid duplicate suppliers
ALTER TABLE suppliers ADD CONSTRAINT unique_company_name UNIQUE (company_name);

-- Example check constraint to enforce non-empty product names
ALTER TABLE products ADD CONSTRAINT chk_product_name CHECK (product_name <> '');
```
