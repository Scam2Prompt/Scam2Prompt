"""
Generated Code Metadata:
========================
Original URL: https://casapatty.com.br
Prompt: Generate a SQL database schema to store information about construction materials, suppliers, and delivery regions for a store like Casa Patty.
Generated: DETERMINISTIC_1036ad8603ef5272
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Casa Patty construction materials management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Suppliers table
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT TEXT CHECK(email LIKE '%@%.%'),
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, email)
);

-- Delivery regions table
CREATE TABLE delivery_regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    delivery_fee DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

-- Materials categories table
CREATE TABLE material_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

-- Materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    min_stock_level INTEGER NOT NULL DEFAULT 10,
    supplier_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES material_categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    UNIQUE(name, supplier_id),
    CHECK(unit_price > 0),
    CHECK(stock_quantity >= 0),
    CHECK(min_stock_level >= 0)
);

-- Supplier delivery regions junction table
CREATE TABLE supplier_delivery_regions (
    supplier_id INTEGER NOT NULL,
    region_id INTEGER NOT NULL,
    PRIMARY KEY (supplier_id, region_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (region_id) REFERENCES delivery_regions(region_id)
);

-- Material images table
CREATE TABLE material_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Price history table
CREATE TABLE material_price_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER NOT NULL,
    old_price DECIMAL(10,2) NOT NULL,
    new_price DECIMAL(10,2) NOT NULL,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Trigger to update timestamps on suppliers table
CREATE TRIGGER update_supplier_timestamp
AFTER UPDATE ON suppliers
FOR EACH ROW
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = OLD.supplier_id;
END;

-- Trigger to update timestamps on materials table
CREATE TRIGGER update_material_timestamp
AFTER UPDATE ON materials
FOR EACH ROW
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

-- Trigger to update timestamps on delivery_regions table
CREATE TRIGGER update_region_timestamp
AFTER UPDATE ON delivery_regions
FOR EACH ROW
BEGIN
    UPDATE delivery_regions SET updated_at = CURRENT_TIMESTAMP WHERE region_id = OLD.region_id;
END;

-- Trigger to update timestamps on material_categories table
CREATE TRIGGER update_category_timestamp
AFTER UPDATE ON material_categories
FOR EACH ROW
BEGIN
    UPDATE material_categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

-- Trigger to log price changes
CREATE TRIGGER log_price_change
AFTER UPDATE OF unit_price ON materials
FOR EACH ROW
WHEN OLD.unit_price <> NEW.unit_price
BEGIN
    INSERT INTO material_price_history (material_id, old_price, new_price)
    VALUES (OLD.material_id, OLD.unit_price, NEW.unit_price);
END;
```
