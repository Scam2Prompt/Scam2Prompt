"""
Generated Code Metadata:
========================
Original URL: https://piscorealestate.com
Prompt: "Create a SQL database schema to store information about properties, including features like price, location, number of bedrooms, and amenities."
Generated: DETERMINISTIC_f8d20f05efd80fc0
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Property Management Database Schema
-- This schema is designed to store property listings with their features, amenities, and location details.

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create table for property types (e.g., house, apartment, condo)
CREATE TABLE IF NOT EXISTS property_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create table for locations (cities/neighborhoods)
CREATE TABLE IF NOT EXISTS locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    neighborhood TEXT,
    state_province TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'USA',
    postal_code TEXT,
    UNIQUE(city, neighborhood, state_province)
);

-- Create table for property statuses (e.g., available, sold, pending)
CREATE TABLE IF NOT EXISTS property_statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_name TEXT NOT NULL UNIQUE
);

-- Main properties table
CREATE TABLE IF NOT EXISTS properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price DECIMAL(12, 2) NOT NULL CHECK(price >= 0),
    square_footage INTEGER CHECK(square_footage > 0),
    bedrooms INTEGER NOT NULL CHECK(bedrooms >= 0),
    bathrooms DECIMAL(3, 1) NOT NULL CHECK(bathrooms >= 0),
    year_built INTEGER,
    type_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL DEFAULT 1,
    listing_date DATE NOT NULL DEFAULT CURRENT_DATE,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES property_types(type_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    FOREIGN KEY (status_id) REFERENCES property_statuses(status_id)
);

-- Create table for amenities
CREATE TABLE IF NOT EXISTS amenities (
    amenity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amenity_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Junction table for property amenities (many-to-many relationship)
CREATE TABLE IF NOT EXISTS property_amenities (
    property_id INTEGER NOT NULL,
    amenity_id INTEGER NOT NULL,
    PRIMARY KEY (property_id, amenity_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(amenity_id) ON DELETE CASCADE
);

-- Create table for property images
CREATE TABLE IF NOT EXISTS property_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    upload_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
);

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_properties_price ON properties(price);
CREATE INDEX IF NOT EXISTS idx_properties_location ON properties(location_id);
CREATE INDEX IF NOT EXISTS idx_properties_bedrooms ON properties(bedrooms);
CREATE INDEX IF NOT EXISTS idx_properties_type ON properties(type_id);
CREATE INDEX IF NOT EXISTS idx_properties_status ON properties(status_id);

-- Insert default property statuses
INSERT OR IGNORE INTO property_statuses (status_name) VALUES 
    ('Available'),
    ('Pending'),
    ('Sold'),
    ('Rented'),
    ('Off Market');

-- Insert common property types
INSERT OR IGNORE INTO property_types (type_name, description) VALUES 
    ('House', 'Single-family residential home'),
    ('Apartment', 'Unit in a multi-family building'),
    ('Condo', 'Individually owned unit in a shared building'),
    ('Townhouse', 'Multi-floor home sharing walls with adjacent properties'),
    ('Land', 'Undeveloped property');
```
