"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: "Design a database schema for an e-commerce platform specializing in paper roll distribution, with tables for products, customers, orders, and pricing information specific to the Chilean market."
Generated: DETERMINISTIC_6caa336d734af67a
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform specializing in paper roll distribution in Chile

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Product categories table
CREATE TABLE product_categories (
    category_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    product_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category_id UUID REFERENCES product_categories(category_id),
    sku VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    width_mm DECIMAL(10, 2) NOT NULL,
    diameter_mm DECIMAL(10, 2) NOT NULL,
    core_diameter_mm DECIMAL(10, 2) NOT NULL,
    paper_type VARCHAR(50) NOT NULL,
    weight_gsm DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_dimensions CHECK (width_mm > 0 AND diameter_mm > 0 AND core_diameter_mm > 0),
    CONSTRAINT positive_weight CHECK (weight_gsm > 0)
);

-- Product pricing table (CLP - Chilean Peso)
CREATE TABLE product_pricing (
    price_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID REFERENCES products(product_id),
    price_clp DECIMAL(12, 2) NOT NULL,
    tax_rate DECIMAL(5, 2) DEFAULT 0.19, -- Chile's standard VAT rate is 19%
    effective_from TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    effective_to TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_price CHECK (price_clp > 0),
    CONSTRAINT valid_tax_rate CHECK (tax_rate >= 0 AND tax_rate <= 1)
);

-- Inventory table
CREATE TABLE inventory (
    inventory_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID REFERENCES products(product_id),
    quantity_in_stock INTEGER NOT NULL DEFAULT 0,
    quantity_reserved INTEGER NOT NULL DEFAULT 0,
    last_restocked TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT non_negative_stock CHECK (quantity_in_stock >= 0),
    CONSTRAINT non_negative_reserved CHECK (quantity_reserved >= 0)
);

-- Regions of Chile
CREATE TABLE regions (
    region_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    short_code VARCHAR(5) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Communes (municipalities) of Chile
CREATE TABLE communes (
    commune_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    region_id UUID REFERENCES regions(region_id),
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Customers table
CREATE TABLE customers (
    customer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    rut VARCHAR(12) UNIQUE NOT NULL, -- Chilean tax ID
    business_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address_street VARCHAR(100) NOT NULL,
    address_number VARCHAR(20) NOT NULL,
    commune_id UUID REFERENCES communes(commune_id),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Order statuses
CREATE TABLE order_statuses (
    status_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
    order_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    customer_id UUID REFERENCES customers(customer_id),
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status_id UUID REFERENCES order_statuses(status_id),
    subtotal_clp DECIMAL(12, 2) NOT NULL,
    tax_clp DECIMAL(12, 2) NOT NULL,
    total_clp DECIMAL(12, 2) NOT NULL,
    shipping_address_street VARCHAR(100) NOT NULL,
    shipping_address_number VARCHAR(20) NOT NULL,
    shipping_commune_id UUID REFERENCES communes(commune_id),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_amounts CHECK (subtotal_clp >= 0 AND tax_clp >= 0 AND total_clp >= 0)
);

-- Order items table
CREATE TABLE order_items (
    order_item_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    order_id UUID REFERENCES orders(order_id),
    product_id UUID REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    unit_price_clp DECIMAL(12, 2) NOT NULL,
    tax_rate DECIMAL(5, 2) NOT NULL,
    total_price_clp DECIMAL(12, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_quantity CHECK (quantity > 0),
    CONSTRAINT positive_unit_price CHECK (unit_price_clp > 0),
    CONSTRAINT valid_tax_rate CHECK (tax_rate >= 0 AND tax_rate <= 1),
    CONSTRAINT positive_total_price CHECK (total_price_clp > 0)
);

-- Shipping methods
CREATE TABLE shipping_methods (
    method_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    base_cost_clp DECIMAL(12, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_cost CHECK (base_cost_clp >= 0)
);

-- Order shipping details
CREATE TABLE order_shipping (
    shipping_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    order_id UUID REFERENCES orders(order_id),
    method_id UUID REFERENCES shipping_methods(method_id),
    tracking_number VARCHAR(100),
    shipping_cost_clp DECIMAL(12, 2) NOT NULL,
    estimated_delivery_date TIMESTAMP WITH TIME ZONE,
    actual_delivery_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_cost CHECK (shipping_cost_clp >= 0)
);

-- Payment methods
CREATE TABLE payment_methods (
    method_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Order payments
CREATE TABLE order_payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    order_id UUID REFERENCES orders(order_id),
    method_id UUID REFERENCES payment_methods(method_id),
    amount_clp DECIMAL(12, 2) NOT NULL,
    transaction_id VARCHAR(100),
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT positive_amount CHECK (amount_clp > 0)
);

-- Create indexes for performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_product_pricing_product ON product_pricing(product_id);
CREATE INDEX idx_inventory_product ON inventory(product_id);
CREATE INDEX idx_communes_region ON communes(region_id);
CREATE INDEX idx_customers_commune ON customers(commune_id);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);
CREATE INDEX idx_order_shipping_order ON order_shipping(order_id);
CREATE INDEX idx_order_payments_order ON order_payments(order_id);

-- Create triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_product_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_customer_timestamp
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER
