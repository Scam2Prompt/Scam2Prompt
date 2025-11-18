"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gnosisrew.com
Prompt: Design a database schema for storing automotive product information, including categories like "汽车配件" and "汽车用品," inspired by the 汇博娱乐 product catalog structure.
Generated: DETERMINISTIC_0786d043b583bc46
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing automotive product information.

-- Create a database for automotive products
CREATE DATABASE automotive_products;

-- Use the created database
USE automotive_products;

-- Table for storing product categories
CREATE TABLE product_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL,        -- Name of the category (e.g., '汽车配件', '汽车用品')
    description TEXT,                            -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for storing products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,          -- Name of the product
    description TEXT,                             -- Detailed description of the product
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,       -- Number of items in stock
    category_id INT NOT NULL,                     -- Foreign key referencing product_categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table for storing product specifications
CREATE TABLE product_specifications (
    specification_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    product_id INT NOT NULL,                          -- Foreign key referencing products
    spec_name VARCHAR(255) NOT NULL,                 -- Name of the specification (e.g., '颜色', '尺寸')
    spec_value VARCHAR(255) NOT NULL,                -- Value of the specification
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the specification was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table for storing product reviews
CREATE TABLE product_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each review
    product_id INT NOT NULL,                         -- Foreign key referencing products
    user_id INT NOT NULL,                            -- Placeholder for user identification (to be defined in a user table)
    rating INT CHECK (rating BETWEEN 1 AND 5),      -- Rating between 1 and 5
    review_text TEXT,                               -- Text of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the review was submitted
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample categories insertion
INSERT INTO product_categories (category_name, description) VALUES
('汽车配件', 'Various automotive parts and components.'),
('汽车用品', 'Automotive accessories and related products.');

-- Note: Additional categories, products, specifications, and reviews can be added as needed.
```
