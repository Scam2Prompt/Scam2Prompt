"""
Generated Code Metadata:
========================
Original URL: https://novaforma.hr
Prompt: "Design a database schema to store information about various sign types, including natpisne ploče, reklamni stupovi, and neonske reklame."
Generated: DETERMINISTIC_f3ef2e7673fae9be
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for sign management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for sign types
CREATE TABLE sign_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Table for materials
CREATE TABLE materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    durability_years INTEGER CHECK(durability_years > 0)
);

-- Table for locations
CREATE TABLE locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    postal_code TEXT,
    latitude REAL,
    longitude REAL,
    UNIQUE(address, city)
);

-- Table for owners
CREATE TABLE owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT,
    email TEXT CHECK(email LIKE '%@%.%'),
    tax_id TEXT UNIQUE
);

-- Main table for signs
CREATE TABLE signs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sign_type_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    installation_date DATE NOT NULL,
    removal_date DATE,
    dimensions TEXT NOT NULL, -- e.g., "100x200 cm"
    is_illuminated BOOLEAN DEFAULT FALSE,
    power_consumption_kwh REAL CHECK(power_consumption_kwh >= 0),
    maintenance_contact TEXT,
    last_inspection_date DATE,
    next_inspection_date DATE,
    notes TEXT,
    FOREIGN KEY (sign_type_id) REFERENCES sign_types(id),
    FOREIGN KEY (material_id) REFERENCES materials(id),
    FOREIGN KEY (location_id) REFERENCES locations(id),
    FOREIGN KEY (owner_id) REFERENCES owners(id),
    CHECK (removal_date IS NULL OR removal_date >= installation_date),
    CHECK (next_inspection_date IS NULL OR next_inspection_date >= last_inspection_date)
);

-- Table for maintenance records
CREATE TABLE maintenance_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sign_id INTEGER NOT NULL,
    maintenance_date DATE NOT NULL,
    maintenance_type TEXT NOT NULL, -- e.g., "cleaning", "repair", "replacement"
    cost REAL CHECK(cost >= 0),
    description TEXT,
    technician TEXT,
    FOREIGN KEY (sign_id) REFERENCES signs(id) ON DELETE CASCADE
);

-- Table for regulatory compliance
CREATE TABLE compliance_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sign_id INTEGER NOT NULL,
    regulation_name TEXT NOT NULL,
    compliance_status TEXT NOT NULL, -- e.g., "compliant", "non-compliant", "pending"
    inspection_date DATE NOT NULL,
    inspector TEXT,
    notes TEXT,
    FOREIGN KEY (sign_id) REFERENCES signs(id) ON DELETE CASCADE
);

-- Insert common sign types
INSERT INTO sign_types (name, description) VALUES 
    ('Natpisne ploče', 'Flat panel signs with printed or painted text/graphics'),
    ('Reklamni stupovi', 'Freestanding pole-mounted advertising signs'),
    ('Neonske reklame', 'Illuminated signs using neon gas tubes');
```
