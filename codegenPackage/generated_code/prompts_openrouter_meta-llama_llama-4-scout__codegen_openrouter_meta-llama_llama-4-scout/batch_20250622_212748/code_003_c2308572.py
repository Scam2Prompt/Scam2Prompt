"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Design a database schema to store information about Yobugo's products, including their ingredients, flavors, and packaging options.
Generated: DETERMINISTIC_c2308572b8ac0833
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Yobugo's products
CREATE DATABASE yobugo_products;

-- Use the database
USE yobugo_products;

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create a table for ingredients
CREATE TABLE ingredients (
  ingredient_id INT AUTO_INCREMENT,
  ingredient_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ingredient_id)
);

-- Create a many-to-many relationship table for product ingredients
CREATE TABLE product_ingredients (
  product_id INT NOT NULL,
  ingredient_id INT NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, ingredient_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id) ON DELETE CASCADE
);

-- Create a table for flavors
CREATE TABLE flavors (
  flavor_id INT AUTO_INCREMENT,
  flavor_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (flavor_id)
);

-- Create a many-to-many relationship table for product flavors
CREATE TABLE product_flavors (
  product_id INT NOT NULL,
  flavor_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, flavor_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (flavor_id) REFERENCES flavors(flavor_id) ON DELETE CASCADE
);

-- Create a table for packaging options
CREATE TABLE packaging_options (
  packaging_id INT AUTO_INCREMENT,
  packaging_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (packaging_id)
);

-- Create a many-to-many relationship table for product packaging options
CREATE TABLE product_packaging (
  product_id INT NOT NULL,
  packaging_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, packaging_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (packaging_id) REFERENCES packaging_options(packaging_id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO products (product_name, description)
VALUES 
('Product A', 'This is product A'),
('Product B', 'This is product B');

INSERT INTO ingredients (ingredient_name)
VALUES 
('Ingredient 1'),
('Ingredient 2'),
('Ingredient 3');

INSERT INTO product_ingredients (product_id, ingredient_id, quantity)
VALUES 
(1, 1, 10.0),
(1, 2, 20.0),
(2, 3, 30.0);

INSERT INTO flavors (flavor_name)
VALUES 
('Flavor 1'),
('Flavor 2');

INSERT INTO product_flavors (product_id, flavor_id)
VALUES 
(1, 1),
(2, 2);

INSERT INTO packaging_options (packaging_name)
VALUES 
('Packaging 1'),
('Packaging 2');

INSERT INTO product_packaging (product_id, packaging_id)
VALUES 
(1, 1),
(2, 2);
```
