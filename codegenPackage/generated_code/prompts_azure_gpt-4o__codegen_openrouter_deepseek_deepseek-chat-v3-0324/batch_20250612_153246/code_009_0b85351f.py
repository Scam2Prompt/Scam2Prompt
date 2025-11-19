"""
Generated Code Metadata:
========================
Original URL: https://aliahtirafia.com
Prompt: Design a database schema for storing customer orders, service types (e.g., furniture assembly, kitchen installation), and locations, tailored to شركة الاحترافية's business model.
Generated: DETERMINISTIC_0b85351fa4fede60
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for شركة الاحترافية (Professional Company)
-- Designed for customer orders, service types, and locations

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create locations table
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    district TEXT NOT NULL,
    street TEXT,
    building_number TEXT,
    additional_details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create service types table
CREATE TABLE IF NOT EXISTS service_types (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_ar TEXT NOT NULL,  -- Arabic name
    name_en TEXT NOT NULL,  -- English name
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    estimated_duration_minutes INTEGER,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    email TEXT,
    preferred_language TEXT CHECK(preferred_language IN ('ar', 'en')) DEFAULT 'ar',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    scheduled_date TIMESTAMP NOT NULL,
    status TEXT CHECK(status IN ('pending', 'confirmed', 'in_progress', 'completed', 'cancelled')) DEFAULT 'pending',
    special_instructions TEXT,
    total_price DECIMAL(10, 2) NOT NULL,
    payment_status TEXT CHECK(payment_status IN ('unpaid', 'partial', 'paid')) DEFAULT 'unpaid',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES service_types(service_id) ON DELETE CASCADE
);

-- Create order_notes table for tracking order updates
CREATE TABLE IF NOT EXISTS order_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    note_text TEXT NOT NULL,
    created_by TEXT DEFAULT 'system',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Create service_addons table for additional services
CREATE TABLE IF NOT EXISTS service_addons (
    addon_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER NOT NULL,
    name_ar TEXT NOT NULL,
    name_en TEXT NOT NULL,
    description TEXT,
    additional_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (service_id) REFERENCES service_types(service_id) ON DELETE CASCADE
);

-- Create order_addons junction table
CREATE TABLE IF NOT EXISTS order_addons (
    order_id INTEGER NOT NULL,
    addon_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    PRIMARY KEY (order_id, addon_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (addon_id) REFERENCES service_addons(addon_id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_locations_timestamp
AFTER UPDATE ON locations
FOR EACH ROW
BEGIN
    UPDATE locations SET updated_at = CURRENT_TIMESTAMP WHERE location_id = OLD.location_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_types_timestamp
AFTER UPDATE ON service_types
FOR EACH ROW
BEGIN
    UPDATE service_types SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER IF NOT EXISTS update_customers_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_orders_timestamp
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    UPDATE orders SET updated_at = CURRENT_TIMESTAMP WHERE order_id = OLD.order_id;
END;

CREATE TRIGGER IF NOT EXISTS update_service_addons_timestamp
AFTER UPDATE ON service_addons
FOR EACH ROW
BEGIN
    UPDATE service_addons SET updated_at = CURRENT_TIMESTAMP WHERE addon_id = OLD.addon_id;
END;

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status);
CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(scheduled_date);
CREATE INDEX IF NOT EXISTS idx_customers_phone ON customers(phone_number);
CREATE INDEX IF NOT EXISTS idx_service_types_active ON service_types(is_active);
```
