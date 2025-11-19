"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Design a database schema for managing supply chain data, including tables for products, manufacturers, suppliers, and quality control metrics, inspired by Trendsetters' supply chain management services.
Generated: DETERMINISTIC_f337fcbfa4ad5b65
Batch ID: 20250622_211606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Supply Chain Management System
-- Inspired by Trendsetters' supply chain management services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for manufacturers
CREATE TABLE manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    contact_person TEXT NOT NULL,
    email TEXT NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    certification_status TEXT CHECK(certification_status IN ('Certified', 'Pending', 'Suspended')),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, email)
);

-- Table for suppliers
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    contact_person TEXT NOT NULL,
    email TEXT NOT NULL CHECK(email LIKE '%@%.%'),
    phone TEXT NOT NULL,
    reliability_score INTEGER CHECK(reliability_score BETWEEN 0 AND 100),
    contract_start_date DATE NOT NULL,
    contract_end_date DATE,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, email)
);

-- Table for product categories
CREATE TABLE product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Table for products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL CHECK(unit_price > 0),
    weight DECIMAL(10, 2) CHECK(weight > 0),
    dimensions TEXT,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

-- Table for inventory
CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity_on_hand INTEGER NOT NULL DEFAULT 0 CHECK(quantity_on_hand >= 0),
    quantity_reserved INTEGER NOT NULL DEFAULT 0 CHECK(quantity_reserved >= 0),
    reorder_level INTEGER NOT NULL DEFAULT 0 CHECK(reorder_level >= 0),
    last_restock_date TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Table for supplier_product relationships
CREATE TABLE supplier_products (
    supplier_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    lead_time_days INTEGER NOT NULL CHECK(lead_time_days > 0),
    unit_cost DECIMAL(10, 2) NOT NULL CHECK(unit_cost > 0),
    min_order_quantity INTEGER NOT NULL CHECK(min_order_quantity > 0),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    UNIQUE(supplier_id, product_id)
);

-- Table for purchase orders
CREATE TABLE purchase_orders (
    po_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expected_delivery_date TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('Draft', 'Submitted', 'Approved', 'Shipped', 'Delivered', 'Cancelled')),
    total_amount DECIMAL(12, 2) NOT NULL CHECK(total_amount > 0),
    notes TEXT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Table for purchase order items
CREATE TABLE po_items (
    po_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    po_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL CHECK(unit_price > 0),
    line_total DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED,
    received_quantity INTEGER DEFAULT 0 CHECK(received_quantity >= 0),
    FOREIGN KEY (po_id) REFERENCES purchase_orders(po_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Table for quality control metrics
CREATE TABLE quality_metrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    target_value DECIMAL(10, 2),
    min_threshold DECIMAL(10, 2),
    max_threshold DECIMAL(10, 2),
    unit TEXT
);

-- Table for product quality inspections
CREATE TABLE quality_inspections (
    inspection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    batch_number TEXT NOT NULL,
    inspection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    inspector_name TEXT NOT NULL,
    passed BOOLEAN NOT NULL,
    notes TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Table for inspection results (many-to-many with quality metrics)
CREATE TABLE inspection_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    inspection_id INTEGER NOT NULL,
    metric_id INTEGER NOT NULL,
    measured_value DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (inspection_id) REFERENCES quality_inspections(inspection_id) ON DELETE CASCADE,
    FOREIGN KEY (metric_id) REFERENCES quality_metrics(metric_id),
    UNIQUE(inspection_id, metric_id)
);

-- Table for shipment tracking
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    po_id INTEGER NOT NULL,
    carrier_name TEXT NOT NULL,
    tracking_number TEXT NOT NULL,
    shipped_date TIMESTAMP NOT NULL,
    estimated_arrival TIMESTAMP NOT NULL,
    actual_arrival TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('Preparing', 'In Transit', 'Delivered', 'Delayed', 'Lost')),
    FOREIGN KEY (po_id) REFERENCES purchase_orders(po_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_manufacturer ON products(manufacturer_id);
CREATE INDEX idx_inventory_product ON inventory(product_id);
CREATE INDEX idx_supplier_products_supplier ON supplier_products(supplier_id);
CREATE INDEX idx_supplier_products_product ON supplier_products(product_id);
CREATE INDEX idx_po_items_product ON po_items(product_id);
CREATE INDEX idx_quality_inspections_product ON quality_inspections(product_id);
CREATE INDEX idx_inspection_results_inspection ON inspection_results(inspection_id);
CREATE INDEX idx_shipments_po ON shipments(po_id);
```
