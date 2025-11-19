"""
Generated Code Metadata:
========================
Original URL: https://volport.com
Prompt: Design a database schema to store product information for an e-commerce platform selling mobile accessories, including car chargers and cases.
Generated: DETERMINISTIC_cfc35f0d18f57c8b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for e-commerce platform selling mobile accessories

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE brands (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    logo_url TEXT,
    website_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    category_id INTEGER NOT NULL,
    brand_id INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id),
    CHECK (price >= 0),
    CHECK (stock_quantity >= 0)
);

CREATE TABLE product_attributes (
    attribute_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_attribute_values (
    product_id INTEGER NOT NULL,
    attribute_id INTEGER NOT NULL,
    value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id, attribute_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (attribute_id) REFERENCES product_attributes(attribute_id) ON DELETE CASCADE
);

CREATE TABLE product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

CREATE TABLE product_variants (
    variant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    price_adjustment DECIMAL(10, 2) DEFAULT 0,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CHECK (stock_quantity >= 0)
);

CREATE TABLE variant_attributes (
    variant_id INTEGER NOT NULL,
    attribute_id INTEGER NOT NULL,
    value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (variant_id, attribute_id),
    FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id) ON DELETE CASCADE,
    FOREIGN KEY (attribute_id) REFERENCES product_attributes(attribute_id) ON DELETE CASCADE
);

-- Create indexes for performance optimization
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_brand ON products(brand_id);
CREATE INDEX idx_product_attribute_values_product ON product_attribute_values(product_id);
CREATE INDEX idx_product_attribute_values_attribute ON product_attribute_values(attribute_id);
CREATE INDEX idx_product_images_product ON product_images(product_id);
CREATE INDEX idx_product_variants_product ON product_variants(product_id);
CREATE INDEX idx_variant_attributes_variant ON variant_attributes(variant_id);
CREATE INDEX idx_variant_attributes_attribute ON variant_attributes(attribute_id);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
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

CREATE TRIGGER update_product_attribute_timestamp
AFTER UPDATE ON product_attributes
FOR EACH ROW
BEGIN
    UPDATE product_attributes SET updated_at = CURRENT_TIMESTAMP WHERE attribute_id = OLD.attribute_id;
END;

CREATE TRIGGER update_product_attribute_value_timestamp
AFTER UPDATE ON product_attribute_values
FOR EACH ROW
BEGIN
    UPDATE product_attribute_values SET updated_at = CURRENT_TIMESTAMP 
    WHERE product_id = OLD.product_id AND attribute_id = OLD.attribute_id;
END;

CREATE TRIGGER update_product_variant_timestamp
AFTER UPDATE ON product_variants
FOR EACH ROW
BEGIN
    UPDATE product_variants SET updated_at = CURRENT_TIMESTAMP WHERE variant_id = OLD.variant_id;
END;

CREATE TRIGGER update_variant_attribute_timestamp
AFTER UPDATE ON variant_attributes
FOR EACH ROW
BEGIN
    UPDATE variant_attributes SET updated_at = CURRENT_TIMESTAMP 
    WHERE variant_id = OLD.variant_id AND attribute_id = OLD.attribute_id;
END;
```
