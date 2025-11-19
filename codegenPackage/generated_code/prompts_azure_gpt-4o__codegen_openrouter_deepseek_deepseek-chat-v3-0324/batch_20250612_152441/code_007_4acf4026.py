"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: Create a database schema to store information about UPVC window and door types, such as tilt windows, villa windows, and sliding doors, based on Dexodoor's product catalog.
Generated: DETERMINISTIC_4acf4026d6397bcf
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for UPVC window and door types based on Dexodoor's product catalog

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for product categories (e.g., windows, doors)
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for product types (e.g., tilt windows, villa windows, sliding doors)
CREATE TABLE IF NOT EXISTS product_types (
    product_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    image_url TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE,
    UNIQUE(category_id, name)
);

-- Table for product variants (e.g., different sizes, colors)
CREATE TABLE IF NOT EXISTS variants (
    variant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    standard_size TEXT,
    available_colors TEXT,
    u_value REAL,
    sound_reduction_index REAL,
    security_rating TEXT,
    price DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_type_id) REFERENCES product_types(product_type_id) ON DELETE CASCADE,
    UNIQUE(product_type_id, name)
);

-- Table for product features
CREATE TABLE IF NOT EXISTS features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for product types and their features
CREATE TABLE IF NOT EXISTS product_features (
    product_type_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    PRIMARY KEY (product_type_id, feature_id),
    FOREIGN KEY (product_type_id) REFERENCES product_types(product_type_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES features(feature_id) ON DELETE CASCADE
);

-- Table for product images
CREATE TABLE IF NOT EXISTS product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_type_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT 0,
    caption TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_type_id) REFERENCES product_types(product_type_id) ON DELETE CASCADE
);

-- Table for technical specifications
CREATE TABLE IF NOT EXISTS technical_specs (
    spec_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_type_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    value TEXT NOT NULL,
    unit TEXT,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_type_id) REFERENCES product_types(product_type_id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp when records are modified
CREATE TRIGGER IF NOT EXISTS update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_type_timestamp
AFTER UPDATE ON product_types
FOR EACH ROW
BEGIN
    UPDATE product_types SET updated_at = CURRENT_TIMESTAMP WHERE product_type_id = OLD.product_type_id;
END;

CREATE TRIGGER IF NOT EXISTS update_variant_timestamp
AFTER UPDATE ON variants
FOR EACH ROW
BEGIN
    UPDATE variants SET updated_at = CURRENT_TIMESTAMP WHERE variant_id = OLD.variant_id;
END;

CREATE TRIGGER IF NOT EXISTS update_feature_timestamp
AFTER UPDATE ON features
FOR EACH ROW
BEGIN
    UPDATE features SET updated_at = CURRENT_TIMESTAMP WHERE feature_id = OLD.feature_id;
END;

-- Indexes for better performance
CREATE INDEX IF NOT EXISTS idx_product_types_category ON product_types(category_id);
CREATE INDEX IF NOT EXISTS idx_variants_product_type ON variants(product_type_id);
CREATE INDEX IF NOT EXISTS idx_product_features_product ON product_features(product_type_id);
CREATE INDEX IF NOT EXISTS idx_product_features_feature ON product_features(feature_id);
CREATE INDEX IF NOT EXISTS idx_product_images_product ON product_images(product_type_id);
CREATE INDEX IF NOT EXISTS idx_technical_specs_product ON technical_specs(product_type_id);
```
