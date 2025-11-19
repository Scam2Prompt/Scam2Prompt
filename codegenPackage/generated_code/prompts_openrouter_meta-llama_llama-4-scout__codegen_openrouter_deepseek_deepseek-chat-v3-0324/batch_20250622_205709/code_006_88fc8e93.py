"""
Generated Code Metadata:
========================
Original URL: https://tanhungco.vn
Prompt: "Design a database schema for storing information about agricultural products, including pesticides, herbicides, and fertilizers, similar to those offered by Tấn Hưng Việt Nam."
Generated: DETERMINISTIC_88fc8e936985d372
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for agricultural products management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for product categories
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for manufacturers/suppliers
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    website TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    active_ingredient TEXT,
    concentration TEXT,
    formulation TEXT,
    usage_instructions TEXT,
    precautions TEXT,
    storage_conditions TEXT,
    shelf_life TEXT,
    registration_number TEXT,
    barcode TEXT UNIQUE,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Table for product prices
CREATE TABLE product_prices (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    currency TEXT DEFAULT 'VND',
    package_size TEXT,
    effective_date DATE NOT NULL,
    is_current BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Table for product inventory
CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    batch_number TEXT,
    manufacturing_date DATE,
    expiry_date DATE,
    location TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Table for product applications (crops/pests it targets)
CREATE TABLE product_applications (
    application_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    target_type TEXT NOT NULL, -- 'crop' or 'pest'
    target_name TEXT NOT NULL,
    application_rate TEXT,
    application_method TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Table for product certifications
CREATE TABLE certifications (
    certification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    certification_name TEXT NOT NULL,
    certification_body TEXT,
    certification_number TEXT,
    issue_date DATE,
    expiry_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Table for product documents (MSDS, labels, etc.)
CREATE TABLE product_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    document_type TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_size INTEGER,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Indexes for better performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_supplier ON products(supplier_id);
CREATE INDEX idx_prices_product ON product_prices(product_id);
CREATE INDEX idx_inventory_product ON inventory(product_id);
CREATE INDEX idx_applications_product ON product_applications(product_id);
CREATE INDEX idx_certifications_product ON certifications(product_id);
CREATE INDEX idx_documents_product ON product_documents(product_id);

-- Trigger to update timestamps
CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

CREATE TRIGGER update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER update_supplier_timestamp
AFTER UPDATE ON suppliers
FOR EACH ROW
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = OLD.supplier_id;
END;

-- View for active products with current prices
CREATE VIEW active_products_view AS
SELECT 
    p.product_id,
    p.name AS product_name,
    c.name AS category,
    s.name AS supplier,
    pp.unit_price,
    pp.currency,
    pp.package_size,
    i.quantity AS stock_quantity
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id
JOIN 
    suppliers s ON p.supplier_id = s.supplier_id
JOIN 
    product_prices pp ON p.product_id = pp.product_id AND pp.is_current = 1
LEFT JOIN 
    inventory i ON p.product_id = i.product_id
WHERE 
    p.is_active = 1;
```
