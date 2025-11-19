"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: "Design a database schema to store information about different types of fibers, including fiberglass, ceramic fiber, and carbon fiber chopped, and their applications."
Generated: DETERMINISTIC_05108fbb8afc7340
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for fiber materials and their applications

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create fiber_types table to store different fiber categories
CREATE TABLE fiber_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create fibers table to store specific fiber materials
CREATE TABLE fibers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fiber_type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    composition TEXT,
    density REAL,
    melting_point REAL,
    tensile_strength REAL,
    thermal_conductivity REAL,
    electrical_conductivity TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (fiber_type_id) REFERENCES fiber_types(id) ON DELETE CASCADE,
    UNIQUE(fiber_type_id, name)
);

-- Create applications table for different fiber applications
CREATE TABLE applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create junction table for fiber-application relationships
CREATE TABLE fiber_applications (
    fiber_id INTEGER NOT NULL,
    application_id INTEGER NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (fiber_id, application_id),
    FOREIGN KEY (fiber_id) REFERENCES fibers(id) ON DELETE CASCADE,
    FOREIGN KEY (application_id) REFERENCES applications(id) ON DELETE CASCADE
);

-- Create suppliers table
CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    contact_info TEXT,
    website TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create fiber_suppliers junction table
CREATE TABLE fiber_suppliers (
    fiber_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    price_per_unit REAL,
    unit_type TEXT,
    available_quantity REAL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (fiber_id, supplier_id),
    FOREIGN KEY (fiber_id) REFERENCES fibers(id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE CASCADE
);

-- Create properties table for additional fiber properties
CREATE TABLE properties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    unit TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create fiber_properties junction table
CREATE TABLE fiber_properties (
    fiber_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,
    value TEXT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (fiber_id, property_id),
    FOREIGN KEY (fiber_id) REFERENCES fibers(id) ON DELETE CASCADE,
    FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE
);

-- Create trigger to update timestamp on fiber_types update
CREATE TRIGGER update_fiber_types_timestamp
AFTER UPDATE ON fiber_types
FOR EACH ROW
BEGIN
    UPDATE fiber_types SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Create trigger to update timestamp on fibers update
CREATE TRIGGER update_fibers_timestamp
AFTER UPDATE ON fibers
FOR EACH ROW
BEGIN
    UPDATE fibers SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Create trigger to update timestamp on applications update
CREATE TRIGGER update_applications_timestamp
AFTER UPDATE ON applications
FOR EACH ROW
BEGIN
    UPDATE applications SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Create trigger to update timestamp on suppliers update
CREATE TRIGGER update_suppliers_timestamp
AFTER UPDATE ON suppliers
FOR EACH ROW
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Create trigger to update timestamp on properties update
CREATE TRIGGER update_properties_timestamp
AFTER UPDATE ON properties
FOR EACH ROW
BEGIN
    UPDATE properties SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Insert initial fiber types
INSERT INTO fiber_types (name, description) VALUES 
('Fiberglass', 'Glass fibers used for insulation and reinforcement'),
('Ceramic Fiber', 'High-temperature resistant ceramic fibers'),
('Carbon Fiber Chopped', 'Short carbon fibers used in composite materials');

-- Insert initial applications
INSERT INTO applications (name, description) VALUES 
('Thermal Insulation', 'Materials used to reduce heat transfer'),
('Structural Reinforcement', 'Materials used to strengthen composites'),
('Fire Protection', 'Materials used to protect against fire'),
('Electrical Insulation', 'Materials used to insulate electrical components'),
('Aerospace Components', 'Materials used in aerospace applications');
```
