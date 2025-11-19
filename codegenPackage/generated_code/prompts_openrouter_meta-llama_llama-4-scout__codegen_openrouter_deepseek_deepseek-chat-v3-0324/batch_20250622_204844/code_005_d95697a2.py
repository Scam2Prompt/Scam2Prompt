"""
Generated Code Metadata:
========================
Original URL: https://thechampionsshop.com
Prompt: Design a database schema to store information about wrestling belts, including title names, promotions, materials, and prices, similar to The Champions Shop catalog.
Generated: DETERMINISTIC_d95697a2d40fcacd
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for wrestling belts catalog
CREATE TABLE promotions (
    promotion_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    founded_year INTEGER,
    headquarters VARCHAR(100),
    website VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE belt_materials (
    material_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    durability_rating INTEGER CHECK (durability_rating BETWEEN 1 AND 10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE belt_titles (
    title_id SERIAL PRIMARY KEY,
    promotion_id INTEGER REFERENCES promotions(promotion_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    first_champion VARCHAR(100),
    date_established DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE belt_products (
    product_id SERIAL PRIMARY KEY,
    title_id INTEGER REFERENCES belt_titles(title_id),
    material_id INTEGER REFERENCES belt_materials(material_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    weight_lbs DECIMAL(5, 2),
    plate_count INTEGER,
    in_stock BOOLEAN DEFAULT TRUE,
    stock_quantity INTEGER DEFAULT 0,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE belt_variants (
    variant_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES belt_products(product_id),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    additional_price DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better performance
CREATE INDEX idx_belt_titles_promotion ON belt_titles(promotion_id);
CREATE INDEX idx_belt_products_title ON belt_products(title_id);
CREATE INDEX idx_belt_products_material ON belt_products(material_id);
CREATE INDEX idx_belt_variants_product ON belt_variants(product_id);

-- Function to update timestamp on row update
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_promotions_timestamp
BEFORE UPDATE ON promotions
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_belt_materials_timestamp
BEFORE UPDATE ON belt_materials
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_belt_titles_timestamp
BEFORE UPDATE ON belt_titles
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_belt_products_timestamp
BEFORE UPDATE ON belt_products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_belt_variants_timestamp
BEFORE UPDATE ON belt_variants
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
