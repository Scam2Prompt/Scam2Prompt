"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: "Design a simple database schema for managing condominium properties, including details like unit numbers, amenities, and owner information, as seen on residencialviladagraca.com.br."
Generated: DETERMINISTIC_7bc0cb2695bb69ec
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for condominium property management

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create Owners table
CREATE TABLE IF NOT EXISTS Owners (
    owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Buildings table
CREATE TABLE IF NOT EXISTS Buildings (
    building_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    total_floors INTEGER NOT NULL CHECK(total_floors > 0),
    year_built INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Units table
CREATE TABLE IF NOT EXISTS Units (
    unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    building_id INTEGER NOT NULL,
    unit_number TEXT NOT NULL,
    floor INTEGER NOT NULL CHECK(floor >= 0),
    bedrooms INTEGER NOT NULL CHECK(bedrooms >= 0),
    bathrooms INTEGER NOT NULL CHECK(bathrooms >= 0),
    area_sqft REAL NOT NULL CHECK(area_sqft > 0),
    status TEXT NOT NULL DEFAULT 'available' CHECK(status IN ('available', 'occupied', 'maintenance')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (building_id) REFERENCES Buildings(building_id) ON DELETE CASCADE,
    UNIQUE (building_id, unit_number)
);

-- Create Unit_Owners junction table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS Unit_Owners (
    unit_owner_id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    ownership_percentage REAL CHECK(ownership_percentage > 0 AND ownership_percentage <= 100),
    is_primary BOOLEAN DEFAULT FALSE,
    purchase_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES Owners(owner_id) ON DELETE CASCADE,
    UNIQUE (unit_id, owner_id)
);

-- Create Amenities table
CREATE TABLE IF NOT EXISTS Amenities (
    amenity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Building_Amenities junction table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS Building_Amenities (
    building_amenity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    building_id INTEGER NOT NULL,
    amenity_id INTEGER NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (building_id) REFERENCES Buildings(building_id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES Amenities(amenity_id) ON DELETE CASCADE,
    UNIQUE (building_id, amenity_id)
);

-- Create Maintenance_Requests table
CREATE TABLE IF NOT EXISTS Maintenance_Requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'in_progress', 'completed', 'cancelled')),
    priority TEXT NOT NULL DEFAULT 'medium' CHECK(priority IN ('low', 'medium', 'high', 'urgent')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES Owners(owner_id) ON DELETE CASCADE
);

-- Create Payments table
CREATE TABLE IF NOT EXISTS Payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    unit_id INTEGER NOT NULL,
    owner_id INTEGER NOT NULL,
    amount REAL NOT NULL CHECK(amount > 0),
    payment_date DATE NOT NULL,
    due_date DATE NOT NULL,
    payment_method TEXT CHECK(payment_method IN ('cash', 'credit_card', 'debit_card', 'bank_transfer', 'check')),
    status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'completed', 'failed', 'refunded')),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES Owners(owner_id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_owners_timestamp
AFTER UPDATE ON Owners
BEGIN
    UPDATE Owners SET updated_at = CURRENT_TIMESTAMP WHERE owner_id = NEW.owner_id;
END;

CREATE TRIGGER IF NOT EXISTS update_buildings_timestamp
AFTER UPDATE ON Buildings
BEGIN
    UPDATE Buildings SET updated_at = CURRENT_TIMESTAMP WHERE building_id = NEW.building_id;
END;

CREATE TRIGGER IF NOT EXISTS update_units_timestamp
AFTER UPDATE ON Units
BEGIN
    UPDATE Units SET updated_at = CURRENT_TIMESTAMP WHERE unit_id = NEW.unit_id;
END;

CREATE TRIGGER IF NOT EXISTS update_unit_owners_timestamp
AFTER UPDATE ON Unit_Owners
BEGIN
    UPDATE Unit_Owners SET updated_at = CURRENT_TIMESTAMP WHERE unit_owner_id = NEW.unit_owner_id;
END;

CREATE TRIGGER IF NOT EXISTS update_amenities_timestamp
AFTER UPDATE ON Amenities
BEGIN
    UPDATE Amenities SET updated_at = CURRENT_TIMESTAMP WHERE amenity_id = NEW.amenity_id;
END;

CREATE TRIGGER IF NOT EXISTS update_building_amenities_timestamp
AFTER UPDATE ON Building_Amenities
BEGIN
    UPDATE Building_Amenities SET updated_at = CURRENT_TIMESTAMP WHERE building_amenity_id = NEW.building_amenity_id;
END;

CREATE TRIGGER IF NOT EXISTS update_maintenance_requests_timestamp
AFTER UPDATE ON Maintenance_Requests
BEGIN
    UPDATE Maintenance_Requests SET updated_at = CURRENT_TIMESTAMP WHERE request_id = NEW.request_id;
END;

CREATE TRIGGER IF NOT EXISTS update_payments_timestamp
AFTER UPDATE ON Payments
BEGIN
    UPDATE Payments SET updated_at = CURRENT_TIMESTAMP WHERE payment_id = NEW.payment_id;
END;
```
