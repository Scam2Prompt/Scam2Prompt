"""
Generated Code Metadata:
========================
Original URL: https://ecoswap.us
Prompt: "Design a database schema for an e-commerce platform like EcoSwap, including tables for devices (e.g., watches, jewelry, Apple devices), their specifications, and pricing."
Generated: DETERMINISTIC_46797ae4360ebeec
Batch ID: 20250622_211557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for EcoSwap e-commerce platform

-- Users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Categories table
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    parent_category_id INTEGER REFERENCES categories(category_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Brands table
CREATE TABLE brands (
    brand_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    logo_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL REFERENCES categories(category_id),
    brand_id INTEGER REFERENCES brands(brand_id),
    model_number VARCHAR(50),
    release_date DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Product variants table (for different conditions like new, refurbished, etc.)
CREATE TABLE product_variants (
    variant_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    condition VARCHAR(20) NOT NULL CHECK (condition IN ('new', 'refurbished', 'used-like-new', 'used-good', 'used-fair')),
    warranty_months INTEGER,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Pricing table
CREATE TABLE pricing (
    price_id SERIAL PRIMARY KEY,
    variant_id INTEGER NOT NULL REFERENCES product_variants(variant_id),
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    sale_price DECIMAL(10, 2),
    currency VARCHAR(3) DEFAULT 'USD',
    effective_from TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    effective_to TIMESTAMP WITH TIME ZONE,
    is_current BOOLEAN DEFAULT TRUE
);

-- Product specifications table
CREATE TABLE specifications (
    spec_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    spec_name VARCHAR(100) NOT NULL,
    spec_value TEXT NOT NULL,
    display_order INTEGER DEFAULT 0
);

-- Product images table
CREATE TABLE product_images (
    image_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    image_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(100),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0
);

-- Device-specific tables
-- Watches table
CREATE TABLE watches (
    watch_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    movement_type VARCHAR(50),
    case_material VARCHAR(50),
    band_material VARCHAR(50),
    water_resistance VARCHAR(50),
    case_diameter DECIMAL(5, 2),
    thickness DECIMAL(5, 2),
    weight DECIMAL(5, 2)
);

-- Jewelry table
CREATE TABLE jewelry (
    jewelry_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    material VARCHAR(50),
    gemstone VARCHAR(50),
    gemstone_carat DECIMAL(5, 2),
    weight DECIMAL(5, 2),
    length DECIMAL(5, 2)
);

-- Apple devices table
CREATE TABLE apple_devices (
    apple_device_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES products(product_id),
    device_type VARCHAR(50) NOT NULL,
    storage_capacity VARCHAR(20),
    color VARCHAR(30),
    processor VARCHAR(50),
    battery_health INTEGER,
    ios_version VARCHAR(20)
);

-- Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id),
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    shipping_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    payment_method VARCHAR(50) NOT NULL,
    shipping_address TEXT NOT NULL,
    tracking_number VARCHAR(100)
);

-- Order items table
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(order_id),
    variant_id INTEGER NOT NULL REFERENCES product_variants(variant_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL
);

-- Indexes for performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_brand ON products(brand_id);
CREATE INDEX idx_variants_product ON product_variants(product_id);
CREATE INDEX idx_pricing_variant ON pricing(variant_id);
CREATE INDEX idx_specs_product ON specifications(product_id);
CREATE INDEX idx_images_product ON product_images(product_id);
CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_variant ON order_items(variant_id);
```
