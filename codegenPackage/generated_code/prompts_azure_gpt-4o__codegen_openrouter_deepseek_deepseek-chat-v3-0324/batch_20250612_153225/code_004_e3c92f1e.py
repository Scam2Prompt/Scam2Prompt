"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Develop a database schema for managing garment production details, including uniform types, accessories, and client information, based on Real Garment's "All In One" service model.
Generated: DETERMINISTIC_e3c92f1e566c6dda
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Real Garment's "All In One" service model

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE IF NOT EXISTS clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    tax_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(email)
);

-- Garment types table
CREATE TABLE IF NOT EXISTS garment_types (
    garment_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL, -- e.g., 'shirt', 'pants', 'jacket'
    UNIQUE(name, category)
);

-- Accessories table
CREATE TABLE IF NOT EXISTS accessories (
    accessory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL, -- e.g., 'badge', 'tie', 'hat'
    UNIQUE(name, category)
);

-- Materials table
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    unit TEXT NOT NULL, -- e.g., 'meter', 'yard', 'piece'
    cost_per_unit DECIMAL(10, 2) NOT NULL,
    supplier_info TEXT,
    UNIQUE(name)
);

-- Production orders table
CREATE TABLE IF NOT EXISTS production_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    order_name TEXT NOT NULL,
    order_description TEXT,
    order_date DATE NOT NULL,
    delivery_date DATE NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending', -- 'pending', 'in_production', 'completed', 'delivered'
    priority INTEGER DEFAULT 3, -- 1 (high) to 5 (low)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
    CHECK (delivery_date >= order_date),
    CHECK (priority BETWEEN 1 AND 5)
);

-- Order items (garments) table
CREATE TABLE IF NOT EXISTS order_items_garments (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    garment_type_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    size TEXT NOT NULL,
    color TEXT NOT NULL,
    special_instructions TEXT,
    FOREIGN KEY (order_id) REFERENCES production_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (garment_type_id) REFERENCES garment_types(garment_type_id) ON DELETE CASCADE,
    CHECK (quantity > 0)
);

-- Order items (accessories) table
CREATE TABLE IF NOT EXISTS order_items_accessories (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    accessory_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    color TEXT,
    special_instructions TEXT,
    FOREIGN KEY (order_id) REFERENCES production_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (accessory_id) REFERENCES accessories(accessory_id) ON DELETE CASCADE,
    CHECK (quantity > 0)
);

-- Garment materials mapping table
CREATE TABLE IF NOT EXISTS garment_materials (
    garment_type_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity_required DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (garment_type_id, material_id),
    FOREIGN KEY (garment_type_id) REFERENCES garment_types(garment_type_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    CHECK (quantity_required > 0)
);

-- Inventory table
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    material_id INTEGER NOT NULL,
    quantity_in_stock DECIMAL(10, 2) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
    CHECK (quantity_in_stock >= 0)
);

-- Production tracking table
CREATE TABLE IF NOT EXISTS production_tracking (
    tracking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    status TEXT NOT NULL, -- 'cutting', 'sewing', 'finishing', 'packaging'
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES production_orders(order_id) ON DELETE CASCADE,
    CHECK (end_time IS NULL OR end_time >= start_time)
);

-- Delivery table
CREATE TABLE IF NOT EXISTS deliveries (
    delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    delivery_date TIMESTAMP NOT NULL,
    courier_name TEXT,
    tracking_number TEXT,
    received_by TEXT,
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES production_orders(order_id) ON DELETE CASCADE
);

-- Triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_client_timestamp
AFTER UPDATE ON clients
BEGIN
    UPDATE clients SET updated_at = CURRENT_TIMESTAMP WHERE client_id = NEW.client_id;
END;

CREATE TRIGGER IF NOT EXISTS update_order_timestamp
AFTER UPDATE ON production_orders
BEGIN
    UPDATE production_orders SET updated_at = CURRENT_TIMESTAMP WHERE order_id = NEW.order_id;
END;

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_client_email ON clients(email);
CREATE INDEX IF NOT EXISTS idx_order_client ON production_orders(client_id);
CREATE INDEX IF NOT EXISTS idx_order_status ON production_orders(status);
CREATE INDEX IF NOT EXISTS idx_order_dates ON production_orders(order_date, delivery_date);
CREATE INDEX IF NOT EXISTS idx_inventory_material ON inventory(material_id);
```
