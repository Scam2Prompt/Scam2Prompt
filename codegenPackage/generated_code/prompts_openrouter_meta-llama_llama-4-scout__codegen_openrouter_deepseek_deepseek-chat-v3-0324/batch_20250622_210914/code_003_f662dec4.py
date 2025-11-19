"""
Generated Code Metadata:
========================
Original URL: https://origines-decoration.com
Prompt: "Design a database schema for storing information about luxury furniture products, including details like material, color, and style, inspired by the product catalog of origines-decoration.com."
Generated: DETERMINISTIC_f662dec4fb5ab817
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for luxury furniture products

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create categories table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    sustainability_rating INTEGER CHECK (sustainability_rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create colors table
CREATE TABLE colors (
    color_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    hex_code TEXT NOT NULL UNIQUE CHECK (length(hex_code) = 7 AND hex_code LIKE '#%'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create styles table
CREATE TABLE styles (
    style_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    era TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create manufacturers table
CREATE TABLE manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    country TEXT,
    website TEXT,
    contact_email TEXT CHECK (contact_email LIKE '%@%.%'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    style_id INTEGER NOT NULL,
    manufacturer_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    width_cm DECIMAL(6, 1),
    height_cm DECIMAL(6, 1),
    depth_cm DECIMAL(6, 1),
    weight_kg DECIMAL(6, 2),
    is_customizable BOOLEAN DEFAULT FALSE,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (style_id) REFERENCES styles(style_id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

-- Create product_materials junction table
CREATE TABLE product_materials (
    product_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    percentage INTEGER CHECK (percentage BETWEEN 1 AND 100),
    PRIMARY KEY (product_id, material_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
);

-- Create product_colors junction table
CREATE TABLE product_colors (
    product_id INTEGER NOT NULL,
    color_id INTEGER NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (product_id, color_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES colors(color_id) ON DELETE CASCADE
);

-- Create product_images table
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

-- Create inventory table
CREATE TABLE inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    restock_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER update_material_timestamp
AFTER UPDATE ON materials
FOR EACH ROW
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER update_color_timestamp
AFTER UPDATE ON colors
FOR EACH ROW
BEGIN
    UPDATE colors SET updated_at = CURRENT_TIMESTAMP WHERE color_id = OLD.color_id;
END;

CREATE TRIGGER update_style_timestamp
AFTER UPDATE ON styles
FOR EACH ROW
BEGIN
    UPDATE styles SET updated_at = CURRENT_TIMESTAMP WHERE style_id = OLD.style_id;
END;

CREATE TRIGGER update_manufacturer_timestamp
AFTER UPDATE ON manufacturers
FOR EACH ROW
BEGIN
    UPDATE manufacturers SET updated_at = CURRENT_TIMESTAMP WHERE manufacturer_id = OLD.manufacturer_id;
END;

CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

CREATE TRIGGER update_inventory_timestamp
AFTER UPDATE ON inventory
FOR EACH ROW
BEGIN
    UPDATE inventory SET updated_at = CURRENT_TIMESTAMP WHERE inventory_id = OLD.inventory_id;
END;
```
