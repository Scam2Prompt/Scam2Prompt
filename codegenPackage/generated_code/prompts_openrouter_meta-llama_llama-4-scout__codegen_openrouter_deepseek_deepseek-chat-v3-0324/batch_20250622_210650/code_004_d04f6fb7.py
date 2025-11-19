"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: "Design a database schema for storing information about window and door products, including their characteristics and installation services, inspired by the content on nellyservis.sk."
Generated: DETERMINISTIC_d04f6fb7d62ed642
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for window and door products with installation services

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Product categories table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    durability_rating INTEGER CHECK (durability_rating BETWEEN 1 AND 10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product colors table
CREATE TABLE colors (
    color_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hex_code TEXT NOT NULL CHECK (hex_code GLOB '#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    width DECIMAL(6, 2) CHECK (width > 0),
    height DECIMAL(6, 2) CHECK (height > 0),
    thickness DECIMAL(4, 2) CHECK (thickness > 0),
    insulation_value DECIMAL(4, 2),
    is_energy_efficient BOOLEAN DEFAULT FALSE,
    warranty_period_months INTEGER DEFAULT 24,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Product colors junction table
CREATE TABLE product_colors (
    product_id INTEGER NOT NULL,
    color_id INTEGER NOT NULL,
    is_default BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (product_id, color_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES colors(color_id) ON DELETE CASCADE
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
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Installation services table
CREATE TABLE installation_services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL CHECK (base_price >= 0),
    price_per_square_meter DECIMAL(10, 2) CHECK (price_per_square_meter >= 0),
    min_price DECIMAL(10, 2) CHECK (min_price >= 0),
    estimated_duration_hours DECIMAL(4, 1) CHECK (estimated_duration_hours > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product installation options junction table
CREATE TABLE product_installation_options (
    product_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    notes TEXT,
    PRIMARY KEY (product_id, service_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES installation_services(service_id) ON DELETE CASCADE
);

-- Product variants table (e.g., different opening mechanisms)
CREATE TABLE product_variants (
    variant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    price_adjustment DECIMAL(10, 2) DEFAULT 0,
    sku TEXT UNIQUE,
    stock_quantity INTEGER DEFAULT 0 CHECK (stock_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Product features table
CREATE TABLE product_features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    icon_url TEXT,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Product specifications table
CREATE TABLE product_specifications (
    spec_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    value TEXT NOT NULL,
    unit TEXT,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Triggers for automatic updated_at timestamps
CREATE TRIGGER update_category_timestamp
AFTER UPDATE ON categories
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = NEW.category_id;
END;

CREATE TRIGGER update_material_timestamp
AFTER UPDATE ON materials
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = NEW.material_id;
END;

CREATE TRIGGER update_color_timestamp
AFTER UPDATE ON colors
BEGIN
    UPDATE colors SET updated_at = CURRENT_TIMESTAMP WHERE color_id = NEW.color_id;
END;

CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = NEW.product_id;
END;

CREATE TRIGGER update_installation_service_timestamp
AFTER UPDATE ON installation_services
BEGIN
    UPDATE installation_services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = NEW.service_id;
END;

CREATE TRIGGER update_product_variant_timestamp
AFTER UPDATE ON product_variants
BEGIN
    UPDATE product_variants SET updated_at = CURRENT_TIMESTAMP WHERE variant_id = NEW.variant_id;
END;
```
