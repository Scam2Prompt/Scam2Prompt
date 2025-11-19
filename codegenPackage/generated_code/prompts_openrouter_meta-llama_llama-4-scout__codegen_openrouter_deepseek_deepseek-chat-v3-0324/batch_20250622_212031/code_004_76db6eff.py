"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Design a database schema to store information about various air conditioning systems, including their specifications and prices, similar to those listed on frigoterm.ro."
Generated: DETERMINISTIC_76db6eff4a9e177a
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for air conditioning systems

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Manufacturers table
CREATE TABLE manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    website TEXT,
    country TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Categories table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    model_number TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    energy_efficiency_class TEXT CHECK(energy_efficiency_class IN ('A+++', 'A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G')),
    cooling_capacity_btu INTEGER,
    cooling_capacity_kw REAL,
    heating_capacity_btu INTEGER,
    heating_capacity_kw REAL,
    power_input_cooling_w REAL,
    power_input_heating_w REAL,
    noise_level_db REAL,
    refrigerant_type TEXT,
    dimensions TEXT,
    weight_kg REAL,
    warranty_years INTEGER,
    is_inverter BOOLEAN DEFAULT FALSE,
    is_smart BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    UNIQUE(manufacturer_id, model_number)
);

-- Prices table
CREATE TABLE prices (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    price_ron REAL NOT NULL CHECK(price_ron > 0),
    vat_percentage REAL DEFAULT 19.0 CHECK(vat_percentage >= 0),
    discount_percentage REAL DEFAULT 0.0 CHECK(discount_percentage >= 0 AND discount_percentage <= 100),
    valid_from DATE NOT NULL,
    valid_to DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Features table
CREATE TABLE features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product features junction table
CREATE TABLE product_features (
    product_id INTEGER NOT NULL,
    feature_id INTEGER NOT NULL,
    PRIMARY KEY (product_id, feature_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (feature_id) REFERENCES features(feature_id)
);

-- Product images table
CREATE TABLE product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    alt_text TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Stock table
CREATE TABLE stock (
    stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0),
    warehouse_location TEXT,
    last_restocked DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Trigger to update timestamps on row modification
CREATE TRIGGER update_manufacturers_timestamp
AFTER UPDATE ON manufacturers
BEGIN
    UPDATE manufacturers SET updated_at = CURRENT_TIMESTAMP WHERE manufacturer_id = NEW.manufacturer_id;
END;

CREATE TRIGGER update_categories_timestamp
AFTER UPDATE ON categories
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = NEW.category_id;
END;

CREATE TRIGGER update_products_timestamp
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = NEW.product_id;
END;

CREATE TRIGGER update_prices_timestamp
AFTER UPDATE ON prices
BEGIN
    UPDATE prices SET updated_at = CURRENT_TIMESTAMP WHERE price_id = NEW.price_id;
END;

CREATE TRIGGER update_features_timestamp
AFTER UPDATE ON features
BEGIN
    UPDATE features SET updated_at = CURRENT_TIMESTAMP WHERE feature_id = NEW.feature_id;
END;

CREATE TRIGGER update_product_images_timestamp
AFTER UPDATE ON product_images
BEGIN
    UPDATE product_images SET updated_at = CURRENT_TIMESTAMP WHERE image_id = NEW.image_id;
END;

CREATE TRIGGER update_stock_timestamp
AFTER UPDATE ON stock
BEGIN
    UPDATE stock SET updated_at = CURRENT_TIMESTAMP WHERE stock_id = NEW.stock_id;
END;
```
