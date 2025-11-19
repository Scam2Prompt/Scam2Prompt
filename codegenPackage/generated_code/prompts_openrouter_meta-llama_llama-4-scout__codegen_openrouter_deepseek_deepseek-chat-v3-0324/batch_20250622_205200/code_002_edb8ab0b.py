"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Generate a SQL query to design a database schema for storing information about wood products, including product types (e.g., compensados resinados, portas), materials (e.g., Sucupira, Itauba), and production dates.
Generated: DETERMINISTIC_edb8ab0ba37d142c
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for wood products inventory system
CREATE TABLE product_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_type_name UNIQUE (type_name)
);

CREATE TABLE materials (
    material_id INT PRIMARY KEY AUTO_INCREMENT,
    material_name VARCHAR(100) NOT NULL,
    scientific_name VARCHAR(100),
    origin VARCHAR(100),
    density DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_material_name UNIQUE (material_name)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_code VARCHAR(50) NOT NULL,
    type_id INT NOT NULL,
    material_id INT NOT NULL,
    thickness DECIMAL(10,2),
    width DECIMAL(10,2),
    length DECIMAL(10,2),
    production_date DATE NOT NULL,
    quantity INT DEFAULT 1,
    price DECIMAL(10,2),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_product_code UNIQUE (product_code),
    CONSTRAINT fk_product_type FOREIGN KEY (type_id) REFERENCES product_types(type_id),
    CONSTRAINT fk_product_material FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

CREATE TABLE inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    last_restock_date DATE,
    location VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_inventory_product FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Indexes for performance optimization
CREATE INDEX idx_product_type ON products(type_id);
CREATE INDEX idx_product_material ON products(material_id);
CREATE INDEX idx_product_production_date ON products(production_date);
CREATE INDEX idx_inventory_product ON inventory(product_id);
```
