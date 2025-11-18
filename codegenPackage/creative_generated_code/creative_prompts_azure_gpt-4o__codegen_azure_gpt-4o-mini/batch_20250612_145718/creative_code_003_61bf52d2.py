"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aakashapps.org
Prompt: Create a database schema for managing product categories such as electronics, fashion, and automotive accessories, as listed on the website.
Generated: DETERMINISTIC_61bf52d265fc0124
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing product categories

-- Check if the categories table exists and drop it if it does
DROP TABLE IF EXISTS categories;

-- Create the categories table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE,    -- Name of the category, must be unique
    description TEXT,                      -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Check if the products table exists and drop it if it does
DROP TABLE IF EXISTS products;

-- Create the products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,                 -- Unique identifier for each product
    name VARCHAR(100) NOT NULL,            -- Name of the product
    description TEXT,                       -- Description of the product
    price DECIMAL(10, 2) NOT NULL,         -- Price of the product
    category_id INT NOT NULL,               -- Foreign key referencing categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Example: Insert default categories
INSERT INTO categories (name, description) VALUES 
('Electronics', 'Devices and gadgets including phones, laptops, and more.'),
('Fashion', 'Clothing, accessories, and footwear.'),
('Automotive Accessories', 'Parts and accessories for vehicles.');

-- Example: Insert a product under the Electronics category
INSERT INTO products (name, description, price, category_id) VALUES 
('Smartphone', 'Latest model smartphone with advanced features.', 699.99, 1);
```
