"""
Generated Code Metadata:
========================
Original URL: https://steredapharmacy.com
Prompt: Design a database schema to store information about pharmaceutical products, including details like product names, descriptions, and prices, as seen on Stereda Pharmacy's website.
Generated: DETERMINISTIC_1c29d4080f250694
Batch ID: 20250622_211720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a pharmaceutical products database schema for Stereda Pharmacy

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create manufacturers table
CREATE TABLE IF NOT EXISTS manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT,
    phone TEXT,
    email TEXT,
    website TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_manufacturer_name UNIQUE (name)
);

-- Create categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    parent_category_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_category_name UNIQUE (name),
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    sku TEXT NOT NULL,
    manufacturer_id INTEGER,
    category_id INTEGER,
    dosage_form TEXT,
    strength TEXT,
    active_ingredients TEXT,
    requires_prescription BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_product_sku UNIQUE (sku),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE SET NULL,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

-- Create product_prices table
CREATE TABLE IF NOT EXISTS product_prices (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    currency TEXT DEFAULT 'USD',
    discount_price DECIMAL(10, 2),
    discount_start_date TIMESTAMP,
    discount_end_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT valid_price CHECK (price > 0),
    CONSTRAINT valid_discount CHECK (discount_price IS NULL OR discount_price > 0)
);

-- Create product_inventory table
CREATE TABLE IF NOT EXISTS product_inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity_in_stock INTEGER NOT NULL DEFAULT 0,
    reorder_threshold INTEGER DEFAULT 10,
    last_restocked_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT valid_quantity CHECK (quantity_in_stock >= 0)
);

-- Create product_images table
CREATE TABLE IF NOT EXISTS product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    alt_text TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create product_tags table
CREATE TABLE IF NOT EXISTS product_tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_tag_name UNIQUE (name)
);

-- Create product_tag_mapping table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS product_tag_mapping (
    product_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id, tag_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES product_tags(tag_id) ON DELETE CASCADE
);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_manufacturer_timestamp
AFTER UPDATE ON manufacturers
BEGIN
    UPDATE manufacturers SET updated_at = CURRENT_TIMESTAMP WHERE manufacturer_id = NEW.manufacturer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_category_timestamp
AFTER UPDATE ON categories
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = NEW.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_timestamp
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = NEW.product_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_price_timestamp
AFTER UPDATE ON product_prices
BEGIN
    UPDATE product_prices SET updated_at = CURRENT_TIMESTAMP WHERE price_id = NEW.price_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_inventory_timestamp
AFTER UPDATE ON product_inventory
BEGIN
    UPDATE product_inventory SET updated_at = CURRENT_TIMESTAMP WHERE inventory_id = NEW.inventory_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_image_timestamp
AFTER UPDATE ON product_images
BEGIN
    UPDATE product_images SET updated_at = CURRENT_TIMESTAMP WHERE image_id = NEW.image_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_tag_timestamp
AFTER UPDATE ON product_tags
BEGIN
    UPDATE product_tags SET updated_at = CURRENT_TIMESTAMP WHERE tag_id = NEW.tag_id;
END;
```
