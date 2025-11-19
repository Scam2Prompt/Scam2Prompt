"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Design a simple database schema to store information about different battery products, including their specifications, prices, and applications, based on the structure of Battery Australia's online catalog.
Generated: DETERMINISTIC_b3231776da447acf
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for battery products
CREATE DATABASE battery_catalog;

-- Use the battery_catalog database
USE battery_catalog;

-- Create a table for manufacturers
CREATE TABLE manufacturers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for battery types
CREATE TABLE battery_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for battery products
CREATE TABLE battery_products (
  id INT AUTO_INCREMENT,
  manufacturer_id INT NOT NULL,
  battery_type_id INT NOT NULL,
  model_number VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  voltage DECIMAL(10, 2) NOT NULL,
  capacity DECIMAL(10, 2) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id),
  FOREIGN KEY (battery_type_id) REFERENCES battery_types(id)
);

-- Create a table for applications
CREATE TABLE applications (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for battery products and applications
CREATE TABLE battery_product_applications (
  battery_product_id INT NOT NULL,
  application_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (battery_product_id, application_id),
  FOREIGN KEY (battery_product_id) REFERENCES battery_products(id),
  FOREIGN KEY (application_id) REFERENCES applications(id)
);

-- Create a table for product specifications
CREATE TABLE product_specifications (
  id INT AUTO_INCREMENT,
  battery_product_id INT NOT NULL,
  specification_name VARCHAR(255) NOT NULL,
  specification_value VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (battery_product_id) REFERENCES battery_products(id)
);

-- Example data for testing
INSERT INTO manufacturers (name, description) 
VALUES 
('Panasonic', 'A Japanese multinational electronics company'),
('Energizer', 'An American multinational company');

INSERT INTO battery_types (name, description) 
VALUES 
('Alkaline', 'Alkaline battery type'),
('Lithium-ion', 'Lithium-ion battery type');

INSERT INTO battery_products (manufacturer_id, battery_type_id, model_number, name, description, voltage, capacity, price) 
VALUES 
(1, 1, 'LR20', 'Panasonic Alkaline Battery', 'A high-quality alkaline battery', 1.50, 20.00, 2.99),
(2, 2, 'L123', 'Energizer Lithium-ion Battery', 'A high-performance lithium-ion battery', 3.70, 10.00, 9.99);

INSERT INTO applications (name, description) 
VALUES 
('Home Appliances', 'Batteries for home appliances'),
('Automotive', 'Batteries for automotive use');

INSERT INTO battery_product_applications (battery_product_id, application_id) 
VALUES 
(1, 1),
(2, 2);

INSERT INTO product_specifications (battery_product_id, specification_name, specification_value) 
VALUES 
(1, 'Dimensions', '10mm x 20mm'),
(2, 'Weight', '50g');
```
