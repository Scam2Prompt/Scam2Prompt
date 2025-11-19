"""
Generated Code Metadata:
========================
Original URL: https://puroworldclub.com
Prompt: Develop a simple database schema to store information about cigar products, including origin, type, and pricing, inspired by the Puro World Club's product offerings.
Generated: DETERMINISTIC_b26638472193518c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for cigar products inventory
-- Inspired by Puro World Club's product offerings

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Countries table to store origin information
CREATE TABLE IF NOT EXISTS countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    region TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cigar wrapper types table
CREATE TABLE IF NOT EXISTS wrapper_types (
    wrapper_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cigar brands table
CREATE TABLE IF NOT EXISTS brands (
    brand_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    country_id INTEGER,
    founded_year INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE SET NULL
);

-- Cigar shapes table
CREATE TABLE IF NOT EXISTS shapes (
    shape_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cigar products table
CREATE TABLE IF NOT EXISTS cigars (
    cigar_id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    shape_id INTEGER,
    length REAL NOT NULL CHECK(length > 0),
    ring_gauge REAL NOT NULL CHECK(ring_gauge > 0),
    wrapper_id INTEGER,
    binder_country_id INTEGER,
    filler_country_id INTEGER,
    strength TEXT CHECK(strength IN ('Mild', 'Medium', 'Full')),
    description TEXT,
    msrp REAL CHECK(msrp > 0),
    current_price REAL CHECK(current_price > 0),
    in_stock BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id) ON DELETE CASCADE,
    FOREIGN KEY (shape_id) REFERENCES shapes(shape_id) ON DELETE SET NULL,
    FOREIGN KEY (wrapper_id) REFERENCES wrapper_types(wrapper_id) ON DELETE SET NULL,
    FOREIGN KEY (binder_country_id) REFERENCES countries(country_id) ON DELETE SET NULL,
    FOREIGN KEY (filler_country_id) REFERENCES countries(country_id) ON DELETE SET NULL,
    CONSTRAINT price_check CHECK (current_price <= msrp)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_cigars_brand ON cigars(brand_id);
CREATE INDEX IF NOT EXISTS idx_cigars_shape ON cigars(shape_id);
CREATE INDEX IF NOT EXISTS idx_cigars_wrapper ON cigars(wrapper_id);
CREATE INDEX IF NOT EXISTS idx_cigars_price ON cigars(current_price);
CREATE INDEX IF NOT EXISTS idx_cigars_stock ON cigars(in_stock) WHERE in_stock = TRUE;

-- Trigger to update timestamp on row update
CREATE TRIGGER IF NOT EXISTS update_cigars_timestamp
AFTER UPDATE ON cigars
BEGIN
    UPDATE cigars SET updated_at = CURRENT_TIMESTAMP WHERE cigar_id = NEW.cigar_id;
END;

CREATE TRIGGER IF NOT EXISTS update_brands_timestamp
AFTER UPDATE ON brands
BEGIN
    UPDATE brands SET updated_at = CURRENT_TIMESTAMP WHERE brand_id = NEW.brand_id;
END;

CREATE TRIGGER IF NOT EXISTS update_countries_timestamp
AFTER UPDATE ON countries
BEGIN
    UPDATE countries SET updated_at = CURRENT_TIMESTAMP WHERE country_id = NEW.country_id;
END;

CREATE TRIGGER IF NOT EXISTS update_wrapper_types_timestamp
AFTER UPDATE ON wrapper_types
BEGIN
    UPDATE wrapper_types SET updated_at = CURRENT_TIMESTAMP WHERE wrapper_id = NEW.wrapper_id;
END;

CREATE TRIGGER IF NOT EXISTS update_shapes_timestamp
AFTER UPDATE ON shapes
BEGIN
    UPDATE shapes SET updated_at = CURRENT_TIMESTAMP WHERE shape_id = NEW.shape_id;
END;
```
