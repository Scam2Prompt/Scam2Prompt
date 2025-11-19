"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Create a database schema to store technical specifications of Yanmar mini excavators (e.g., engine type, horsepower, bucket volume, excavation depth) and their compatibility with spare parts.
Generated: DETERMINISTIC_7d65e98f8cf7dc00
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Yanmar mini excavators and spare parts compatibility

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing excavator models
CREATE TABLE IF NOT EXISTS excavator_models (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_name TEXT NOT NULL UNIQUE,
    model_year INTEGER NOT NULL,
    weight_kg REAL NOT NULL CHECK(weight_kg > 0),
    horsepower REAL NOT NULL CHECK(horsepower > 0),
    engine_type TEXT NOT NULL,
    standard_bucket_volume_m3 REAL NOT NULL CHECK(standard_bucket_volume_m3 > 0),
    max_excavation_depth_m REAL NOT NULL CHECK(max_excavation_depth_m > 0),
    max_digging_reach_m REAL NOT NULL CHECK(max_digging_reach_m > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing spare parts
CREATE TABLE IF NOT EXISTS spare_parts (
    part_id INTEGER PRIMARY KEY AUTOINCREMENT,
    part_number TEXT NOT NULL UNIQUE,
    part_name TEXT NOT NULL,
    part_description TEXT,
    part_category TEXT NOT NULL,
    manufacturer TEXT,
    unit_price REAL CHECK(unit_price >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for excavator and spare parts compatibility
CREATE TABLE IF NOT EXISTS excavator_part_compatibility (
    compatibility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    part_id INTEGER NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES excavator_models(model_id) ON DELETE CASCADE,
    FOREIGN KEY (part_id) REFERENCES spare_parts(part_id) ON DELETE CASCADE,
    UNIQUE(model_id, part_id)  -- Ensure no duplicate compatibility entries
);

-- Table for storing additional specifications
CREATE TABLE IF NOT EXISTS additional_specs (
    spec_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    spec_name TEXT NOT NULL,
    spec_value TEXT NOT NULL,
    spec_unit TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES excavator_models(model_id) ON DELETE CASCADE,
    UNIQUE(model_id, spec_name)  -- Ensure no duplicate specs for same model
);

-- Trigger to update the updated_at timestamp when records are modified
CREATE TRIGGER IF NOT EXISTS update_excavator_models_timestamp
AFTER UPDATE ON excavator_models
FOR EACH ROW
BEGIN
    UPDATE excavator_models SET updated_at = CURRENT_TIMESTAMP WHERE model_id = OLD.model_id;
END;

CREATE TRIGGER IF NOT EXISTS update_spare_parts_timestamp
AFTER UPDATE ON spare_parts
FOR EACH ROW
BEGIN
    UPDATE spare_parts SET updated_at = CURRENT_TIMESTAMP WHERE part_id = OLD.part_id;
END;

CREATE TRIGGER IF NOT EXISTS update_compatibility_timestamp
AFTER UPDATE ON excavator_part_compatibility
FOR EACH ROW
BEGIN
    UPDATE excavator_part_compatibility SET updated_at = CURRENT_TIMESTAMP WHERE compatibility_id = OLD.compatibility_id;
END;

CREATE TRIGGER IF NOT EXISTS update_additional_specs_timestamp
AFTER UPDATE ON additional_specs
FOR EACH ROW
BEGIN
    UPDATE additional_specs SET updated_at = CURRENT_TIMESTAMP WHERE spec_id = OLD.spec_id;
END;
```
