"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: "Design a simple database schema to store information about packaging products, including product types (e.g., arándanos, uva mesa), and their export destinations."
Generated: DETERMINISTIC_a107a49b6d6bf9f9
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a packaging products database schema

-- Create database
CREATE DATABASE IF NOT EXISTS packaging_products;
USE packaging_products;

-- Create product_types table
CREATE TABLE IF NOT EXISTS product_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_product_type_name UNIQUE (name)
) ENGINE=InnoDB;

-- Create countries table
CREATE TABLE IF NOT EXISTS countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(2) NOT NULL COMMENT 'ISO 2-letter country code',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_country_name UNIQUE (name),
    CONSTRAINT unique_country_code UNIQUE (code)
) ENGINE=InnoDB;

-- Create packaging_products table
CREATE TABLE IF NOT EXISTS packaging_products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_type_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    weight DECIMAL(10,2) COMMENT 'Weight in kilograms',
    dimensions VARCHAR(50) COMMENT 'Format: LxWxH in cm',
    barcode VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_type_id) REFERENCES product_types(id) ON DELETE RESTRICT,
    CONSTRAINT unique_product_name UNIQUE (name)
) ENGINE=InnoDB;

-- Create export_destinations table (junction table for many-to-many relationship)
CREATE TABLE IF NOT EXISTS export_destinations (
    product_id INT NOT NULL,
    country_id INT NOT NULL,
    export_price DECIMAL(10,2) COMMENT 'Price in USD',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id, country_id),
    FOREIGN KEY (product_id) REFERENCES packaging_products(id) ON DELETE CASCADE,
    FOREIGN KEY (country_id) REFERENCES countries(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for better performance
CREATE INDEX idx_packaging_products_product_type ON packaging_products(product_type_id);
CREATE INDEX idx_export_destinations_country ON export_destinations(country_id);
```
