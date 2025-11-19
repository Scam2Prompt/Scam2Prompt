"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: "Design a database schema to store information about various agricultural products, including fertilizers, bio stimulants, and their applications."
Generated: DETERMINISTIC_384e47212bd87e68
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for agricultural products management

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for product categories
CREATE TABLE product_categories (
    category_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_category_name UNIQUE (name)
);

-- Table for manufacturers
CREATE TABLE manufacturers (
    manufacturer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    website VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_manufacturer_name UNIQUE (name)
);

-- Table for products
CREATE TABLE products (
    product_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id UUID NOT NULL,
    manufacturer_id UUID NOT NULL,
    active_ingredients TEXT,
    application_method TEXT,
    dosage_instructions TEXT,
    storage_conditions TEXT,
    safety_precautions TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES product_categories(category_id),
    CONSTRAINT fk_manufacturer FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id),
    CONSTRAINT unique_product_name_per_manufacturer UNIQUE (name, manufacturer_id)
);

-- Table for crops
CREATE TABLE crops (
    crop_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    scientific_name VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_crop_name UNIQUE (name)
);

-- Table for product applications (linking products to crops)
CREATE TABLE product_applications (
    application_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID NOT NULL,
    crop_id UUID NOT NULL,
    growth_stage VARCHAR(100),
    application_rate VARCHAR(100),
    frequency VARCHAR(100),
    optimal_conditions TEXT,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT fk_crop FOREIGN KEY (crop_id) REFERENCES crops(crop_id) ON DELETE CASCADE,
    CONSTRAINT unique_product_crop_combination UNIQUE (product_id, crop_id)
);

-- Table for regulatory information
CREATE TABLE product_regulations (
    regulation_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID NOT NULL,
    country_code VARCHAR(2) NOT NULL,
    registration_number VARCHAR(100),
    registration_status VARCHAR(50),
    registration_date DATE,
    expiry_date DATE,
    restrictions TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    CONSTRAINT unique_product_country_combination UNIQUE (product_id, country_code)
);

-- Indexes for performance optimization
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_manufacturer ON products(manufacturer_id);
CREATE INDEX idx_product_applications_product ON product_applications(product_id);
CREATE INDEX idx_product_applications_crop ON product_applications(crop_id);
CREATE INDEX idx_product_regulations_product ON product_regulations(product_id);

-- Trigger function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for all tables with updated_at field
CREATE TRIGGER update_product_categories_timestamp
BEFORE UPDATE ON product_categories
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_manufacturers_timestamp
BEFORE UPDATE ON manufacturers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_crops_timestamp
BEFORE UPDATE ON crops
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_product_applications_timestamp
BEFORE UPDATE ON product_applications
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_product_regulations_timestamp
BEFORE UPDATE ON product_regulations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
