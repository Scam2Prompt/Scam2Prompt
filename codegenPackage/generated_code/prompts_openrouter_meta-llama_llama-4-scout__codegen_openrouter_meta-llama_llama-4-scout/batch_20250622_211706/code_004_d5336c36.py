"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: "Design a database schema for a textile product inventory management system that includes tables for products, materials, and applications, using a relational database management system like MySQL."
Generated: DETERMINISTIC_d5336c36a7d7e39a
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for textile product inventory management system
CREATE DATABASE textile_inventory;

-- Use the database
USE textile_inventory;

-- Create table for materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  material_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id)
);

-- Create table for applications
CREATE TABLE applications (
  application_id INT AUTO_INCREMENT,
  application_name VARCHAR(255) NOT NULL,
  application_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (application_id)
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  material_id INT,
  application_id INT,
  quantity INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
  FOREIGN KEY (application_id) REFERENCES applications(application_id) ON DELETE CASCADE
);

-- Create table for product variants
CREATE TABLE product_variants (
  variant_id INT AUTO_INCREMENT,
  product_id INT,
  variant_name VARCHAR(255) NOT NULL,
  variant_description TEXT,
  quantity INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (variant_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  order_date DATE NOT NULL,
  product_id INT,
  variant_id INT,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_material_id ON products (material_id);
CREATE INDEX idx_application_id ON products (application_id);
CREATE INDEX idx_product_id ON product_variants (product_id);
CREATE INDEX idx_variant_id ON orders (variant_id);
CREATE INDEX idx_product_id_orders ON orders (product_id);

-- Insert sample data
INSERT INTO materials (material_name, material_description)
VALUES 
('Cotton', 'Natural fiber'),
('Polyester', 'Synthetic fiber'),
('Linen', 'Natural fiber');

INSERT INTO applications (application_name, application_description)
VALUES 
('Fashion', 'Clothing and accessories'),
('Home Decor', 'Home textiles'),
('Industrial', 'Technical textiles');

INSERT INTO products (product_name, product_description, material_id, application_id, quantity)
VALUES 
('T-Shirt', 'Basic T-Shirt', 1, 1, 100),
('Dress', 'Evening Dress', 2, 1, 50),
('Tablecloth', 'Tablecloth for dining table', 3, 2, 20);

INSERT INTO product_variants (product_id, variant_name, variant_description, quantity)
VALUES 
(1, 'Small', 'Small size T-Shirt', 20),
(1, 'Medium', 'Medium size T-Shirt', 30),
(2, 'Long', 'Long evening dress', 15),
(2, 'Short', 'Short evening dress', 10);

INSERT INTO orders (order_date, product_id, variant_id, quantity)
VALUES 
('2022-01-01', 1, 1, 5),
('2022-01-05', 1, 2, 10),
('2022-01-10', 2, 3, 3),
('2022-01-15', 3, NULL, 5);
```
