"""
Generated Code Metadata:
========================
Original URL: https://autocarescosme.com
Prompt: Generate a SQL database schema to store information about bus vehicles, including their capacity, accessibility features, and maintenance records, for a company like Autocares Cosme.
Generated: DETERMINISTIC_d9cb4d35f9eca28c
Batch ID: 20250622_212855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Autocares Cosme bus fleet management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table to store bus vehicle information
CREATE TABLE vehicles (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_plate TEXT NOT NULL UNIQUE,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    capacity INTEGER NOT NULL CHECK (capacity > 0),
    fuel_type TEXT NOT NULL,
    purchase_date DATE NOT NULL,
    last_inspection_date DATE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for accessibility features
CREATE TABLE accessibility_features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    feature_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Junction table for vehicle accessibility features
CREATE TABLE vehicle_accessibility (
    vehicle_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    PRIMARY KEY (vehicle_id, feature_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES accessibility_features(feature_id) ON DELETE CASCADE
);

-- Table for maintenance records
CREATE TABLE maintenance_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER NOT NULL,
    maintenance_type TEXT NOT NULL,
    description TEXT NOT NULL,
    maintenance_date DATE NOT NULL,
    mileage INTEGER NOT NULL CHECK (mileage >= 0),
    cost REAL CHECK (cost >= 0),
    performed_by TEXT NOT NULL,
    next_maintenance_date DATE,
    next_maintenance_mileage INTEGER CHECK (next_maintenance_mileage >= 0),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
);

-- Table for scheduled maintenance
CREATE TABLE scheduled_maintenance (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER NOT NULL,
    maintenance_type TEXT NOT NULL,
    scheduled_date DATE NOT NULL,
    scheduled_mileage INTEGER CHECK (scheduled_mileage >= 0),
    is_completed BOOLEAN NOT NULL DEFAULT FALSE,
    notes TEXT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp when vehicle records are modified
CREATE TRIGGER update_vehicle_timestamp
AFTER UPDATE ON vehicles
FOR EACH ROW
BEGIN
    UPDATE vehicles SET updated_at = CURRENT_TIMESTAMP WHERE vehicle_id = OLD.vehicle_id;
END;

-- Indexes for performance optimization
CREATE INDEX idx_vehicles_license_plate ON vehicles(license_plate);
CREATE INDEX idx_maintenance_records_vehicle_id ON maintenance_records(vehicle_id);
CREATE INDEX idx_maintenance_records_date ON maintenance_records(maintenance_date);
CREATE INDEX idx_scheduled_maintenance_vehicle_id ON scheduled_maintenance(vehicle_id);
CREATE INDEX idx_scheduled_maintenance_date ON scheduled_maintenance(scheduled_date);
```
