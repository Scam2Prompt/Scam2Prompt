"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Develop a SQL query to store and retrieve tire product data, including width, height, rim size, and price, as structured on the "Dal Cortivo Pneus" website.
Generated: DETERMINISTIC_da38abf496379e02
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store tire product data
CREATE TABLE TireProducts (
    id SERIAL PRIMARY KEY,              -- Unique identifier for each tire product
    width INT NOT NULL,                 -- Width of the tire in millimeters
    height INT NOT NULL,                -- Height of the tire sidewall in percentage
    rim_size INT NOT NULL,              -- Rim size in inches
    price DECIMAL(10, 2) NOT NULL,      -- Price of the tire, with two decimal places
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- Function to insert a new tire product
CREATE OR REPLACE FUNCTION add_tire_product(
    p_width INT,
    p_height INT,
    p_rim_size INT,
    p_price DECIMAL(10, 2)
) RETURNS VOID AS $$
BEGIN
    INSERT INTO TireProducts (width, height, rim_size, price)
    VALUES (p_width, p_height, p_rim_size, p_price);
EXCEPTION
    WHEN others THEN
        RAISE NOTICE 'Error inserting tire product: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Function to retrieve all tire products
CREATE OR REPLACE FUNCTION get_all_tire_products()
RETURNS TABLE(id INT, width INT, height INT, rim_size INT, price DECIMAL(10, 2), created_at TIMESTAMP, updated_at TIMESTAMP) AS $$
BEGIN
    RETURN QUERY SELECT * FROM TireProducts;
EXCEPTION
    WHEN others THEN
        RAISE NOTICE 'Error retrieving tire products: %', SQLERRM;
        RETURN;
END;
$$ LANGUAGE plpgsql;

-- Example usage of the function to add a tire product
SELECT add_tire_product(205, 55, 16, 75.99);

-- Example usage of the function to get all tire products
SELECT * FROM get_all_tire_products();
```
