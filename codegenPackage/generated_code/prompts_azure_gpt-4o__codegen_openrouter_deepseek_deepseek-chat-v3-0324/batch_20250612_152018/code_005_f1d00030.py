"""
Generated Code Metadata:
========================
Original URL: https://ortopedic.cl
Prompt: Create a database schema in SQL to store information about orthopedic products such as "Plantillas Ortopédicas," "Rodilleras," and "Colchones," including attributes like price, stock availability, and certification (ISO, CE, ISP).
Generated: DETERMINISTIC_f1d00030b8e94dc3
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for orthopedic products
CREATE TABLE product_categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE certifications (
    certification_id INT PRIMARY KEY AUTO_INCREMENT,
    certification_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    category_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

CREATE TABLE product_certifications (
    product_certification_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    certification_id INT NOT NULL,
    certification_number VARCHAR(50),
    expiry_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (certification_id) REFERENCES certifications(certification_id)
);

-- Indexes for better performance
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_name ON products(product_name);
CREATE INDEX idx_product_certifications ON product_certifications(product_id, certification_id);

-- Sample data for product categories
INSERT INTO product_categories (category_name, description) VALUES
('Plantillas Ortopédicas', 'Plantillas diseñadas para soporte y comodidad'),
('Rodilleras', 'Dispositivos de soporte para articulaciones de la rodilla'),
('Colchones', 'Colchones ortopédicos para soporte postural');

-- Sample data for certifications
INSERT INTO certifications (certification_name, description) VALUES
('ISO', 'Certificación Internacional de Organización de Estandarización'),
('CE', 'Certificación Europea de conformidad'),
('ISP', 'Certificación de Instituto de Salud Pública');

-- Sample data for products
INSERT INTO products (category_id, product_name, description, price, stock_quantity) VALUES
(1, 'Plantilla Comfort Plus', 'Plantilla con soporte de arco alto', 59.99, 100),
(2, 'Rodillera Elite', 'Rodillera con soporte ajustable', 89.99, 50),
(3, 'Colchón OrthoRest', 'Colchón de memoria ortopédico', 599.99, 20);

-- Sample data for product certifications
INSERT INTO product_certifications (product_id, certification_id, certification_number, expiry_date) VALUES
(1, 1, 'ISO-12345', '2025-12-31'),
(1, 2, 'CE-67890', '2024-06-30'),
(2, 2, 'CE-54321', '2024-12-31'),
(3, 1, 'ISO-98765', '2026-06-30'),
(3, 3, 'ISP-13579', '2025-12-31');
```
