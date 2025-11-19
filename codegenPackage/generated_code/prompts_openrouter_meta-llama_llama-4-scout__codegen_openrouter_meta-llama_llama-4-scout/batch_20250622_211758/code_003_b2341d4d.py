"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: "Design a simple database schema to store information about wood products, including their applications, advantages, and treatment processes, similar to those described on the Trattar Madeiras website."
Generated: DETERMINISTIC_b2341d4da1332be3
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- wood_products database schema

-- Create database
CREATE DATABASE wood_products;

-- Use database
USE wood_products;

-- Create table for wood product types
CREATE TABLE product_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for wood products
CREATE TABLE wood_products (
  id INT AUTO_INCREMENT,
  product_type_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (product_type_id) REFERENCES product_types(id)
);

-- Create table for applications
CREATE TABLE applications (
  id INT AUTO_INCREMENT,
  wood_product_id INT NOT NULL,
  application VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (wood_product_id) REFERENCES wood_products(id)
);

-- Create table for advantages
CREATE TABLE advantages (
  id INT AUTO_INCREMENT,
  wood_product_id INT NOT NULL,
  advantage VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (wood_product_id) REFERENCES wood_products(id)
);

-- Create table for treatment processes
CREATE TABLE treatment_processes (
  id INT AUTO_INCREMENT,
  wood_product_id INT NOT NULL,
  process VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (wood_product_id) REFERENCES wood_products(id)
);

-- Example data for product types
INSERT INTO product_types (name, description)
VALUES 
('Softwoods', 'Softwoods are woods that come from coniferous trees.'),
('Hardwoods', 'Hardwoods are woods that come from deciduous trees.');

-- Example data for wood products
INSERT INTO wood_products (product_type_id, name, description)
VALUES 
(1, 'Pine', 'Pine is a softwood commonly used for furniture and construction.'),
(2, 'Oak', 'Oak is a hardwood commonly used for furniture and flooring.');

-- Example data for applications
INSERT INTO applications (wood_product_id, application, description)
VALUES 
(1, 'Furniture', 'Pine is often used to make furniture due to its affordability and workability.'),
(1, 'Construction', 'Pine is often used in construction due to its durability and resistance to rot.'),
(2, 'Flooring', 'Oak is often used for flooring due to its hardness and resistance to wear.'),
(2, 'Furniture', 'Oak is often used to make furniture due to its strength and durability.');

-- Example data for advantages
INSERT INTO advantages (wood_product_id, advantage, description)
VALUES 
(1, 'Affordability', 'Pine is generally less expensive than other types of wood.'),
(1, 'Workability', 'Pine is easy to work with due to its softness and straight grain.'),
(2, 'Durability', 'Oak is extremely durable and resistant to wear and tear.'),
(2, 'Strength', 'Oak is incredibly strong and can withstand heavy loads.');

-- Example data for treatment processes
INSERT INTO treatment_processes (wood_product_id, process, description)
VALUES 
(1, 'Staining', 'Pine can be stained to enhance its appearance and protect it from damage.'),
(1, 'Sealing', 'Pine can be sealed to protect it from moisture and damage.'),
(2, 'Sanding', 'Oak can be sanded to smooth out its surface and prepare it for finishing.'),
(2, 'Finishing', 'Oak can be finished with a variety of coatings to enhance its appearance and protect it from damage.');
```
