"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: Create a database schema for storing product details, including size, material, and application specifications for thermal paper rolls, modeled after the product offerings on the Apos Chile website.
Generated: DETERMINISTIC_0a7c133861df2190
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing product details of thermal paper rolls

-- Create a schema named 'product_catalog' (optional, can be modified based on your database setup)
CREATE SCHEMA IF NOT EXISTS product_catalog;

-- Use the schema for subsequent operations
SET search_path TO product_catalog;

-- Table for storing products
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(255) NOT NULL, -- Name of the product
    description TEXT, -- Detailed description of the product
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product (cannot be negative)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for storing size specifications of the products
CREATE TABLE IF NOT EXISTS product_sizes (
    size_id SERIAL PRIMARY KEY, -- Unique identifier for each size specification
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE, -- Foreign key to products table
    width_mm NUMERIC(10, 2) NOT NULL CHECK (width_mm > 0), -- Width in millimeters
    diameter_mm NUMERIC(10, 2) NOT NULL CHECK (diameter_mm > 0), -- Diameter in millimeters
    length_m NUMERIC(10, 2) NOT NULL CHECK (length_m > 0), -- Length in meters
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the size specification was added
);

-- Table for storing material specifications of the products
CREATE TABLE IF NOT EXISTS product_materials (
    material_id SERIAL PRIMARY KEY, -- Unique identifier for each material specification
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE, -- Foreign key to products table
    material_type VARCHAR(255) NOT NULL, -- Type of material (e.g., thermal paper, synthetic paper, etc.)
    material_description TEXT, -- Additional description of the material
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the material specification was added
);

-- Table for storing application specifications of the products
CREATE TABLE IF NOT EXISTS product_applications (
    application_id SERIAL PRIMARY KEY, -- Unique identifier for each application specification
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE, -- Foreign key to products table
    application_type VARCHAR(255) NOT NULL, -- Type of application (e.g., POS receipts, labels, etc.)
    application_description TEXT, -- Additional description of the application
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the application specification was added
);

-- Indexes for improving query performance
CREATE INDEX idx_product_name ON products (name);
CREATE INDEX idx_material_type ON product_materials (material_type);
CREATE INDEX idx_application_type ON product_applications (application_type);

-- Example of error handling: Use transactions in a production application when inserting data
-- Example:
-- BEGIN;
-- INSERT INTO products (name, description, price) VALUES ('Thermal Paper Roll', 'High-quality thermal paper', 12.50);
-- INSERT INTO product_sizes (product_id, width_mm, diameter_mm, length_m) VALUES (LASTVAL(), 80.00, 50.00, 100.00);
-- COMMIT;
```
