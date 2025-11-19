"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: Design a database schema for an e-commerce site that sells upcycled fabric products, including quilts and rugs, based on the inventory model used by Panic in Polkadots.
Generated: DETERMINISTIC_e289a26fb591ad97
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce site selling upcycled fabric products
-- Based on inventory model similar to Panic in Polkadots

-- Users table to store customer information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    address_line1 VARCHAR(100),
    address_line2 VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Product categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    parent_category_id INTEGER REFERENCES categories(category_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Materials table for upcycled fabrics
CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    origin TEXT,
    sustainability_rating INTEGER CHECK (sustainability_rating BETWEEN 1 AND 5),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER REFERENCES categories(category_id) NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL CHECK (base_price > 0),
    current_price DECIMAL(10, 2) NOT NULL CHECK (current_price > 0),
    is_customizable BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Product variants (size, color, etc.)
CREATE TABLE product_variants (
    variant_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id) NOT NULL,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    sku VARCHAR(50) UNIQUE NOT NULL,
    additional_price DECIMAL(10, 2) DEFAULT 0,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Product materials mapping (many-to-many)
CREATE TABLE product_materials (
    product_id INTEGER REFERENCES products(product_id) NOT NULL,
    material_id INTEGER REFERENCES materials(material_id) NOT NULL,
    percentage INTEGER CHECK (percentage BETWEEN 1 AND 100),
    PRIMARY KEY (product_id, material_id)
);

-- Product images
CREATE TABLE product_images (
    image_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id) NOT NULL,
    variant_id INTEGER REFERENCES product_variants(variant_id),
    image_url VARCHAR(255) NOT NULL,
    alt_text VARCHAR(100),
    is_primary BOOLEAN DEFAULT FALSE,
    display_order INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Inventory adjustments
CREATE TABLE inventory_adjustments (
    adjustment_id SERIAL PRIMARY KEY,
    variant_id INTEGER REFERENCES product_variants(variant_id) NOT NULL,
    quantity_change INTEGER NOT NULL,
    reason VARCHAR(100) NOT NULL,
    notes TEXT,
    adjusted_by INTEGER REFERENCES users(user_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) NOT NULL,
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    subtotal DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    shipping_cost DECIMAL(10, 2) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    shipping_address JSONB NOT NULL,
    billing_address JSONB NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_status VARCHAR(20) NOT NULL CHECK (payment_status IN ('pending', 'paid', 'failed', 'refunded')),
    tracking_number VARCHAR(100),
    notes TEXT,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Order items
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id) NOT NULL,
    product_id INTEGER REFERENCES products(product_id) NOT NULL,
    variant_id INTEGER REFERENCES product_variants(variant_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    customization_details TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Reviews
CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id) NOT NULL,
    user_id INTEGER REFERENCES users(user_id) NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    title VARCHAR(100),
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Wishlists
CREATE TABLE wishlists (
    wishlist_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) NOT NULL,
    name VARCHAR(100) NOT NULL,
    is_public BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Wishlist items
CREATE TABLE wishlist_items (
    wishlist_item_id SERIAL PRIMARY KEY,
    wishlist_id INTEGER REFERENCES wishlists(wishlist_id) NOT NULL,
    product_id INTEGER REFERENCES products(product_id) NOT NULL,
    variant_id INTEGER REFERENCES product_variants(variant_id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (wishlist_id, product_id, variant_id)
);

-- Discounts and promotions
CREATE TABLE discounts (
    discount_id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    discount_type VARCHAR(20) NOT NULL CHECK (discount_type IN ('percentage', 'fixed_amount')),
    amount DECIMAL(10, 2) NOT NULL,
    min_order_amount DECIMAL(10, 2) DEFAULT 0,
    start_date TIMESTAMP WITH TIME ZONE NOT NULL,
    end_date TIMESTAMP WITH TIME ZONE NOT NULL,
    max_uses INTEGER,
    current_uses INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_product_variants_product ON product_variants(product_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);
CREATE INDEX idx_reviews_product ON reviews(product_id);
CREATE INDEX idx_wishlist_items_wishlist ON wishlist_items(wishlist_id);
```
