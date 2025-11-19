"""
Generated Code Metadata:
========================
Original URL: https://jgtcom.com
Prompt: Design a database schema for an online store that includes tables for premium fabrics and customer reviews, based on JGT's product categories.
Generated: DETERMINISTIC_b0d4e97685b05445
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Online Store (Premium Fabrics and Customer Reviews)

```sql
-- Database: online_store

-- Table for product categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for premium fabrics
CREATE TABLE fabrics (
    fabric_id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES categories(category_id) ON DELETE SET NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    material_composition VARCHAR(200),
    weight_gsm INTEGER,
    width_cm DECIMAL(5,2),
    price_per_meter DECIMAL(10,2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    color VARCHAR(50),
    pattern VARCHAR(50),
    origin_country VARCHAR(50),
    is_eco_friendly BOOLEAN DEFAULT FALSE,
    is_limited_edition BOOLEAN DEFAULT FALSE,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_price CHECK (price_per_meter > 0),
    CONSTRAINT positive_quantity CHECK (stock_quantity >= 0)
);

-- Table for customers
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Table for customer reviews
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    fabric_id INTEGER REFERENCES fabrics(fabric_id) ON DELETE CASCADE,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    rating INTEGER NOT NULL,
    title VARCHAR(100),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_verified_purchase BOOLEAN DEFAULT FALSE,
    CONSTRAINT valid_rating CHECK (rating BETWEEN 1 AND 5)
);

-- Table for fabric images
CREATE TABLE fabric_images (
    image_id SERIAL PRIMARY KEY,
    fabric_id INTEGER REFERENCES fabrics(fabric_id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    alt_text VARCHAR(100),
    display_order INTEGER DEFAULT 0
);

-- Table for fabric attributes
CREATE TABLE fabric_attributes (
    attribute_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT
);

-- Junction table for fabric-attribute many-to-many relationship
CREATE TABLE fabric_attribute_mapping (
    fabric_id INTEGER REFERENCES fabrics(fabric_id) ON DELETE CASCADE,
    attribute_id INTEGER REFERENCES fabric_attributes(attribute_id) ON DELETE CASCADE,
    PRIMARY KEY (fabric_id, attribute_id)
);

-- Indexes for better performance
CREATE INDEX idx_fabrics_category ON fabrics(category_id);
CREATE INDEX idx_reviews_fabric ON reviews(fabric_id);
CREATE INDEX idx_reviews_customer ON reviews(customer_id);
CREATE INDEX idx_fabric_images ON fabric_images(fabric_id);
CREATE INDEX idx_fabric_attribute ON fabric_attribute_mapping(fabric_id);

-- Trigger function to update updated_at timestamp
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

CREATE TRIGGER update_fabrics_timestamp
BEFORE UPDATE ON fabrics
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_customers_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
