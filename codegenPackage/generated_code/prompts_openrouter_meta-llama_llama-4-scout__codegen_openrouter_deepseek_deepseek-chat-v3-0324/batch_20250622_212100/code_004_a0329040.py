"""
Generated Code Metadata:
========================
Original URL: https://air-tonway.top
Prompt: Design a database schema to store information about track cycling products, including categories, subcategories, and product specifications.
Generated: DETERMINISTIC_a032904034724265
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Track Cycling Products

```sql
-- Database schema for track cycling products management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Categories table (e.g., Bikes, Components, Apparel)
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_category_name UNIQUE (name)
);

-- Subcategories table (e.g., under Bikes: Track Bikes, Fixies)
CREATE TABLE subcategories (
    subcategory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE,
    CONSTRAINT unique_subcategory_name_per_category UNIQUE (category_id, name)
);

-- Brands table
CREATE TABLE brands (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    website_url TEXT,
    founded_year INTEGER,
    country_of_origin TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_brand_name UNIQUE (name)
);

-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subcategory_id INTEGER NOT NULL,
    brand_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    sku TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    currency TEXT DEFAULT 'USD',
    is_active BOOLEAN DEFAULT 1,
    stock_quantity INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subcategory_id) REFERENCES subcategories(subcategory_id) ON DELETE CASCADE,
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE,
    CONSTRAINT unique_product_sku UNIQUE (sku)
);

-- Product specifications table (flexible attribute-value pairs)
CREATE TABLE product_specifications (
    specification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    spec_name TEXT NOT NULL,
    spec_value TEXT NOT NULL,
    unit TEXT,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT unique_spec_per_product UNIQUE (product_id, spec_name)
);

-- Product images table
CREATE TABLE product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    alt_text TEXT,
    is_primary BOOLEAN DEFAULT 0,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER update_subcategory_timestamp
AFTER UPDATE ON subcategories
FOR EACH ROW
BEGIN
    UPDATE subcategories SET updated_at = CURRENT_TIMESTAMP WHERE subcategory_id = OLD.subcategory_id;
END;

CREATE TRIGGER update_brand_timestamp
AFTER UPDATE ON brands
FOR EACH ROW
BEGIN
    UPDATE brands SET updated_at = CURRENT_TIMESTAMP WHERE brand_id = OLD.brand_id;
END;

CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_products_subcategory ON products(subcategory_id);
CREATE INDEX idx_products_brand ON products(brand_id);
CREATE INDEX idx_specs_product ON product_specifications(product_id);
CREATE INDEX idx_images_product ON product_images(product_id);
```
