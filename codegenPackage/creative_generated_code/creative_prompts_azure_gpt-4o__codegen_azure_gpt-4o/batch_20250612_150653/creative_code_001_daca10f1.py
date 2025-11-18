"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: Create a database schema for managing a catalog of reinforced concrete products (ЖБИ) with categories such as "road and railway construction" and "energy construction," inspired by the organization of the catalog on paradigmagbi.ru.
Generated: DETERMINISTIC_daca10f1fe6e60e2
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing a Catalog of Reinforced Concrete Products (ЖБИ)

-- Table to store product categories
CREATE TABLE product_categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(255) NOT NULL,    -- Name of the category (e.g., "road and railway construction")
    description TEXT               -- Optional description of the category
);

-- Table to store reinforced concrete products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,    -- Name of the product
    category_id INT NOT NULL,      -- Foreign key to the product_categories table
    specifications JSONB,          -- Specifications of the product stored as JSON (e.g., dimensions, weight, etc.)
    price NUMERIC(10, 2),          -- Price of the product
    stock_quantity INT DEFAULT 0,  -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product is added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the product is last updated
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES product_categories (category_id) ON DELETE CASCADE
);

-- Table to store images associated with products
CREATE TABLE product_images (
    image_id SERIAL PRIMARY KEY,  -- Unique identifier for each image
    product_id INT NOT NULL,      -- Foreign key to the products table
    image_url TEXT NOT NULL,      -- URL of the product image
    is_main BOOLEAN DEFAULT FALSE, -- Flag indicating if the image is the main image
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products (product_id) ON DELETE CASCADE
);

-- Table to manage product tags for easier searching and categorization
CREATE TABLE product_tags (
    tag_id SERIAL PRIMARY KEY,    -- Unique identifier for each tag
    name VARCHAR(255) NOT NULL    -- Name of the tag (e.g., "heavy-duty", "prefabricated")
);

-- Table for relationship between products and tags (many-to-many)
CREATE TABLE product_tag_mapping (
    mapping_id SERIAL PRIMARY KEY, -- Unique mapping ID
    product_id INT NOT NULL,       -- Foreign key to the products table
    tag_id INT NOT NULL,           -- Foreign key to the product_tags table
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products (product_id) ON DELETE CASCADE,
    CONSTRAINT fk_tag FOREIGN KEY (tag_id) REFERENCES product_tags (tag_id) ON DELETE CASCADE
);

-- Sample constraints for data integrity
-- Ensure category names are unique
CREATE UNIQUE INDEX idx_unique_category_name ON product_categories (name);

-- Ensure product tags are unique
CREATE UNIQUE INDEX idx_unique_tag_name ON product_tags (name);
```
