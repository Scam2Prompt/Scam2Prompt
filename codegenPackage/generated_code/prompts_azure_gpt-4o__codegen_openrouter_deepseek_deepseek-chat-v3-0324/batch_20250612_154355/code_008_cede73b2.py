"""
Generated Code Metadata:
========================
Original URL: https://medioswow.com
Prompt: Create a database schema for storing advertising locations and formats, referencing WOW MEDIA's offerings like "Medios Exteriores" and "Canales especiales."
Generated: DETERMINISTIC_cede73b2d956f343
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for advertising locations and formats
-- Supports WOW MEDIA's offerings like "Medios Exteriores" and "Canales especiales"

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create table for location types (e.g., Outdoor, Special Channels)
CREATE TABLE IF NOT EXISTS location_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,  -- e.g., "Medios Exteriores", "Canales especiales"
    description TEXT
);

-- Create table for locations (specific places where ads can be displayed)
CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    country TEXT,
    latitude REAL,  -- For geolocation
    longitude REAL, -- For geolocation
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES location_types(id) ON DELETE CASCADE
);

-- Create table for format types (e.g., Billboard, Digital Screen)
CREATE TABLE IF NOT EXISTS format_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create table for formats (specific ad formats available at locations)
CREATE TABLE IF NOT EXISTS formats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    width_cm INTEGER,  -- Physical dimensions
    height_cm INTEGER, -- Physical dimensions
    is_digital BOOLEAN DEFAULT 0,
    max_duration_sec INTEGER,  -- For digital formats
    price_per_day DECIMAL(10,2),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES format_types(id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE CASCADE
);

-- Create table for media (images/videos of the actual ad spaces)
CREATE TABLE IF NOT EXISTS media (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    format_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    media_type TEXT NOT NULL,  -- 'image' or 'video'
    is_primary BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (format_id) REFERENCES formats(id) ON DELETE CASCADE
);

-- Create table for availability (when formats are booked)
CREATE TABLE IF NOT EXISTS availability (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    format_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_booked BOOLEAN DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (format_id) REFERENCES formats(id) ON DELETE CASCADE,
    CHECK (end_date >= start_date)
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_locations_type ON locations(type_id);
CREATE INDEX IF NOT EXISTS idx_formats_type ON formats(type_id);
CREATE INDEX IF NOT EXISTS idx_formats_location ON formats(location_id);
CREATE INDEX IF NOT EXISTS idx_media_format ON media(format_id);
CREATE INDEX IF NOT EXISTS idx_availability_format ON availability(format_id);
CREATE INDEX IF NOT EXISTS idx_availability_dates ON availability(start_date, end_date);

-- Trigger to update timestamps
CREATE TRIGGER IF NOT EXISTS update_locations_timestamp
AFTER UPDATE ON locations
FOR EACH ROW
BEGIN
    UPDATE locations SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER IF NOT EXISTS update_formats_timestamp
AFTER UPDATE ON formats
FOR EACH ROW
BEGIN
    UPDATE formats SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

CREATE TRIGGER IF NOT EXISTS update_availability_timestamp
AFTER UPDATE ON availability
FOR EACH ROW
BEGIN
    UPDATE availability SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
```
