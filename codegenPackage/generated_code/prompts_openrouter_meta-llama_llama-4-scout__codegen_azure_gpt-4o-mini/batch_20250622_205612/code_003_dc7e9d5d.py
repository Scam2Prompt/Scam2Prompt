"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Design a database schema to store auto parts products with attributes such as product code, name, price, and application (e.g., vehicle make, model, year), inspired by the product listings on autopecasbrazz.
Generated: DETERMINISTIC_dc7e9d5d7fbe1001
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing auto parts products

CREATE TABLE AutoParts (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    product_code VARCHAR(50) NOT NULL UNIQUE, -- Unique code for the product
    name VARCHAR(255) NOT NULL, -- Name of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product, must be non-negative
    application JSONB NOT NULL, -- JSONB field to store vehicle application details (make, model, year)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- Index for faster searching by product code
CREATE INDEX idx_product_code ON AutoParts(product_code);

-- Example of how to insert a new product into the AutoParts table
-- INSERT INTO AutoParts (product_code, name, price, application)
-- VALUES ('AP12345', 'Brake Pad', 49.99, '{"make": "Toyota", "model": "Camry", "year": 2020}');
```

This SQL code defines a database schema for storing auto parts products, including necessary attributes and constraints. It also includes an index for efficient searching and an example of how to insert a new product.
