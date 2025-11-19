"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.paradigmagbi.ru
Prompt: How can I create a database schema to store information about железобетонные изделия and their suppliers in Санкт-Петербурге, as described on the Paradigma site?
Generated: DETERMINISTIC_f373f88d41876a0e
Batch ID: 20250612_162822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Here's a clean, production-ready code snippet to create a database schema using PostgreSQL for storing information about железобетонные изделия (reinforced concrete products) and their suppliers in Санкт-Петербурге.

```sql
-- Create the database schema for reinforced concrete products and suppliers.

-- Create the table for suppliers.
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY,  -- Unique identifier for each supplier
    name VARCHAR(255) NOT NULL,     -- Name of the supplier
    contact_info TEXT,              -- Contact information (e.g., phone, email, address)
    address TEXT NOT NULL,          -- Address of the supplier
    city VARCHAR(100) NOT NULL,     -- City (for filtering suppliers in Санкт-Петербург)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Record last update timestamp
);

-- Create the table for reinforced concrete products.
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,  -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,     -- Name or description of the product
    dimensions TEXT,                -- Dimensions of the product (e.g., length, width, height)
    weight FLOAT,                   -- Weight of the product in kilograms
    material TEXT NOT NULL,         -- Type of material (e.g., concrete grade)
    price DECIMAL(10, 2),           -- Price of the product
    supplier_id INT REFERENCES suppliers(supplier_id) ON DELETE CASCADE,  -- Foreign key linking to the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Record last update timestamp
);

-- Create the table for tracking orders (optional, if needed).
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,    -- Unique identifier for each order
    product_id INT REFERENCES products(product_id) ON DELETE CASCADE,  -- Foreign key linking to the product
    quantity INT NOT NULL,          -- Quantity of products ordered
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Order date
    total_price DECIMAL(10, 2),     -- Total price of the order
    customer_name VARCHAR(255),     -- Name of the customer
    customer_contact TEXT           -- Contact information for the customer
);

-- Add indexes to optimize queries.
CREATE INDEX idx_suppliers_city ON suppliers(city);  -- Index to quickly filter suppliers by city
CREATE INDEX idx_products_supplier ON products(supplier_id);  -- Index to quickly find products by supplier

-- Example: Insert sample data into the suppliers table.
INSERT INTO suppliers (name, contact_info, address, city)
VALUES 
('ООО Конструкции СПб', 'contact@company.ru, +7 (812) 123-4567', 'ул. Московская, д. 1', 'Санкт-Петербург'),
('ЗАО БетонСПб', 'info@betonspb.ru, +7 (812) 987-6543', 'пр. Ленина, д. 25', 'Санкт-Петербург');

-- Example: Insert sample data into the products table.
INSERT INTO products (name, dimensions, weight, material, price, supplier_id)
VALUES 
('Фундаментная плита ФБС 24-4-6', '2400x400x600', 1200.5, 'Бетон B25', 3450.00, 1),
('Плита перекрытия ПК 22-12', '2200x1200x150', 850.3, 'Бетон B20', 2500.00, 2);

```

This schema includes tables for `suppliers` and `products`, along with relationships between them. It also includes optional fields for tracking orders. Error handling for relational integrity is achieved via `ON DELETE CASCADE` for foreign key constraints.
