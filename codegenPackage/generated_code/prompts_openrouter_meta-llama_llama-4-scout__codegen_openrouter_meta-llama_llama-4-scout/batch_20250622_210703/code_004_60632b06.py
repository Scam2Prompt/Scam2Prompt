"""
Generated Code Metadata:
========================
Original URL: https://bekon.rs
Prompt: Design a database schema to store information about meat products, including types (e.g., fresh meat, sausages, dry products) and recipes, inspired by Bekon Promet's product offerings.
Generated: DETERMINISTIC_60632b0620af7fba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for meat products
CREATE DATABASE meat_products;

-- Use the database
USE meat_products;

-- Create a table for product types
CREATE TABLE product_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  type_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (type_id) REFERENCES product_types(id) ON DELETE CASCADE
);

-- Create a table for ingredients
CREATE TABLE ingredients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for recipes
CREATE TABLE recipes (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  ingredient_id INT NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  FOREIGN KEY (ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
);

-- Create a table for suppliers
CREATE TABLE suppliers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for product suppliers
CREATE TABLE product_suppliers (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  supplier_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO product_types (name, description)
VALUES
  ('Fresh Meat', 'Fresh meat products'),
  ('Sausages', 'Sausages and similar products'),
  ('Dry Products', 'Dried meat products');

INSERT INTO products (type_id, name, description, price)
VALUES
  (1, 'Pork Chops', 'Thick-cut pork chops', 8.99),
  (1, 'Beef Steaks', 'Thick-cut beef steaks', 12.99),
  (2, 'Classic Sausages', 'Traditional sausages', 5.99),
  (3, 'Dried Beef', 'Dried and cured beef', 7.99);

INSERT INTO ingredients (name)
VALUES
  ('Pork'),
  ('Beef'),
  ('Salt'),
  ('Spices'),
  ('Preservatives');

INSERT INTO recipes (product_id, ingredient_id, quantity, unit)
VALUES
  (1, 1, 1000.00, 'g'),
  (1, 3, 10.00, 'g'),
  (2, 2, 1000.00, 'g'),
  (2, 4, 5.00, 'g'),
  (3, 1, 500.00, 'g'),
  (3, 4, 10.00, 'g'),
  (4, 2, 1000.00, 'g'),
  (4, 3, 20.00, 'g');

INSERT INTO suppliers (name, address, phone, email)
VALUES
  ('Supplier 1', 'Address 1', '1234567890', 'supplier1@example.com'),
  ('Supplier 2', 'Address 2', '9876543210', 'supplier2@example.com');

INSERT INTO product_suppliers (product_id, supplier_id, price)
VALUES
  (1, 1, 7.99),
  (1, 2, 8.49),
  (2, 1, 11.99),
  (2, 2, 12.49),
  (3, 1, 5.49),
  (3, 2, 5.99),
  (4, 1, 6.99),
  (4, 2, 7.49);
```
