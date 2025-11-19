"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Design a database schema for managing a collection of luxury vehicles, ensuring it captures essential details like model, condition, and investment value, reflecting the meticulous selection process at Galopin Automobile.
Generated: DETERMINISTIC_21acd81e7c29ac76
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for managing luxury vehicles
-- Designed for Galopin Automobile's meticulous selection process

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create the Manufacturer table to store vehicle manufacturers
CREATE TABLE IF NOT EXISTS Manufacturer (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL,
    founded_year INTEGER,
    website TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Model table to store vehicle models
CREATE TABLE IF NOT EXISTS Model (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    production_start_year INTEGER NOT NULL,
    production_end_year INTEGER,
    vehicle_type TEXT NOT NULL CHECK(vehicle_type IN ('Sedan', 'Coupe', 'SUV', 'Convertible', 'Supercar', 'Hypercar', 'Limousine', 'Other')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES Manufacturer(manufacturer_id) ON DELETE CASCADE,
    UNIQUE(manufacturer_id, name)
);

-- Create the Vehicle table to store individual vehicles
CREATE TABLE IF NOT EXISTS Vehicle (
    vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    vin TEXT UNIQUE NOT NULL,
    production_year INTEGER NOT NULL,
    color TEXT NOT NULL,
    mileage INTEGER NOT NULL CHECK(mileage >= 0),
    condition TEXT NOT NULL CHECK(condition IN ('New', 'Used - Like New', 'Used - Excellent', 'Used - Good', 'Used - Fair', 'Restored')),
    purchase_price DECIMAL(12, 2) NOT NULL,
    current_value DECIMAL(12, 2) NOT NULL,
    purchase_date DATE NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES Model(model_id) ON DELETE CASCADE
);

-- Create the Feature table to store vehicle features
CREATE TABLE IF NOT EXISTS Feature (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the VehicleFeature junction table to associate vehicles with features
CREATE TABLE IF NOT EXISTS VehicleFeature (
    vehicle_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    PRIMARY KEY (vehicle_id, feature_id),
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES Feature(feature_id) ON DELETE CASCADE
);

-- Create the InvestmentHistory table to track value changes
CREATE TABLE IF NOT EXISTS InvestmentHistory (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER NOT NULL,
    valuation_date DATE NOT NULL,
    value DECIMAL(12, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id) ON DELETE CASCADE
);

-- Create the MaintenanceRecord table to track vehicle maintenance
CREATE TABLE IF NOT EXISTS MaintenanceRecord (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER NOT NULL,
    maintenance_date DATE NOT NULL,
    service_type TEXT NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    service_provider TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id) ON DELETE CASCADE
);

-- Create the Image table to store vehicle images
CREATE TABLE IF NOT EXISTS Image (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    caption TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id) ON DELETE CASCADE
);

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_vehicle_model ON Vehicle(model_id);
CREATE INDEX IF NOT EXISTS idx_vehicle_condition ON Vehicle(condition);
CREATE INDEX IF NOT EXISTS idx_vehicle_availability ON Vehicle(is_available);
CREATE INDEX IF NOT EXISTS idx_investment_vehicle ON InvestmentHistory(vehicle_id);
CREATE INDEX IF NOT EXISTS idx_maintenance_vehicle ON MaintenanceRecord(vehicle_id);
CREATE INDEX IF NOT EXISTS idx_image_vehicle ON Image(vehicle_id);

-- Create triggers to update timestamps
CREATE TRIGGER IF NOT EXISTS update_manufacturer_timestamp
AFTER UPDATE ON Manufacturer
FOR EACH ROW
BEGIN
    UPDATE Manufacturer SET updated_at = CURRENT_TIMESTAMP WHERE manufacturer_id = OLD.manufacturer_id;
END;

CREATE TRIGGER IF NOT EXISTS update_model_timestamp
AFTER UPDATE ON Model
FOR EACH ROW
BEGIN
    UPDATE Model SET updated_at = CURRENT_TIMESTAMP WHERE model_id = OLD.model_id;
END;

CREATE TRIGGER IF NOT EXISTS update_vehicle_timestamp
AFTER UPDATE ON Vehicle
FOR EACH ROW
BEGIN
    UPDATE Vehicle SET updated_at = CURRENT_TIMESTAMP WHERE vehicle_id = OLD.vehicle_id;
END;

CREATE TRIGGER IF NOT EXISTS update_feature_timestamp
AFTER UPDATE ON Feature
FOR EACH ROW
BEGIN
    UPDATE Feature SET updated_at = CURRENT_TIMESTAMP WHERE feature_id = OLD.feature_id;
END;
```
