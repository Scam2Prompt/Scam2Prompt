"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Create a database schema for managing timber products, including categories like softwood, hardwood, and sawn timber, as described by Askar Trading International.
Generated: DETERMINISTIC_63c27bfee277f6b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing timber products for Askar Trading International

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create table for timber categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create table for timber products
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    scientific_name TEXT,
    origin TEXT,
    density TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create table for product specifications
CREATE TABLE IF NOT EXISTS specifications (
    specification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    thickness TEXT,
    width TEXT,
    length TEXT,
    grade TEXT,
    moisture_content TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for inventory
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    unit TEXT NOT NULL DEFAULT 'cubic_meter',
    location TEXT,
    batch_number TEXT,
    arrival_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for pricing
CREATE TABLE IF NOT EXISTS pricing (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    currency TEXT NOT NULL DEFAULT 'USD',
    valid_from DATE NOT NULL,
    valid_to DATE,
    notes TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id);
CREATE INDEX IF NOT EXISTS idx_specifications_product ON specifications(product_id);
CREATE INDEX IF NOT EXISTS idx_inventory_product ON inventory(product_id);
CREATE INDEX IF NOT EXISTS idx_pricing_product ON pricing(product_id);

-- Insert default categories
INSERT OR IGNORE INTO categories (name, description) VALUES 
    ('Softwood', 'Timber from coniferous trees, typically lighter and less dense'),
    ('Hardwood', 'Timber from deciduous trees, typically denser and more durable'),
    ('Sawn Timber', 'Processed timber cut into standardized dimensions');
```
