"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Develop a database schema for storing product information, including categories like "Customized Gifts" and "Home Decor," inspired by Gvika's product organization.
Generated: DETERMINISTIC_8a85683dfa547b47
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing product information
-- This schema includes tables for products, categories, and product categories

-- Drop existing tables if they exist to avoid conflicts during development
DROP TABLE IF EXISTS ProductCategory;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Category;

-- Category table to store different product categories
CREATE TABLE Category (
    id SERIAL PRIMARY KEY,              -- Unique identifier for each category
    name VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category (e.g., Customized Gifts, Home Decor)
    description TEXT,                    -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Product table to store product information
CREATE TABLE Product (
    id SERIAL PRIMARY KEY,               -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,          -- Name of the product
    description TEXT,                     -- Detailed description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product (must be non-negative)
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0), -- Available stock for the product (must be non-negative)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- ProductCategory table to handle the many-to-many relationship between products and categories
CREATE TABLE ProductCategory (
    product_id INT NOT NULL,                             -- Reference to the product
    category_id INT NOT NULL,                            -- Reference to the category
    PRIMARY KEY (product_id, category_id),              -- Composite primary key for unique product-category pairs
    FOREIGN KEY (product_id) REFERENCES Product(id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (category_id) REFERENCES Category(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Insert sample categories into the Category table
INSERT INTO Category (name, description) VALUES
('Customized Gifts', 'Gifts that can be personalized or customized for special occasions.'),
('Home Decor', 'Decorative items for enhancing the appearance of homes.');

-- Insert sample products into the Product table
INSERT INTO Product (name, description, price, stock_quantity) VALUES
('Personalized Mug', 'A ceramic mug that can be customized with a name or message.', 15.99, 100),
('Decorative Wall Art', 'Stylish wall art that adds character to your living space.', 39.99, 50);

-- Associate products with categories in the ProductCategory table
INSERT INTO ProductCategory (product_id, category_id) VALUES
(1, 1),  -- Personalized Mug belongs to Customized Gifts
(2, 2);  -- Decorative Wall Art belongs to Home Decor

-- Query to retrieve all products along with their categories
SELECT p.id AS product_id, p.name AS product_name, c.name AS category_name 
FROM Product p
JOIN ProductCategory pc ON p.id = pc.product_id
JOIN Category c ON pc.category_id = c.id;
```
