"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Design a database schema to store auto parts products with attributes such as product code, name, price, and application (e.g., vehicle make, model, year), inspired by the product listings on autopecasbrazz.
Generated: DETERMINISTIC_dc7e9d5d7fbe1001
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- auto_parts_schema.sql

-- Create database schema for auto parts products
CREATE DATABASE auto_parts;

-- Use the auto_parts database
USE auto_parts;

-- Create table for vehicle makes
CREATE TABLE vehicle_makes (
  make_id INT AUTO_INCREMENT,
  make_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (make_id),
  UNIQUE KEY (make_name)
);

-- Create table for vehicle models
CREATE TABLE vehicle_models (
  model_id INT AUTO_INCREMENT,
  make_id INT NOT NULL,
  model_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (model_id),
  FOREIGN KEY (make_id) REFERENCES vehicle_makes(make_id) ON DELETE CASCADE
);

-- Create table for vehicle years
CREATE TABLE vehicle_years (
  year_id INT AUTO_INCREMENT,
  year_value INT NOT NULL,
  PRIMARY KEY (year_id),
  UNIQUE KEY (year_value)
);

-- Create table for product applications
CREATE TABLE product_applications (
  application_id INT AUTO_INCREMENT,
  model_id INT NOT NULL,
  year_id INT NOT NULL,
  PRIMARY KEY (application_id),
  FOREIGN KEY (model_id) REFERENCES vehicle_models(model_id) ON DELETE CASCADE,
  FOREIGN KEY (year_id) REFERENCES vehicle_years(year_id) ON DELETE CASCADE
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_code VARCHAR(50) NOT NULL,
  product_name VARCHAR(200) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (product_id),
  UNIQUE KEY (product_code)
);

-- Create many-to-many relationship table for products and applications
CREATE TABLE product_application_links (
  product_id INT NOT NULL,
  application_id INT NOT NULL,
  PRIMARY KEY (product_id, application_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (application_id) REFERENCES product_applications(application_id) ON DELETE CASCADE
);

-- Example data insertion
INSERT INTO vehicle_makes (make_name) VALUES
  ('Toyota'),
  ('Honda'),
  ('Ford');

INSERT INTO vehicle_models (make_id, model_name) VALUES
  (1, 'Corolla'),
  (1, 'Camry'),
  (2, 'Civic'),
  (3, 'Fusion');

INSERT INTO vehicle_years (year_value) VALUES
  (2015),
  (2018),
  (2020);

INSERT INTO product_applications (model_id, year_id) VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 1),
  (4, 2);

INSERT INTO products (product_code, product_name, price) VALUES
  ('ABC123', 'Oil Filter', 15.99),
  ('DEF456', 'Air Filter', 8.99),
  ('GHI789', 'Spark Plug', 5.99);

INSERT INTO product_application_links (product_id, application_id) VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 4),
  (1, 5);
```
