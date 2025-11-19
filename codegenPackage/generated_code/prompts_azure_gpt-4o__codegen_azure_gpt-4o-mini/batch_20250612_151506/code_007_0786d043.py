"""
Generated Code Metadata:
========================
Original URL: https://gnosisrew.com
Prompt: Design a database schema for storing automotive product information, including categories like "汽车配件" and "汽车用品," inspired by the 汇博娱乐 product catalog structure.
Generated: DETERMINISTIC_0786d043b583bc46
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing automotive product information

-- Create a database for automotive products
CREATE DATABASE automotive_products;

-- Use the created database
USE automotive_products;

-- Table to store product categories
CREATE TABLE product_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,        -- Name of the category (e.g., 汽车配件, 汽车用品)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,           -- Name of the product
    description TEXT,                              -- Description of the product
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,        -- Quantity of the product in stock
    category_id INT,                               -- Foreign key referencing product_categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store product images
CREATE TABLE product_images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each image
    product_id INT,                               -- Foreign key referencing products
    image_url VARCHAR(255) NOT NULL,             -- URL of the product image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image was added
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store product reviews
CREATE TABLE product_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each review
    product_id INT,                               -- Foreign key referencing products
    reviewer_name VARCHAR(100) NOT NULL,         -- Name of the reviewer
    rating INT CHECK (rating BETWEEN 1 AND 5),   -- Rating given by the reviewer (1 to 5)
    comment TEXT,                                 -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store product specifications
CREATE TABLE product_specifications (
    specification_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    product_id INT,                                   -- Foreign key referencing products
    spec_name VARCHAR(100) NOT NULL,                 -- Name of the specification (e.g., color, size)
    spec_value VARCHAR(255) NOT NULL,                -- Value of the specification
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the specification was added
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_category_name ON product_categories(category_name);
CREATE INDEX idx_product_name ON products(product_name);
CREATE INDEX idx_product_id ON product_images(product_id);
CREATE INDEX idx_review_product_id ON product_reviews(product_id);
CREATE INDEX idx_spec_product_id ON product_specifications(product_id);
```
