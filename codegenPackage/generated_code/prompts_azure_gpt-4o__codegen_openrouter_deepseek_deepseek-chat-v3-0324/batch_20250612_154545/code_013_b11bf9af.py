"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Create a database schema to store product information for AirstyleArt, including stencils, paints, accessories, and airbrush equipment.
Generated: DETERMINISTIC_b11bf9af71bde2be
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for AirstyleArt product information

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create categories table to classify products
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create products table to store common product information
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create product_images table to store multiple images per product
CREATE TABLE IF NOT EXISTS product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create stencils table for stencil-specific attributes
CREATE TABLE IF NOT EXISTS stencils (
    stencil_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL UNIQUE,
    material TEXT NOT NULL,
    size TEXT NOT NULL,
    complexity_level TEXT CHECK(complexity_level IN ('Beginner', 'Intermediate', 'Advanced')),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create paints table for paint-specific attributes
CREATE TABLE IF NOT EXISTS paints (
    paint_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL UNIQUE,
    color TEXT NOT NULL,
    volume_ml INTEGER NOT NULL,
    opacity TEXT CHECK(opacity IN ('Transparent', 'Semi-transparent', 'Opaque')),
    is_water_based BOOLEAN NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create accessories table for accessory-specific attributes
CREATE TABLE IF NOT EXISTS accessories (
    accessory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL UNIQUE,
    accessory_type TEXT NOT NULL,
    material TEXT,
    compatible_with TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create airbrush_equipment table for airbrush-specific attributes
CREATE TABLE IF NOT EXISTS airbrush_equipment (
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL UNIQUE,
    equipment_type TEXT NOT NULL CHECK(equipment_type IN ('Airbrush', 'Compressor', 'Hose', 'Nozzle', 'Other')),
    power_source TEXT,
    pressure_range TEXT,
    weight_grams INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create product_tags table for tagging products
CREATE TABLE IF NOT EXISTS product_tags (
    tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Create product_tag_mapping table for many-to-many relationship between products and tags
CREATE TABLE IF NOT EXISTS product_tag_mapping (
    product_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (product_id, tag_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES product_tags(tag_id) ON DELETE CASCADE
);

-- Create trigger to update the updated_at timestamp when a product is modified
CREATE TRIGGER IF NOT EXISTS update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id);
CREATE INDEX IF NOT EXISTS idx_products_sku ON products(sku);
CREATE INDEX IF NOT EXISTS idx_product_images_product ON product_images(product_id);
CREATE INDEX IF NOT EXISTS idx_product_tags_mapping ON product_tag_mapping(product_id, tag_id);
```
