"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Create a database schema for managing a catalog of reinforced concrete products (ЖБИ) with categories such as "road and railway construction" and "energy construction," inspired by the organization of the catalog on paradigmagbi.ru.
Generated: DETERMINISTIC_daca10f1fe6e60e2
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for reinforced concrete products (ЖБИ) catalog

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create enum for product status
CREATE TYPE product_status AS ENUM ('active', 'discontinued', 'coming_soon');

-- Categories table
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    slug VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    parent_id UUID REFERENCES categories(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_featured BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0
);

-- Products table
CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(200) NOT NULL,
    slug VARCHAR(200) NOT NULL UNIQUE,
    short_description TEXT,
    full_description TEXT,
    technical_specifications JSONB,
    status product_status DEFAULT 'active',
    category_id UUID REFERENCES categories(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    weight_kg DECIMAL(10, 2),
    dimensions VARCHAR(100),
    material_grade VARCHAR(50),
    standard VARCHAR(100),
    price DECIMAL(12, 2),
    is_featured BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0
);

-- Product images table
CREATE TABLE product_images (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(100),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Product documents (specs, certificates, etc.)
CREATE TABLE product_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    document_url VARCHAR(255) NOT NULL,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Product variants (different sizes, configurations)
CREATE TABLE product_variants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    sku VARCHAR(50) UNIQUE,
    price DECIMAL(12, 2),
    weight_kg DECIMAL(10, 2),
    dimensions VARCHAR(100),
    stock_quantity INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better performance
CREATE INDEX idx_categories_parent_id ON categories(parent_id);
CREATE INDEX idx_products_category_id ON products(category_id);
CREATE INDEX idx_product_images_product_id ON product_images(product_id);
CREATE INDEX idx_product_documents_product_id ON product_documents(product_id);
CREATE INDEX idx_product_variants_product_id ON product_variants(product_id);

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_categories_timestamp
BEFORE UPDATE ON categories
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_product_variants_timestamp
BEFORE UPDATE ON product_variants
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Insert initial categories
INSERT INTO categories (id, name, slug, description, is_featured, display_order) VALUES
    ('11111111-1111-1111-1111-111111111111', 'Road and Railway Construction', 'road-railway-construction', 'Products for road and railway infrastructure', TRUE, 1),
    ('22222222-2222-2222-2222-222222222222', 'Energy Construction', 'energy-construction', 'Products for energy sector construction', TRUE, 2),
    ('33333333-3333-3333-3333-333333333333', 'Industrial Construction', 'industrial-construction', 'Products for industrial facilities', FALSE, 3),
    ('44444444-4444-4444-4444-444444444444', 'Civil Construction', 'civil-construction', 'Products for residential and public buildings', FALSE, 4);
```
