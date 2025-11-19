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
-- Database Schema for Textile Product Inventory Management System

-- Table: products
-- Stores information about textile products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,                -- Name of the product
    description TEXT,                          -- Description of the product
    price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    stock_quantity INT NOT NULL,               -- Quantity of the product in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the product was last updated
);

-- Table: materials
-- Stores information about materials used in textile products
CREATE TABLE materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each material
    name VARCHAR(255) NOT NULL,                 -- Name of the material
    description TEXT,                           -- Description of the material
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the material was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the material was last updated
);

-- Table: applications
-- Stores information about applications of textile products
CREATE TABLE applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    name VARCHAR(255) NOT NULL,                    -- Name of the application
    description TEXT,                              -- Description of the application
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the application was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the application was last updated
);

-- Table: product_materials
-- Many-to-Many relationship between products and materials
CREATE TABLE product_materials (
    product_id INT NOT NULL, -- Foreign key referencing products table
    material_id INT NOT NULL, -- Foreign key referencing materials table
    PRIMARY KEY (product_id, material_id), -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE -- Cascade delete
);

-- Table: product_applications
-- Many-to-Many relationship between products and applications
CREATE TABLE product_applications (
    product_id INT NOT NULL, -- Foreign key referencing products table
    application_id INT NOT NULL, -- Foreign key referencing applications table
    PRIMARY KEY (product_id, application_id), -- Composite primary key
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (application_id) REFERENCES applications(application_id) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON products(name); -- Index on product name for faster searches
CREATE INDEX idx_material_name ON materials(name); -- Index on material name for faster searches
CREATE INDEX idx_application_name ON applications(name); -- Index on application name for faster searches
```
