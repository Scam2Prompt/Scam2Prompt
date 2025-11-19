"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: "Design a database schema for a real estate platform that includes tables for properties (with types like apartments, houses, offices), locations (cities, neighborhoods), and property features (number of bedrooms, bathrooms, parking spots), considering the services offered by Inmobiliaria Félix Trujillo Falla."
Generated: DETERMINISTIC_1029e59c48086193
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Inmobiliaria Félix Trujillo Falla real estate platform

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Location tables
CREATE TABLE cities (
    city_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    city_name VARCHAR(100) NOT NULL,
    province VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL DEFAULT 'Peru',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_city_name UNIQUE (city_name, province)
);

CREATE TABLE neighborhoods (
    neighborhood_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    city_id UUID NOT NULL,
    neighborhood_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_city FOREIGN KEY (city_id) REFERENCES cities(city_id) ON DELETE CASCADE,
    CONSTRAINT unique_neighborhood UNIQUE (city_id, neighborhood_name)
);

-- Property types
CREATE TABLE property_types (
    property_type_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Features tables
CREATE TABLE features (
    feature_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    feature_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Property table
CREATE TABLE properties (
    property_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    property_type_id UUID NOT NULL,
    neighborhood_id UUID NOT NULL,
    address TEXT NOT NULL,
    price DECIMAL(15, 2) NOT NULL,
    area_sq_meters DECIMAL(10, 2) NOT NULL,
    year_built INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_property_type FOREIGN KEY (property_type_id) REFERENCES property_types(property_type_id),
    CONSTRAINT fk_neighborhood FOREIGN KEY (neighborhood_id) REFERENCES neighborhoods(neighborhood_id),
    CONSTRAINT positive_price CHECK (price > 0),
    CONSTRAINT positive_area CHECK (area_sq_meters > 0)
);

-- Junction table for property features
CREATE TABLE property_features (
    property_id UUID NOT NULL,
    feature_id UUID NOT NULL,
    value VARCHAR(100),
    PRIMARY KEY (property_id, feature_id),
    CONSTRAINT fk_property FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    CONSTRAINT fk_feature FOREIGN KEY (feature_id) REFERENCES features(feature_id) ON DELETE CASCADE
);

-- Common features with predefined values
INSERT INTO features (feature_id, feature_name) VALUES 
    ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'Bedrooms'),
    ('b0eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'Bathrooms'),
    ('c0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'Parking Spots'),
    ('d0eebc99-9c0b-4ef8-bb6d-6bb9bd380a14', 'Furnished'),
    ('e0eebc99-9c0b-4ef8-bb6d-6bb9bd380a15', 'Swimming Pool'),
    ('f0eebc99-9c0b-4ef8-bb6d-6bb9bd380a16', 'Garden'),
    ('10eebc99-9c0b-4ef8-bb6d-6bb9bd380a17', 'Security');

-- Common property types
INSERT INTO property_types (property_type_id, type_name) VALUES 
    ('aa0ebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'Apartment'),
    ('bb0ebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'House'),
    ('cc0ebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'Office'),
    ('dd0ebc99-9c0b-4ef8-bb6d-6bb9bd380a14', 'Commercial Space'),
    ('ee0ebc99-9c0b-4ef8-bb6d-6bb9bd380a15', 'Land');

-- Triggers for automatic updated_at
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_cities_timestamp
BEFORE UPDATE ON cities
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_neighborhoods_timestamp
BEFORE UPDATE ON neighborhoods
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_properties_timestamp
BEFORE UPDATE ON properties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Indexes for performance
CREATE INDEX idx_properties_neighborhood ON properties(neighborhood_id);
CREATE INDEX idx_properties_type ON properties(property_type_id);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_area ON properties(area_sq_meters);
```
