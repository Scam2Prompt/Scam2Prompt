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
-- Database schema for storing automotive product information

-- Create the 'categories' table to store product categories
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each category
    name VARCHAR(255) NOT NULL,              -- Name of the category, e.g., "汽车配件" or "汽车用品"
    description TEXT DEFAULT NULL,           -- Optional description for the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category is updated
);

-- Create the 'products' table to store automotive product details
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,              -- Name of the product
    category_id INT NOT NULL,                -- Foreign key linking to the 'categories' table
    price DECIMAL(10, 2) NOT NULL,           -- Price of the product
    stock_quantity INT NOT NULL,             -- Quantity of the product in stock
    description TEXT DEFAULT NULL,           -- Optional description for the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product is updated
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES categories(id) -- Foreign key constraint
);

-- Create the 'product_images' table to store images for products
CREATE TABLE product_images (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each image
    product_id INT NOT NULL,                 -- Foreign key linking to the 'products' table
    image_url VARCHAR(2083) NOT NULL,        -- URL of the product image
    alt_text VARCHAR(255) DEFAULT NULL,      -- Optional alt text for the image (e.g., for accessibility)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the image is added
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(id) -- Foreign key constraint
);

-- Create the 'reviews' table to store customer reviews for products
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each review
    product_id INT NOT NULL,                 -- Foreign key linking to the 'products' table
    customer_name VARCHAR(255) NOT NULL,     -- Name of the customer who left the review
    rating INT CHECK (rating BETWEEN 1 AND 5), -- Rating given by the customer (1-5 scale)
    comment TEXT DEFAULT NULL,               -- Optional comment provided by the customer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review is created
    CONSTRAINT fk_review_product FOREIGN KEY (product_id) REFERENCES products(id) -- Foreign key constraint
);

-- Create the 'suppliers' table to store supplier information
CREATE TABLE suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each supplier
    name VARCHAR(255) NOT NULL,              -- Name of the supplier
    contact_email VARCHAR(255) DEFAULT NULL, -- Contact email for the supplier
    phone_number VARCHAR(20) DEFAULT NULL,   -- Contact phone number for the supplier
    address TEXT DEFAULT NULL,               -- Address of the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier is added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the supplier is updated
);

-- Create the 'product_supplier' table to establish many-to-many relationship between products and suppliers
CREATE TABLE product_supplier (
    product_id INT NOT NULL,                 -- Foreign key linking to the 'products' table
    supplier_id INT NOT NULL,                -- Foreign key linking to the 'suppliers' table
    supply_price DECIMAL(10, 2) NOT NULL,    -- Price at which the supplier provides the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the relationship is established
    CONSTRAINT fk_ps_product FOREIGN KEY (product_id) REFERENCES products(id), -- Foreign key constraint
    CONSTRAINT fk_ps_supplier FOREIGN KEY (supplier_id) REFERENCES suppliers(id), -- Foreign key constraint
    PRIMARY KEY (product_id, supplier_id)   -- Composite primary key to ensure uniqueness
);
```
