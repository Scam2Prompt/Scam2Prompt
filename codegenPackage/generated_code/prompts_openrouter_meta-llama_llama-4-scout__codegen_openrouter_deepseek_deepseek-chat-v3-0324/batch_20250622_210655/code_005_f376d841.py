"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: Design a database schema to store information on health products and their classifications in Thailand.
Generated: DETERMINISTIC_f376d8416bd73202
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for health products and classifications in Thailand

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Product categories table
CREATE TABLE product_categories (
    category_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_category_name UNIQUE (category_name)
);

-- Product classifications table (e.g., FDA classifications)
CREATE TABLE product_classifications (
    classification_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    classification_name VARCHAR(100) NOT NULL,
    description TEXT,
    regulatory_code VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_classification_name UNIQUE (classification_name)
);

-- Manufacturers table
CREATE TABLE manufacturers (
    manufacturer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    address TEXT,
    contact_number VARCHAR(20),
    email VARCHAR(100),
    license_number VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_manufacturer_name UNIQUE (name)
);

-- Products table
CREATE TABLE products (
    product_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id UUID REFERENCES product_categories(category_id),
    classification_id UUID REFERENCES product_classifications(classification_id),
    manufacturer_id UUID REFERENCES manufacturers(manufacturer_id),
    registration_number VARCHAR(50),
    dosage_form VARCHAR(50),
    active_ingredients TEXT,
    indications TEXT,
    precautions TEXT,
    storage_conditions TEXT,
    expiry_duration_months INTEGER,
    thai_fda_approved BOOLEAN DEFAULT FALSE,
    approval_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_registration_number UNIQUE (registration_number)
);

-- Product prices table (for tracking price changes over time)
CREATE TABLE product_prices (
    price_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID REFERENCES products(product_id),
    price NUMERIC(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'THB',
    effective_date DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_price CHECK (price > 0)
);

-- Product images table
CREATE TABLE product_images (
    image_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID REFERENCES products(product_id),
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic updated_at
CREATE TRIGGER update_product_categories_modtime
BEFORE UPDATE ON product_categories
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_product_classifications_modtime
BEFORE UPDATE ON product_classifications
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_manufacturers_modtime
BEFORE UPDATE ON manufacturers
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_products_modtime
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

-- Indexes for performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_classification ON products(classification_id);
CREATE INDEX idx_products_manufacturer ON products(manufacturer_id);
CREATE INDEX idx_product_prices_product ON product_prices(product_id);
CREATE INDEX idx_product_images_product ON product_images(product_id);
```
