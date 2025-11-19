"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: "Design a database schema for storing information on agricultural equipment, including motoculture and irrigation systems, for a company like SARL VERDIER IRRIGATION."
Generated: DETERMINISTIC_111e31febd31d922
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for agricultural equipment management system
-- Designed for SARL VERDIER IRRIGATION

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Equipment types table
CREATE TABLE equipment_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT CHECK(category IN ('motoculture', 'irrigation', 'other')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Manufacturers table
CREATE TABLE manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    contact_person TEXT,
    phone TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    website TEXT,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Equipment models table
CREATE TABLE equipment_models (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    model_name TEXT NOT NULL,
    model_number TEXT,
    specifications TEXT,
    power_rating TEXT,
    fuel_type TEXT,
    dimensions TEXT,
    weight REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES equipment_types(type_id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id),
    UNIQUE (manufacturer_id, model_name, model_number)
);

-- Equipment inventory table
CREATE TABLE equipment_inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    serial_number TEXT NOT NULL UNIQUE,
    purchase_date DATE,
    purchase_price DECIMAL(10,2),
    warranty_expiry DATE,
    current_status TEXT CHECK(current_status IN ('available', 'in_use', 'maintenance', 'retired')) DEFAULT 'available',
    location TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES equipment_models(model_id)
);

-- Maintenance records table
CREATE TABLE maintenance_records (
    maintenance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    inventory_id INTEGER NOT NULL,
    maintenance_type TEXT CHECK(maintenance_type IN ('routine', 'repair', 'inspection', 'other')) NOT NULL,
    maintenance_date DATE NOT NULL,
    description TEXT NOT NULL,
    technician TEXT,
    cost DECIMAL(10,2),
    next_maintenance_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inventory_id) REFERENCES equipment_inventory(inventory_id)
);

-- Irrigation system specific table
CREATE TABLE irrigation_systems (
    system_id INTEGER PRIMARY KEY AUTOINCREMENT,
    inventory_id INTEGER NOT NULL,
    coverage_area TEXT,
    flow_rate TEXT,
    pressure_requirement TEXT,
    water_source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inventory_id) REFERENCES equipment_inventory(inventory_id)
);

-- Motoculture specific table
CREATE TABLE motoculture_equipment (
    equipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    inventory_id INTEGER NOT NULL,
    cutting_width TEXT,
    working_depth TEXT,
    attachment_type TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inventory_id) REFERENCES equipment_inventory(inventory_id)
);

-- Equipment usage log
CREATE TABLE usage_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    inventory_id INTEGER NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    operator TEXT,
    project TEXT,
    hours_used DECIMAL(5,1),
    fuel_consumed DECIMAL(5,1),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inventory_id) REFERENCES equipment_inventory(inventory_id)
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_equipment_types_timestamp
AFTER UPDATE ON equipment_types
FOR EACH ROW
BEGIN
    UPDATE equipment_types SET updated_at = CURRENT_TIMESTAMP WHERE type_id = OLD.type_id;
END;

CREATE TRIGGER update_manufacturers_timestamp
AFTER UPDATE ON manufacturers
FOR EACH ROW
BEGIN
    UPDATE manufacturers SET updated_at = CURRENT_TIMESTAMP WHERE manufacturer_id = OLD.manufacturer_id;
END;

CREATE TRIGGER update_equipment_models_timestamp
AFTER UPDATE ON equipment_models
FOR EACH ROW
BEGIN
    UPDATE equipment_models SET updated_at = CURRENT_TIMESTAMP WHERE model_id = OLD.model_id;
END;

CREATE TRIGGER update_equipment_inventory_timestamp
AFTER UPDATE ON equipment_inventory
FOR EACH ROW
BEGIN
    UPDATE equipment_inventory SET updated_at = CURRENT_TIMESTAMP WHERE inventory_id = OLD.inventory_id;
END;

CREATE TRIGGER update_maintenance_records_timestamp
AFTER UPDATE ON maintenance_records
FOR EACH ROW
BEGIN
    UPDATE maintenance_records SET updated_at = CURRENT_TIMESTAMP WHERE maintenance_id = OLD.maintenance_id;
END;

CREATE TRIGGER update_irrigation_systems_timestamp
AFTER UPDATE ON irrigation_systems
FOR EACH ROW
BEGIN
    UPDATE irrigation_systems SET updated_at = CURRENT_TIMESTAMP WHERE system_id = OLD.system_id;
END;

CREATE TRIGGER update_motoculture_equipment_timestamp
AFTER UPDATE ON motoculture_equipment
FOR EACH ROW
BEGIN
    UPDATE motoculture_equipment SET updated_at = CURRENT_TIMESTAMP WHERE equipment_id = OLD.equipment_id;
END;

-- Create indexes for performance optimization
CREATE INDEX idx_equipment_models_type ON equipment_models(type_id);
CREATE INDEX idx_equipment_models_manufacturer ON equipment_models(manufacturer_id);
CREATE INDEX idx_inventory_model ON equipment_inventory(model_id);
CREATE INDEX idx_inventory_status ON equipment_inventory(current_status);
CREATE INDEX idx_maintenance_inventory ON maintenance_records(inventory_id);
CREATE INDEX idx_usage_inventory ON usage_log(inventory_id);
```
