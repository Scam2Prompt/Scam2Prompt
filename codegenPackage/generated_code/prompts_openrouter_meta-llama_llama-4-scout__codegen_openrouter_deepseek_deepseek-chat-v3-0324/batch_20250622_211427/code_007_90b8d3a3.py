"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Design a database schema to store information about small-batch producers, cooking oils, and their regions, inspired by Authentic Oil's curated selection and regional diversity.
Generated: DETERMINISTIC_90b8d3a39bd56cb6
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for small-batch producers, cooking oils, and regions

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create regions table to store geographical information
CREATE TABLE regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    description TEXT,
    climate TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_region UNIQUE (name, country)
);

-- Create producers table to store information about small-batch producers
CREATE TABLE producers (
    producer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    region_id INTEGER NOT NULL,
    founded_year INTEGER,
    description TEXT,
    production_capacity TEXT,
    sustainability_practices TEXT,
    website_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (region_id) REFERENCES regions(region_id) ON DELETE RESTRICT,
    CONSTRAINT valid_website_url CHECK (website_url LIKE 'http%' OR website_url IS NULL)
);

-- Create oil_types table for different types of cooking oils
CREATE TABLE oil_types (
    oil_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    smoke_point_celsius INTEGER,
    health_benefits TEXT,
    common_uses TEXT
);

-- Create oils table to store specific oil products
CREATE TABLE oils (
    oil_id INTEGER PRIMARY KEY AUTOINCREMENT,
    producer_id INTEGER NOT NULL,
    oil_type_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    harvest_year INTEGER,
    extraction_method TEXT NOT NULL,
    flavor_profile TEXT,
    price_per_ml REAL NOT NULL,
    is_organic BOOLEAN DEFAULT FALSE,
    is_cold_pressed BOOLEAN DEFAULT FALSE,
    certification TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producer_id) REFERENCES producers(producer_id) ON DELETE CASCADE,
    FOREIGN KEY (oil_type_id) REFERENCES oil_types(oil_type_id) ON DELETE RESTRICT,
    CONSTRAINT positive_price CHECK (price_per_ml > 0),
    CONSTRAINT valid_harvest_year CHECK (harvest_year > 1900 AND harvest_year <= strftime('%Y', 'now'))
);

-- Create indexes for performance optimization
CREATE INDEX idx_producer_region ON producers(region_id);
CREATE INDEX idx_oil_producer ON oils(producer_id);
CREATE INDEX idx_oil_type ON oils(oil_type_id);

-- Create triggers for automatic updated_at timestamps
CREATE TRIGGER update_region_timestamp
AFTER UPDATE ON regions
BEGIN
    UPDATE regions SET updated_at = CURRENT_TIMESTAMP WHERE region_id = OLD.region_id;
END;

CREATE TRIGGER update_producer_timestamp
AFTER UPDATE ON producers
BEGIN
    UPDATE producers SET updated_at = CURRENT_TIMESTAMP WHERE producer_id = OLD.producer_id;
END;

CREATE TRIGGER update_oil_timestamp
AFTER UPDATE ON oils
BEGIN
    UPDATE oils SET updated_at = CURRENT_TIMESTAMP WHERE oil_id = OLD.oil_id;
END;
```
