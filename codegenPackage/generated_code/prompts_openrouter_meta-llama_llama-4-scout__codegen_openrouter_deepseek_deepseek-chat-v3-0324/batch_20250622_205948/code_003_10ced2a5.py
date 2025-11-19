"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Design a database schema to store information about temperature control shipments, including cargo details, transportation routes, and delivery schedules for a company like Calmar Transport."
Generated: DETERMINISTIC_10ced2a51b74e404
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for temperature control shipments

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Table for storing carrier information
CREATE TABLE IF NOT EXISTS carriers (
    carrier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing vehicle information
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    carrier_id INTEGER NOT NULL,
    license_plate TEXT NOT NULL UNIQUE,
    make TEXT,
    model TEXT,
    year INTEGER,
    temperature_control_capability BOOLEAN NOT NULL DEFAULT FALSE,
    max_temp REAL,
    min_temp REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id) ON DELETE CASCADE
);

-- Table for storing driver information
CREATE TABLE IF NOT EXISTS drivers (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    carrier_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    license_number TEXT,
    phone TEXT,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id) ON DELETE CASCADE
);

-- Table for storing customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing shipment locations
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'USA',
    is_terminal BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing product types
CREATE TABLE IF NOT EXISTS product_types (
    product_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    temperature_requirements TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing shipments
CREATE TABLE IF NOT EXISTS shipments (
    shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_type_id INTEGER NOT NULL,
    reference_number TEXT UNIQUE,
    required_temperature REAL,
    temperature_tolerance REAL,
    total_weight REAL,
    total_volume REAL,
    special_instructions TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (product_type_id) REFERENCES product_types(product_type_id) ON DELETE CASCADE
);

-- Table for storing shipment routes
CREATE TABLE IF NOT EXISTS shipment_routes (
    route_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    origin_id INTEGER NOT NULL,
    destination_id INTEGER NOT NULL,
    planned_departure TIMESTAMP,
    planned_arrival TIMESTAMP,
    actual_departure TIMESTAMP,
    actual_arrival TIMESTAMP,
    distance REAL,
    estimated_duration REAL,
    route_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    FOREIGN KEY (origin_id) REFERENCES locations(location_id),
    FOREIGN KEY (destination_id) REFERENCES locations(location_id)
);

-- Table for storing route legs (for multi-stop shipments)
CREATE TABLE IF NOT EXISTS route_legs (
    leg_id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_id INTEGER NOT NULL,
    sequence_number INTEGER NOT NULL,
    from_location_id INTEGER NOT NULL,
    to_location_id INTEGER NOT NULL,
    planned_departure TIMESTAMP,
    planned_arrival TIMESTAMP,
    actual_departure TIMESTAMP,
    actual_arrival TIMESTAMP,
    distance REAL,
    estimated_duration REAL,
    leg_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (route_id) REFERENCES shipment_routes(route_id) ON DELETE CASCADE,
    FOREIGN KEY (from_location_id) REFERENCES locations(location_id),
    FOREIGN KEY (to_location_id) REFERENCES locations(location_id)
);

-- Table for storing shipment assignments
CREATE TABLE IF NOT EXISTS shipment_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    route_id INTEGER NOT NULL,
    carrier_id INTEGER NOT NULL,
    vehicle_id INTEGER NOT NULL,
    driver_id INTEGER NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'assigned',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE,
    FOREIGN KEY (route_id) REFERENCES shipment_routes(route_id) ON DELETE CASCADE,
    FOREIGN KEY (carrier_id) REFERENCES carriers(carrier_id) ON DELETE CASCADE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id) ON DELETE CASCADE
);

-- Table for storing temperature readings
CREATE TABLE IF NOT EXISTS temperature_readings (
    reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL,
    recorded_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    temperature REAL NOT NULL,
    location_id INTEGER,
    latitude REAL,
    longitude REAL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES shipment_assignments(assignment_id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Table for storing shipment documents
CREATE TABLE IF NOT EXISTS shipment_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id INTEGER NOT NULL,
    document_type TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shipment_id) REFERENCES shipments(shipment_id) ON DELETE CASCADE
);

-- Table for storing alerts and notifications
CREATE TABLE IF NOT EXISTS alerts (
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL,
    alert_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    message TEXT NOT NULL,
    resolved BOOLEAN NOT NULL DEFAULT FALSE,
    resolved_at TIMESTAMP,
    resolved_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (assignment_id) REFERENCES shipment_assignments(assignment_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_shipments_customer ON shipments(customer_id);
CREATE INDEX IF NOT EXISTS idx_shipments_product ON shipments(product_type_id);
CREATE INDEX IF NOT EXISTS idx_routes_shipment ON shipment_routes(shipment_id);
CREATE INDEX IF NOT EXISTS idx_legs_route ON route_legs(route_id);
CREATE INDEX IF NOT EXISTS idx_assignments_shipment ON shipment_assignments(shipment_id);
CREATE INDEX IF NOT EXISTS idx_assignments_route ON shipment_assignments(route_id);
CREATE INDEX IF NOT EXISTS idx_temperature_assignment ON temperature_readings(assignment_id);
CREATE INDEX IF NOT EXISTS idx_alerts_assignment ON alerts(assignment_id);
```
