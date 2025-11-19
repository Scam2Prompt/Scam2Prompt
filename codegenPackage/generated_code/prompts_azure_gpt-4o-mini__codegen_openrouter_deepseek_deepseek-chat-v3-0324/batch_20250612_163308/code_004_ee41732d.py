"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: Design a database schema for storing information about various types of pebbles, including their source, quality certification, and usage recommendations.
Generated: DETERMINISTIC_ee41732df0941c81
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# PostgreSQL Database Schema for Pebble Information

```sql
-- Pebble database schema
-- Tables for storing information about pebbles, their sources, certifications, and usage

CREATE TABLE pebble_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    scientific_name VARCHAR(100),
    description TEXT,
    average_size_mm DECIMAL(5,2),
    density_gcm3 DECIMAL(5,3),
    hardness_mohs DECIMAL(3,1),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_pebble_name UNIQUE (name)
);

CREATE TABLE colors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    hex_code CHAR(7),
    CONSTRAINT unique_color_name UNIQUE (name)
);

CREATE TABLE pebble_colors (
    pebble_type_id INTEGER REFERENCES pebble_types(id) ON DELETE CASCADE,
    color_id INTEGER REFERENCES colors(id) ON DELETE CASCADE,
    PRIMARY KEY (pebble_type_id, color_id)
);

CREATE TABLE sources (
    id SERIAL PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    region VARCHAR(100),
    specific_location VARCHAR(200),
    coordinates POINT,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_location UNIQUE (country, region, specific_location)
);

CREATE TABLE pebble_sources (
    pebble_type_id INTEGER REFERENCES pebble_types(id) ON DELETE CASCADE,
    source_id INTEGER REFERENCES sources(id) ON DELETE CASCADE,
    abundance VARCHAR(50),
    collection_notes TEXT,
    PRIMARY KEY (pebble_type_id, source_id)
);

CREATE TABLE certification_bodies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    website VARCHAR(255),
    description TEXT,
    CONSTRAINT unique_cert_body_name UNIQUE (name)
);

CREATE TABLE quality_certifications (
    id SERIAL PRIMARY KEY,
    pebble_type_id INTEGER REFERENCES pebble_types(id) ON DELETE CASCADE,
    certification_body_id INTEGER REFERENCES certification_bodies(id) ON DELETE CASCADE,
    certification_standard VARCHAR(100) NOT NULL,
    grade VARCHAR(50),
    issued_date DATE,
    expiry_date DATE,
    certificate_number VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_certification UNIQUE (pebble_type_id, certification_body_id, certificate_number)
);

CREATE TABLE usage_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    CONSTRAINT unique_usage_category UNIQUE (name)
);

CREATE TABLE pebble_usages (
    pebble_type_id INTEGER REFERENCES pebble_types(id) ON DELETE CASCADE,
    usage_category_id INTEGER REFERENCES usage_categories(id) ON DELETE CASCADE,
    recommendation TEXT,
    suitability_rating INTEGER CHECK (suitability_rating BETWEEN 1 AND 5),
    PRIMARY KEY (pebble_type_id, usage_category_id)
);

-- Indexes for better performance
CREATE INDEX idx_pebble_types_name ON pebble_types(name);
CREATE INDEX idx_sources_country ON sources(country);
CREATE INDEX idx_sources_region ON sources(region);
CREATE INDEX idx_quality_certifications_pebble ON quality_certifications(pebble_type_id);
CREATE INDEX idx_quality_certifications_body ON quality_certifications(certification_body_id);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_pebble_types_timestamp
BEFORE UPDATE ON pebble_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_sources_timestamp
BEFORE UPDATE ON sources
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_quality_certifications_timestamp
BEFORE UPDATE ON quality_certifications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
