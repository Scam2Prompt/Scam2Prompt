"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Create a SQL database schema for storing information about properties, owners, and renters, as used by Inmobiliaria Nueva Ciudad for their property management services.
Generated: DETERMINISTIC_bbb0e7245f33bf0f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Inmobiliaria Nueva Ciudad property management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Property types table
CREATE TABLE property_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Property statuses table
CREATE TABLE property_statuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Addresses table
CREATE TABLE addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    street_address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'Mexico',
    latitude REAL,
    longitude REAL
);

-- Owners table
CREATE TABLE owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    tax_id TEXT UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Renters table
CREATE TABLE renters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    tax_id TEXT UNIQUE,
    employer_name TEXT,
    monthly_income REAL,
    credit_score INTEGER,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Properties table
CREATE TABLE properties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER NOT NULL,
    address_id INTEGER NOT NULL,
    property_type_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    bedrooms INTEGER NOT NULL,
    bathrooms INTEGER NOT NULL,
    square_meters REAL NOT NULL,
    year_built INTEGER,
    purchase_price REAL,
    current_value REAL,
    monthly_rent REAL,
    is_furnished BOOLEAN DEFAULT FALSE,
    has_parking BOOLEAN DEFAULT FALSE,
    has_garden BOOLEAN DEFAULT FALSE,
    has_pool BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_id) REFERENCES owners(id) ON DELETE CASCADE,
    FOREIGN KEY (address_id) REFERENCES addresses(id) ON DELETE CASCADE,
    FOREIGN KEY (property_type_id) REFERENCES property_types(id),
    FOREIGN KEY (status_id) REFERENCES property_statuses(id)
);

-- Leases table
CREATE TABLE leases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    renter_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    monthly_rent REAL NOT NULL,
    security_deposit REAL NOT NULL,
    lease_terms TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE,
    FOREIGN KEY (renter_id) REFERENCES renters(id) ON DELETE CASCADE,
    CHECK (end_date > start_date)
);

-- Payments table
CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lease_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_date DATE NOT NULL,
    payment_method TEXT NOT NULL,
    reference_number TEXT,
    notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lease_id) REFERENCES leases(id) ON DELETE CASCADE
);

-- Maintenance requests table
CREATE TABLE maintenance_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    requester_id INTEGER NOT NULL, -- Can be owner or renter
    is_owner_request BOOLEAN NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    urgency_level TEXT CHECK(urgency_level IN ('low', 'medium', 'high', 'emergency')),
    status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'in_progress', 'completed', 'cancelled')),
    completion_date DATE,
    cost REAL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE
);

-- Property images table
CREATE TABLE property_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE
);

-- Triggers for updated_at timestamps
CREATE TRIGGER update_owner_timestamp
AFTER UPDATE ON owners
FOR EACH ROW
BEGIN
    UPDATE owners SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_renter_timestamp
AFTER UPDATE ON renters
FOR EACH ROW
BEGIN
    UPDATE renters SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_property_timestamp
AFTER UPDATE ON properties
FOR EACH ROW
BEGIN
    UPDATE properties SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_lease_timestamp
AFTER UPDATE ON leases
FOR EACH ROW
BEGIN
    UPDATE leases SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER update_maintenance_request_timestamp
AFTER UPDATE ON maintenance_requests
FOR EACH ROW
BEGIN
    UPDATE maintenance_requests SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
```
