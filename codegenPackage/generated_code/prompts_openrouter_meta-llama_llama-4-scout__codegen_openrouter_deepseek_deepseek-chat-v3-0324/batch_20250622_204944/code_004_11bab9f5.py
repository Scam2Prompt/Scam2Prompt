"""
Generated Code Metadata:
========================
Original URL: https://naimatabbasind.com
Prompt: "Design a database schema to store information about sports wear products, including product categories, materials, and sizes, similar to Naimat Abbas Industries' product range."
Generated: DETERMINISTIC_11bab9f59a2cc293
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for sports wear products

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create product categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create materials table
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    properties TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create sizes table
CREATE TABLE IF NOT EXISTS sizes (
    size_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    category_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    image_url TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Create product_sizes junction table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS product_sizes (
    product_id INTEGER NOT NULL,
    size_id INTEGER NOT NULL,
    PRIMARY KEY (product_id, size_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (size_id) REFERENCES sizes(size_id) ON DELETE CASCADE
);

-- Create product variants table (for color variations)
CREATE TABLE IF NOT EXISTS product_variants (
    variant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    color TEXT NOT NULL,
    image_url TEXT,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_material_timestamp
AFTER UPDATE ON materials
FOR EACH ROW
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER IF NOT EXISTS update_size_timestamp
AFTER UPDATE ON sizes
FOR EACH ROW
BEGIN
    UPDATE sizes SET updated_at = CURRENT_TIMESTAMP WHERE size_id = OLD.size_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

CREATE TRIGGER IF NOT EXISTS update_variant_timestamp
AFTER UPDATE ON product_variants
FOR EACH ROW
BEGIN
    UPDATE product_variants SET updated_at = CURRENT_TIMESTAMP WHERE variant_id = OLD.variant_id;
END;

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id);
CREATE INDEX IF NOT EXISTS idx_products_material ON products(material_id);
CREATE INDEX IF NOT EXISTS idx_product_sizes_product ON product_sizes(product_id);
CREATE INDEX IF NOT EXISTS idx_product_sizes_size ON product_sizes(size_id);
CREATE INDEX IF NOT EXISTS idx_product_variants_product ON product_variants(product_id);
```
