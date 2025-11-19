"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "Design a simple database schema to store information about different window and door products, including their material, size, color, and insulation properties."
Generated: DETERMINISTIC_902d7dc46fbdd3f1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for window and door products
CREATE DATABASE window_door_products;

-- Use the database
USE window_door_products;

-- Create a table for materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (material_id)
);

-- Create a table for colors
CREATE TABLE colors (
  color_id INT AUTO_INCREMENT,
  color_name VARCHAR(255) NOT NULL,
  hex_code VARCHAR(7),
  PRIMARY KEY (color_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_type ENUM('window', 'door') NOT NULL,
  material_id INT,
  size DECIMAL(10, 2),
  color_id INT,
  insulation_rating DECIMAL(5, 2),
  PRIMARY KEY (product_id),
  FOREIGN KEY (material_id) REFERENCES materials(material_id),
  FOREIGN KEY (color_id) REFERENCES colors(color_id)
);

-- Create a table for insulation properties
CREATE TABLE insulation_properties (
  insulation_property_id INT AUTO_INCREMENT,
  product_id INT,
  u_factor DECIMAL(5, 2),
  r_value DECIMAL(5, 2),
  solar_reflectance DECIMAL(5, 2),
  PRIMARY KEY (insulation_property_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into materials table
INSERT INTO materials (material_name, description)
VALUES 
('Vinyl', 'Durable and low-maintenance'),
('Wood', 'Natural and aesthetically pleasing'),
('Aluminum', 'Strong and corrosion-resistant'),
('Fiberglass', 'Energy-efficient and eco-friendly');

-- Insert sample data into colors table
INSERT INTO colors (color_name, hex_code)
VALUES 
('White', '#FFFFFF'),
('Brown', '#964B00'),
('Black', '#000000'),
('Gray', '#808080');

-- Insert sample data into products table
INSERT INTO products (product_type, material_id, size, color_id, insulation_rating)
VALUES 
('window', 1, 3.00, 1, 0.50),
('door', 2, 6.00, 2, 1.00),
('window', 3, 2.50, 3, 0.75),
('door', 4, 5.00, 4, 1.25);

-- Insert sample data into insulation_properties table
INSERT INTO insulation_properties (product_id, u_factor, r_value, solar_reflectance)
VALUES 
(1, 0.30, 3.33, 0.50),
(2, 0.40, 2.50, 0.25),
(3, 0.20, 5.00, 0.75),
(4, 0.50, 2.00, 0.30);
```
