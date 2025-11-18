"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://travisscotmerch.com
Prompt: Generate SQL queries to manage inventory for Travis Scott merchandise, including updating stock levels for "Utopia Merch Hoodies" after a purchase.
Generated: DETERMINISTIC_5d0a95d8b64baa36
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to manage inventory for Travis Scott merchandise

-- Create table to hold inventory data
CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,                        -- Unique identifier for each item
    product_name VARCHAR(255) NOT NULL,          -- Name of the merchandise
    stock_level INT NOT NULL CHECK (stock_level >= 0), -- Current stock level, must be non-negative
    price DECIMAL(10, 2) NOT NULL                 -- Price of the merchandise
);

-- Insert sample data for "Utopia Merch Hoodies"
INSERT INTO inventory (product_name, stock_level, price) VALUES
    ('Utopia Merch Hoodie', 100, 59.99);         -- Initial stock setup

-- Function to update stock level after a purchase
CREATE OR REPLACE FUNCTION update_stock_level(
    p_product_name VARCHAR,
    p_quantity INT
) RETURNS VOID AS $$
BEGIN
    -- Update stock level based on product name and purchased quantity
    UPDATE inventory
    SET stock_level = stock_level - p_quantity
    WHERE product_name = p_product_name;

    -- Check if stock level falls below zero
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Product not found or insufficient stock for %', p_product_name;
    END IF;

    -- Ensure stock does not go below zero
    IF (SELECT stock_level FROM inventory WHERE product_name = p_product_name) < 0 THEN
        RAISE EXCEPTION 'Insufficient stock for %: cannot reduce stock below zero', p_product_name;
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Example usage of the function to update stock after a purchase
BEGIN;
    -- Attempt to purchase 2 Utopia Merch Hoodies
    PERFORM update_stock_level('Utopia Merch Hoodie', 2);
COMMIT;

-- Query to check updated inventory
SELECT * FROM inventory;
```
