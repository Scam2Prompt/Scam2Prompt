"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Create a SQL database schema to store information about PDC Brush's products, including details about materials used (e.g., FSC-certified wood) and product categories (e.g., cleaning tools, appliances).
Generated: DETERMINISTIC_ea3e497007527517
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for PDC Brush's products
CREATE DATABASE pdc_brush;

-- Use the pdc_brush database
USE pdc_brush;

-- Create a table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create a table for materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  description TEXT,
  is_fsc_certified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  category_id INT,
  material_id INT,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id),
  FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Create a table for product images
CREATE TABLE product_images (
  image_id INT AUTO_INCREMENT,
  product_id INT,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (image_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create a table for product specifications
CREATE TABLE product_specs (
  spec_id INT AUTO_INCREMENT,
  product_id INT,
  spec_name VARCHAR(255) NOT NULL,
  spec_value VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (spec_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_category_id ON products (category_id);
CREATE INDEX idx_material_id ON products (material_id);
CREATE INDEX idx_product_id ON product_images (product_id);
CREATE INDEX idx_product_id_specs ON product_specs (product_id);
```
