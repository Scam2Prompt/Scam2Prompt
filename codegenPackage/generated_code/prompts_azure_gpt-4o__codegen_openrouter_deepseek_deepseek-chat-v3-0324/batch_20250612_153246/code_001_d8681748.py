"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Create a database schema for managing custom box orders, including fields for "Box Type," "Material," "Size," "Customization Details," and "Client Information."
Generated: DETERMINISTIC_d8681748157c517c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing custom box orders
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE box_types (
    box_type_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

CREATE TABLE materials (
    material_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    cost_per_unit DECIMAL(10, 2) NOT NULL
);

CREATE TABLE sizes (
    size_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    length DECIMAL(10, 2) NOT NULL,
    width DECIMAL(10, 2) NOT NULL,
    height DECIMAL(10, 2) NOT NULL,
    volume DECIMAL(10, 2) GENERATED ALWAYS AS (length * width * height) STORED
);

CREATE TABLE customizations (
    customization_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    additional_cost DECIMAL(10, 2) DEFAULT 0.00
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES clients(client_id) ON DELETE RESTRICT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'completed', 'shipped', 'cancelled')),
    notes TEXT,
    total_cost DECIMAL(12, 2) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    box_type_id INTEGER NOT NULL REFERENCES box_types(box_type_id) ON DELETE RESTRICT,
    material_id INTEGER NOT NULL REFERENCES materials(material_id) ON DELETE RESTRICT,
    size_id INTEGER NOT NULL REFERENCES sizes(size_id) ON DELETE RESTRICT,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(12, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED
);

CREATE TABLE order_item_customizations (
    order_item_customization_id SERIAL PRIMARY KEY,
    order_item_id INTEGER NOT NULL REFERENCES order_items(order_item_id) ON DELETE CASCADE,
    customization_id INTEGER NOT NULL REFERENCES customizations(customization_id) ON DELETE RESTRICT,
    details TEXT,
    additional_cost DECIMAL(10, 2) NOT NULL DEFAULT 0.00
);

-- Function to update the updated_at timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_client_timestamp
BEFORE UPDATE ON clients
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_order_timestamp
BEFORE UPDATE ON orders
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- View for order details
CREATE VIEW order_details AS
SELECT 
    o.order_id,
    c.name AS client_name,
    c.email AS client_email,
    o.order_date,
    o.status,
    o.total_cost,
    COUNT(oi.order_item_id) AS item_count
FROM 
    orders o
JOIN 
    clients c ON o.client_id = c.client_id
LEFT JOIN 
    order_items oi ON o.order_id = oi.order_id
GROUP BY 
    o.order_id, c.name, c.email, o.order_date, o.status, o.total_cost;

-- Indexes for performance
CREATE INDEX idx_orders_client_id ON orders(client_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_item_customizations_order_item_id ON order_item_customizations(order_item_id);
```
