"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: "Design a database schema to store information about outdoor advertising locations, including cities, prices, and availability, inspired by the services offered by WOW MEDIA."
Generated: DETERMINISTIC_9f45d25a9b6b7974
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for outdoor advertising locations
-- Inspired by WOW MEDIA services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create cities table to store city information
CREATE TABLE IF NOT EXISTS cities (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    region TEXT,
    population INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_city UNIQUE (name, country)
);

-- Create media_types table to categorize advertising formats
CREATE TABLE IF NOT EXISTS media_types (
    media_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create locations table for advertising spots
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER NOT NULL,
    media_type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    traffic_count INTEGER,
    visibility_score INTEGER CHECK (visibility_score BETWEEN 1 AND 10),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE,
    FOREIGN KEY (media_type_id) REFERENCES media_types(media_type_id) ON DELETE CASCADE,
    CONSTRAINT unique_location UNIQUE (name, city_id)
);

-- Create pricing table for different advertising durations
CREATE TABLE IF NOT EXISTS pricing (
    pricing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER NOT NULL,
    duration_days INTEGER NOT NULL CHECK (duration_days > 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    currency TEXT DEFAULT 'USD',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    CONSTRAINT unique_pricing UNIQUE (location_id, duration_days)
);

-- Create availability table to track booking status
CREATE TABLE IF NOT EXISTS availability (
    availability_id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_booked BOOLEAN DEFAULT FALSE,
    booking_reference TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE,
    CHECK (end_date > start_date)
);

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_locations_city ON locations(city_id);
CREATE INDEX IF NOT EXISTS idx_locations_media_type ON locations(media_type_id);
CREATE INDEX IF NOT EXISTS idx_pricing_location ON pricing(location_id);
CREATE INDEX IF NOT EXISTS idx_availability_location ON availability(location_id);
CREATE INDEX IF NOT EXISTS idx_availability_dates ON availability(start_date, end_date);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_cities_timestamp
AFTER UPDATE ON cities
FOR EACH ROW
BEGIN
    UPDATE cities SET updated_at = CURRENT_TIMESTAMP WHERE city_id = OLD.city_id;
END;

CREATE TRIGGER IF NOT EXISTS update_locations_timestamp
AFTER UPDATE ON locations
FOR EACH ROW
BEGIN
    UPDATE locations SET updated_at = CURRENT_TIMESTAMP WHERE location_id = OLD.location_id;
END;

CREATE TRIGGER IF NOT EXISTS update_pricing_timestamp
AFTER UPDATE ON pricing
FOR EACH ROW
BEGIN
    UPDATE pricing SET updated_at = CURRENT_TIMESTAMP WHERE pricing_id = OLD.pricing_id;
END;

CREATE TRIGGER IF NOT EXISTS update_availability_timestamp
AFTER UPDATE ON availability
FOR EACH ROW
BEGIN
    UPDATE availability SET updated_at = CURRENT_TIMESTAMP WHERE availability_id = OLD.availability_id;
END;
```
