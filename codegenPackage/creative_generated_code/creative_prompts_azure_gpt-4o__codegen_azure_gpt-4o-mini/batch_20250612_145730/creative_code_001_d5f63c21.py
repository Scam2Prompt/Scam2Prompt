"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Generate a database schema for storing homeopathic product details, including categories, product names (e.g., "PK 84 MUNDIPUR"), prices, and availability status, based on the structure of PEKANA.PK.
Generated: DETERMINISTIC_d5f63c215352ba39
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing homeopathic product details

-- Drop the existing tables if they exist (for re-creation purposes)
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS products;

-- Table to store product categories
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,                  -- Unique identifier for each category
    name VARCHAR(100) NOT NULL,             -- Name of the category
    description TEXT,                        -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store product details
CREATE TABLE products (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,              -- Name of the product
    category_id INT NOT NULL,                -- Foreign key referencing the categories table
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the product, must be non-negative
    availability_status BOOLEAN NOT NULL DEFAULT TRUE,  -- Availability status of the product (true = available, false = unavailable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Sample data insertion (can be removed in production)
INSERT INTO categories (name, description) VALUES 
('Homeopathic Remedies', 'Products that help in healing using natural substances.'),
('Therapeutic Products', 'Products designed for specific therapeutic purposes.');

INSERT INTO products (name, category_id, price, availability_status) VALUES 
('PK 84 MUNDIPUR', 1, 20.50, TRUE),
('PK 10 MUNDIAL', 15.00, TRUE),
('PK 99 MUNDIFLEX', 30.00, FALSE);
```
