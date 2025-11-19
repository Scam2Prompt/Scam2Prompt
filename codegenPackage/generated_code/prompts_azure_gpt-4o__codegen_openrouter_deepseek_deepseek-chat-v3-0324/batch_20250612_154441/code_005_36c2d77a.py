"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Create a database schema to store information about various rubber flooring products (e.g., Eva Mats, EPDM) and their applications in areas like parking lots and sports fields, based on Rubber Flooring Indonesia's offerings.
Generated: DETERMINISTIC_36c2d77a4679e445
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Rubber Flooring Indonesia product catalog
-- Supports storing product information, applications, and specifications

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
BEGIN TRANSACTION;

-- Product categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product materials table
CREATE TABLE IF NOT EXISTS materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    durability_rating INTEGER CHECK (durability_rating BETWEEN 1 AND 10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    thickness_mm REAL NOT NULL CHECK (thickness_mm > 0),
    width_mm REAL NOT NULL CHECK (width_mm > 0),
    length_mm REAL NOT NULL CHECK (length_mm > 0),
    color_options TEXT,
    price_per_sqm REAL CHECK (price_per_sqm >= 0),
    is_available BOOLEAN DEFAULT TRUE,
    description TEXT,
    technical_specs TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Application areas table
CREATE TABLE IF NOT EXISTS application_areas (
    area_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Junction table for product applications
CREATE TABLE IF NOT EXISTS product_applications (
    product_id INTEGER NOT NULL,
    area_id INTEGER NOT NULL,
    suitability_rating INTEGER CHECK (suitability_rating BETWEEN 1 AND 5),
    notes TEXT,
    PRIMARY KEY (product_id, area_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (area_id) REFERENCES application_areas(area_id) ON DELETE CASCADE
);

-- Product images table
CREATE TABLE IF NOT EXISTS product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    caption TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER IF NOT EXISTS update_category_timestamp
AFTER UPDATE ON categories
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = NEW.category_id;
END;

CREATE TRIGGER IF NOT EXISTS update_material_timestamp
AFTER UPDATE ON materials
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = NEW.material_id;
END;

CREATE TRIGGER IF NOT EXISTS update_product_timestamp
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = NEW.product_id;
END;

CREATE TRIGGER IF NOT EXISTS update_application_area_timestamp
AFTER UPDATE ON application_areas
BEGIN
    UPDATE application_areas SET updated_at = CURRENT_TIMESTAMP WHERE area_id = NEW.area_id;
END;

COMMIT;

-- Insert initial data for categories
INSERT OR IGNORE INTO categories (name, description) VALUES 
('EVA Mats', 'Ethylene-vinyl acetate foam mats for various applications'),
('EPDM Flooring', 'Ethylene propylene diene monomer rubber flooring'),
('Rubber Tiles', 'Interlocking rubber tiles for versatile use'),
('Rolled Rubber', 'Continuous rolled rubber flooring solutions');

-- Insert initial data for materials
INSERT OR IGNORE INTO materials (name, description, durability_rating) VALUES 
('EVA', 'Ethylene-vinyl acetate foam', 7),
('EPDM', 'Ethylene propylene diene monomer rubber', 9),
('SBR', 'Styrene-butadiene rubber', 8),
('NBR', 'Nitrile rubber', 6),
('Recycled Rubber', 'Made from recycled rubber materials', 8);

-- Insert initial data for application areas
INSERT OR IGNORE INTO application_areas (name, description) VALUES 
('Parking Lots', 'Vehicle parking areas and garages'),
('Sports Fields', 'Athletic tracks and sports facilities'),
('Playgrounds', 'Children''s play areas and schools'),
('Gyms', 'Fitness centers and workout areas'),
('Industrial', 'Factories and warehouses'),
('Commercial', 'Retail spaces and offices');
```
