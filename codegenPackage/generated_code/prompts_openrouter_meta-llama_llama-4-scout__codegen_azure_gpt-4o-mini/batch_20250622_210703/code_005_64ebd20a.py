"""
Generated Code Metadata:
========================
Original URL: https://granstore.co
Prompt: "Design a simple database schema to store product information similar to what is found on GranStore, including categories and subcategories."
Generated: DETERMINISTIC_64ebd20a41e0856b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information, categories, and subcategories

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Subcategory;
DROP TABLE IF EXISTS Category;

-- Create a table for categories
CREATE TABLE Category (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each category
    name VARCHAR(255) NOT NULL UNIQUE,    -- Name of the category, must be unique
    description TEXT,                      -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Create a table for subcategories
CREATE TABLE Subcategory (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each subcategory
    name VARCHAR(255) NOT NULL UNIQUE,    -- Name of the subcategory, must be unique
    description TEXT,                      -- Optional description of the subcategory
    category_id INT NOT NULL,              -- Foreign key referencing the Category table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the subcategory was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the subcategory was last updated
    FOREIGN KEY (category_id) REFERENCES Category(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for products
CREATE TABLE Product (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,           -- Name of the product
    description TEXT,                      -- Description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the product, must be non-negative
    stock INT NOT NULL CHECK (stock >= 0),  -- Stock quantity, must be non-negative
    subcategory_id INT NOT NULL,           -- Foreign key referencing the Subcategory table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the product was last updated
    FOREIGN KEY (subcategory_id) REFERENCES Subcategory(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes can be added for performance optimization if necessary
CREATE INDEX idx_product_name ON Product(name);
CREATE INDEX idx_subcategory_name ON Subcategory(name);
CREATE INDEX idx_category_name ON Category(name);
```
