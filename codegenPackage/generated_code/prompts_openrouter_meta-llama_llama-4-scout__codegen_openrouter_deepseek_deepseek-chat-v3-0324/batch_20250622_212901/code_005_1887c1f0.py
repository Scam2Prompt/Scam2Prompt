"""
Generated Code Metadata:
========================
Original URL: https://unitramabrazz.blogspot.com
Prompt: Design a simple database schema to store information about various visual communication products, including chapas de alumínio composto, lonas uniflex, and tecido flag banner.
Generated: DETERMINISTIC_1887c1f0b59616ee
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for visual communication products
CREATE TABLE product_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE materials (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit_of_measure VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_type_id INTEGER REFERENCES product_types(id) ON DELETE CASCADE,
    material_id INTEGER REFERENCES materials(id) ON DELETE SET NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    thickness DECIMAL(10,2),
    width DECIMAL(10,2),
    height DECIMAL(10,2),
    weight DECIMAL(10,2),
    color VARCHAR(50),
    price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_images (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id) ON DELETE CASCADE,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert initial product types
INSERT INTO product_types (name, description) VALUES 
('Chapa de Alumínio Composto', 'Painéis de alumínio composto para fachadas e comunicação visual'),
('Lona Uniflex', 'Lonas de PVC flexível para impressão digital'),
('Tecido Flag Banner', 'Tecido leve para banners e displays');

-- Insert common materials
INSERT INTO materials (name, description, unit_of_measure) VALUES 
('Alumínio Composto', 'Painéis de alumínio composto', 'm²'),
('PVC', 'Lona de PVC flexível', 'm²'),
('Poliester', 'Tecido de poliester para banners', 'm²'),
('Adesivo', 'Vinil adesivo', 'm²');
```
