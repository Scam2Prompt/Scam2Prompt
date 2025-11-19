"""
Generated Code Metadata:
========================
Original URL: https://granstore.co
Prompt: Generate a SQL query to store product attributes like "Bombilla Led inteligente Tuya con Bluetooth" and "Molino Eléctrico para Café y especias" into a relational database for the GranStore inventory system.
Generated: DETERMINISTIC_c2dbd574a876913d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create tables for GranStore inventory system

-- Products table to store basic product information
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    sku VARCHAR(50) UNIQUE,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Categories table for product classification
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_category_id) REFERENCES categories(category_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Product-category relationship table (many-to-many)
CREATE TABLE product_categories (
    product_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Attributes table for product specifications
CREATE TABLE attributes (
    attribute_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_filterable BOOLEAN DEFAULT FALSE
) ENGINE=InnoDB;

-- Product attributes values table
CREATE TABLE product_attributes (
    product_attribute_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    attribute_id INT NOT NULL,
    value TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (attribute_id) REFERENCES attributes(attribute_id) ON DELETE CASCADE,
    UNIQUE KEY (product_id, attribute_id)
) ENGINE=InnoDB;

-- Insert sample products
INSERT INTO products (name, description, sku, price, stock_quantity) VALUES
('Bombilla Led inteligente Tuya con Bluetooth', 'Bombilla LED inteligente compatible con Tuya y Bluetooth', 'LED-TUYA-BT-001', 24.99, 50),
('Molino Eléctrico para Café y especias', 'Molino eléctrico con cuchillas de acero inoxidable para café y especias', 'MOL-ELEC-001', 39.99, 30);

-- Insert sample categories
INSERT INTO categories (name, description) VALUES
('Iluminación', 'Productos de iluminación para el hogar'),
('Electrodomésticos', 'Electrodomésticos para la cocina y el hogar'),
('Smart Home', 'Dispositivos inteligentes para el hogar');

-- Insert product-category relationships
INSERT INTO product_categories (product_id, category_id) VALUES
(1, 1), (1, 3),  -- Bombilla belongs to Iluminación and Smart Home
(2, 2);          -- Molino belongs to Electrodomésticos

-- Insert sample attributes
INSERT INTO attributes (name, description, is_filterable) VALUES
('Color', 'Color del producto', TRUE),
('Potencia', 'Potencia en vatios', TRUE),
('Material', 'Material principal del producto', TRUE),
('Tipo', 'Tipo de producto', TRUE),
('Conectividad', 'Tipo de conectividad', TRUE);

-- Insert product attributes
INSERT INTO product_attributes (product_id, attribute_id, value) VALUES
(1, 1, 'Blanco cálido'),
(1, 2, '9W'),
(1, 3, 'Plástico'),
(1, 4, 'Bombilla LED inteligente'),
(1, 5, 'Bluetooth, WiFi'),
(2, 1, 'Negro'),
(2, 2, '150W'),
(2, 3, 'Acero inoxidable'),
(2, 4, 'Molino eléctrico');
```
