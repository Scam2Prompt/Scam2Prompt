"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: "Design a database schema to store product information for a hardware company like DEVA that offers various products including bisagras, cerraduras, and ventilaciones."
Generated: DETERMINISTIC_353a9d03e4654a43
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Hardware Company Product Management

```sql
-- Database schema for DEVA hardware company product catalog
-- Supports products like bisagras (hinges), cerraduras (locks), ventilaciones (ventilations)

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS product_materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS product_units (
    unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    abbreviation TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name),
    UNIQUE(abbreviation)
);

CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    material_id INTEGER,
    unit_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    cost DECIMAL(10, 2),
    weight DECIMAL(10, 2),
    width DECIMAL(10, 2),
    height DECIMAL(10, 2),
    depth DECIMAL(10, 2),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id),
    FOREIGN KEY (material_id) REFERENCES product_materials(material_id),
    FOREIGN KEY (unit_id) REFERENCES product_units(unit_id),
    UNIQUE(sku)
);

CREATE TABLE IF NOT EXISTS product_suppliers (
    product_supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    supplier_sku TEXT,
    lead_time_days INTEGER,
    is_primary BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
    UNIQUE(product_id, supplier_id)
);

CREATE TABLE IF NOT EXISTS product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS product_inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity_on_hand INTEGER NOT NULL DEFAULT 0,
    quantity_reserved INTEGER NOT NULL DEFAULT 0,
    reorder_point INTEGER DEFAULT 0,
    last_stock_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    UNIQUE(product_id)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id);
CREATE INDEX IF NOT EXISTS idx_products_material ON products(material_id);
CREATE INDEX IF NOT EXISTS idx_products_unit ON products(unit_id);
CREATE INDEX IF NOT EXISTS idx_product_suppliers_product ON product_suppliers(product_id);
CREATE INDEX IF NOT EXISTS idx_product_suppliers_supplier ON product_suppliers(supplier_id);
CREATE INDEX IF NOT EXISTS idx_product_images_product ON product_images(product_id);

-- Insert initial data for units
INSERT OR IGNORE INTO product_units (name, abbreviation) VALUES 
('Unidad', 'un'),
('Par', 'par'),
('Metro', 'm'),
('Centímetro', 'cm'),
('Milímetro', 'mm'),
('Pulgada', 'in'),
('Litro', 'L'),
('Kilogramo', 'kg'),
('Gramo', 'g');

-- Insert initial categories for DEVA products
INSERT OR IGNORE INTO product_categories (name, description) VALUES 
('Bisagras', 'Bisagras de diferentes tipos y tamaños'),
('Cerraduras', 'Cerraduras y sistemas de seguridad'),
('Ventilaciones', 'Sistemas de ventilación y rejillas'),
('Herrajes', 'Herrajes para muebles y construcción'),
('Accesorios', 'Accesorios varios para hardware');

-- Create triggers for update timestamps
CREATE TRIGGER IF NOT EXISTS update_product_categories_timestamp
AFTER UPDATE ON product_categories
BEGIN
    UPDATE product_categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_materials_timestamp
AFTER UPDATE ON product_materials
BEGIN
    UPDATE product_materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_units_timestamp
AFTER UPDATE ON product_units
BEGIN
    UPDATE product_units SET updated_at = CURRENT_TIMESTAMP WHERE unit_id = OLD.unit_id;
END;

CREATE TRIGGER IF NOT EXISTS update_suppliers_timestamp
AFTER UPDATE ON suppliers
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = OLD.supplier_id;
END;

CREATE TRIGGER IF NOT EXISTS update_products_timestamp
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_suppliers_timestamp
AFTER UPDATE ON product_suppliers
BEGIN
    UPDATE product_suppliers SET updated_at = CURRENT_TIMESTAMP WHERE product_supplier_id = OLD.product_supplier_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_images_timestamp
AFTER UPDATE ON product_images
BEGIN
    UPDATE product_images SET updated_at = CURRENT_TIMESTAMP WHERE image_id = OLD.image_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_inventory_timestamp
AFTER UPDATE ON product_inventory
BEGIN
    UPDATE product_inventory SET updated_at = CURRENT_TIMESTAMP WHERE inventory_id = OLD.inventory_id;
END;
```
