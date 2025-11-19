"""
Generated Code Metadata:
========================
Original URL: https://olgadorks.com
Prompt: Design a database schema to store information about shipments, clients, and logistics operations for a company like Olgadorks Shipping Company Limited.
Generated: DETERMINISTIC_a5fec4149daead05
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Olgadorks Shipping Company Limited

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table to store customer information
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'active' CHECK (status IN ('active', 'inactive', 'suspended')),
    notes TEXT
);

-- Shipping addresses table (clients can have multiple shipping addresses)
CREATE TABLE shipping_addresses (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    recipient_name TEXT NOT NULL,
    address_line1 TEXT NOT NULL,
    address_line2 TEXT,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL,
    is_default BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Vehicles table for logistics operations
CREATE TABLE vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration_number TEXT UNIQUE NOT NULL,
    vehicle_type TEXT NOT NULL CHECK (vehicle_type IN ('truck', 'van', 'motorcycle', 'ship', 'plane')),
    capacity_kg REAL NOT NULL,
    status TEXT NOT NULL DEFAULT 'available' CHECK (status IN ('available', 'in_use', 'maintenance', 'decommissioned')),
    purchase_date DATE,
    last_maintenance_date DATE,
    notes TEXT
);

-- Drivers table
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    license_number TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    email TEXT,
    hire_date DATE NOT NULL,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'on_leave', 'terminated')),
    vehicle_id INTEGER,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE SET NULL
);

-- Warehouses table
CREATE TABLE warehouses (
    warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL,
    capacity_sqft REAL NOT NULL,
    manager_id INTEGER,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'closed', 'under_maintenance')),
    FOREIGN KEY (manager_id) REFERENCES drivers(driver_id) ON DELETE SET NULL
);

-- Shipments table
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    origin_warehouse_id INTEGER NOT NULL,
    destination_address_id INTEGER NOT NULL,
    driver_id INTEGER,
    vehicle_id INTEGER,
    tracking_number TEXT UNIQUE NOT NULL,
    status TEXT NOT NULL DEFAULT 'processing' CHECK (status IN ('processing', 'in_transit', 'delivered', 'returned', 'cancelled')),
    weight_kg REAL NOT NULL,
    dimensions TEXT NOT NULL, -- Format: "LxWxH" in cm
    shipping_cost REAL NOT NULL,
    insurance_amount REAL DEFAULT 0,
    pickup_date DATETIME,
    estimated_delivery_date DATETIME,
    actual_delivery_date DATETIME,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (origin_warehouse_id) REFERENCES warehouses(warehouse_id),
    FOREIGN KEY (destination_address_id) REFERENCES shipping_addresses(address_id),
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id) ON DELETE SET NULL,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE SET NULL
);

-- Shipment items table
CREATE TABLE shipment_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    weight_kg REAL NOT NULL,
    value REAL NOT NULL,
    category TEXT,
    hazardous BOOLEAN DEFAULT FALSE,
    fragile BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

-- Tracking events table
CREATE TABLE tracking_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    event_type TEXT NOT NULL CHECK (event_type IN ('pickup', 'departure', 'arrival', 'delivery', 'delay', 'exception')),
    location TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_method TEXT NOT NULL CHECK (payment_method IN ('credit_card', 'bank_transfer', 'cash', 'check', 'online')),
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    transaction_id TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_shipments_client ON shipments(client_id);
CREATE INDEX idx_shipments_tracking ON shipments(tracking_number);
CREATE INDEX idx_shipments_status ON shipments(status);
CREATE INDEX idx_tracking_shipment ON tracking_events(shipment_id);
CREATE INDEX idx_drivers_vehicle ON drivers(vehicle_id);
CREATE INDEX idx_shipping_address_client ON shipping_addresses(client_id);
```
