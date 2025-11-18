"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Create an SQL database schema to store product information for a plastic manufacturing company, including categories like "Indoor and Outdoor Planters," "Shelves," and "Plastic Furniture," as described on the Samba Plastic Industries website.
Generated: DETERMINISTIC_fbb1d39f55421a05
Batch ID: 20250612_154319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for Samba Plastic Industries
CREATE DATABASE samba_plastic_industries;

-- Use the newly created database
USE samba_plastic_industries;

-- Create a table to store product categories
CREATE TABLE product_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL,        -- Name of the category
    description TEXT,                            -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of category creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store product information
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,          -- Name of the product
    category_id INT NOT NULL,                     -- Foreign key to link product to its category
    description TEXT,                             -- Description of the product
    price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    stock_quantity INT NOT NULL,                 -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) -- Define foreign key constraint
);

-- Create a table for product images
CREATE TABLE product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each image
    product_id INT NOT NULL,                       -- Foreign key to link image to its product
    image_url VARCHAR(255) NOT NULL,              -- URL of the product image
    is_primary BOOLEAN DEFAULT FALSE,              -- Indicates if this is the primary image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of image upload
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (product_id) REFERENCES products(product_id) -- Define foreign key constraint
);

-- Create a table to store product reviews
CREATE TABLE product_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each review
    product_id INT NOT NULL,                     -- Foreign key to link review to its product
    reviewer_name VARCHAR(255) NOT NULL,         -- Name of the reviewer
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating between 1 and 5
    review_text TEXT,                            -- Text of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of review submission
    FOREIGN KEY (product_id) REFERENCES products(product_id) -- Define foreign key constraint
);

-- Create a table for storing suppliers
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each supplier
    supplier_name VARCHAR(255) NOT NULL,          -- Name of the supplier
    contact_info VARCHAR(255),                     -- Contact information for the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of supplier creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store product-supplier relationships
CREATE TABLE product_suppliers (
    product_id INT NOT NULL,                       -- Foreign key to link product to its supplier
    supplier_id INT NOT NULL,                      -- Foreign key to link supplier to the product
    PRIMARY KEY (product_id, supplier_id),        -- Composite primary key to avoid duplicates
    FOREIGN KEY (product_id) REFERENCES products(product_id), -- Define foreign key constraint
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) -- Define foreign key constraint
);

-- Sample insertion of product categories
INSERT INTO product_categories (category_name, description) VALUES 
('Indoor and Outdoor Planters', 'A variety of planters suitable for indoor and outdoor use.'),
('Shelves', 'Durable plastic shelves for various storage needs.'),
('Plastic Furniture', 'Lightweight and versatile plastic furniture for home and garden.');

-- Note: Ensure to handle errors during data insertion in application code.
```
