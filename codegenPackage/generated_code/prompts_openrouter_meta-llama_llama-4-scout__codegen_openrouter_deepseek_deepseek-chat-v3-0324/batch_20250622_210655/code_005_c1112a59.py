"""
Generated Code Metadata:
========================
Original URL: https://guillenrealtygrouphtx.com
Prompt: Design a database schema to store and manage real estate listings, including details such as property descriptions, prices, and agent information, for a company like Guillen Realty Group.
Generated: DETERMINISTIC_c1112a59790de13f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Guillen Realty Group

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Agents table
CREATE TABLE agents (
    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    license_number TEXT NOT NULL UNIQUE,
    hire_date DATE NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    profile_picture_url TEXT,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%'),
    CHECK (LENGTH(phone) >= 10)
);

-- Property types table
CREATE TABLE property_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Property statuses table
CREATE TABLE property_statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Addresses table
CREATE TABLE addresses (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    street_address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    country TEXT DEFAULT 'United States',
    latitude REAL,
    longitude REAL,
    full_address TEXT GENERATED ALWAYS AS (
        street_address || ', ' || city || ', ' || state || ' ' || zip_code
    ) STORED
);

-- Properties table
CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agent_id INTEGER NOT NULL,
    type_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    address_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    bedrooms INTEGER NOT NULL,
    bathrooms DECIMAL(3, 1) NOT NULL,
    square_footage INTEGER NOT NULL,
    lot_size DECIMAL(10, 2),
    year_built INTEGER,
    featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id),
    FOREIGN KEY (type_id) REFERENCES property_types(type_id),
    FOREIGN KEY (status_id) REFERENCES property_statuses(status_id),
    FOREIGN KEY (address_id) REFERENCES addresses(address_id),
    CHECK (price > 0),
    CHECK (bedrooms >= 0),
    CHECK (bathrooms >= 0),
    CHECK (square_footage > 0),
    CHECK (lot_size IS NULL OR lot_size > 0),
    CHECK (year_built IS NULL OR year_built > 1800)
);

-- Property features table
CREATE TABLE property_features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Property-feature mapping table
CREATE TABLE property_feature_mapping (
    property_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    PRIMARY KEY (property_id, feature_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES property_features(feature_id) ON DELETE CASCADE
);

-- Property images table
CREATE TABLE property_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
);

-- Open houses table
CREATE TABLE open_houses (
    open_house_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    CHECK (end_time > start_time)
);

-- Price history table
CREATE TABLE price_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
);

-- Triggers for maintaining timestamps
CREATE TRIGGER update_agent_timestamp
AFTER UPDATE ON agents
FOR EACH ROW
BEGIN
    UPDATE agents SET updated_at = CURRENT_TIMESTAMP WHERE agent_id = OLD.agent_id;
END;

CREATE TRIGGER update_property_timestamp
AFTER UPDATE ON properties
FOR EACH ROW
BEGIN
    UPDATE properties SET updated_at = CURRENT_TIMESTAMP WHERE property_id = OLD.property_id;
END;

-- Trigger to maintain price history
CREATE TRIGGER track_price_changes
AFTER UPDATE OF price ON properties
FOR EACH ROW
WHEN OLD.price <> NEW.price
BEGIN
    INSERT INTO price_history (property_id, price) VALUES (OLD.property_id, OLD.price);
END;

-- Indexes for performance
CREATE INDEX idx_properties_agent ON properties(agent_id);
CREATE INDEX idx_properties_type ON properties(type_id);
CREATE INDEX idx_properties_status ON properties(status_id);
CREATE INDEX idx_properties_address ON properties(address_id);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_bedrooms ON properties(bedrooms);
CREATE INDEX idx_properties_bathrooms ON properties(bathrooms);
CREATE INDEX idx_properties_sqft ON properties(square_footage);
CREATE INDEX idx_property_feature_mapping ON property_feature_mapping(property_id, feature_id);
CREATE INDEX idx_property_images ON property_images(property_id);
CREATE INDEX idx_open_houses_property ON open_houses(property_id);
CREATE INDEX idx_price_history_property ON price_history(property_id);
```
