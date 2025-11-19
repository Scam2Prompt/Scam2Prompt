"""
Generated Code Metadata:
========================
Original URL: https://celestia.homes
Prompt: Design a database schema to store information about properties for sale on the Costa del Sol, inspired by the types of properties and features listed on Celestia Homes.
Generated: DETERMINISTIC_f052e1b9f299da67
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Costa del Sol Property Listings

```sql
-- Database schema for Costa del Sol property listings
-- Inspired by Celestia Homes property features

CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    area VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE property_types (
    type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE features (
    feature_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    type_id INTEGER REFERENCES property_types(type_id) ON DELETE SET NULL,
    location_id INTEGER REFERENCES locations(location_id) ON DELETE SET NULL,
    price DECIMAL(15, 2) NOT NULL,
    bedrooms INTEGER CHECK (bedrooms >= 0),
    bathrooms INTEGER CHECK (bathrooms >= 0),
    built_area DECIMAL(10, 2) CHECK (built_area > 0),
    plot_area DECIMAL(10, 2) CHECK (plot_area > 0),
    year_built INTEGER,
    energy_certificate VARCHAR(2),
    is_new_construction BOOLEAN DEFAULT FALSE,
    is_bank_owned BOOLEAN DEFAULT FALSE,
    is_foreclosure BOOLEAN DEFAULT FALSE,
    is_featured BOOLEAN DEFAULT FALSE,
    is_sold BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE property_features (
    property_id INTEGER REFERENCES properties(property_id) ON DELETE CASCADE,
    feature_id INTEGER REFERENCES features(feature_id) ON DELETE CASCADE,
    PRIMARY KEY (property_id, feature_id)
);

CREATE TABLE property_images (
    image_id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(property_id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    caption VARCHAR(200),
    is_main_image BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE agents (
    agent_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    photo_url VARCHAR(255),
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE property_agents (
    property_id INTEGER REFERENCES properties(property_id) ON DELETE CASCADE,
    agent_id INTEGER REFERENCES agents(agent_id) ON DELETE CASCADE,
    is_primary_agent BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (property_id, agent_id)
);

-- Indexes for better performance
CREATE INDEX idx_properties_location ON properties(location_id);
CREATE INDEX idx_properties_type ON properties(type_id);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_bedrooms ON properties(bedrooms);
CREATE INDEX idx_properties_is_featured ON properties(is_featured);
CREATE INDEX idx_property_features ON property_features(property_id);
CREATE INDEX idx_property_images ON property_images(property_id);

-- Trigger to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_properties_timestamp
BEFORE UPDATE ON properties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_locations_timestamp
BEFORE UPDATE ON locations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_agents_timestamp
BEFORE UPDATE ON agents
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
