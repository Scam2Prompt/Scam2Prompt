"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Design a database schema to store information about Medpointye's products, including Elisa Kits, and their respective product categories.
Generated: DETERMINISTIC_8891941d79fdb45d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Medpointye's products and product categories

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProductCategory;
DROP TABLE IF EXISTS Product;

-- Create a table to store product categories
CREATE TABLE ProductCategory (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL UNIQUE, -- Name of the category, must be unique
    description TEXT, -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store products
CREATE TABLE Product (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL, -- Name of the product
    category_id INT NOT NULL, -- Foreign key referencing the product category
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product, must be non-negative
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0), -- Quantity in stock, must be non-negative
    description TEXT, -- Optional description of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (category_id) REFERENCES ProductCategory(category_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Example of inserting data into ProductCategory
INSERT INTO ProductCategory (category_name, description) VALUES
('Elisa Kits', 'Diagnostic kits for various diseases'),
('Reagents', 'Chemical substances used in reactions'),
('Consumables', 'Single-use items for laboratory use');

-- Example of inserting data into Product
INSERT INTO Product (product_name, category_id, price, stock_quantity, description) VALUES
('Elisa Kit A', 1, 150.00, 100, 'Elisa Kit for testing disease A'),
('Elisa Kit B', 1, 200.00, 50, 'Elisa Kit for testing disease B'),
('Reagent X', 2, 75.00, 200, 'Reagent for use in Elisa tests'),
('Consumable Y', 3, 10.00, 500, 'Single-use consumable for lab tests');

-- Ensure that the schema is ready for production use with proper indexing
CREATE INDEX idx_product_name ON Product(product_name);
CREATE INDEX idx_category_name ON ProductCategory(category_name);
```
