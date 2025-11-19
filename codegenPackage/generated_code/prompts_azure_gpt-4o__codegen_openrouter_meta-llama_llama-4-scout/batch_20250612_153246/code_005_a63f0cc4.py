"""
Generated Code Metadata:
========================
Original URL: https://www.pensar.inf.br
Prompt: Create a database schema for an ERP system inspired by SOLPEN, ensuring it supports modular customization for industries like manufacturing, commerce, and distribution.
Generated: DETERMINISTIC_a63f0cc4cc91f6d5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE erp_system;

-- Use database
USE erp_system;

-- Create table for industries
CREATE TABLE industries (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for modules
CREATE TABLE modules (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  industry_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (industry_id) REFERENCES industries(id)
);

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for companies
CREATE TABLE companies (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  industry_id INT,
  address VARCHAR(255),
  city VARCHAR(255),
  state VARCHAR(255),
  country VARCHAR(255),
  zip_code VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (industry_id) REFERENCES industries(id)
);

-- Create table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2),
  company_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- Create table for orders
CREATE TABLE orders (
  id INT AUTO_INCREMENT,
  order_date DATE,
  total DECIMAL(10, 2),
  company_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id)
);

-- Create table for order items
CREATE TABLE order_items (
  id INT AUTO_INCREMENT,
  order_id INT,
  product_id INT,
  quantity INT,
  unit_price DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (order_id) REFERENCES orders(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create table for inventory
CREATE TABLE inventory (
  id INT AUTO_INCREMENT,
  product_id INT,
  quantity INT,
  warehouse VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create table for manufacturing
CREATE TABLE manufacturing (
  id INT AUTO_INCREMENT,
  product_id INT,
  production_date DATE,
  quantity INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create table for commerce
CREATE TABLE commerce (
  id INT AUTO_INCREMENT,
  order_id INT,
  payment_method VARCHAR(255),
  payment_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (order_id) REFERENCES orders(id)
);

-- Create table for distribution
CREATE TABLE distribution (
  id INT AUTO_INCREMENT,
  order_id INT,
  shipping_method VARCHAR(255),
  shipping_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (order_id) REFERENCES orders(id)
);

-- Create views for industries
CREATE VIEW industry_modules AS
SELECT 
  i.name AS industry_name,
  m.name AS module_name
FROM 
  industries i
  JOIN modules m ON i.id = m.industry_id;

-- Create stored procedure for adding new industry
DELIMITER //
CREATE PROCEDURE add_industry(
  IN p_name VARCHAR(255),
  IN p_description TEXT
)
BEGIN
  INSERT INTO industries (name, description)
  VALUES (p_name, p_description);
END//
DELIMITER ;

-- Create stored procedure for adding new module
DELIMITER //
CREATE PROCEDURE add_module(
  IN p_name VARCHAR(255),
  IN p_description TEXT,
  IN p_industry_id INT
)
BEGIN
  INSERT INTO modules (name, description, industry_id)
  VALUES (p_name, p_description, p_industry_id);
END//
DELIMITER ;

-- Create triggers for auditing
DELIMITER //
CREATE TRIGGER audit_industry_update
AFTER UPDATE ON industries
FOR EACH ROW
BEGIN
  INSERT INTO audit_log (table_name, record_id, updated_at)
  VALUES ('industries', OLD.id, NOW());
END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER audit_module_update
AFTER UPDATE ON modules
FOR EACH ROW
BEGIN
  INSERT INTO audit_log (table_name, record_id, updated_at)
  VALUES ('modules', OLD.id, NOW());
END//
DELIMITER ;

-- Create audit log table
CREATE TABLE audit_log (
  id INT AUTO_INCREMENT,
  table_name VARCHAR(255),
  record_id INT,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);
```
