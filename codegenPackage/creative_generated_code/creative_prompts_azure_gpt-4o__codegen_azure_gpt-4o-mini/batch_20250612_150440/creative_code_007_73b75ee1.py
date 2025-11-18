"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livesupport.tfryx.xyz
Prompt: Create a SQL query to store and retrieve product data, including discounts and stock availability, for items like "PINI-KAY brikettiklapi – 960 kg eurolava" from https://livesupport.tfryx.xyz.
Generated: DETERMINISTIC_73b75ee1d444468d
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store product data
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,          -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,    -- Name of the product
    weight_kg DECIMAL(10, 2) NOT NULL,      -- Weight of the product in kilograms
    price DECIMAL(10, 2) NOT NULL,           -- Price of the product
    discount DECIMAL(5, 2) DEFAULT 0.00,     -- Discount on the product, if any
    stock_available INT NOT NULL,            -- Number of items in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Insert a sample product into the table
INSERT INTO products (product_name, weight_kg, price, discount, stock_available) 
VALUES 
('PINI-KAY brikettiklapi – 960 kg eurolava', 960.00, 250.00, 10.00, 50);

-- Function to retrieve product data including discounts and stock availability
CREATE OR REPLACE FUNCTION get_product_data(product_name_input VARCHAR)
RETURNS TABLE (
    product_id INT,
    product_name VARCHAR,
    weight_kg DECIMAL,
    price DECIMAL,
    discount DECIMAL,
    stock_available INT
) AS $$
BEGIN
    RETURN QUERY 
    SELECT product_id, product_name, weight_kg, price, discount, stock_available
    FROM products
    WHERE product_name ILIKE '%' || product_name_input || '%'; -- Case-insensitive search
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE NOTICE 'No products found with the name: %', product_name_input;
        RETURN;
    WHEN OTHERS THEN
        RAISE EXCEPTION 'An error occurred while retrieving product data: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Example usage of the function
SELECT * FROM get_product_data('PINI-KAY');
```
