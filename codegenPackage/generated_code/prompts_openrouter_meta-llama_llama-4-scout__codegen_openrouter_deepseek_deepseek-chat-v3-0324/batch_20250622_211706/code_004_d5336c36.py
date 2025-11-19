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
-- SQL script to create a textile product inventory management system database schema
-- This schema includes tables for products, materials, applications, and their relationships

-- Create the database
CREATE DATABASE IF NOT EXISTS textile_inventory;
USE textile_inventory;

-- Table for storing material information
CREATE TABLE IF NOT EXISTS materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit_of_measure VARCHAR(20) NOT NULL COMMENT 'e.g., meters, yards, kilograms',
    current_stock DECIMAL(10, 2) NOT NULL DEFAULT 0,
    reorder_level DECIMAL(10, 2) NOT NULL DEFAULT 0,
    cost_per_unit DECIMAL(10, 2) NOT NULL,
    supplier_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_stock_non_negative CHECK (current_stock >= 0),
    CONSTRAINT chk_cost_non_negative CHECK (cost_per_unit >= 0)
) ENGINE=InnoDB;

-- Table for storing application types (e.g., clothing, upholstery, medical)
CREATE TABLE IF NOT EXISTS applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing product categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing products
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INT NOT NULL,
    application_id INT NOT NULL,
    current_price DECIMAL(10, 2) NOT NULL,
    current_stock INT NOT NULL DEFAULT 0,
    reorder_level INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (application_id) REFERENCES applications(application_id),
    CONSTRAINT chk_price_non_negative CHECK (current_price >= 0),
    CONSTRAINT chk_product_stock_non_negative CHECK (current_stock >= 0)
) ENGINE=InnoDB;

-- Junction table for product-material relationship (many-to-many)
CREATE TABLE IF NOT EXISTS product_materials (
    product_id INT NOT NULL,
    material_id INT NOT NULL,
    quantity_required DECIMAL(10, 2) NOT NULL COMMENT 'Amount of material needed per product',
    PRIMARY KEY (product_id, material_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    CONSTRAINT chk_quantity_positive CHECK (quantity_required > 0)
) ENGINE=InnoDB;

-- Table for inventory transactions (material usage and replenishment)
CREATE TABLE IF NOT EXISTS inventory_transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    material_id INT NOT NULL,
    transaction_type ENUM('IN', 'OUT') NOT NULL COMMENT 'IN for addition, OUT for consumption',
    quantity DECIMAL(10, 2) NOT NULL,
    reference_id INT COMMENT 'Reference to purchase order or product production',
    reference_type VARCHAR(50) COMMENT 'e.g., "purchase_order", "production"',
    notes TEXT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id),
    CONSTRAINT chk_transaction_quantity_positive CHECK (quantity > 0)
) ENGINE=InnoDB;

-- Table for product inventory adjustments
CREATE TABLE IF NOT EXISTS product_inventory_adjustments (
    adjustment_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    adjustment_type ENUM('IN', 'OUT') NOT NULL COMMENT 'IN for addition, OUT for deduction',
    quantity INT NOT NULL,
    reason VARCHAR(255) NOT NULL,
    notes TEXT,
    adjusted_by VARCHAR(100) NOT NULL,
    adjustment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    CONSTRAINT chk_adjustment_quantity_positive CHECK (quantity > 0)
) ENGINE=InnoDB;

-- Create indexes for better performance on frequently queried columns
CREATE INDEX idx_product_name ON products(name);
CREATE INDEX idx_product_category ON products(category_id);
CREATE INDEX idx_product_application ON products(application_id);
CREATE INDEX idx_material_name ON materials(name);
CREATE INDEX idx_transaction_material ON inventory_transactions(material_id);
CREATE INDEX idx_transaction_date ON inventory_transactions(transaction_date);
```
