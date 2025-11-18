"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Create a database schema to store information about UPVC window and door types, such as tilt windows, villa windows, and sliding doors, based on Dexodoor's product catalog.
Generated: DETERMINISTIC_4acf4026d6397bcf
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing information about UPVC window and door types.

-- Drop existing schema if it exists
DROP SCHEMA IF EXISTS upvc_products CASCADE;

-- Create new schema for UPVC products
CREATE SCHEMA upvc_products;

-- Set the search path to the new schema
SET search_path TO upvc_products;

-- Table to store product categories (e.g., window, door)
CREATE TABLE product_categories (
    id SERIAL PRIMARY KEY,           -- Unique identifier for each category
    name VARCHAR(50) NOT NULL UNIQUE, -- Name of the product category
    description TEXT                 -- Description of the category
);

-- Table to store UPVC products
CREATE TABLE products (
    id SERIAL PRIMARY KEY,           -- Unique identifier for each product
    name VARCHAR(100) NOT NULL,      -- Name of the product
    category_id INT NOT NULL,        -- Foreign key referencing product_categories
    type VARCHAR(50) NOT NULL,       -- Type of the product (e.g., tilt, villa, sliding)
    dimensions VARCHAR(50),          -- Dimensions of the product (e.g., width x height)
    color VARCHAR(30),               -- Color of the product
    price DECIMAL(10, 2) NOT NULL,   -- Price of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (category_id) REFERENCES product_categories(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store product specifications
CREATE TABLE product_specifications (
    id SERIAL PRIMARY KEY,           -- Unique identifier for each specification
    product_id INT NOT NULL,         -- Foreign key referencing products
    specification_name VARCHAR(100) NOT NULL, -- Name of the specification
    specification_value VARCHAR(100) NOT NULL, -- Value of the specification
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Insert initial product categories
INSERT INTO product_categories (name, description) VALUES
('Windows', 'Various types of UPVC windows'),
('Doors', 'Various types of UPVC doors');

-- Example insert for products (to be customized based on actual product catalog)
INSERT INTO products (name, category_id, type, dimensions, color, price) VALUES
('Tilt Window', 1, 'Tilt', '120 x 150', 'White', 150.00),
('Villa Window', 1, 'Villa', '200 x 150', 'Gray', 180.00),
('Sliding Door', 2, 'Sliding', '240 x 210', 'White', 350.00);

-- Example insert for product specifications
INSERT INTO product_specifications (product_id, specification_name, specification_value) VALUES
(1, 'Material', 'UPVC'),
(1, 'Warranty', '10 years'),
(2, 'Material', 'UPVC'),
(2, 'Warranty', '10 years'),
(3, 'Material', 'UPVC'),
(3, 'Warranty', '10 years');
```
