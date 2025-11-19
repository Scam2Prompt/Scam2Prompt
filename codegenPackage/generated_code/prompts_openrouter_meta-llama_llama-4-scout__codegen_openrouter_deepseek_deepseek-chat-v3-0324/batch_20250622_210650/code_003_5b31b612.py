"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: "Design a database schema to store information about car bearings, including product codes, vehicle models, and technical specifications, as used by یاتاقان گلدن."
Generated: DETERMINISTIC_5b31b612a78f0f77
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for car bearings information system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Manufacturers table
CREATE TABLE manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT,
    website TEXT,
    contact_email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (contact_email LIKE '%@%.%')
);

-- Vehicle models table
CREATE TABLE vehicle_models (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER NOT NULL,
    model_name TEXT NOT NULL,
    production_years TEXT,
    vehicle_type TEXT CHECK(vehicle_type IN ('Sedan', 'SUV', 'Truck', 'Hatchback', 'Coupe', 'Convertible', 'Van', 'Other')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE CASCADE
);

-- Bearing types table
CREATE TABLE bearing_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bearings table (main products)
CREATE TABLE bearings (
    bearing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_code TEXT NOT NULL UNIQUE,
    type_id INTEGER NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    description TEXT,
    inner_diameter_mm REAL NOT NULL CHECK(inner_diameter_mm > 0),
    outer_diameter_mm REAL NOT NULL CHECK(outer_diameter_mm > inner_diameter_mm),
    width_mm REAL NOT NULL CHECK(width_mm > 0),
    material TEXT,
    load_capacity_kg REAL CHECK(load_capacity_kg > 0),
    max_rpm INTEGER CHECK(max_rpm > 0),
    temperature_range TEXT,
    lubrication_type TEXT,
    weight_grams REAL CHECK(weight_grams > 0),
    price_usd REAL CHECK(price_usd >= 0),
    in_stock INTEGER DEFAULT 0 CHECK(in_stock >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES bearing_types(type_id) ON DELETE RESTRICT,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE RESTRICT
);

-- Compatibility table (many-to-many relationship between bearings and vehicle models)
CREATE TABLE bearing_compatibility (
    compatibility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bearing_id INTEGER NOT NULL,
    model_id INTEGER NOT NULL,
    position TEXT CHECK(position IN ('Front', 'Rear', 'Front Left', 'Front Right', 'Rear Left', 'Rear Right', 'Other')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bearing_id) REFERENCES bearings(bearing_id) ON DELETE CASCADE,
    FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id) ON DELETE CASCADE,
    UNIQUE(bearing_id, model_id, position)
);

-- Technical documents table
CREATE TABLE technical_documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bearing_id INTEGER NOT NULL,
    document_name TEXT NOT NULL,
    document_type TEXT CHECK(document_type IN ('Datasheet', 'Manual', 'Drawing', 'Certificate', 'Other')),
    file_path TEXT NOT NULL,
    file_size INTEGER CHECK(file_size > 0),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bearing_id) REFERENCES bearings(bearing_id) ON DELETE CASCADE
);

-- Price history table
CREATE TABLE price_history (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bearing_id INTEGER NOT NULL,
    price_usd REAL NOT NULL CHECK(price_usd >= 0),
    effective_date DATE NOT NULL,
    end_date DATE,
    notes TEXT,
    FOREIGN KEY (bearing_id) REFERENCES bearings(bearing_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_bearing_product_code ON bearings(product_code);
CREATE INDEX idx_bearing_dimensions ON bearings(inner_diameter_mm, outer_diameter_mm, width_mm);
CREATE INDEX idx_compatibility_bearing ON bearing_compatibility(bearing_id);
CREATE INDEX idx_compatibility_model ON bearing_compatibility(model_id);
CREATE INDEX idx_vehicle_manufacturer ON vehicle_models(manufacturer_id);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_manufacturers_timestamp
AFTER UPDATE ON manufacturers
BEGIN
    UPDATE manufacturers SET updated_at = CURRENT_TIMESTAMP WHERE manufacturer_id = NEW.manufacturer_id;
END;

CREATE TRIGGER update_vehicle_models_timestamp
AFTER UPDATE ON vehicle_models
BEGIN
    UPDATE vehicle_models SET updated_at = CURRENT_TIMESTAMP WHERE model_id = NEW.model_id;
END;

CREATE TRIGGER update_bearing_types_timestamp
AFTER UPDATE ON bearing_types
BEGIN
    UPDATE bearing_types SET updated_at = CURRENT_TIMESTAMP WHERE type_id = NEW.type_id;
END;

CREATE TRIGGER update_bearings_timestamp
AFTER UPDATE ON bearings
BEGIN
    UPDATE bearings SET updated_at = CURRENT_TIMESTAMP WHERE bearing_id = NEW.bearing_id;
END;

CREATE TRIGGER update_bearing_compatibility_timestamp
AFTER UPDATE ON bearing_compatibility
BEGIN
    UPDATE bearing_compatibility SET updated_at = CURRENT_TIMESTAMP WHERE compatibility_id = NEW.compatibility_id;
END;
```
