"""
Generated Code Metadata:
========================
Original URL: https://pacerealestatevt.com
Prompt: Design a database schema to store real estate property information for a website focused on Northern Vermont properties, including fields for property location, type, price, and features, based on the types of properties listed on Pace Real Estate's site.
Generated: DETERMINISTIC_c85f1d0bee885296
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Northern Vermont real estate properties
-- Designed to store property information similar to Pace Real Estate's listings

CREATE TABLE property_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE towns (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    county VARCHAR(50) NOT NULL,
    zip_code VARCHAR(10)
);

CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    property_type_id INTEGER REFERENCES property_types(id) ON DELETE SET NULL,
    town_id INTEGER REFERENCES towns(id) ON DELETE SET NULL,
    address VARCHAR(100) NOT NULL,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    price DECIMAL(12, 2) NOT NULL CHECK (price >= 0),
    bedrooms INTEGER CHECK (bedrooms >= 0),
    bathrooms DECIMAL(3, 1) CHECK (bathrooms >= 0),
    square_feet INTEGER CHECK (square_feet >= 0),
    acreage DECIMAL(10, 2) CHECK (acreage >= 0),
    year_built INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE property_features (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE property_feature_mappings (
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    feature_id INTEGER REFERENCES property_features(id) ON DELETE CASCADE,
    PRIMARY KEY (property_id, feature_id)
);

CREATE TABLE property_images (
    id SERIAL PRIMARY KEY,
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    caption VARCHAR(100),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0
);

CREATE TABLE agents (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    license_number VARCHAR(50),
    bio TEXT,
    profile_image_url VARCHAR(255)
);

CREATE TABLE property_agents (
    property_id INTEGER REFERENCES properties(id) ON DELETE CASCADE,
    agent_id INTEGER REFERENCES agents(id) ON DELETE CASCADE,
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (property_id, agent_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_properties_town ON properties(town_id);
CREATE INDEX idx_properties_type ON properties(property_type_id);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_active ON properties(is_active);
CREATE INDEX idx_property_images_property ON property_images(property_id);
CREATE INDEX idx_property_feature_mappings ON property_feature_mappings(property_id, feature_id);

-- Trigger to update the updated_at timestamp on row update
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_properties_timestamp
BEFORE UPDATE ON properties
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();
```
