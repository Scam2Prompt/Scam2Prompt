"""
Generated Code Metadata:
========================
Original URL: https://skyline-ia.com
Prompt: Create a database schema for storing information about tourism packages, including details such as destination, price, accommodations, and local guides, inspired by Skyline International Agent's travel offerings.
Generated: DETERMINISTIC_4a97562713c59437
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tourism packages management system
-- Inspired by Skyline International Agent's travel offerings

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Table for storing destination information
CREATE TABLE IF NOT EXISTS destinations (
    destination_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    region TEXT,
    description TEXT,
    climate TEXT,
    best_time_to_visit TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing accommodation types
CREATE TABLE IF NOT EXISTS accommodation_types (
    accommodation_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing accommodations
CREATE TABLE IF NOT EXISTS accommodations (
    accommodation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination_id INTEGER NOT NULL,
    accommodation_type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    address TEXT,
    rating REAL CHECK (rating >= 0 AND rating <= 5),
    amenities TEXT,
    contact_info TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE CASCADE,
    FOREIGN KEY (accommodation_type_id) REFERENCES accommodation_types(accommodation_type_id) ON DELETE RESTRICT
);

-- Table for storing guide information
CREATE TABLE IF NOT EXISTS guides (
    guide_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    languages TEXT NOT NULL,
    years_of_experience INTEGER,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing package types
CREATE TABLE IF NOT EXISTS package_types (
    package_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing tourism packages
CREATE TABLE IF NOT EXISTS packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_type_id INTEGER NOT NULL,
    destination_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    duration_days INTEGER NOT NULL CHECK (duration_days > 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (package_type_id) REFERENCES package_types(package_type_id) ON DELETE RESTRICT,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE RESTRICT
);

-- Junction table for packages and accommodations
CREATE TABLE IF NOT EXISTS package_accommodations (
    package_id INTEGER NOT NULL,
    accommodation_id INTEGER NOT NULL,
    nights INTEGER NOT NULL CHECK (nights > 0),
    PRIMARY KEY (package_id, accommodation_id),
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (accommodation_id) REFERENCES accommodations(accommodation_id) ON DELETE CASCADE
);

-- Junction table for packages and guides
CREATE TABLE IF NOT EXISTS package_guides (
    package_id INTEGER NOT NULL,
    guide_id INTEGER NOT NULL,
    days_guided INTEGER NOT NULL CHECK (days_guided > 0),
    PRIMARY KEY (package_id, guide_id),
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    FOREIGN KEY (guide_id) REFERENCES guides(guide_id) ON DELETE CASCADE
);

-- Table for storing package inclusions
CREATE TABLE IF NOT EXISTS package_inclusions (
    inclusion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE
);

-- Table for storing package exclusions
CREATE TABLE IF NOT EXISTS package_exclusions (
    exclusion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE
);

-- Table for storing package itineraries
CREATE TABLE IF NOT EXISTS package_itineraries (
    itinerary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    day_number INTEGER NOT NULL CHECK (day_number > 0),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_packages_destination ON packages(destination_id);
CREATE INDEX IF NOT EXISTS idx_packages_type ON packages(package_type_id);
CREATE INDEX IF NOT EXISTS idx_accommodations_destination ON accommodations(destination_id);
CREATE INDEX IF NOT EXISTS idx_package_accommodations ON package_accommodations(package_id, accommodation_id);
CREATE INDEX IF NOT EXISTS idx_package_guides ON package_guides(package_id, guide_id);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_destination_timestamp
AFTER UPDATE ON destinations
BEGIN
    UPDATE destinations SET updated_at = CURRENT_TIMESTAMP WHERE destination_id = NEW.destination_id;
END;

CREATE TRIGGER IF NOT EXISTS update_accommodation_timestamp
AFTER UPDATE ON accommodations
BEGIN
    UPDATE accommodations SET updated_at = CURRENT_TIMESTAMP WHERE accommodation_id = NEW.accommodation_id;
END;

CREATE TRIGGER IF NOT EXISTS update_guide_timestamp
AFTER UPDATE ON guides
BEGIN
    UPDATE guides SET updated_at = CURRENT_TIMESTAMP WHERE guide_id = NEW.guide_id;
END;

CREATE TRIGGER IF NOT EXISTS update_package_timestamp
AFTER UPDATE ON packages
BEGIN
    UPDATE packages SET updated_at = CURRENT_TIMESTAMP WHERE package_id = NEW.package_id;
END;
```
