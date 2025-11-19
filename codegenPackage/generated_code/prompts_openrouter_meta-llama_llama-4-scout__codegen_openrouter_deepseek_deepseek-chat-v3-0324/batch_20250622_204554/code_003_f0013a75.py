"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: "Design a database schema to store information about ITACA CERAMIC's tile products, including product categories, sizes, materials, and features, and provide a SQL code snippet to populate the database with sample data."
Generated: DETERMINISTIC_f0013a759ad27848
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# SQL Database Schema for ITACA CERAMIC Tile Products

```sql
-- Database schema for ITACA CERAMIC tile products
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (category_name)
);

CREATE TABLE materials (
    material_id INT PRIMARY KEY AUTO_INCREMENT,
    material_name VARCHAR(50) NOT NULL,
    description TEXT,
    durability_rating INT CHECK (durability_rating BETWEEN 1 AND 10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (material_name)
);

CREATE TABLE sizes (
    size_id INT PRIMARY KEY AUTO_INCREMENT,
    length_cm DECIMAL(6,2) NOT NULL,
    width_cm DECIMAL(6,2) NOT NULL,
    thickness_mm DECIMAL(4,1) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (length_cm, width_cm, thickness_mm)
);

CREATE TABLE features (
    feature_id INT PRIMARY KEY AUTO_INCREMENT,
    feature_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (feature_name)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_code VARCHAR(20) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    material_id INT NOT NULL,
    size_id INT NOT NULL,
    price_per_sqm DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    is_waterproof BOOLEAN DEFAULT FALSE,
    is_anti_slip BOOLEAN DEFAULT FALSE,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (material_id) REFERENCES materials(material_id),
    FOREIGN KEY (size_id) REFERENCES sizes(size_id),
    UNIQUE KEY (product_code)
);

CREATE TABLE product_features (
    product_id INT NOT NULL,
    feature_id INT NOT NULL,
    PRIMARY KEY (product_id, feature_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES features(feature_id) ON DELETE CASCADE
);

-- Sample data insertion
INSERT INTO categories (category_name, description) VALUES
('Floor Tiles', 'Ceramic tiles designed for flooring applications'),
('Wall Tiles', 'Tiles specifically made for wall installations'),
('Outdoor Tiles', 'Weather-resistant tiles for exterior use'),
('Mosaic Tiles', 'Small decorative tiles for artistic patterns');

INSERT INTO materials (material_name, description, durability_rating) VALUES
('Porcelain', 'Dense, durable ceramic material', 9),
('Ceramic', 'Traditional clay-based material', 7),
('Stoneware', 'Dense, chip-resistant material', 8),
('Terracotta', 'Porous, rustic clay material', 6);

INSERT INTO sizes (length_cm, width_cm, thickness_mm) VALUES
(30.0, 30.0, 8.0),
(60.0, 60.0, 10.0),
(45.0, 45.0, 9.0),
(20.0, 20.0, 6.0),
(60.0, 30.0, 9.0);

INSERT INTO features (feature_name, description) VALUES
('Frost Resistant', 'Suitable for cold climates'),
('Stain Resistant', 'Resists common stains'),
('High Gloss', 'Reflective glossy finish'),
('Matte Finish', 'Non-reflective surface'),
('Textured', 'Tactile surface for better grip');

INSERT INTO products (product_code, product_name, category_id, material_id, size_id, price_per_sqm, stock_quantity, is_waterproof, is_anti_slip) VALUES
('ITC-FP01', 'Premium Porcelain Floor Tile', 1, 1, 2, 45.99, 500, TRUE, TRUE),
('ITC-WC02', 'Classic Ceramic Wall Tile', 2, 2, 1, 28.50, 800, TRUE, FALSE),
('ITC-OS03', 'Outdoor Stoneware Tile', 3, 3, 2, 39.75, 300, TRUE, TRUE),
('ITC-MM04', 'Mosaic Medallion Tile', 4, 4, 4, 52.25, 150, FALSE, FALSE),
('ITC-FP05', 'Modern Porcelain Plank', 1, 1, 5, 49.99, 400, TRUE, TRUE);

INSERT INTO product_features (product_id, feature_id) VALUES
(1, 1), (1, 2), (1, 5),
(2, 2), (2, 3),
(3, 1), (3, 5),
(4, 4),
(5, 1), (5, 2), (5, 5);
```
