"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Develop a database schema for managing retail partnerships and product distribution, inspired by PDC Brush's role as a retail partner.
Generated: DETERMINISTIC_b552589189a42416
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing retail partnerships and product distribution

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table for storing retail partners
CREATE TABLE retail_partners (
    partner_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    partner_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'United States',
    tax_id VARCHAR(50),
    partnership_start_date DATE NOT NULL,
    partnership_end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT email_unique UNIQUE (email)
);

-- Table for product categories
CREATE TABLE product_categories (
    category_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT category_name_unique UNIQUE (category_name)
);

-- Table for products
CREATE TABLE products (
    product_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    sku VARCHAR(50) NOT NULL,
    category_id UUID REFERENCES product_categories(category_id),
    unit_price DECIMAL(10, 2) NOT NULL,
    cost_price DECIMAL(10, 2) NOT NULL,
    weight DECIMAL(10, 2),
    dimensions VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT sku_unique UNIQUE (sku)
);

-- Table for partner agreements
CREATE TABLE partner_agreements (
    agreement_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    partner_id UUID REFERENCES retail_partners(partner_id) NOT NULL,
    agreement_name VARCHAR(100) NOT NULL,
    agreement_details TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    discount_rate DECIMAL(5, 2) DEFAULT 0.00,
    payment_terms VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for product distribution to partners
CREATE TABLE partner_product_distribution (
    distribution_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    partner_id UUID REFERENCES retail_partners(partner_id) NOT NULL,
    product_id UUID REFERENCES products(product_id) NOT NULL,
    agreement_id UUID REFERENCES partner_agreements(agreement_id),
    distribution_start_date DATE NOT NULL,
    distribution_end_date DATE,
    wholesale_price DECIMAL(10, 2) NOT NULL,
    min_order_quantity INTEGER DEFAULT 1,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT partner_product_unique UNIQUE (partner_id, product_id)
);

-- Table for partner orders
CREATE TABLE partner_orders (
    order_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    partner_id UUID REFERENCES retail_partners(partner_id) NOT NULL,
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expected_delivery_date DATE,
    actual_delivery_date DATE,
    order_status VARCHAR(20) NOT NULL CHECK (order_status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    total_amount DECIMAL(12, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) DEFAULT 0.00,
    tax_amount DECIMAL(10, 2) DEFAULT 0.00,
    shipping_cost DECIMAL(10, 2) DEFAULT 0.00,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for order line items
CREATE TABLE order_items (
    item_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    order_id UUID REFERENCES partner_orders(order_id) NOT NULL,
    product_id UUID REFERENCES products(product_id) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    discount_rate DECIMAL(5, 2) DEFAULT 0.00,
    line_total DECIMAL(12, 2) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for partner payments
CREATE TABLE partner_payments (
    payment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    partner_id UUID REFERENCES retail_partners(partner_id) NOT NULL,
    order_id UUID REFERENCES partner_orders(order_id),
    payment_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(12, 2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    transaction_reference VARCHAR(100),
    payment_status VARCHAR(20) NOT NULL CHECK (payment_status IN ('pending', 'completed', 'failed', 'refunded')),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for partner performance metrics
CREATE TABLE partner_performance (
    performance_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    partner_id UUID REFERENCES retail_partners(partner_id) NOT NULL,
    month DATE NOT NULL,
    total_sales DECIMAL(12, 2) DEFAULT 0.00,
    total_orders INTEGER DEFAULT 0,
    average_order_value DECIMAL(10, 2) DEFAULT 0.00,
    payment_delay_days INTEGER DEFAULT 0,
    customer_feedback_score DECIMAL(3, 1),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT partner_month_unique UNIQUE (partner_id, month)
);

-- Trigger function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for all tables with updated_at field
CREATE TRIGGER update_retail_partners_timestamp
BEFORE UPDATE ON retail_partners
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_product_categories_timestamp
BEFORE UPDATE ON product_categories
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp
BEFORE UPDATE ON products
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_partner_agreements_timestamp
BEFORE UPDATE ON partner_agreements
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_partner_product_distribution_timestamp
BEFORE UPDATE ON partner_product_distribution
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_partner_orders_timestamp
BEFORE UPDATE ON partner_orders
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_partner_payments_timestamp
BEFORE UPDATE ON partner_payments
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_partner_performance_timestamp
BEFORE UPDATE ON partner_performance
FOR EACH ROW EXECUTE FUNCTION update_timestamp();
```
