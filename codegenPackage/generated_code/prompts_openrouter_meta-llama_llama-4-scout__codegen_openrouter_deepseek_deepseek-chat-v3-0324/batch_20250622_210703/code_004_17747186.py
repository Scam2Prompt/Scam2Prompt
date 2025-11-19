"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Design a data model for a maritime supply company's database, including tables for customers, products, orders, and services such as provisioning and maintenance.
Generated: DETERMINISTIC_17747186629809b5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Maritime Supply Company Database Schema

-- Customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) UNIQUE NOT NULL,
    contact_phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tax_id VARCHAR(50) UNIQUE,
    credit_limit DECIMAL(10, 2),
    active BOOLEAN DEFAULT TRUE,
    CONSTRAINT valid_email CHECK (contact_email ~* '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

-- Product categories
CREATE TABLE product_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INTEGER REFERENCES product_categories(category_id),
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    units_in_stock INTEGER NOT NULL DEFAULT 0,
    units_on_order INTEGER DEFAULT 0,
    discontinued BOOLEAN DEFAULT FALSE,
    CONSTRAINT positive_price CHECK (unit_price > 0),
    CONSTRAINT positive_stock CHECK (units_in_stock >= 0),
    CONSTRAINT positive_order CHECK (units_on_order >= 0)
);

-- Services table
CREATE TABLE services (
    service_id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    base_cost DECIMAL(10, 2) NOT NULL,
    hourly_rate DECIMAL(10, 2),
    minimum_hours INTEGER DEFAULT 1,
    active BOOLEAN DEFAULT TRUE,
    CONSTRAINT positive_cost CHECK (base_cost >= 0),
    CONSTRAINT positive_rate CHECK (hourly_rate >= 0)
);

-- Orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    required_date TIMESTAMP,
    shipped_date TIMESTAMP,
    ship_via VARCHAR(50),
    freight_charges DECIMAL(10, 2) DEFAULT 0,
    ship_name VARCHAR(100),
    ship_address TEXT,
    ship_city VARCHAR(50),
    ship_country VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Pending',
    CONSTRAINT valid_status CHECK (status IN ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled')),
    CONSTRAINT valid_dates CHECK (shipped_date IS NULL OR shipped_date >= order_date),
    CONSTRAINT valid_required_date CHECK (required_date IS NULL OR required_date >= order_date)
);

-- Order details (line items)
CREATE TABLE order_details (
    order_detail_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(product_id),
    service_id INTEGER REFERENCES services(service_id),
    unit_price DECIMAL(10, 2) NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    discount DECIMAL(4, 2) DEFAULT 0,
    CONSTRAINT valid_line_item CHECK (product_id IS NOT NULL OR service_id IS NOT NULL),
    CONSTRAINT positive_price CHECK (unit_price >= 0),
    CONSTRAINT positive_quantity CHECK (quantity > 0),
    CONSTRAINT valid_discount CHECK (discount >= 0 AND discount <= 1)
);

-- Vessels table
CREATE TABLE vessels (
    vessel_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    vessel_name VARCHAR(100) NOT NULL,
    imo_number VARCHAR(15) UNIQUE,
    vessel_type VARCHAR(50),
    flag VARCHAR(50),
    year_built INTEGER,
    gross_tonnage DECIMAL(10, 2),
    CONSTRAINT valid_imo CHECK (imo_number ~ '^IMO\d{7}$')
);

-- Maintenance services table
CREATE TABLE maintenance_services (
    maintenance_id SERIAL PRIMARY KEY,
    vessel_id INTEGER NOT NULL REFERENCES vessels(vessel_id),
    service_id INTEGER NOT NULL REFERENCES services(service_id),
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Scheduled',
    hours_worked DECIMAL(5, 2),
    notes TEXT,
    CONSTRAINT valid_status CHECK (status IN ('Scheduled', 'In Progress', 'Completed', 'Cancelled')),
    CONSTRAINT valid_dates CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Provisioning services table
CREATE TABLE provisioning_services (
    provisioning_id SERIAL PRIMARY KEY,
    vessel_id INTEGER NOT NULL REFERENCES vessels(vessel_id),
    order_id INTEGER REFERENCES orders(order_id),
    service_date TIMESTAMP NOT NULL,
    delivery_date TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Requested',
    notes TEXT,
    CONSTRAINT valid_status CHECK (status IN ('Requested', 'Scheduled', 'Delivered', 'Cancelled')),
    CONSTRAINT valid_dates CHECK (delivery_date IS NULL OR delivery_date >= service_date)
);

-- Payments table
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    order_id INTEGER REFERENCES orders(order_id),
    maintenance_id INTEGER REFERENCES maintenance_services(maintenance_id),
    provisioning_id INTEGER REFERENCES provisioning_services(provisioning_id),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(20) NOT NULL,
    transaction_id VARCHAR(100),
    notes TEXT,
    CONSTRAINT valid_payment_target CHECK (
        (order_id IS NOT NULL AND maintenance_id IS NULL AND provisioning_id IS NULL) OR
        (order_id IS NULL AND maintenance_id IS NOT NULL AND provisioning_id IS NULL) OR
        (order_id IS NULL AND maintenance_id IS NULL AND provisioning_id IS NOT NULL)
    ),
    CONSTRAINT positive_amount CHECK (amount > 0)
);

-- Create indexes for performance
CREATE INDEX idx_customers_company_name ON customers(company_name);
CREATE INDEX idx_products_product_name ON products(product_name);
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_order_date ON orders(order_date);
CREATE INDEX idx_order_details_order_id ON order_details(order_id);
CREATE INDEX idx_vessels_customer_id ON vessels(customer_id);
CREATE INDEX idx_maintenance_vessel_id ON maintenance_services(vessel_id);
CREATE INDEX idx_provisioning_vessel_id ON provisioning_services(vessel_id);
CREATE INDEX idx_payments_customer_id ON payments(customer_id);
CREATE INDEX idx_payments_order_id ON payments(order_id);
```
