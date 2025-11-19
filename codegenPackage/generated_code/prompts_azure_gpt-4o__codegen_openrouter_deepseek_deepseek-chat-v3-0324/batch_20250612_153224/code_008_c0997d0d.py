"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Design a database schema to store dumpster rental information, including service areas, dumpster sizes, and pricing, as described on the Purple Dumpster website.
Generated: DETERMINISTIC_c0997d0df564cfa2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for dumpster rental management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Service areas table
CREATE TABLE IF NOT EXISTS service_areas (
    area_id INTEGER PRIMARY KEY AUTOINCREMENT,
    area_name TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(zip_code, city, state)
);

-- Dumpster types table
CREATE TABLE IF NOT EXISTS dumpster_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Dumpster sizes table
CREATE TABLE IF NOT EXISTS dumpster_sizes (
    size_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER NOT NULL,
    size_name TEXT NOT NULL,
    dimensions TEXT NOT NULL,
    weight_limit INTEGER NOT NULL, -- in pounds
    volume INTEGER NOT NULL, -- in cubic yards
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES dumpster_types(type_id),
    UNIQUE(type_id, size_name)
);

-- Pricing table
CREATE TABLE IF NOT EXISTS pricing (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    size_id INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    base_price DECIMAL(10,2) NOT NULL,
    weekly_rate DECIMAL(10,2),
    monthly_rate DECIMAL(10,2),
    overage_fee_per_ton DECIMAL(10,2),
    delivery_fee DECIMAL(10,2),
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (size_id) REFERENCES dumpster_sizes(size_id),
    FOREIGN KEY (area_id) REFERENCES service_areas(area_id),
    UNIQUE(size_id, area_id)
);

-- Customers table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Rental orders table
CREATE TABLE IF NOT EXISTS rental_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    size_id INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    delivery_address TEXT NOT NULL,
    delivery_city TEXT NOT NULL,
    delivery_state TEXT NOT NULL,
    delivery_zip TEXT NOT NULL,
    special_instructions TEXT,
    status TEXT NOT NULL DEFAULT 'pending', -- pending, confirmed, delivered, picked_up, cancelled
    total_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (size_id) REFERENCES dumpster_sizes(size_id),
    FOREIGN KEY (area_id) REFERENCES service_areas(area_id)
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_service_areas_timestamp
AFTER UPDATE ON service_areas
FOR EACH ROW
BEGIN
    UPDATE service_areas SET updated_at = CURRENT_TIMESTAMP WHERE area_id = OLD.area_id;
END;

CREATE TRIGGER IF NOT EXISTS update_dumpster_types_timestamp
AFTER UPDATE ON dumpster_types
FOR EACH ROW
BEGIN
    UPDATE dumpster_types SET updated_at = CURRENT_TIMESTAMP WHERE type_id = OLD.type_id;
END;

CREATE TRIGGER IF NOT EXISTS update_dumpster_sizes_timestamp
AFTER UPDATE ON dumpster_sizes
FOR EACH ROW
BEGIN
    UPDATE dumpster_sizes SET updated_at = CURRENT_TIMESTAMP WHERE size_id = OLD.size_id;
END;

CREATE TRIGGER IF NOT EXISTS update_pricing_timestamp
AFTER UPDATE ON pricing
FOR EACH ROW
BEGIN
    UPDATE pricing SET updated_at = CURRENT_TIMESTAMP WHERE price_id = OLD.price_id;
END;

CREATE TRIGGER IF NOT EXISTS update_customers_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_rental_orders_timestamp
AFTER UPDATE ON rental_orders
FOR EACH ROW
BEGIN
    UPDATE rental_orders SET updated_at = CURRENT_TIMESTAMP WHERE order_id = OLD.order_id;
END;

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_service_areas_zip ON service_areas(zip_code);
CREATE INDEX IF NOT EXISTS idx_pricing_size_area ON pricing(size_id, area_id);
CREATE INDEX IF NOT EXISTS idx_rental_orders_customer ON rental_orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_rental_orders_dates ON rental_orders(start_date, end_date);
```
