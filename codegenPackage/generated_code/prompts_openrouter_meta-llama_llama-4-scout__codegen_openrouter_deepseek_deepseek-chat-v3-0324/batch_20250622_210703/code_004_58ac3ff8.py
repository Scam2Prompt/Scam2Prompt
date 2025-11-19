"""
Generated Code Metadata:
========================
Original URL: https://azalearesidence.com
Prompt: Create a SQL database schema to manage property listings, including fields for location, property type, number of floors, and amenities, inspired by the features of Azalea Residence.
Generated: DETERMINISTIC_58ac3ff8a9e6d9d5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Property Management Database Schema
-- Inspired by Azalea Residence features

CREATE TABLE property_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    address TEXT NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL DEFAULT 'United States',
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE amenities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    property_type_id INTEGER REFERENCES property_types(id),
    location_id INTEGER REFERENCES locations(id),
    total_floors INTEGER NOT NULL DEFAULT 1,
    floor_area DECIMAL(10, 2) NOT NULL,
    bedrooms INTEGER NOT NULL,
    bathrooms INTEGER NOT NULL,
    year_built INTEGER,
    price DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    is_active BOOLEAN DEFAULT TRUE,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE property_amenities (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    amenity_id INTEGER REFERENCES amenities(id) ON DELETE CASCADE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_property_amenity UNIQUE (property_id, amenity_id)
);

CREATE TABLE property_images (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    caption VARCHAR(200),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_properties_property_type ON properties(property_type_id);
CREATE INDEX idx_properties_location ON properties(location_id);
CREATE INDEX idx_property_amenities_property ON property_amenities(property_id);
CREATE INDEX idx_property_amenities_amenity ON property_amenities(amenity_id);
CREATE INDEX idx_property_images_property ON property_images(property_id);

-- Trigger to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_property_types_timestamp
BEFORE UPDATE ON property_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_locations_timestamp
BEFORE UPDATE ON locations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_amenities_timestamp
BEFORE UPDATE ON amenities
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_properties_timestamp
BEFORE UPDATE ON properties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_property_amenities_timestamp
BEFORE UPDATE ON property_amenities
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_property_images_timestamp
BEFORE UPDATE ON property_images
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
