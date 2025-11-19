"""
Generated Code Metadata:
========================
Original URL: https://gprobolsa.com
Prompt: Write SQL queries to manage a database of eco-friendly products, including categories like "reusable bags" and "customizable promotional items," inspired by Grupo ProBolsa's product catalog.
Generated: DETERMINISTIC_b5493d9f6364604d
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for eco-friendly products
CREATE DATABASE IF NOT EXISTS eco_friendly_products;
USE eco_friendly_products;

-- Create product categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (category_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create products table
CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    is_customizable BOOLEAN DEFAULT FALSE,
    is_featured BOOLEAN DEFAULT FALSE,
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE,
    INDEX (product_name),
    INDEX (price)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create product materials table (for sustainability tracking)
CREATE TABLE IF NOT EXISTS materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    material_name VARCHAR(100) NOT NULL,
    is_recyclable BOOLEAN DEFAULT TRUE,
    is_biodegradable BOOLEAN DEFAULT FALSE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY (material_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Junction table for product materials
CREATE TABLE IF NOT EXISTS product_materials (
    product_id INT NOT NULL,
    material_id INT NOT NULL,
    percentage DECIMAL(5,2) DEFAULT 100.00,
    PRIMARY KEY (product_id, material_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert sample categories
INSERT INTO categories (category_name, description) VALUES
('Reusable Bags', 'Eco-friendly bags for shopping and everyday use'),
('Customizable Promotional Items', 'Brandable eco-friendly products for marketing'),
('Bamboo Products', 'Sustainable products made from bamboo'),
('Recycled Materials', 'Products made from recycled materials');

-- Insert sample materials
INSERT INTO materials (material_name, is_recyclable, is_biodegradable, description) VALUES
('Organic Cotton', TRUE, TRUE, 'Natural fiber grown without pesticides'),
('Recycled PET', TRUE, FALSE, 'Polyester made from recycled plastic bottles'),
('Bamboo', TRUE, TRUE, 'Fast-growing sustainable plant material'),
('Jute', TRUE, TRUE, 'Natural vegetable fiber'),
('Recycled Paper', TRUE, TRUE, 'Paper made from post-consumer waste');

-- Insert sample products
INSERT INTO products (category_id, product_name, description, price, stock_quantity, is_customizable, is_featured) VALUES
(1, 'Organic Cotton Tote Bag', 'Large reusable shopping bag made from organic cotton', 12.99, 100, TRUE, TRUE),
(1, 'Recycled PET Backpack', 'Durable backpack made from recycled plastic bottles', 24.99, 75, TRUE, FALSE),
(2, 'Custom Bamboo Pen', 'Eco-friendly pen with bamboo body, customizable logo', 3.50, 200, TRUE, TRUE),
(2, 'Recycled Notebook', 'Notebook made from 100% recycled paper, customizable cover', 8.99, 150, TRUE, FALSE),
(3, 'Bamboo Cutlery Set', 'Portable reusable cutlery set with bamboo handles', 9.99, 80, FALSE, TRUE);

-- Insert product-material relationships
INSERT INTO product_materials (product_id, material_id, percentage) VALUES
(1, 1, 100.00),
(2, 2, 100.00),
(3, 3, 85.00),
(4, 5, 100.00),
(5, 3, 100.00);

-- Query to get all products with their categories and materials
SELECT 
    p.product_id,
    p.product_name,
    p.price,
    p.stock_quantity,
    c.category_name,
    GROUP_CONCAT(m.material_name SEPARATOR ', ') AS materials
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id
LEFT JOIN 
    product_materials pm ON p.product_id = pm.product_id
LEFT JOIN 
    materials m ON pm.material_id = m.material_id
GROUP BY 
    p.product_id;

-- Query to get customizable promotional items
SELECT 
    p.product_id,
    p.product_name,
    p.price,
    p.description
FROM 
    products p
JOIN 
    categories c ON p.category_id = c.category_id
WHERE 
    c.category_name = 'Customizable Promotional Items'
    AND p.is_customizable = TRUE;

-- Query to update stock quantity after purchase
UPDATE products
SET stock_quantity = stock_quantity - 1
WHERE product_id = 1 AND stock_quantity > 0;

-- Query to find all biodegradable products
SELECT 
    p.product_id,
    p.product_name,
    p.price
FROM 
    products p
JOIN 
    product_materials pm ON p.product_id = pm.product_id
JOIN 
    materials m ON pm.material_id = m.material_id
WHERE 
    m.is_biodegradable = TRUE
GROUP BY 
    p.product_id;

-- Query to add a new product
INSERT INTO products (category_id, product_name, description, price, stock_quantity, is_customizable)
VALUES (4, 'Recycled Glass Water Bottle', 'Eco-friendly water bottle made from recycled glass', 14.99, 50, TRUE);

-- Query to delete a discontinued product
DELETE FROM products WHERE product_id = 5;
```
