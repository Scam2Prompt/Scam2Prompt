"""
Generated Code Metadata:
========================
Original URL: https://bllabs.co
Prompt: What is the best way to structure a database for storing information about peptides and bioregulators, based on the product details from BioLongevity Labs?
Generated: DETERMINISTIC_f92ce184518e5cc7
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Peptide and Bioregulator Database Schema

```sql
-- Database schema for storing peptide and bioregulator information
-- Designed for BioLongevity Labs product details

CREATE TABLE peptides (
    peptide_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sequence VARCHAR(255) NOT NULL,
    molecular_formula VARCHAR(100),
    molecular_weight DECIMAL(10, 4),
    purity DECIMAL(5, 2),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bioregulators (
    bioregulator_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    source VARCHAR(100),
    molecular_weight DECIMAL(10, 4),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    type VARCHAR(20) CHECK (type IN ('peptide', 'bioregulator')),
    related_id INTEGER NOT NULL, -- References either peptide_id or bioregulator_id
    concentration DECIMAL(10, 4),
    concentration_unit VARCHAR(20),
    vial_size DECIMAL(10, 4),
    vial_size_unit VARCHAR(20),
    price DECIMAL(10, 2) NOT NULL,
    storage_conditions VARCHAR(100),
    shelf_life VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_benefits (
    benefit_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    benefit TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_research (
    research_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    authors VARCHAR(255),
    journal VARCHAR(100),
    publication_date DATE,
    doi VARCHAR(100),
    abstract TEXT,
    url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_usage (
    usage_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    recommended_dosage VARCHAR(100),
    administration_method VARCHAR(100),
    frequency VARCHAR(50),
    duration VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_safety (
    safety_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    side_effects TEXT,
    contraindications TEXT,
    precautions TEXT,
    interactions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_categories (
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories(category_id) ON DELETE CASCADE,
    PRIMARY KEY (product_id, category_id)
);

-- Indexes for better performance
CREATE INDEX idx_products_name ON products(name);
CREATE INDEX idx_products_sku ON products(sku);
CREATE INDEX idx_products_type ON products(type);
CREATE INDEX idx_peptides_name ON peptides(name);
CREATE INDEX idx_bioregulators_name ON bioregulators(name);
CREATE INDEX idx_product_benefits_product ON product_benefits(product_id);
CREATE INDEX idx_product_research_product ON product_research(product_id);

-- Trigger to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_peptides_timestamp
BEFORE UPDATE ON peptides
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_bioregulators_timestamp
BEFORE UPDATE ON bioregulators
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
