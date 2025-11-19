"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Design a database schema to store product information for an e-commerce store selling children's products, including tables for products, categories, and customer reviews.
Generated: DETERMINISTIC_9d397be497cde00a
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce store selling children's products

-- Table to store product categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL, -- Name of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0, -- Quantity of the product in stock
    category_id INT REFERENCES categories(category_id) ON DELETE SET NULL, -- Foreign key referencing categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- Table to store customer reviews for products
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY, -- Unique identifier for each review
    product_id INT REFERENCES products(product_id) ON DELETE CASCADE, -- Foreign key referencing products
    customer_name VARCHAR(255) NOT NULL, -- Name of the customer who wrote the review
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating given by the customer (1 to 5)
    review_text TEXT, -- Text of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the review was last updated
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON products(product_name);
CREATE INDEX idx_category_name ON categories(category_name);
CREATE INDEX idx_product_id ON reviews(product_id);
```
