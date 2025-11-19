"""
Generated Code Metadata:
========================
Original URL: https://www.cymrepuestos.com.ar
Prompt: "Create a database schema for storing information about automotive spare parts, including product categories, brands, and supplier details, inspired by CYM Repuestos' product offerings."
Generated: DETERMINISTIC_2ed20f62577f434c
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for Automotive Spare Parts

```sql
-- Database schema for automotive spare parts management system
-- Inspired by CYM Repuestos product offerings

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT NOT NULL,
    email TEXT,
    address TEXT,
    city TEXT,
    country TEXT,
    tax_id TEXT,
    payment_terms TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_supplier UNIQUE (name, tax_id)
);

CREATE TABLE IF NOT EXISTS brands (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    country_of_origin TEXT,
    website TEXT,
    logo_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    parent_category_id INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS parts (
    part_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    brand_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    cost_price DECIMAL(10, 2) NOT NULL,
    quantity_in_stock INTEGER DEFAULT 0,
    min_stock_level INTEGER DEFAULT 5,
    weight DECIMAL(10, 2),
    dimensions TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE RESTRICT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS part_suppliers (
    part_supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    supplier_part_number TEXT,
    lead_time_days INTEGER,
    last_purchase_price DECIMAL(10, 2),
    is_preferred_supplier BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (part_id) REFERENCES parts(part_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
    CONSTRAINT unique_part_supplier UNIQUE (part_id, supplier_id)
);

CREATE TABLE IF NOT EXISTS part_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT 0,
    caption TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (part_id) REFERENCES parts(part_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS part_compatibility (
    compatibility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_id INTEGER NOT NULL,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year_from INTEGER,
    year_to INTEGER,
    engine_type TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (part_id) REFERENCES parts(part_id) ON DELETE CASCADE,
    CONSTRAINT unique_compatibility UNIQUE (part_id, make, model, year_from, year_to, engine_type)
);

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_parts_brand ON parts(brand_id);
CREATE INDEX IF NOT EXISTS idx_parts_category ON parts(category_id);
CREATE INDEX IF NOT EXISTS idx_parts_sku ON parts(sku);
CREATE INDEX IF NOT EXISTS idx_part_suppliers_part ON part_suppliers(part_id);
CREATE INDEX IF NOT EXISTS idx_part_suppliers_supplier ON part_suppliers(supplier_id);
CREATE INDEX IF NOT EXISTS idx_part_images_part ON part_images(part_id);
CREATE INDEX IF NOT EXISTS idx_part_compatibility_part ON part_compatibility(part_id);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_supplier_timestamp
AFTER UPDATE ON suppliers
FOR EACH ROW
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = OLD.supplier_id;
END;

CREATE TRIGGER IF NOT EXISTS update_part_timestamp
AFTER UPDATE ON parts
FOR EACH ROW
BEGIN
    UPDATE parts SET updated_at = CURRENT_TIMESTAMP WHERE part_id = OLD.part_id;
END;

CREATE TRIGGER IF NOT EXISTS update_part_supplier_timestamp
AFTER UPDATE ON part_suppliers
FOR EACH ROW
BEGIN
    UPDATE part_suppliers SET updated_at = CURRENT_TIMESTAMP WHERE part_supplier_id = OLD.part_supplier_id;
END;
```
