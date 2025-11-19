"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Create a database schema for storing golf grip profiles, including customization details like material type (PU, TPE, rubber), embossing style, and customer preferences, as described on the Longhui Golf website.
Generated: DETERMINISTIC_f57f86f9a440f9f3
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a PostgreSQL database schema for storing golf grip profiles with customization details:

```sql
-- Database schema for golf grip profiles
CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE embossing_styles (
    style_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE colors (
    color_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    hex_code VARCHAR(7) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

CREATE TABLE grip_profiles (
    profile_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE grip_customizations (
    customization_id SERIAL PRIMARY KEY,
    profile_id INTEGER REFERENCES grip_profiles(profile_id) ON DELETE CASCADE,
    material_id INTEGER REFERENCES materials(material_id) ON DELETE SET NULL,
    style_id INTEGER REFERENCES embossing_styles(style_id) ON DELETE SET NULL,
    color_id INTEGER REFERENCES colors(color_id) ON DELETE SET NULL,
    thickness_mm DECIMAL(5,2) CHECK (thickness_mm > 0),
    length_mm DECIMAL(6,2) CHECK (length_mm > 0),
    weight_g DECIMAL(6,2) CHECK (weight_g > 0),
    hardness_rating INTEGER CHECK (hardness_rating BETWEEN 1 AND 10),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE grip_orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE SET NULL,
    profile_id INTEGER REFERENCES grip_profiles(profile_id) ON DELETE SET NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'completed', 'shipped', 'cancelled')),
    tracking_number VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_grip_profiles_customer ON grip_profiles(customer_id);
CREATE INDEX idx_grip_customizations_profile ON grip_customizations(profile_id);
CREATE INDEX idx_grip_orders_customer ON grip_orders(customer_id);
CREATE INDEX idx_grip_orders_profile ON grip_orders(profile_id);

-- Triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_materials_timestamp
BEFORE UPDATE ON materials
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_embossing_styles_timestamp
BEFORE UPDATE ON embossing_styles
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_colors_timestamp
BEFORE UPDATE ON colors
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_customers_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_grip_profiles_timestamp
BEFORE UPDATE ON grip_profiles
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_grip_customizations_timestamp
BEFORE UPDATE ON grip_customizations
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_grip_orders_timestamp
BEFORE UPDATE ON grip_orders
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
