"""
Generated Code Metadata:
========================
Original URL: https://app-rneta-mask-io.blogspot.com
Prompt: "Design a database schema to store information about glass products, including product types, materials, and dimensions, inspired by the product offerings on the Maryart website."
Generated: DETERMINISTIC_1a6480100eae495d
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for glass products inventory
-- Inspired by Maryart product offerings

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Product categories table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    durability_rating INTEGER CHECK (durability_rating BETWEEN 1 AND 10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Colors table
CREATE TABLE colors (
    color_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    hex_code TEXT CHECK (hex_code GLOB '#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    color_id INTEGER,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (material_id) REFERENCES materials(material_id),
    FOREIGN KEY (color_id) REFERENCES colors(color_id)
);

-- Product dimensions table
CREATE TABLE product_dimensions (
    dimension_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    length DECIMAL(10, 2) CHECK (length > 0),
    width DECIMAL(10, 2) CHECK (width > 0),
    height DECIMAL(10, 2) CHECK (height > 0),
    weight DECIMAL(10, 2) CHECK (weight > 0),
    thickness DECIMAL(10, 2) CHECK (thickness > 0),
    unit TEXT DEFAULT 'cm' CHECK (unit IN ('cm', 'mm', 'inch')),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Product images table
CREATE TABLE product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    alt_text TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Product variants table (for different colors/sizes of the same product)
CREATE TABLE product_variants (
    variant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    sku TEXT NOT NULL UNIQUE,
    color_id INTEGER,
    dimension_id INTEGER,
    price_adjustment DECIMAL(10, 2) DEFAULT 0,
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES colors(color_id),
    FOREIGN KEY (dimension_id) REFERENCES product_dimensions(dimension_id)
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER update_categories_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER update_materials_timestamp
AFTER UPDATE ON materials
FOR EACH ROW
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER update_colors_timestamp
AFTER UPDATE ON colors
FOR EACH ROW
BEGIN
    UPDATE colors SET updated_at = CURRENT_TIMESTAMP WHERE color_id = OLD.color_id;
END;

CREATE TRIGGER update_products_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

CREATE TRIGGER update_variants_timestamp
AFTER UPDATE ON product_variants
FOR EACH ROW
BEGIN
    UPDATE product_variants SET updated_at = CURRENT_TIMESTAMP WHERE variant_id = OLD.variant_id;
END;
```
