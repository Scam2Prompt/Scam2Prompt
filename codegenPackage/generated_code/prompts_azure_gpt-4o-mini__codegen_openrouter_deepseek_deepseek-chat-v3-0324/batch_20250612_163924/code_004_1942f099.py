"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Design a database schema for storing information about commercial properties for sale, including fields for type of business, location, and price, inspired by the lighting store listing.
Generated: DETERMINISTIC_1942f099297cb395
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a commercial properties database schema
-- Includes tables for properties, business types, locations, and agents

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create business types table
CREATE TABLE IF NOT EXISTS business_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create locations table
CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'USA',
    latitude REAL,
    longitude REAL,
    UNIQUE(address, city, state, zip_code)
);

-- Create real estate agents table
CREATE TABLE IF NOT EXISTS agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    license_number TEXT NOT NULL UNIQUE
);

-- Create commercial properties table
CREATE TABLE IF NOT EXISTS commercial_properties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    business_type_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    square_footage INTEGER NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    year_built INTEGER,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    date_listed DATE NOT NULL DEFAULT CURRENT_DATE,
    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (business_type_id) REFERENCES business_types(id),
    FOREIGN KEY (location_id) REFERENCES locations(id),
    FOREIGN KEY (agent_id) REFERENCES agents(id),
    CHECK (price > 0),
    CHECK (square_footage > 0),
    CHECK (year_built > 1800 AND year_built <= strftime('%Y', 'now'))
);

-- Create property features table (many-to-many with commercial_properties)
CREATE TABLE IF NOT EXISTS property_features (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create junction table for property features
CREATE TABLE IF NOT EXISTS property_feature_mapping (
    property_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    PRIMARY KEY (property_id, feature_id),
    FOREIGN KEY (property_id) REFERENCES commercial_properties(id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES property_features(id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_properties_business_type ON commercial_properties(business_type_id);
CREATE INDEX IF NOT EXISTS idx_properties_location ON commercial_properties(location_id);
CREATE INDEX IF NOT EXISTS idx_properties_agent ON commercial_properties(agent_id);
CREATE INDEX IF NOT EXISTS idx_properties_price ON commercial_properties(price);
CREATE INDEX IF NOT EXISTS idx_properties_active ON commercial_properties(is_active);
```
