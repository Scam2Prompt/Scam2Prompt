"""
Generated Code Metadata:
========================
Original URL: https://shahkarco.com
Prompt: "Design a simple database schema to store information about clothes rack products, including product names, descriptions, prices, and images, inspired by the product listings on shahkarco.com."
Generated: DETERMINISTIC_36fd8c60033de21a
Batch ID: 20250622_205654
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/images/wooden_rack.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/portable_rack.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/images/metal_rack.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing clothes rack products

-- Create a database named 'clothes_rack_store'
CREATE DATABASE clothes_rack_store;

-- Use the created database
USE clothes_rack_store;

-- Create a table named 'products' to store product information
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,         -- Name of the product
    description TEXT,                            -- Description of the product
    price DECIMAL(10, 2) NOT NULL,              -- Price of the product (up to 10 digits, 2 decimal places)
    image_url VARCHAR(255),                      -- URL of the product image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create an index on the product_name for faster search queries
CREATE INDEX idx_product_name ON products(product_name);

-- Sample data insertion (for demonstration purposes)
INSERT INTO products (product_name, description, price, image_url) VALUES
('Wooden Clothes Rack', 'A sturdy wooden clothes rack for organizing your clothes.', 49.99, 'https://example.com/images/wooden_rack.jpg'),
('Metal Clothes Rack', 'A durable metal clothes rack with adjustable height.', 39.99, 'https://example.com/images/metal_rack.jpg'),
('Portable Clothes Rack', 'A lightweight and portable clothes rack for travel.', 29.99, 'https://example.com/images/portable_rack.jpg');

-- Query to retrieve all products
SELECT * FROM products;

-- Note: Ensure to handle errors in your application code when executing these SQL statements.
-- For example, check for connection errors, handle SQL exceptions, and validate input data.
```
