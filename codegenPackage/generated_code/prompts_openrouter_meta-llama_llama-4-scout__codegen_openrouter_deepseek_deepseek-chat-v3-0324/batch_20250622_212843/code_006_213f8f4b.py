"""
Generated Code Metadata:
========================
Original URL: https://florerialima.com
Prompt: Generate a SQL query to create a database schema for storing Florería Lima's product catalog, including tables for products, prices, and inventory.
Generated: DETERMINISTIC_213f8f4b4ecf59d7
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Florería Lima product catalog
CREATE SCHEMA florerialima;

SET search_path TO florerialima;

-- Product categories table
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES categories(category_id),
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    image_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product variants (e.g., different sizes/colors of the same flower arrangement)
CREATE TABLE variants (
    variant_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    variant_name VARCHAR(50) NOT NULL,
    sku VARCHAR(20) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Pricing information
CREATE TABLE prices (
    price_id SERIAL PRIMARY KEY,
    variant_id INTEGER REFERENCES variants(variant_id) ON DELETE CASCADE,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    cost DECIMAL(10, 2),
    is_current BOOLEAN DEFAULT TRUE,
    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valid_to TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inventory tracking
CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    variant_id INTEGER REFERENCES variants(variant_id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    last_restocked TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product tags for search and categorization
CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    tag_name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product-tag mapping
CREATE TABLE product_tags (
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (product_id, tag_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_variants_product ON variants(product_id);
CREATE INDEX idx_prices_variant ON prices(variant_id);
CREATE INDEX idx_inventory_variant ON inventory(variant_id);
CREATE INDEX idx_product_tags_product ON product_tags(product_id);
CREATE INDEX idx_product_tags_tag ON product_tags(tag_id);

-- Trigger to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_product_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_variant_timestamp
BEFORE UPDATE ON variants
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_inventory_timestamp
BEFORE UPDATE ON inventory
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- View for active products with current prices
CREATE VIEW active_products_with_prices AS
SELECT 
    p.product_id,
    p.product_name,
    p.description,
    p.image_url,
    c.category_name,
    v.variant_id,
    v.variant_name,
    v.sku,
    pr.price,
    pr.cost,
    i.quantity
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id
JOIN 
    variants v ON p.product_id = v.product_id
JOIN 
    prices pr ON v.variant_id = pr.variant_id AND pr.is_current = TRUE
JOIN 
    inventory i ON v.variant_id = i.variant_id
WHERE 
    p.is_active = TRUE;
```
