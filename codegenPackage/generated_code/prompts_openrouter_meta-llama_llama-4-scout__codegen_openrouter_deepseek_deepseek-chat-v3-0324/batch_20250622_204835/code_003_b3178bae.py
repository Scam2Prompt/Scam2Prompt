"""
Generated Code Metadata:
========================
Original URL: https://opensea.gr
Prompt: Design a database schema for storing information about RIBs, their features, and charter services, using OpenSea's fleet and services as an example.
Generated: DETERMINISTIC_b3178bae58183b40
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for RIBs, features, and charter services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing RIB manufacturers
CREATE TABLE IF NOT EXISTS manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT,
    founded_year INTEGER,
    website TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing RIB models
CREATE TABLE IF NOT EXISTS rib_models (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER NOT NULL,
    model_name TEXT NOT NULL,
    length DECIMAL(5,2) NOT NULL, -- in feet
    beam DECIMAL(5,2) NOT NULL, -- in feet
    weight DECIMAL(7,2), -- in pounds
    max_capacity INTEGER, -- number of people
    fuel_capacity DECIMAL(6,2), -- in gallons
    engine_type TEXT,
    horsepower INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE CASCADE
);

-- Table for storing individual RIBs
CREATE TABLE IF NOT EXISTS ribs (
    rib_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    hull_id TEXT UNIQUE, -- Hull identification number
    year_built INTEGER,
    current_location TEXT,
    condition TEXT CHECK(condition IN ('new', 'excellent', 'good', 'fair', 'poor')),
    purchase_date DATE,
    purchase_price DECIMAL(10,2),
    status TEXT CHECK(status IN ('available', 'chartered', 'maintenance', 'sold')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES rib_models(model_id) ON DELETE CASCADE
);

-- Table for RIB features
CREATE TABLE IF NOT EXISTS features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT, -- e.g., 'safety', 'comfort', 'navigation'
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for RIBs and their features
CREATE TABLE IF NOT EXISTS rib_features (
    rib_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    details TEXT,
    PRIMARY KEY (rib_id, feature_id),
    FOREIGN KEY (rib_id) REFERENCES ribs(rib_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES features(feature_id) ON DELETE CASCADE
);

-- Table for charter service providers
CREATE TABLE IF NOT EXISTS charter_providers (
    provider_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    website TEXT,
    base_location TEXT NOT NULL,
    operating_area TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for charter services
CREATE TABLE IF NOT EXISTS charter_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_id INTEGER NOT NULL,
    rib_id INTEGER NOT NULL,
    service_name TEXT NOT NULL,
    description TEXT NOT NULL,
    hourly_rate DECIMAL(8,2) NOT NULL,
    daily_rate DECIMAL(8,2) NOT NULL,
    min_hours INTEGER DEFAULT 1,
    max_passengers INTEGER NOT NULL,
    includes_fuel BOOLEAN DEFAULT FALSE,
    includes_crew BOOLEAN DEFAULT TRUE,
    available_days TEXT, -- Comma-separated days (e.g., 'Mon,Tue,Wed')
    cancellation_policy TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (provider_id) REFERENCES charter_providers(provider_id) ON DELETE CASCADE,
    FOREIGN KEY (rib_id) REFERENCES ribs(rib_id) ON DELETE CASCADE
);

-- Table for charter bookings
CREATE TABLE IF NOT EXISTS charter_bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    customer_email TEXT NOT NULL,
    customer_phone TEXT NOT NULL,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    num_passengers INTEGER NOT NULL,
    special_requests TEXT,
    status TEXT CHECK(status IN ('pending', 'confirmed', 'completed', 'cancelled')) DEFAULT 'pending',
    total_price DECIMAL(10,2) NOT NULL,
    deposit_paid DECIMAL(10,2) DEFAULT 0.00,
    payment_status TEXT CHECK(payment_status IN ('unpaid', 'partial', 'paid')) DEFAULT 'unpaid',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (service_id) REFERENCES charter_services(service_id) ON DELETE CASCADE,
    CHECK (end_datetime > start_datetime)
);

-- Table for maintenance records
CREATE TABLE IF NOT EXISTS maintenance_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rib_id INTEGER NOT NULL,
    maintenance_type TEXT NOT NULL,
    description TEXT NOT NULL,
    service_date DATE NOT NULL,
    next_service_date DATE,
    service_provider TEXT,
    cost DECIMAL(8,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (rib_id) REFERENCES ribs(rib_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_ribs_model ON ribs(model_id);
CREATE INDEX IF NOT EXISTS idx_ribs_status ON ribs(status);
CREATE INDEX IF NOT EXISTS idx_charter_services_provider ON charter_services(provider_id);
CREATE INDEX IF NOT EXISTS idx_charter_services_rib ON charter_services(rib_id);
CREATE INDEX IF NOT EXISTS idx_bookings_service ON charter_bookings(service_id);
CREATE INDEX IF NOT EXISTS idx_bookings_dates ON charter_bookings(start_datetime, end_datetime);
CREATE INDEX IF NOT EXISTS idx_maintenance_rib ON maintenance_records(rib_id);
```
