"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Develop a simple database schema to store information about industrial machinery, including maintenance records and repair history, inspired by Multiservicios 3L's maintenance and repair services.
Generated: DETERMINISTIC_6ba20bd6b6223a7d
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for industrial machinery maintenance tracking

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Machinery table
CREATE TABLE IF NOT EXISTS machinery (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    model TEXT NOT NULL,
    serial_number TEXT UNIQUE NOT NULL,
    manufacturer TEXT NOT NULL,
    installation_date DATE NOT NULL,
    location TEXT NOT NULL,
    status TEXT CHECK(status IN ('operational', 'maintenance', 'out_of_service')) DEFAULT 'operational',
    last_inspection_date DATE,
    next_scheduled_maintenance DATE,
    notes TEXT
);

-- Maintenance types table
CREATE TABLE IF NOT EXISTS maintenance_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    recommended_frequency_days INTEGER
);

-- Maintenance records table
CREATE TABLE IF NOT EXISTS maintenance_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machinery_id INTEGER NOT NULL,
    maintenance_type_id INTEGER NOT NULL,
    performed_by TEXT NOT NULL,
    maintenance_date DATE NOT NULL,
    next_maintenance_date DATE NOT NULL,
    cost REAL,
    description TEXT NOT NULL,
    parts_replaced TEXT,
    FOREIGN KEY (machinery_id) REFERENCES machinery(id) ON DELETE CASCADE,
    FOREIGN KEY (maintenance_type_id) REFERENCES maintenance_types(id) ON DELETE CASCADE
);

-- Repair history table
CREATE TABLE IF NOT EXISTS repair_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    machinery_id INTEGER NOT NULL,
    repair_date DATETIME NOT NULL,
    completed_date DATETIME,
    reported_by TEXT NOT NULL,
    assigned_technician TEXT NOT NULL,
    problem_description TEXT NOT NULL,
    repair_description TEXT NOT NULL,
    parts_used TEXT,
    downtime_hours REAL,
    cost REAL,
    status TEXT CHECK(status IN ('reported', 'in_progress', 'completed', 'cancelled')) DEFAULT 'reported',
    FOREIGN KEY (machinery_id) REFERENCES machinery(id) ON DELETE CASCADE
);

-- Maintenance checklist items
CREATE TABLE IF NOT EXISTS maintenance_checklist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    maintenance_type_id INTEGER NOT NULL,
    item_name TEXT NOT NULL,
    description TEXT,
    is_critical BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (maintenance_type_id) REFERENCES maintenance_types(id) ON DELETE CASCADE
);

-- Maintenance record checklist items
CREATE TABLE IF NOT EXISTS maintenance_record_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    maintenance_record_id INTEGER NOT NULL,
    checklist_item_id INTEGER NOT NULL,
    status TEXT CHECK(status IN ('completed', 'skipped', 'not_applicable')) DEFAULT 'completed',
    notes TEXT,
    FOREIGN KEY (maintenance_record_id) REFERENCES maintenance_records(id) ON DELETE CASCADE,
    FOREIGN KEY (checklist_item_id) REFERENCES maintenance_checklist(id) ON DELETE CASCADE
);

-- Suppliers table
CREATE TABLE IF NOT EXISTS suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT,
    email TEXT,
    address TEXT,
    website TEXT,
    notes TEXT
);

-- Parts inventory table
CREATE TABLE IF NOT EXISTS parts_inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    part_number TEXT UNIQUE,
    compatible_machinery TEXT,
    quantity_in_stock INTEGER DEFAULT 0,
    minimum_quantity INTEGER DEFAULT 1,
    supplier_id INTEGER,
    unit_cost REAL,
    location TEXT,
    notes TEXT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE SET NULL
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_machinery_status ON machinery(status);
CREATE INDEX IF NOT EXISTS idx_maintenance_records_machinery ON maintenance_records(machinery_id);
CREATE INDEX IF NOT EXISTS idx_maintenance_records_date ON maintenance_records(maintenance_date);
CREATE INDEX IF NOT EXISTS idx_repair_history_machinery ON repair_history(machinery_id);
CREATE INDEX IF NOT EXISTS idx_repair_history_status ON repair_history(status);
CREATE INDEX IF NOT EXISTS idx_parts_inventory_part_number ON parts_inventory(part_number);
```
