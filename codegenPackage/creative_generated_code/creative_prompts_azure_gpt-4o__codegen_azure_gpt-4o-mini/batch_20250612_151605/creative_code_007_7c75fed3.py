"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Write a SQL query to store and retrieve product categories (e.g., "Kerti gépek" or "Fotelek") and their associated details from a database modeled after "Poly-Market.hu."
Generated: DETERMINISTIC_7c75fed39118b1ad
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a table for storing product categories and to retrieve them.

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    id SERIAL PRIMARY KEY,                        -- Unique identifier for each category
    name VARCHAR(255) NOT NULL UNIQUE,           -- Name of the category (e.g., "Kerti gépek")
    description TEXT,                             -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Insert sample data into the ProductCategories table
INSERT INTO ProductCategories (name, description) VALUES 
    ('Kerti gépek', 'Various tools and machinery for gardening.'),
    ('Fotelek', 'Chairs and armchairs for comfortable seating.');

-- Retrieve all product categories with their details
SELECT 
    id, 
    name, 
    description, 
    created_at, 
    updated_at 
FROM 
    ProductCategories;

-- Function to safely insert a new product category
CREATE OR REPLACE FUNCTION insert_product_category(p_name VARCHAR, p_description TEXT)
RETURNS VOID AS $$
BEGIN
    INSERT INTO ProductCategories (name, description) 
    VALUES (p_name, p_description);
EXCEPTION
    WHEN unique_violation THEN
        RAISE NOTICE 'Category "%" already exists.', p_name;
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error inserting category: %', SQLERRM;
END;
$$ LANGUAGE plpgsql;

-- Example of using the function to insert a new category
-- CALL insert_product_category('Új Kategória', 'Description for the new category.');

-- Function to retrieve categories with error handling
CREATE OR REPLACE FUNCTION get_product_categories()
RETURNS TABLE (id INT, name VARCHAR, description TEXT, created_at TIMESTAMP, updated_at TIMESTAMP) AS $$
BEGIN
    RETURN QUERY 
    SELECT 
        id, 
        name, 
        description, 
        created_at, 
        updated_at 
    FROM 
        ProductCategories;

EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Error retrieving categories: %', SQLERRM;

END;
$$ LANGUAGE plpgsql;

-- Example of using the function to get product categories
-- SELECT * FROM get_product_categories();
```
