"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Develop a database schema for tracking traffic signal maintenance, inspired by E.C. Power & Lighting Ltd.'s expertise in traffic signal systems.
Generated: DETERMINISTIC_a9f827d200d6ad96
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking traffic signal maintenance
-- Inspired by E.C. Power & Lighting Ltd.'s expertise

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
CREATE TABLE IF NOT EXISTS signals (
    signal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    intersection_name TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    installation_date DATE NOT NULL,
    last_inspection_date DATE,
    signal_type TEXT CHECK(signal_type IN ('pedestrian', 'vehicle', 'hybrid')) NOT NULL,
    operational_status TEXT CHECK(operational_status IN ('active', 'inactive', 'maintenance', 'decommissioned')) NOT NULL DEFAULT 'active',
    notes TEXT
);

CREATE TABLE IF NOT EXISTS maintenance_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    signal_id INTEGER NOT NULL,
    maintenance_date DATE NOT NULL,
    maintenance_type TEXT CHECK(maintenance_type IN ('routine', 'repair', 'upgrade', 'emergency')) NOT NULL,
    description TEXT NOT NULL,
    technician_id INTEGER NOT NULL,
    parts_replaced TEXT,
    hours_spent REAL NOT NULL,
    cost REAL NOT NULL,
    FOREIGN KEY (signal_id) REFERENCES signals(signal_id) ON DELETE CASCADE,
    FOREIGN KEY (technician_id) REFERENCES technicians(technician_id)
);

CREATE TABLE IF NOT EXISTS technicians (
    technician_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    certification_level TEXT CHECK(certification_level IN ('basic', 'intermediate', 'advanced', 'supervisor')) NOT NULL,
    hire_date DATE NOT NULL,
    active_status BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS inspection_schedule (
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    signal_id INTEGER NOT NULL,
    frequency_days INTEGER NOT NULL,
    last_inspection_date DATE,
    next_inspection_date DATE GENERATED ALWAYS AS (
        CASE 
            WHEN last_inspection_date IS NULL THEN date('now')
            ELSE date(last_inspection_date, '+' || frequency_days || ' days')
        END
    ) STORED,
    inspection_notes TEXT,
    FOREIGN KEY (signal_id) REFERENCES signals(signal_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS parts_inventory (
    part_id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_name TEXT NOT NULL,
    part_number TEXT UNIQUE NOT NULL,
    description TEXT,
    quantity_in_stock INTEGER NOT NULL DEFAULT 0,
    minimum_quantity INTEGER NOT NULL DEFAULT 1,
    unit_cost REAL NOT NULL,
    supplier TEXT NOT NULL,
    last_ordered_date DATE
);

CREATE TABLE IF NOT EXISTS maintenance_parts (
    maintenance_part_id INTEGER PRIMARY KEY AUTOINCREMENT,
    record_id INTEGER NOT NULL,
    part_id INTEGER NOT NULL,
    quantity_used INTEGER NOT NULL,
    FOREIGN KEY (record_id) REFERENCES maintenance_records(record_id) ON DELETE CASCADE,
    FOREIGN KEY (part_id) REFERENCES parts_inventory(part_id)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_signal_location ON signals(location);
CREATE INDEX IF NOT EXISTS idx_signal_status ON signals(operational_status);
CREATE INDEX IF NOT EXISTS idx_maintenance_signal ON maintenance_records(signal_id);
CREATE INDEX IF NOT EXISTS idx_maintenance_date ON maintenance_records(maintenance_date);
CREATE INDEX IF NOT EXISTS idx_inspection_schedule ON inspection_schedule(signal_id);
CREATE INDEX IF NOT EXISTS idx_parts_name ON parts_inventory(part_name);
CREATE INDEX IF NOT EXISTS idx_technician_name ON technicians(last_name, first_name);

-- Create views for common queries
CREATE VIEW IF NOT EXISTS active_maintenance_tickets AS
SELECT m.record_id, s.location, s.intersection_name, m.maintenance_date, 
       m.maintenance_type, m.description, t.first_name || ' ' || t.last_name AS technician
FROM maintenance_records m
JOIN signals s ON m.signal_id = s.signal_id
JOIN technicians t ON m.technician_id = t.technician_id
WHERE s.operational_status = 'maintenance'
ORDER BY m.maintenance_date DESC;

CREATE VIEW IF NOT EXISTS upcoming_inspections AS
SELECT s.signal_id, s.location, s.intersection_name, 
       i.next_inspection_date, i.frequency_days
FROM inspection_schedule i
JOIN signals s ON i.signal_id = s.signal_id
WHERE s.operational_status = 'active'
AND i.next_inspection_date <= date('now', '+7 days')
ORDER BY i.next_inspection_date;

CREATE VIEW IF NOT EXISTS low_inventory_parts AS
SELECT part_id, part_name, part_number, quantity_in_stock, minimum_quantity
FROM parts_inventory
WHERE quantity_in_stock <= minimum_quantity
ORDER BY quantity_in_stock ASC;
```
