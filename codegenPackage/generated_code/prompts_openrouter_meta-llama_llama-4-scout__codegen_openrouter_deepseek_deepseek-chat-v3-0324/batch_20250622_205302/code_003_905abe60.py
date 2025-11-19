"""
Generated Code Metadata:
========================
Original URL: https://regency-towel.com
Prompt: Design a database schema to store information about different types of cotton used in textile production, including carded, combed, Egyptian, Turkish, and American cotton, as mentioned in Regency Towel's product range.
Generated: DETERMINISTIC_905abe60147f182c
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for cotton types used in textile production

CREATE TABLE cotton_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    fiber_length_mm DECIMAL(5,2),
    fiber_strength_cN_tex DECIMAL(5,2),
    micronaire DECIMAL(4,2),
    origin_country VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cotton_properties (
    id SERIAL PRIMARY KEY,
    cotton_type_id INTEGER REFERENCES cotton_types(id) ON DELETE CASCADE,
    absorbency_rating INTEGER CHECK (absorbency_rating BETWEEN 1 AND 10),
    softness_rating INTEGER CHECK (softness_rating BETWEEN 1 AND 10),
    durability_rating INTEGER CHECK (durability_rating BETWEEN 1 AND 10),
    typical_uses TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL,
    sustainability_rating INTEGER CHECK (sustainability_rating BETWEEN 1 AND 5),
    contact_email VARCHAR(100),
    website VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cotton_suppliers (
    cotton_type_id INTEGER REFERENCES cotton_types(id) ON DELETE CASCADE,
    supplier_id INTEGER REFERENCES suppliers(id) ON DELETE CASCADE,
    price_per_kg DECIMAL(10,2),
    available_quantity_kg DECIMAL(10,2),
    PRIMARY KEY (cotton_type_id, supplier_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    product_code VARCHAR(50) UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_cotton_composition (
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    cotton_type_id INTEGER REFERENCES cotton_types(id) ON DELETE CASCADE,
    percentage DECIMAL(5,2) CHECK (percentage > 0 AND percentage <= 100),
    PRIMARY KEY (product_id, cotton_type_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Trigger to update the updated_at timestamp on row modification
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_cotton_types_timestamp
BEFORE UPDATE ON cotton_types
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cotton_properties_timestamp
BEFORE UPDATE ON cotton_properties
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_suppliers_timestamp
BEFORE UPDATE ON suppliers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_cotton_suppliers_timestamp
BEFORE UPDATE ON cotton_suppliers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_product_cotton_composition_timestamp
BEFORE UPDATE ON product_cotton_composition
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Insert initial cotton types
INSERT INTO cotton_types (name, description, fiber_length_mm, fiber_strength_cN_tex, micronaire, origin_country)
VALUES 
    ('Carded', 'Cotton processed by carding to remove short fibers and align the remaining fibers', 25.00, 28.00, 4.20, 'Various'),
    ('Combed', 'Carded cotton that undergoes additional combing process for smoother, stronger yarn', 28.00, 30.00, 4.00, 'Various'),
    ('Egyptian', 'Premium long-staple cotton known for its softness and luster', 35.00, 32.00, 3.80, 'Egypt'),
    ('Turkish', 'High-quality cotton with excellent absorbency and durability', 30.00, 30.00, 4.10, 'Turkey'),
    ('American', 'Upland cotton known for its versatility and medium staple length', 26.00, 28.00, 4.30, 'United States');
```
