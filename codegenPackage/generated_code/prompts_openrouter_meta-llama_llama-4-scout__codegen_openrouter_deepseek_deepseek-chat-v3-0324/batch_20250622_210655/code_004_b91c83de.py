"""
Generated Code Metadata:
========================
Original URL: https://cmcbukittinggi.co.id
Prompt: Design a simple database schema to store information about computer products like those sold on Central Multi Computer.
Generated: DETERMINISTIC_b91c83de93480996
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Central Multi Computer product inventory
-- Tables: products, categories, manufacturers, inventory

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create manufacturers table
CREATE TABLE IF NOT EXISTS manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    website TEXT,
    contact_email TEXT,
    contact_phone TEXT
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK(price >= 0),
    category_id INTEGER NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    release_date DATE,
    warranty_months INTEGER DEFAULT 12 CHECK(warranty_months >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

-- Create inventory table
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0),
    location TEXT,
    last_restocked DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create product specifications table
CREATE TABLE IF NOT EXISTS specifications (
    specification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    spec_name TEXT NOT NULL,
    spec_value TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create index for frequently queried columns
CREATE INDEX IF NOT EXISTS idx_product_category ON products(category_id);
CREATE INDEX IF NOT EXISTS idx_product_manufacturer ON products(manufacturer_id);
CREATE INDEX IF NOT EXISTS idx_product_price ON products(price);
CREATE INDEX IF NOT EXISTS idx_inventory_product ON inventory(product_id);

-- Trigger to update the updated_at timestamp when a product is modified
CREATE TRIGGER IF NOT EXISTS update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;
```
