"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: How can I create a database schema to store information about железобетонные изделия and their suppliers in Санкт-Петербурге, as described on the Paradigma site?
Generated: DETERMINISTIC_f373f88d41876a0e
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# PostgreSQL Database Schema for железобетонные изделия (Reinforced Concrete Products) and Suppliers

```sql
-- Database schema for reinforced concrete products and suppliers in Saint Petersburg
-- Designed based on typical requirements for construction materials tracking

CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    address TEXT NOT NULL,
    city VARCHAR(50) DEFAULT 'Санкт-Петербург',
    registration_number VARCHAR(50),
    tax_id VARCHAR(50),
    quality_certification VARCHAR(100),
    year_established INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email IS NULL OR email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

CREATE TABLE product_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    UNIQUE(category_name)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_code VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    category_id INTEGER REFERENCES product_categories(category_id),
    description TEXT,
    dimensions VARCHAR(50),
    weight_kg DECIMAL(10,2),
    volume_m3 DECIMAL(10,3),
    strength_class VARCHAR(20),
    frost_resistance VARCHAR(20),
    water_resistance VARCHAR(20),
    reinforcement_type VARCHAR(50),
    unit_of_measure VARCHAR(10) DEFAULT 'шт',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(product_code)
);

CREATE TABLE supplier_products (
    supplier_product_id SERIAL PRIMARY KEY,
    supplier_id INTEGER NOT NULL REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    price_per_unit DECIMAL(12,2) NOT NULL,
    min_order_quantity INTEGER DEFAULT 1,
    delivery_time_days INTEGER,
    available_quantity INTEGER,
    production_lead_time_days INTEGER,
    is_available BOOLEAN DEFAULT TRUE,
    last_price_update TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(supplier_id, product_id)
);

CREATE TABLE product_documents (
    document_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL,
    document_name VARCHAR(100) NOT NULL,
    file_path TEXT NOT NULL,
    issue_date DATE,
    expiration_date DATE,
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE supplier_reviews (
    review_id SERIAL PRIMARY KEY,
    supplier_id INTEGER NOT NULL REFERENCES suppliers(supplier_id) ON DELETE CASCADE,
    reviewer_name VARCHAR(100),
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    review_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_approved BOOLEAN DEFAULT FALSE
);

-- Indexes for better performance
CREATE INDEX idx_suppliers_city ON suppliers(city);
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_supplier_products_product ON supplier_products(product_id);
CREATE INDEX idx_supplier_products_supplier ON supplier_products(supplier_id);
CREATE INDEX idx_product_documents_product ON product_documents(product_id);
CREATE INDEX idx_supplier_reviews_supplier ON supplier_reviews(supplier_id);

-- Trigger to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_suppliers_timestamp
BEFORE UPDATE ON suppliers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
