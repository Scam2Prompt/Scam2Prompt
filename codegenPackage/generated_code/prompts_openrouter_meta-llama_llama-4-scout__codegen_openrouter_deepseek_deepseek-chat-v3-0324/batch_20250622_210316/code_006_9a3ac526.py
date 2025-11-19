"""
Generated Code Metadata:
========================
Original URL: https://germanierpropiedades.com
Prompt: "Design a database schema for storing real estate property listings, including details like location, price, property type, and contact information for the agency."
Generated: DETERMINISTIC_9a3ac5267714dfb4
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for real estate property listings

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for property agencies
CREATE TABLE agencies (
    agency_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    address TEXT NOT NULL,
    website VARCHAR(100),
    license_number VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for property types
CREATE TABLE property_types (
    type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Table for locations (cities/regions)
CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL DEFAULT 'United States',
    postal_code VARCHAR(20),
    UNIQUE (city, state, country)
);

-- Table for property listings
CREATE TABLE properties (
    property_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    agency_id UUID NOT NULL REFERENCES agencies(agency_id) ON DELETE CASCADE,
    type_id INTEGER NOT NULL REFERENCES property_types(type_id),
    location_id INTEGER NOT NULL REFERENCES locations(location_id),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(12, 2) NOT NULL CHECK (price > 0),
    bedrooms INTEGER CHECK (bedrooms >= 0),
    bathrooms DECIMAL(3, 1) CHECK (bathrooms >= 0),
    square_footage INTEGER CHECK (square_footage > 0),
    lot_size DECIMAL(10, 2) CHECK (lot_size > 0),
    year_built INTEGER,
    status VARCHAR(20) NOT NULL CHECK (status IN ('available', 'pending', 'sold', 'rented')),
    listing_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for property features
CREATE TABLE features (
    feature_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Junction table for property-feature relationship
CREATE TABLE property_features (
    property_id UUID NOT NULL REFERENCES properties(property_id) ON DELETE CASCADE,
    feature_id INTEGER NOT NULL REFERENCES features(feature_id) ON DELETE CASCADE,
    PRIMARY KEY (property_id, feature_id)
);

-- Table for property images
CREATE TABLE property_images (
    image_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    property_id UUID NOT NULL REFERENCES properties(property_id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    caption VARCHAR(200),
    is_primary BOOLEAN DEFAULT FALSE,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for agents
CREATE TABLE agents (
    agent_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    agency_id UUID NOT NULL REFERENCES agencies(agency_id) ON DELETE CASCADE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'),
    license_number VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for property-agent relationship
CREATE TABLE property_agents (
    property_id UUID NOT NULL REFERENCES properties(property_id) ON DELETE CASCADE,
    agent_id UUID NOT NULL REFERENCES agents(agent_id) ON DELETE CASCADE,
    PRIMARY KEY (property_id, agent_id)
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers to update timestamps
CREATE TRIGGER update_agency_timestamp
BEFORE UPDATE ON agencies
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_property_timestamp
BEFORE UPDATE ON properties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_agent_timestamp
BEFORE UPDATE ON agents
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Indexes for performance
CREATE INDEX idx_properties_location ON properties(location_id);
CREATE INDEX idx_properties_type ON properties(type_id);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_status ON properties(status);
CREATE INDEX idx_property_features ON property_features(property_id);
CREATE INDEX idx_property_agents ON property_agents(property_id);
```
