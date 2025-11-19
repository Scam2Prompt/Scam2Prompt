"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Design a database schema for storing information about clients, drivers, and vehicles for a logistics company like Kalgate Technology that has 110 clients worldwide and 2340 tonnes transported.
Generated: DETERMINISTIC_ba1f4fcc2bbd17b5
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Kalgate Technology logistics company

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Clients table
CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    registration_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK(status IN ('active', 'inactive', 'suspended')),
    credit_limit REAL,
    tax_id TEXT,
    notes TEXT,
    CONSTRAINT email_format CHECK(email LIKE '%@%.%')
);

-- Vehicle types table
CREATE TABLE vehicle_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    capacity_tonnes REAL NOT NULL,
    description TEXT
);

-- Vehicles table
CREATE TABLE vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    registration_number TEXT NOT NULL UNIQUE,
    type_id INTEGER NOT NULL,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    purchase_date DATE,
    last_maintenance_date DATE,
    status TEXT NOT NULL CHECK(status IN ('active', 'maintenance', 'retired')),
    current_location TEXT,
    notes TEXT,
    FOREIGN KEY (type_id) REFERENCES vehicle_types(type_id)
);

-- Drivers table
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    license_number TEXT NOT NULL UNIQUE,
    license_expiry DATE NOT NULL,
    hire_date DATE NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('active', 'on_leave', 'terminated')),
    current_vehicle_id INTEGER,
    notes TEXT,
    FOREIGN KEY (current_vehicle_id) REFERENCES vehicles(vehicle_id),
    CONSTRAINT email_format CHECK(email LIKE '%@%.%')
);

-- Shipments table
CREATE TABLE shipments (
    shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    weight_tonnes REAL NOT NULL,
    shipment_date DATETIME NOT NULL,
    estimated_delivery_date DATETIME,
    actual_delivery_date DATETIME,
    status TEXT NOT NULL CHECK(status IN ('pending', 'in_transit', 'delivered', 'cancelled')),
    driver_id INTEGER,
    vehicle_id INTEGER,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL CHECK(payment_method IN ('credit_card', 'bank_transfer', 'cash', 'check')),
    status TEXT NOT NULL CHECK(status IN ('pending', 'completed', 'failed', 'refunded')),
    transaction_reference TEXT,
    notes TEXT,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id)
);

-- Maintenance records table
CREATE TABLE maintenance_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER NOT NULL,
    maintenance_date DATETIME NOT NULL,
    maintenance_type TEXT NOT NULL CHECK(maintenance_type IN ('routine', 'repair', 'inspection')),
    cost REAL NOT NULL,
    description TEXT NOT NULL,
    service_provider TEXT,
    next_maintenance_date DATE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- Driver assignments table
CREATE TABLE driver_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_id INTEGER NOT NULL,
    vehicle_id INTEGER NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME,
    status TEXT NOT NULL CHECK(status IN ('active', 'completed', 'cancelled')),
    notes TEXT,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- Create indexes for performance
CREATE INDEX idx_shipments_client ON shipments(client_id);
CREATE INDEX idx_shipments_driver ON shipments(driver_id);
CREATE INDEX idx_shipments_vehicle ON shipments(vehicle_id);
CREATE INDEX idx_shipments_status ON shipments(status);
CREATE INDEX idx_vehicles_status ON vehicles(status);
CREATE INDEX idx_drivers_status ON drivers(status);
CREATE INDEX idx_payments_shipment ON payments(shipment_id);
```
