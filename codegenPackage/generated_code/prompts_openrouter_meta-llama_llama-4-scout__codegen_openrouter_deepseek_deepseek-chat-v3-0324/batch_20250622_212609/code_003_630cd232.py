"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Design a database schema to store information about electronic components, including categories, pricing, and inventory levels.
Generated: DETERMINISTIC_630cd2329bddb719
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for electronic components inventory system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Component categories table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    parent_category_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

-- Manufacturers table
CREATE TABLE manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    website TEXT,
    contact_email TEXT CHECK(contact_email LIKE '%_@__%.__%'),
    phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Components table
CREATE TABLE components (
    component_id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_number TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    datasheet_url TEXT,
    image_url TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE RESTRICT,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE RESTRICT
);

-- Component specifications table
CREATE TABLE specifications (
    specification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    component_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    value TEXT NOT NULL,
    unit TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE
);

-- Pricing table
CREATE TABLE pricing (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    component_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK(price > 0),
    currency TEXT DEFAULT 'USD',
    quantity_break INTEGER DEFAULT 1 CHECK(quantity_break > 0),
    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valid_to TIMESTAMP,
    is_current BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    CHECK (valid_to IS NULL OR valid_from < valid_to)
);

-- Inventory table
CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    component_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0),
    location TEXT,
    batch_number TEXT,
    date_received TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expiry_date TIMESTAMP,
    min_stock_level INTEGER DEFAULT 0 CHECK(min_stock_level >= 0),
    reorder_quantity INTEGER DEFAULT 0 CHECK(reorder_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    CHECK (expiry_date IS NULL OR date_received < expiry_date)
);

-- Suppliers table
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT CHECK(email LIKE '%_@__%.__%'),
    phone TEXT,
    address TEXT,
    website TEXT,
    lead_time_days INTEGER DEFAULT 0 CHECK(lead_time_days >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Component suppliers relationship table
CREATE TABLE component_suppliers (
    component_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    supplier_part_number TEXT,
    is_preferred BOOLEAN DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (component_id, supplier_id),
    FOREIGN KEY (component_id) REFERENCES components(component_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_components_category ON components(category_id);
CREATE INDEX idx_components_manufacturer ON components(manufacturer_id);
CREATE INDEX idx_pricing_component ON pricing(component_id);
CREATE INDEX idx_inventory_component ON inventory(component_id);
CREATE INDEX idx_specifications_component ON specifications(component_id);
CREATE INDEX idx_component_suppliers_component ON component_suppliers(component_id);
CREATE INDEX idx_component_suppliers_supplier ON component_suppliers(supplier_id);

-- Trigger to update timestamps on category updates
CREATE TRIGGER update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

-- Trigger to update timestamps on component updates
CREATE TRIGGER update_component_timestamp
AFTER UPDATE ON components
FOR EACH ROW
BEGIN
    UPDATE components SET updated_at = CURRENT_TIMESTAMP WHERE component_id = OLD.component_id;
END;

-- Trigger to update timestamps on manufacturer updates
CREATE TRIGGER update_manufacturer_timestamp
AFTER UPDATE ON manufacturers
FOR EACH ROW
BEGIN
    UPDATE manufacturers SET updated_at = CURRENT_TIMESTAMP WHERE manufacturer_id = OLD.manufacturer_id;
END;

-- Trigger to update timestamps on supplier updates
CREATE TRIGGER update_supplier_timestamp
AFTER UPDATE ON suppliers
FOR EACH ROW
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = OLD.supplier_id;
END;

-- Trigger to update timestamps on inventory updates
CREATE TRIGGER update_inventory_timestamp
AFTER UPDATE ON inventory
FOR EACH ROW
BEGIN
    UPDATE inventory SET updated_at = CURRENT_TIMESTAMP WHERE inventory_id = OLD.inventory_id;
END;

-- View for current component inventory status
CREATE VIEW component_inventory_status AS
SELECT 
    c.component_id,
    c.part_number,
    c.name AS component_name,
    cat.name AS category,
    m.name AS manufacturer,
    SUM(i.quantity) AS total_quantity,
    MIN(i.min_stock_level) AS min_stock_level,
    CASE 
        WHEN SUM(i.quantity) <= MIN(i.min_stock_level) THEN 'Reorder'
        WHEN SUM(i.quantity) <= MIN(i.min_stock_level) * 1.5 THEN 'Low'
        ELSE 'OK'
    END AS stock_status
FROM components c
JOIN categories cat ON c.category_id = cat.category_id
JOIN manufacturers m ON c.manufacturer_id = m.manufacturer_id
LEFT JOIN inventory i ON c.component_id = i.component_id
GROUP BY c.component_id;

-- View for current pricing information
CREATE VIEW component_pricing AS
SELECT 
    c.component_id,
    c.part_number,
    c.name AS component_name,
    p.price,
    p.currency,
    p.quantity_break,
    p.valid_from,
    p.valid_to
FROM components c
JOIN pricing p ON c.component_id = p.component_id
WHERE p.is_current = 1;
```
