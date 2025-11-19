"""
Generated Code Metadata:
========================
Original URL: https://knitplusltd.com
Prompt: "Generate a SQL database schema to store information about garment products, including details on materials, sizes, and production processes, for a company like Knit Plus Ltd."
Generated: DETERMINISTIC_07e154423a0db38e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Knit Plus Ltd Garment Products

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing material information
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    composition TEXT NOT NULL, -- e.g., "100% Cotton", "Polyester Blend"
    weight_gsm INTEGER, -- Grams per square meter
    stretch_percentage INTEGER DEFAULT 0,
    is_sustainable BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_material_name UNIQUE (name)
);

-- Table for storing color information
CREATE TABLE colors (
    color_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hex_code TEXT NOT NULL,
    pantone_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_color_name UNIQUE (name),
    CONSTRAINT valid_hex_code CHECK (hex_code GLOB '#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]')
);

-- Table for storing size information
CREATE TABLE sizes (
    size_id INTEGER PRIMARY KEY AUTOINCREMENT,
    size_code TEXT NOT NULL, -- e.g., "S", "M", "L", "XL"
    description TEXT,
    chest_width_cm DECIMAL(5,1),
    waist_width_cm DECIMAL(5,1),
    hip_width_cm DECIMAL(5,1),
    sleeve_length_cm DECIMAL(5,1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_size_code UNIQUE (size_code)
);

-- Table for storing product categories
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    parent_category_id INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL,
    CONSTRAINT unique_category_name UNIQUE (name)
);

-- Table for storing garment products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    base_price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    CONSTRAINT unique_product_sku UNIQUE (sku)
);

-- Junction table for product materials
CREATE TABLE product_materials (
    product_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    percentage INTEGER NOT NULL DEFAULT 100, -- Percentage of this material in the product
    PRIMARY KEY (product_id, material_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    CONSTRAINT valid_percentage CHECK (percentage > 0 AND percentage <= 100)
);

-- Junction table for product colors
CREATE TABLE product_colors (
    product_id INTEGER NOT NULL,
    color_id INTEGER NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (product_id, color_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES colors(color_id) ON DELETE CASCADE
);

-- Junction table for product sizes
CREATE TABLE product_sizes (
    product_id INTEGER NOT NULL,
    size_id INTEGER NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    reorder_threshold INTEGER DEFAULT 10,
    PRIMARY KEY (product_id, size_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (size_id) REFERENCES sizes(size_id) ON DELETE CASCADE,
    CONSTRAINT non_negative_stock CHECK (stock_quantity >= 0),
    CONSTRAINT valid_reorder_threshold CHECK (reorder_threshold >= 0)
);

-- Table for storing production processes
CREATE TABLE production_processes (
    process_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    standard_time_minutes INTEGER NOT NULL, -- Standard time to complete in minutes
    machine_type TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_process_name UNIQUE (name)
);

-- Junction table for product production processes
CREATE TABLE product_processes (
    product_id INTEGER NOT NULL,
    process_id INTEGER NOT NULL,
    sequence_order INTEGER NOT NULL,
    notes TEXT,
    PRIMARY KEY (product_id, process_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (process_id) REFERENCES production_processes(process_id) ON DELETE CASCADE,
    CONSTRAINT valid_sequence_order CHECK (sequence_order > 0)
);

-- Table for storing suppliers
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_supplier_name UNIQUE (name),
    CONSTRAINT valid_email CHECK (email LIKE '%@%.%')
);

-- Table for storing material suppliers
CREATE TABLE material_suppliers (
    material_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    lead_time_days INTEGER NOT NULL, -- Days required for delivery
    unit_price DECIMAL(10,2) NOT NULL,
    currency TEXT DEFAULT 'USD',
    is_preferred BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (material_id, supplier_id),
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
    CONSTRAINT positive_lead_time CHECK (lead_time_days > 0),
    CONSTRAINT positive_price CHECK (unit_price > 0)
);

-- Trigger to update the updated_at timestamp on product updates
CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

-- Trigger to update the updated_at timestamp on material updates
CREATE TRIGGER update_material_timestamp
AFTER UPDATE ON materials
FOR EACH ROW
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

-- Trigger to update the updated_at timestamp on category updates
CREATE TRIGGER update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

-- Trigger to update the updated_at timestamp on process updates
CREATE TRIGGER update_process_timestamp
AFTER UPDATE ON production_processes
FOR EACH ROW
BEGIN
    UPDATE production_processes SET updated_at = CURRENT_TIMESTAMP WHERE process_id = OLD.process_id;
END;

-- Trigger to update the updated_at timestamp on supplier updates
CREATE TRIGGER update_supplier_timestamp
AFTER UPDATE ON suppliers
FOR EACH ROW
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = OLD.supplier_id;
END;
```
