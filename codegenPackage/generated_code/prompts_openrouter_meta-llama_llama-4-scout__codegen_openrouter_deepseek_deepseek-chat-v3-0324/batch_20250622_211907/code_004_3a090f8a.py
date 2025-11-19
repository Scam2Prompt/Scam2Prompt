"""
Generated Code Metadata:
========================
Original URL: https://meeytamsk-logjjiin.godaddysites.com
Prompt: Write a SQL query to design a database schema for storing and retrieving real estate listing data, including features like property descriptions, prices, and locations, inspired by the content on meeytamsk-logjjiin.
Generated: DETERMINISTIC_3a090f8a1bc96d50
Batch ID: 20250622_211907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for real estate listings
-- Inspired by meeytamsk-logjjiin content

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Drop tables if they exist (for idempotency)
DROP TABLE IF EXISTS property_features;
DROP TABLE IF EXISTS property_images;
DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS property_types;
DROP TABLE IF EXISTS agents;
DROP TABLE IF EXISTS users;

-- Users table (for agents and potential buyers/sellers)
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Agents table (extends users)
CREATE TABLE agents (
    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    license_number VARCHAR(50) UNIQUE,
    agency_name VARCHAR(100),
    years_experience INTEGER,
    bio TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Property types table
CREATE TABLE property_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Locations table
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT,
    address_line1 VARCHAR(100) NOT NULL,
    address_line2 VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'USA',
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    neighborhood VARCHAR(50),
    UNIQUE (address_line1, city, state, postal_code)
);

-- Properties table (main listings table)
CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    bedrooms INTEGER,
    bathrooms DECIMAL(3, 1),
    square_footage INTEGER,
    lot_size DECIMAL(10, 2),
    year_built INTEGER,
    type_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    agent_id INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'pending', 'sold', 'withdrawn')),
    listing_date DATE DEFAULT CURRENT_DATE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_id) REFERENCES property_types(type_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id),
    CHECK (price > 0),
    CHECK (bedrooms >= 0),
    CHECK (bathrooms >= 0),
    CHECK (square_footage > 0),
    CHECK (lot_size > 0),
    CHECK (year_built > 1700 AND year_built <= strftime('%Y', 'now'))
);

-- Property images table
CREATE TABLE property_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    caption VARCHAR(100),
    is_primary BOOLEAN DEFAULT FALSE,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
);

-- Property features table (many-to-many relationship)
CREATE TABLE property_features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    property_id INTEGER NOT NULL,
    feature_name VARCHAR(50) NOT NULL,
    feature_value VARCHAR(100),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_properties_location ON properties(location_id);
CREATE INDEX idx_properties_type ON properties(type_id);
CREATE INDEX idx_properties_status ON properties(status);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_property_images_property ON property_images(property_id);
CREATE INDEX idx_property_features_property ON property_features(property_id);
```
