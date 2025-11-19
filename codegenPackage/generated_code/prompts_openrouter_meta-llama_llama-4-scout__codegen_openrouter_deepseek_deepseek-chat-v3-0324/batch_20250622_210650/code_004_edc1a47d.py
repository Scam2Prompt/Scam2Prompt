"""
Generated Code Metadata:
========================
Original URL: https://aceitescondadoloma.com
Prompt: Develop a simple database schema to store information about olive oil products, customers, and export orders for a company like Aceites Condado Loma, focusing on efficient data retrieval and reporting.
Generated: DETERMINISTIC_edc1a47df204eb69
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for olive oil export management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Olive oil product categories
CREATE TABLE product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Olive oil products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    origin TEXT NOT NULL,
    acidity_level REAL CHECK(acidity_level >= 0 AND acidity_level <= 1),
    volume_ml INTEGER NOT NULL CHECK(volume_ml > 0),
    price_per_unit REAL NOT NULL CHECK(price_per_unit > 0),
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK(stock_quantity >= 0),
    production_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    organic_certified BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id),
    CHECK (expiry_date > production_date)
);

-- Countries for export
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    iso_code TEXT NOT NULL UNIQUE,
    import_tariff REAL DEFAULT 0 CHECK(import_tariff >= 0)
);

-- Customer information
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    contact_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    country_id INTEGER NOT NULL,
    tax_id TEXT,
    preferred_shipping_method TEXT,
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

-- Order statuses
CREATE TABLE order_statuses (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Export orders
CREATE TABLE export_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL DEFAULT CURRENT_DATE,
    status_id INTEGER NOT NULL DEFAULT 1,
    shipping_address TEXT NOT NULL,
    shipping_country_id INTEGER NOT NULL,
    shipping_cost REAL NOT NULL CHECK(shipping_cost >= 0),
    tax_amount REAL NOT NULL CHECK(tax_amount >= 0),
    notes TEXT,
    estimated_delivery_date DATE,
    actual_delivery_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (status_id) REFERENCES order_statuses(status_id),
    FOREIGN KEY (shipping_country_id) REFERENCES countries(country_id),
    CHECK (estimated_delivery_date >= order_date),
    CHECK (actual_delivery_date IS NULL OR actual_delivery_date >= order_date)
);

-- Order items
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    unit_price REAL NOT NULL CHECK(unit_price > 0),
    discount REAL DEFAULT 0 CHECK(discount >= 0 AND discount < 1),
    FOREIGN KEY (order_id) REFERENCES export_orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    UNIQUE (order_id, product_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_customers_country ON customers(country_id);
CREATE INDEX idx_orders_customer ON export_orders(customer_id);
CREATE INDEX idx_orders_status ON export_orders(status_id);
CREATE INDEX idx_orders_country ON export_orders(shipping_country_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);

-- Insert initial data for order statuses
INSERT INTO order_statuses (name, description) VALUES 
    ('Pending', 'Order received but not processed'),
    ('Processing', 'Order is being prepared for shipment'),
    ('Shipped', 'Order has been shipped'),
    ('Delivered', 'Order has been delivered to customer'),
    ('Cancelled', 'Order was cancelled');

-- Insert initial product categories
INSERT INTO product_categories (name, description) VALUES 
    ('Extra Virgin', 'Highest quality olive oil with perfect taste and aroma'),
    ('Virgin', 'Good quality olive oil with slight defects'),
    ('Refined', 'Processed olive oil with neutral taste'),
    ('Pomace', 'Oil extracted from olive pomace');
```
