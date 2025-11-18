"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Create a database schema in SQL for storing product details, including categories like "zabawki dla niemowląt," "chodziki," and "maty piankowe," as seen on the Milly Mally website.
Generated: DETERMINISTIC_838ce91385a434bf
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for storing product details

-- Drop the existing schema if it exists (optional, for development purposes)
DROP SCHEMA IF EXISTS product_catalog CASCADE;

-- Create a new schema for the product catalog
CREATE SCHEMA product_catalog;

-- Set the search path to the new schema
SET search_path TO product_catalog;

-- Create a table for product categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table for products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,  -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,  -- Name of the product
    description TEXT,  -- Description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the product
    category_id INT NOT NULL REFERENCES categories(category_id) ON DELETE CASCADE,  -- Foreign key to categories
    stock_quantity INT DEFAULT 0 CHECK (stock_quantity >= 0),  -- Quantity in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Insert initial categories into the categories table
INSERT INTO categories (category_name) VALUES
('zabawki dla niemowląt'),
('chodziki'),
('maty piankowe');

-- Create an index on the product name for faster searches
CREATE INDEX idx_product_name ON products (product_name);

-- Create an index on the category_id for faster joins
CREATE INDEX idx_category_id ON products (category_id);

-- Create a view to easily see products with their categories
CREATE VIEW product_overview AS
SELECT 
    p.product_id,
    p.product_name,
    p.description,
    p.price,
    c.category_name,
    p.stock_quantity
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id;

-- Error handling: Ensure the database operations are wrapped in transactions if needed
-- Example: BEGIN; ... COMMIT; OR ROLLBACK; can be used in application code
```
