"""
Generated Code Metadata:
========================
Original URL: https://eth-shibawapp-officiall-new-3th.blogspot.com
Prompt: Design a database schema to store products, categories, and tags for an e-commerce platform similar to the one described on this webpage.
Generated: DETERMINISTIC_9a333f5708b72b46
Batch ID: 20250622_211551
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS ProductTags;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Tags;

-- Table to store product categories
CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each category
    name VARCHAR(255) NOT NULL UNIQUE,    -- Name of the category, must be unique
    description TEXT,                      -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store tags
CREATE TABLE Tags (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each tag
    name VARCHAR(255) NOT NULL UNIQUE,    -- Name of the tag, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the tag was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store products
CREATE TABLE Products (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,           -- Name of the product
    description TEXT,                      -- Description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the product, must be non-negative
    category_id INT REFERENCES Categories(id) ON DELETE SET NULL,  -- Foreign key to Categories table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store the many-to-many relationship between products and tags
CREATE TABLE ProductTags (
    product_id INT REFERENCES Products(id) ON DELETE CASCADE,  -- Foreign key to Products table
    tag_id INT REFERENCES Tags(id) ON DELETE CASCADE,          -- Foreign key to Tags table
    PRIMARY KEY (product_id, tag_id)                           -- Composite primary key
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(name);
CREATE INDEX idx_category_name ON Categories(name);
CREATE INDEX idx_tag_name ON Tags(name);
```
