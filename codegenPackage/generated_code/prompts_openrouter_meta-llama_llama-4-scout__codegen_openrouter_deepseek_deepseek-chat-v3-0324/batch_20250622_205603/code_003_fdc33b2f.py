"""
Generated Code Metadata:
========================
Original URL: https://oneylighter.com
Prompt: Design a simple database schema to store product information, including lighters and condoms, with fields for weight, dimensions, and product codes, inspired by the product listings on https://oneylighter.com.
Generated: DETERMINISTIC_fdc33b2fbb0b971d
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for product information storage
-- Supports products like lighters and condoms with common attributes

CREATE TABLE product_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES product_categories(category_id),
    product_code VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    weight_grams DECIMAL(10, 2),
    length_mm DECIMAL(10, 2),
    width_mm DECIMAL(10, 2),
    height_mm DECIMAL(10, 2),
    is_flame_related BOOLEAN DEFAULT FALSE,
    is_sensitive_product BOOLEAN DEFAULT FALSE,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER DEFAULT 0,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_weight CHECK (weight_grams > 0),
    CONSTRAINT positive_dimensions CHECK (length_mm > 0 AND width_mm > 0 AND height_mm > 0),
    CONSTRAINT positive_price CHECK (price > 0),
    CONSTRAINT positive_stock CHECK (stock_quantity >= 0)
);

CREATE TABLE product_attributes (
    attribute_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    attribute_name VARCHAR(50) NOT NULL,
    attribute_value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_product_attribute UNIQUE (product_id, attribute_name)
);

-- Indexes for better performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_product_code ON products(product_code);
CREATE INDEX idx_product_attributes_product ON product_attributes(product_id);

-- Triggers for maintaining updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_product_categories_timestamp
BEFORE UPDATE ON product_categories
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_product_attributes_timestamp
BEFORE UPDATE ON product_attributes
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Sample data insertion
INSERT INTO product_categories (category_name, description)
VALUES 
    ('Lighters', 'Various types of lighters including disposable and refillable'),
    ('Condoms', 'Different types of condoms with various features');

INSERT INTO products (
    category_id, product_code, name, description, 
    weight_grams, length_mm, width_mm, height_mm, 
    is_flame_related, is_sensitive_product, price, stock_quantity
) VALUES 
    (1, 'LTR-001', 'Classic Disposable Lighter', 'Single-use lighter with adjustable flame', 
     20.5, 85.0, 35.0, 12.0, TRUE, FALSE, 1.99, 1000),
    (2, 'CON-001', 'Premium Latex Condoms', 'Ultra-thin condoms for maximum sensitivity', 
     15.0, 180.0, 52.0, 5.0, FALSE, TRUE, 9.99, 500);

INSERT INTO product_attributes (product_id, attribute_name, attribute_value)
VALUES 
    (1, 'Flame Type', 'Adjustable'),
    (1, 'Fuel', 'Butane'),
    (1, 'Color', 'Black'),
    (2, 'Material', 'Latex'),
    (2, 'Count', '12'),
    (2, 'Flavor', 'Unflavored');
```
