"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Create a database schema for managing private label cleaning tool production, inspired by PDC Brush's operational model.
Generated: DETERMINISTIC_5465e921e19b876b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for private label cleaning tool production management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    contact_name TEXT,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT,
    tax_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Product categories table
CREATE TABLE product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Raw materials table
CREATE TABLE raw_materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    unit_of_measure TEXT NOT NULL,
    current_stock REAL DEFAULT 0,
    min_stock_level REAL DEFAULT 0,
    supplier_info TEXT,
    unit_cost REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (current_stock >= 0),
    CHECK (min_stock_level >= 0),
    CHECK (unit_cost > 0)
);

-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    category_id INTEGER,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    unit_price REAL NOT NULL,
    production_cost REAL,
    min_order_quantity INTEGER DEFAULT 1,
    lead_time_days INTEGER DEFAULT 14,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE SET NULL,
    CHECK (unit_price > 0),
    CHECK (production_cost >= 0),
    CHECK (min_order_quantity > 0),
    CHECK (lead_time_days >= 0)
);

-- Product materials (bill of materials)
CREATE TABLE product_materials (
    product_id INTEGER,
    material_id INTEGER,
    quantity REAL NOT NULL,
    notes TEXT,
    PRIMARY KEY (product_id, material_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES raw_materials(material_id) ON DELETE CASCADE,
    CHECK (quantity > 0)
);

-- Production batches table
CREATE TABLE production_batches (
    batch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    production_date DATE NOT NULL,
    completion_date DATE,
    status TEXT NOT NULL DEFAULT 'planned', -- planned, in_progress, completed, cancelled
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CHECK (quantity > 0),
    CHECK (status IN ('planned', 'in_progress', 'completed', 'cancelled')),
    CHECK (completion_date IS NULL OR completion_date >= production_date)
);

-- Batch material usage
CREATE TABLE batch_material_usage (
    usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity_used REAL NOT NULL,
    notes TEXT,
    FOREIGN KEY (batch_id) REFERENCES production_batches(batch_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES raw_materials(material_id) ON DELETE CASCADE,
    CHECK (quantity_used > 0)
);

-- Orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    required_date DATE,
    shipped_date DATE,
    status TEXT NOT NULL DEFAULT 'new', -- new, processing, shipped, delivered, cancelled
    tracking_number TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    CHECK (status IN ('new', 'processing', 'shipped', 'delivered', 'cancelled')),
    CHECK (required_date IS NULL OR required_date >= order_date),
    CHECK (shipped_date IS NULL OR shipped_date >= order_date)
);

-- Order details table
CREATE TABLE order_details (
    order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    discount REAL DEFAULT 0,
    batch_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (batch_id) REFERENCES production_batches(batch_id) ON DELETE SET NULL,
    CHECK (quantity > 0),
    CHECK (unit_price > 0),
    CHECK (discount >= 0 AND discount <= 1)
);

-- Inventory adjustments table
CREATE TABLE inventory_adjustments (
    adjustment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER NOT NULL,
    adjustment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quantity REAL NOT NULL,
    reason TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (material_id) REFERENCES raw_materials(material_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_products_customer ON products(customer_id);
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_product_materials_product ON product_materials(product_id);
CREATE INDEX idx_product_materials_material ON product_materials(material_id);
CREATE INDEX idx_production_batches_product ON production_batches(product_id);
CREATE INDEX idx_batch_material_usage_batch ON batch_material_usage(batch_id);
CREATE INDEX idx_batch_material_usage_material ON batch_material_usage(material_id);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_order_details_order ON order_details(order_id);
CREATE INDEX idx_order_details_product ON order_details(product_id);
```
