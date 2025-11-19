"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Design a database schema to store information about various stone products, including Premium Pennsylvania Bluestone, Treads, Steps, and Boulders, and their respective suppliers.
Generated: DETERMINISTIC_3f518451611763e2
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for stone products inventory management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Suppliers table
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    phone TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    zip_code TEXT,
    country TEXT DEFAULT 'USA',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, email)
);

-- Product categories table
CREATE TABLE product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    unit_of_measure TEXT NOT NULL DEFAULT 'piece',
    thickness TEXT,
    color TEXT,
    finish TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE RESTRICT,
    UNIQUE(name, category_id)
);

-- Product variants table (for different sizes/quantities of the same product)
CREATE TABLE product_variants (
    variant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    size TEXT NOT NULL,
    weight_kg DECIMAL(10,2),
    price_per_unit DECIMAL(10,2) NOT NULL,
    stock_quantity INTEGER DEFAULT 0,
    min_order_quantity INTEGER DEFAULT 1,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Supplier products (many-to-many relationship)
CREATE TABLE supplier_products (
    supplier_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    lead_time_days INTEGER,
    preferred_supplier BOOLEAN DEFAULT FALSE,
    notes TEXT,
    PRIMARY KEY (supplier_id, product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Product images table
CREATE TABLE product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Initial data for product categories
INSERT INTO product_categories (name, description) VALUES
    ('Premium Pennsylvania Bluestone', 'High-quality natural bluestone from Pennsylvania'),
    ('Treads', 'Stone stair treads for outdoor steps'),
    ('Steps', 'Pre-cut stone steps for landscaping'),
    ('Boulders', 'Large natural stone boulders for landscaping');

-- Trigger to update the updated_at timestamp
CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

CREATE TRIGGER update_supplier_timestamp
AFTER UPDATE ON suppliers
FOR EACH ROW
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = OLD.supplier_id;
END;
```
