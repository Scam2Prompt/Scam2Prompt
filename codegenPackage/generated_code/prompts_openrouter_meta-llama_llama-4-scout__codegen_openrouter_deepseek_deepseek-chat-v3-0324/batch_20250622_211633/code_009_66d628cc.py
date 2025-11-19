"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: "Design a database schema for storing and managing industrial product information, including product categories, pricing, and supplier details."
Generated: DETERMINISTIC_66d628cc2ce147e1
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for industrial product management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create Suppliers table
CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT,
    country TEXT NOT NULL,
    postal_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    CHECK (LENGTH(phone) >= 8)
);

-- Create ProductCategories table
CREATE TABLE IF NOT EXISTS ProductCategories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT,
    parent_category_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES ProductCategories(category_id)
);

-- Create Products table
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_code TEXT NOT NULL UNIQUE,
    product_name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    unit_of_measure TEXT NOT NULL,
    weight REAL,
    dimensions TEXT,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES ProductCategories(category_id),
    CHECK (weight >= 0)
);

-- Create ProductPricing table
CREATE TABLE IF NOT EXISTS ProductPricing (
    pricing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2),
    currency TEXT NOT NULL DEFAULT 'USD',
    valid_from DATE NOT NULL,
    valid_to DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    CHECK (base_price > 0),
    CHECK (discount_price IS NULL OR discount_price > 0),
    CHECK (valid_to IS NULL OR valid_to >= valid_from)
);

-- Create ProductSuppliers table (junction table for many-to-many relationship)
CREATE TABLE IF NOT EXISTS ProductSuppliers (
    product_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    supplier_product_code TEXT,
    lead_time_days INTEGER,
    min_order_quantity INTEGER NOT NULL DEFAULT 1,
    is_primary_supplier BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id, supplier_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id),
    CHECK (lead_time_days IS NULL OR lead_time_days >= 0),
    CHECK (min_order_quantity > 0)
);

-- Create Inventory table
CREATE TABLE IF NOT EXISTS Inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity_in_stock INTEGER NOT NULL DEFAULT 0,
    reorder_level INTEGER DEFAULT 0,
    last_restocked_date DATE,
    warehouse_location TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    CHECK (quantity_in_stock >= 0),
    CHECK (reorder_level >= 0)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_products_category ON Products(category_id);
CREATE INDEX IF NOT EXISTS idx_product_pricing_product ON ProductPricing(product_id);
CREATE INDEX IF NOT EXISTS idx_product_suppliers_product ON ProductSuppliers(product_id);
CREATE INDEX IF NOT EXISTS idx_product_suppliers_supplier ON ProductSuppliers(supplier_id);
CREATE INDEX IF NOT EXISTS idx_inventory_product ON Inventory(product_id);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_suppliers_timestamp
AFTER UPDATE ON Suppliers
BEGIN
    UPDATE Suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = NEW.supplier_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_categories_timestamp
AFTER UPDATE ON ProductCategories
BEGIN
    UPDATE ProductCategories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = NEW.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_products_timestamp
AFTER UPDATE ON Products
BEGIN
    UPDATE Products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = NEW.product_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_pricing_timestamp
AFTER UPDATE ON ProductPricing
BEGIN
    UPDATE ProductPricing SET updated_at = CURRENT_TIMESTAMP WHERE pricing_id = NEW.pricing_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_suppliers_timestamp
AFTER UPDATE ON ProductSuppliers
BEGIN
    UPDATE ProductSuppliers SET updated_at = CURRENT_TIMESTAMP 
    WHERE product_id = NEW.product_id AND supplier_id = NEW.supplier_id;
END;

CREATE TRIGGER IF NOT EXISTS update_inventory_timestamp
AFTER UPDATE ON Inventory
BEGIN
    UPDATE Inventory SET updated_at = CURRENT_TIMESTAMP WHERE inventory_id = NEW.inventory_id;
END;
```
