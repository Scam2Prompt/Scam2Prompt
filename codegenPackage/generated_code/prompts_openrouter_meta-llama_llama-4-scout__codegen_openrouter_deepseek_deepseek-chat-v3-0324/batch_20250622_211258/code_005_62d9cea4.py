"""
Generated Code Metadata:
========================
Original URL: https://xn--grsklippare-m8a.se
Prompt: Design a database schema to store information about lawn mowers, including their type, brand, price, and features, similar to the product catalog on Gräsklippare.se.
Generated: DETERMINISTIC_62d9cea41512be78
Batch ID: 20250622_211258
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Lawn Mower Database Schema

```sql
-- Database schema for lawn mower product catalog
-- Tables for storing lawn mower information similar to Gräsklippare.se

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Brands table
CREATE TABLE IF NOT EXISTS brands (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    website_url TEXT,
    logo_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    parent_category_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id)
);

-- Features table
CREATE TABLE IF NOT EXISTS features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    model_name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2),
    stock_quantity INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    CHECK (price > 0),
    CHECK (discount_price IS NULL OR discount_price > 0),
    CHECK (stock_quantity >= 0)
);

-- Product features junction table
CREATE TABLE IF NOT EXISTS product_features (
    product_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    value TEXT,
    PRIMARY KEY (product_id, feature_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES features(feature_id) ON DELETE CASCADE
);

-- Product images table
CREATE TABLE IF NOT EXISTS product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    alt_text TEXT,
    is_primary BOOLEAN DEFAULT 0,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Product specifications table
CREATE TABLE IF NOT EXISTS specifications (
    specification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    value TEXT NOT NULL,
    unit TEXT,
    display_order INTEGER DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_products_brand ON products(brand_id);
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id);
CREATE INDEX IF NOT EXISTS idx_product_features_product ON product_features(product_id);
CREATE INDEX IF NOT EXISTS idx_product_features_feature ON product_features(feature_id);
CREATE INDEX IF NOT EXISTS idx_product_images_product ON product_images(product_id);
CREATE INDEX IF NOT EXISTS idx_specifications_product ON specifications(product_id);

-- Trigger to update the updated_at timestamp on row modification
CREATE TRIGGER IF NOT EXISTS update_brands_timestamp
AFTER UPDATE ON brands
FOR EACH ROW
BEGIN
    UPDATE brands SET updated_at = CURRENT_TIMESTAMP WHERE brand_id = OLD.brand_id;
END;

CREATE TRIGGER IF NOT EXISTS update_categories_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_features_timestamp
AFTER UPDATE ON features
FOR EACH ROW
BEGIN
    UPDATE features SET updated_at = CURRENT_TIMESTAMP WHERE feature_id = OLD.feature_id;
END;

CREATE TRIGGER IF NOT EXISTS update_products_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;
```
