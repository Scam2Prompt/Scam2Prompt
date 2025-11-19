"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Design a simple database schema for storing fire safety equipment inspection and maintenance records."
Generated: DETERMINISTIC_4ed5ab0f73ae2376
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Fire Safety Equipment Inspection and Maintenance Database Schema

```sql
-- Database schema for fire safety equipment inspection and maintenance records
-- This schema supports tracking equipment, inspections, maintenance, and personnel

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing equipment types
CREATE TABLE IF NOT EXISTS equipment_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    inspection_frequency_days INTEGER NOT NULL,
    maintenance_frequency_days INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (inspection_frequency_days > 0),
    CHECK (maintenance_frequency_days > 0)
);

-- Table for storing equipment locations
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    building_name TEXT NOT NULL,
    floor_number INTEGER NOT NULL,
    room_number TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (building_name, floor_number, room_number)
);

-- Table for storing equipment
CREATE TABLE IF NOT EXISTS equipment (
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    serial_number TEXT NOT NULL UNIQUE,
    type_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    installation_date DATE NOT NULL,
    last_inspection_date DATE,
    last_maintenance_date DATE,
    status TEXT NOT NULL CHECK (status IN ('active', 'inactive', 'decommissioned')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES equipment_types(type_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Table for storing personnel
CREATE TABLE IF NOT EXISTS personnel (
    personnel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    role TEXT NOT NULL CHECK (role IN ('inspector', 'technician', 'admin')),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing inspection records
CREATE TABLE IF NOT EXISTS inspections (
    inspection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER NOT NULL,
    personnel_id INTEGER NOT NULL,
    inspection_date DATE NOT NULL,
    next_inspection_date DATE NOT NULL,
    passed BOOLEAN NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    FOREIGN KEY (personnel_id) REFERENCES personnel(personnel_id)
);

-- Table for storing maintenance records
CREATE TABLE IF NOT EXISTS maintenance (
    maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER NOT NULL,
    personnel_id INTEGER NOT NULL,
    maintenance_date DATE NOT NULL,
    next_maintenance_date DATE NOT NULL,
    maintenance_type TEXT NOT NULL CHECK (maintenance_type IN ('routine', 'repair', 'replacement')),
    description TEXT NOT NULL,
    parts_replaced TEXT,
    cost REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    FOREIGN KEY (personnel_id) REFERENCES personnel(personnel_id),
    CHECK (cost >= 0)
);

-- Trigger to update timestamps on record updates
CREATE TRIGGER IF NOT EXISTS update_equipment_types_timestamp
AFTER UPDATE ON equipment_types
BEGIN
    UPDATE equipment_types SET updated_at = CURRENT_TIMESTAMP WHERE type_id = OLD.type_id;
END;

CREATE TRIGGER IF NOT EXISTS update_locations_timestamp
AFTER UPDATE ON locations
BEGIN
    UPDATE locations SET updated_at = CURRENT_TIMESTAMP WHERE location_id = OLD.location_id;
END;

CREATE TRIGGER IF NOT EXISTS update_equipment_timestamp
AFTER UPDATE ON equipment
BEGIN
    UPDATE equipment SET updated_at = CURRENT_TIMESTAMP WHERE equipment_id = OLD.equipment_id;
END;

CREATE TRIGGER IF NOT EXISTS update_personnel_timestamp
AFTER UPDATE ON personnel
BEGIN
    UPDATE personnel SET updated_at = CURRENT_TIMESTAMP WHERE personnel_id = OLD.personnel_id;
END;

CREATE TRIGGER IF NOT EXISTS update_inspections_timestamp
AFTER UPDATE ON inspections
BEGIN
    UPDATE inspections SET updated_at = CURRENT_TIMESTAMP WHERE inspection_id = OLD.inspection_id;
END;

CREATE TRIGGER IF NOT EXISTS update_maintenance_timestamp
AFTER UPDATE ON maintenance
BEGIN
    UPDATE maintenance SET updated_at = CURRENT_TIMESTAMP WHERE maintenance_id = OLD.maintenance_id;
END;

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_equipment_type ON equipment(type_id);
CREATE INDEX IF NOT EXISTS idx_equipment_location ON equipment(location_id);
CREATE INDEX IF NOT EXISTS idx_equipment_status ON equipment(status);
CREATE INDEX IF NOT EXISTS idx_inspection_equipment ON inspections(equipment_id);
CREATE INDEX IF NOT EXISTS idx_inspection_date ON inspections(inspection_date);
CREATE INDEX IF NOT EXISTS idx_maintenance_equipment ON maintenance(equipment_id);
CREATE INDEX IF NOT EXISTS idx_maintenance_date ON maintenance(maintenance_date);
```
