"""
Generated Code Metadata:
========================
Original URL: https://tuningdesign.gr
Prompt: "Design a database schema to store information about car models, tuning accessories, and their compatibility, using the Tuning Design website as a reference."
Generated: DETERMINISTIC_ff28960e53b0a060
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for car models, tuning accessories, and compatibility

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create manufacturers table
CREATE TABLE manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    country TEXT,
    founded_year INTEGER,
    logo_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create car_models table
CREATE TABLE car_models (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    generation TEXT,
    production_start_year INTEGER,
    production_end_year INTEGER,
    body_type TEXT CHECK(body_type IN ('Sedan', 'Coupe', 'Hatchback', 'SUV', 'Truck', 'Convertible', 'Van', 'Wagon')),
    engine_type TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE CASCADE,
    UNIQUE (manufacturer_id, name, generation)
);

-- Create categories table for tuning accessories
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    parent_category_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

-- Create accessories table
CREATE TABLE accessories (
    accessory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) CHECK(price >= 0),
    material TEXT,
    weight_kg DECIMAL(6, 2),
    manufacturer TEXT,
    part_number TEXT UNIQUE,
    stock_quantity INTEGER DEFAULT 0 CHECK(stock_quantity >= 0),
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create compatibility table (junction table between car_models and accessories)
CREATE TABLE compatibility (
    compatibility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL,
    accessory_id INTEGER NOT NULL,
    notes TEXT,
    fitment_rating INTEGER CHECK(fitment_rating BETWEEN 1 AND 5),
    requires_modification BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES car_models(model_id) ON DELETE CASCADE,
    FOREIGN KEY (accessory_id) REFERENCES accessories(accessory_id) ON DELETE CASCADE,
    UNIQUE (model_id, accessory_id)
);

-- Create indexes for performance
CREATE INDEX idx_car_models_manufacturer ON car_models(manufacturer_id);
CREATE INDEX idx_accessories_category ON accessories(category_id);
CREATE INDEX idx_compatibility_model ON compatibility(model_id);
CREATE INDEX idx_compatibility_accessory ON compatibility(accessory_id);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_manufacturers_timestamp
AFTER UPDATE ON manufacturers
BEGIN
    UPDATE manufacturers SET updated_at = CURRENT_TIMESTAMP WHERE manufacturer_id = OLD.manufacturer_id;
END;

CREATE TRIGGER update_car_models_timestamp
AFTER UPDATE ON car_models
BEGIN
    UPDATE car_models SET updated_at = CURRENT_TIMESTAMP WHERE model_id = OLD.model_id;
END;

CREATE TRIGGER update_categories_timestamp
AFTER UPDATE ON categories
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER update_accessories_timestamp
AFTER UPDATE ON accessories
BEGIN
    UPDATE accessories SET updated_at = CURRENT_TIMESTAMP WHERE accessory_id = OLD.accessory_id;
END;

CREATE TRIGGER update_compatibility_timestamp
AFTER UPDATE ON compatibility
BEGIN
    UPDATE compatibility SET updated_at = CURRENT_TIMESTAMP WHERE compatibility_id = OLD.compatibility_id;
END;
```
