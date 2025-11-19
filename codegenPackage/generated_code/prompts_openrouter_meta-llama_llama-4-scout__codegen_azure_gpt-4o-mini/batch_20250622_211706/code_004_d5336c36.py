"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: "Design a database schema for a textile product inventory management system that includes tables for products, materials, and applications, using a relational database management system like MySQL."
Generated: DETERMINISTIC_d5336c36a7d7e39a
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Textile Product Inventory Management System

-- Create the database
CREATE DATABASE IF NOT EXISTS textile_inventory;
USE textile_inventory;

-- Table to store product information
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,         -- Name of the product
    description TEXT,                            -- Description of the product
    price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store material information
CREATE TABLE IF NOT EXISTS materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each material
    material_name VARCHAR(255) NOT NULL,         -- Name of the material
    material_type VARCHAR(100),                   -- Type of the material (e.g., cotton, polyester)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the material was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store application information
CREATE TABLE IF NOT EXISTS applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each application
    application_name VARCHAR(255) NOT NULL,         -- Name of the application (e.g., clothing, upholstery)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the application was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Junction table to associate products with materials
CREATE TABLE IF NOT EXISTS product_materials (
    product_id INT NOT NULL,                        -- Foreign key referencing products
    material_id INT NOT NULL,                       -- Foreign key referencing materials
    quantity DECIMAL(10, 2) NOT NULL,              -- Quantity of the material used in the product
    PRIMARY KEY (product_id, material_id),         -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Junction table to associate products with applications
CREATE TABLE IF NOT EXISTS product_applications (
    product_id INT NOT NULL,                        -- Foreign key referencing products
    application_id INT NOT NULL,                    -- Foreign key referencing applications
    PRIMARY KEY (product_id, application_id),      -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (application_id) REFERENCES applications(application_id) ON DELETE CASCADE  -- Foreign key constraint
);

-- Indexes can be added for performance optimization as needed
-- Example: CREATE INDEX idx_product_name ON products(product_name);
```
