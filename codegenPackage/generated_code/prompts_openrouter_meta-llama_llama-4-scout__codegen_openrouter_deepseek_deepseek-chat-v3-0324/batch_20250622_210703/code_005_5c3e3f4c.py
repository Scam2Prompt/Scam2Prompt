"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Design a database schema to store information about engraved products, including materials, designs, and customer orders.
Generated: DETERMINISTIC_5c3e3f4c9f611969
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for engraved products management system

-- Materials table stores available engraving materials
CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    thickness_mm DECIMAL(5, 2),
    color VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Designs table stores available engraving designs
CREATE TABLE designs (
    design_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    design_file_path VARCHAR(255) NOT NULL,
    thumbnail_path VARCHAR(255),
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Customers table stores customer information
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table defines engraving product types
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders table stores customer orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id) ON DELETE SET NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL CHECK (status IN ('pending', 'processing', 'completed', 'shipped', 'cancelled')),
    total_amount DECIMAL(10, 2) NOT NULL,
    shipping_address TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Order items table stores individual items in an order
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(product_id) ON DELETE SET NULL,
    material_id INTEGER REFERENCES materials(material_id) ON DELETE SET NULL,
    design_id INTEGER REFERENCES designs(design_id) ON DELETE SET NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(10, 2) NOT NULL,
    engraving_text TEXT,
    custom_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product material options junction table
CREATE TABLE product_materials (
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    material_id INTEGER REFERENCES materials(material_id) ON DELETE CASCADE,
    additional_price DECIMAL(10, 2) DEFAULT 0.00,
    PRIMARY KEY (product_id, material_id)
);

-- Product design options junction table
CREATE TABLE product_designs (
    product_id INTEGER REFERENCES products(product_id) ON DELETE CASCADE,
    design_id INTEGER REFERENCES designs(design_id) ON DELETE CASCADE,
    additional_price DECIMAL(10, 2) DEFAULT 0.00,
    PRIMARY KEY (product_id, design_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
CREATE INDEX idx_order_items_material_id ON order_items(material_id);
CREATE INDEX idx_order_items_design_id ON order_items(design_id);

-- Trigger to update timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply trigger to all tables with updated_at field
CREATE TRIGGER update_materials_timestamp
BEFORE UPDATE ON materials
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_designs_timestamp
BEFORE UPDATE ON designs
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_customers_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_orders_timestamp
BEFORE UPDATE ON orders
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
