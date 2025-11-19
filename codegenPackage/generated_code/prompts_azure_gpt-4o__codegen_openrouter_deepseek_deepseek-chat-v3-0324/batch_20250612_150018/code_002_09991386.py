"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Create a database schema for managing inventory of food packaging products like microwavable containers, drinking cups, and plastic cutlery, referencing Isoplas Corporation's offerings.
Generated: DETERMINISTIC_099913865e141dde
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing inventory of food packaging products
-- Inspired by Isoplas Corporation's product offerings

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create product categories table
CREATE TABLE IF NOT EXISTS product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    product_name TEXT NOT NULL,
    description TEXT,
    material_type TEXT NOT NULL,
    capacity_volume TEXT, -- For containers/cups (e.g., "500ml", "32oz")
    dimensions TEXT, -- For containers (e.g., "10x10x5cm")
    color TEXT,
    is_microwave_safe BOOLEAN DEFAULT FALSE,
    is_recyclable BOOLEAN DEFAULT FALSE,
    unit_price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    min_stock_level INTEGER NOT NULL DEFAULT 10,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE
);

-- Create suppliers table
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create inventory_transactions table
CREATE TABLE IF NOT EXISTS inventory_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    supplier_id INTEGER,
    transaction_type TEXT NOT NULL CHECK(transaction_type IN ('IN', 'OUT', 'ADJUSTMENT', 'RETURN')),
    quantity INTEGER NOT NULL,
    unit_cost DECIMAL(10, 2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE SET NULL
);

-- Create product_images table
CREATE TABLE IF NOT EXISTS product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_category_timestamp
AFTER UPDATE ON product_categories
FOR EACH ROW
BEGIN
    UPDATE product_categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

CREATE TRIGGER IF NOT EXISTS update_supplier_timestamp
AFTER UPDATE ON suppliers
FOR EACH ROW
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = OLD.supplier_id;
END;

-- Create view for low stock alerts
CREATE VIEW IF NOT EXISTS low_stock_products AS
SELECT 
    p.product_id,
    p.product_name,
    pc.category_name,
    p.stock_quantity,
    p.min_stock_level
FROM 
    products p
JOIN 
    product_categories pc ON p.category_id = pc.category_id
WHERE 
    p.stock_quantity <= p.min_stock_level;

-- Insert initial categories
INSERT OR IGNORE INTO product_categories (category_name, description) VALUES
('Microwavable Containers', 'Heat-resistant containers for microwave use'),
('Drinking Cups', 'Various types of cups for beverages'),
('Plastic Cutlery', 'Disposable utensils including forks, knives, and spoons'),
('Lids and Covers', 'Compatible lids for containers and cups'),
('Takeaway Packaging', 'Complete packaging solutions for food delivery');

-- Create index for frequently queried columns
CREATE INDEX IF NOT EXISTS idx_product_category ON products(category_id);
CREATE INDEX IF NOT EXISTS idx_product_name ON products(product_name);
CREATE INDEX IF NOT EXISTS idx_transaction_product ON inventory_transactions(product_id);
CREATE INDEX IF NOT EXISTS idx_transaction_date ON inventory_transactions(transaction_date);
```
