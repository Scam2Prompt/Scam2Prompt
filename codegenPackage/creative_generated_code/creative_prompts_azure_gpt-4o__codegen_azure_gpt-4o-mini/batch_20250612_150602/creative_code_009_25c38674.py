"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Create a database schema for storing product information, including categories like "Probepackungen," "Eisen," and "Haare, Haut & Nägel," as outlined on the PlusMedica Shop website.
Generated: DETERMINISTIC_25c386746fd1653e
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing product information at PlusMedica Shop

-- Create a table for product categories
CREATE TABLE ProductCategories (
    category_id SERIAL PRIMARY KEY,               -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category (e.g., "Probepackungen")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for products
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,                -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,          -- Name of the product
    product_description TEXT,                     -- Detailed description of the product
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,       -- Available stock quantity
    category_id INT REFERENCES ProductCategories(category_id) ON DELETE SET NULL, -- Foreign key to categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CHECK (price >= 0),                          -- Ensure price is not negative
    CHECK (stock_quantity >= 0)                   -- Ensure stock quantity is not negative
);

-- Insert default categories into the ProductCategories table
INSERT INTO ProductCategories (category_name) VALUES
('Probepackungen'),
('Eisen'),
('Haare, Haut & Nägel');

-- To ensure that the schema is ready for production, consider adding indexes and
-- additional constraints for performance and data integrity, if necessary.
-- Example: CREATE INDEX idx_product_name ON Products(product_name);
```
