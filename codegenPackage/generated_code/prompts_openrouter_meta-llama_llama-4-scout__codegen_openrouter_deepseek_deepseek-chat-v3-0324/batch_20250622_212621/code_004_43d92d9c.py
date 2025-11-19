"""
Generated Code Metadata:
========================
Original URL: https://the-quantcastz.net
Prompt: Design a database schema to store Quantcast's product information, including details for furniture products with Swiss movement-powered watches.
Generated: DETERMINISTIC_43d92d9c5bb4570e
Batch ID: 20250622_212621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Quantcast product information with Swiss movement watches

CREATE TABLE brands (
    brand_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(100) NOT NULL,
    description TEXT,
    founded_year INT,
    headquarters VARCHAR(100),
    website_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    parent_category_id INT REFERENCES product_categories(category_id),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    brand_id INT NOT NULL REFERENCES brands(brand_id),
    category_id INT NOT NULL REFERENCES product_categories(category_id),
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    sku VARCHAR(50) UNIQUE NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE furniture_products (
    product_id INT PRIMARY KEY REFERENCES products(product_id),
    material VARCHAR(100),
    dimensions VARCHAR(50),
    weight_kg DECIMAL(6, 2),
    color VARCHAR(50),
    assembly_required BOOLEAN DEFAULT FALSE,
    warranty_months INT
);

CREATE TABLE watch_movements (
    movement_id SERIAL PRIMARY KEY,
    movement_name VARCHAR(100) NOT NULL,
    movement_type VARCHAR(50) NOT NULL CHECK (movement_type IN ('Automatic', 'Manual', 'Quartz', 'Solar')),
    jewels_count INT,
    power_reserve_hours INT,
    accuracy_seconds_per_day DECIMAL(5, 2),
    is_swiss_made BOOLEAN DEFAULT FALSE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE watch_products (
    product_id INT PRIMARY KEY REFERENCES products(product_id),
    movement_id INT NOT NULL REFERENCES watch_movements(movement_id),
    case_material VARCHAR(50),
    case_diameter_mm DECIMAL(5, 2),
    water_resistance_meters INT,
    dial_color VARCHAR(50),
    strap_material VARCHAR(50),
    features TEXT,
    warranty_years INT DEFAULT 2
);

CREATE TABLE product_images (
    image_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES products(product_id),
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    alt_text VARCHAR(255),
    display_order INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES products(product_id),
    quantity INT NOT NULL DEFAULT 0,
    restock_threshold INT DEFAULT 10,
    last_restocked DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_tags (
    tag_id SERIAL PRIMARY KEY,
    tag_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_tag_mapping (
    product_id INT NOT NULL REFERENCES products(product_id),
    tag_id INT NOT NULL REFERENCES product_tags(tag_id),
    PRIMARY KEY (product_id, tag_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_products_brand_id ON products(brand_id);
CREATE INDEX idx_products_category_id ON products(category_id);
CREATE INDEX idx_product_images_product_id ON product_images(product_id);
CREATE INDEX idx_inventory_product_id ON inventory(product_id);
CREATE INDEX idx_product_tag_mapping_product_id ON product_tag_mapping(product_id);
CREATE INDEX idx_product_tag_mapping_tag_id ON product_tag_mapping(tag_id);
```
