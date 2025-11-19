"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: "Design a database schema to store information about various agricultural products, including fertilizers, bio stimulants, and their applications."
Generated: DETERMINISTIC_384e47212bd87e68
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for agricultural products
CREATE DATABASE agricultural_products;

-- Use the database
USE agricultural_products;

-- Create a table for product categories
CREATE TABLE product_categories (
  id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_category_id INT,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_category_id) REFERENCES product_categories(id)
);

-- Create a table for product types (fertilizers, bio stimulants, etc.)
CREATE TABLE product_types (
  id INT AUTO_INCREMENT,
  product_type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for products and product types
CREATE TABLE product_product_types (
  product_id INT,
  product_type_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, product_type_id),
  FOREIGN KEY (product_id) REFERENCES products(id),
  FOREIGN KEY (product_type_id) REFERENCES product_types(id)
);

-- Create a table for product applications
CREATE TABLE product_applications (
  id INT AUTO_INCREMENT,
  product_id INT,
  application_method VARCHAR(255) NOT NULL,
  dosage VARCHAR(255) NOT NULL,
  frequency VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create a table for crops
CREATE TABLE crops (
  id INT AUTO_INCREMENT,
  crop_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for products and crops
CREATE TABLE product_crops (
  product_id INT,
  crop_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, crop_id),
  FOREIGN KEY (product_id) REFERENCES products(id),
  FOREIGN KEY (crop_id) REFERENCES crops(id)
);

-- Insert sample data
INSERT INTO product_categories (category_name, description)
VALUES 
('Fertilizers', 'Fertilizers for plant growth'),
('Bio Stimulants', 'Bio stimulants for plant growth');

INSERT INTO products (product_name, product_category_id, description)
VALUES 
('Urea Fertilizer', 1, 'Urea fertilizer for plant growth'),
('Rhizobacteria Bio Stimulant', 2, 'Rhizobacteria bio stimulant for plant growth');

INSERT INTO product_types (product_type_name, description)
VALUES 
('Nitrogen-based', 'Nitrogen-based fertilizers'),
('Phosphorus-based', 'Phosphorus-based fertilizers');

INSERT INTO product_product_types (product_id, product_type_id)
VALUES 
(1, 1),
(1, 2);

INSERT INTO product_applications (product_id, application_method, dosage, frequency)
VALUES 
(1, 'Foliar Spray', '10ml/L', 'Weekly');

INSERT INTO crops (crop_name, description)
VALUES 
('Wheat', 'Wheat crop'),
('Corn', 'Corn crop');

INSERT INTO product_crops (product_id, crop_id)
VALUES 
(1, 1),
(1, 2);
```
