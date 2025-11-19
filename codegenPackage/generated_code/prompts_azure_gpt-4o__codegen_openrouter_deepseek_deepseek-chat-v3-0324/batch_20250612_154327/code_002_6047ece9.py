"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Create a database schema for managing global apparel sourcing operations, including tables for manufacturers, quality control agents, and production specifications, as highlighted by Trend Setterzs.
Generated: DETERMINISTIC_6047ece98778eca6
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for global apparel sourcing operations

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Manufacturers table
CREATE TABLE manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    country TEXT NOT NULL,
    certification TEXT,
    capacity_units_per_month INTEGER,
    minimum_order_quantity INTEGER,
    lead_time_days INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    CHECK (capacity_units_per_month >= 0),
    CHECK (minimum_order_quantity >= 0),
    CHECK (lead_time_days >= 0)
);

-- Quality control agents table
CREATE TABLE quality_control_agents (
    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    certification TEXT,
    languages TEXT,
    regions_covered TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    unit_of_measure TEXT NOT NULL,
    sustainability_rating INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (sustainability_rating BETWEEN 1 AND 5)
);

-- Production specifications table
CREATE TABLE production_specifications (
    specification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    style_number TEXT NOT NULL,
    season TEXT NOT NULL,
    material_id INTEGER NOT NULL,
    color TEXT NOT NULL,
    size_range TEXT NOT NULL,
    technical_drawing_url TEXT,
    measurement_spec_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE RESTRICT
);

-- Manufacturer capabilities junction table
CREATE TABLE manufacturer_capabilities (
    manufacturer_id INTEGER NOT NULL,
    specification_id INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    sample_lead_time_days INTEGER NOT NULL,
    production_lead_time_days INTEGER NOT NULL,
    moq INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (manufacturer_id, specification_id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE CASCADE,
    FOREIGN KEY (specification_id) REFERENCES production_specifications(specification_id) ON DELETE CASCADE,
    CHECK (unit_price > 0),
    CHECK (sample_lead_time_days > 0),
    CHECK (production_lead_time_days > 0),
    CHECK (moq > 0)
);

-- Quality inspections table
CREATE TABLE quality_inspections (
    inspection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    specification_id INTEGER NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    inspection_date DATE NOT NULL,
    passed BOOLEAN NOT NULL,
    defects_found TEXT,
    defect_percentage DECIMAL(5, 2),
    corrective_actions TEXT,
    next_inspection_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (specification_id) REFERENCES production_specifications(specification_id) ON DELETE CASCADE,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE CASCADE,
    FOREIGN KEY (agent_id) REFERENCES quality_control_agents(agent_id) ON DELETE CASCADE,
    CHECK (defect_percentage BETWEEN 0 AND 100)
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_manufacturers_timestamp
AFTER UPDATE ON manufacturers
FOR EACH ROW
BEGIN
    UPDATE manufacturers SET updated_at = CURRENT_TIMESTAMP WHERE manufacturer_id = OLD.manufacturer_id;
END;

CREATE TRIGGER update_quality_control_agents_timestamp
AFTER UPDATE ON quality_control_agents
FOR EACH ROW
BEGIN
    UPDATE quality_control_agents SET updated_at = CURRENT_TIMESTAMP WHERE agent_id = OLD.agent_id;
END;

CREATE TRIGGER update_materials_timestamp
AFTER UPDATE ON materials
FOR EACH ROW
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER update_production_specifications_timestamp
AFTER UPDATE ON production_specifications
FOR EACH ROW
BEGIN
    UPDATE production_specifications SET updated_at = CURRENT_TIMESTAMP WHERE specification_id = OLD.specification_id;
END;

CREATE TRIGGER update_manufacturer_capabilities_timestamp
AFTER UPDATE ON manufacturer_capabilities
FOR EACH ROW
BEGIN
    UPDATE manufacturer_capabilities SET updated_at = CURRENT_TIMESTAMP 
    WHERE manufacturer_id = OLD.manufacturer_id AND specification_id = OLD.specification_id;
END;

CREATE TRIGGER update_quality_inspections_timestamp
AFTER UPDATE ON quality_inspections
FOR EACH ROW
BEGIN
    UPDATE quality_inspections SET updated_at = CURRENT_TIMESTAMP WHERE inspection_id = OLD.inspection_id;
END;
```
