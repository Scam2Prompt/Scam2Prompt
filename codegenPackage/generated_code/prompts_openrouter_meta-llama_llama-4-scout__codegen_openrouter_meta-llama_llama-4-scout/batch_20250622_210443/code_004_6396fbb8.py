"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: "Design a database schema to store information about various Himalayan salt products, including their types, prices, and quantities."
Generated: DETERMINISTIC_6396fbb87d309e2e
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Himalayan salt products
CREATE DATABASE himalayan_salt_products;

-- Use the database
USE himalayan_salt_products;

-- Create a table for product types
CREATE TABLE product_types (
  id INT AUTO_INCREMENT,
  type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  type_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (type_id) REFERENCES product_types(id) ON DELETE CASCADE
);

-- Create a table for product variations
CREATE TABLE product_variations (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  variation_name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create a table for orders
CREATE TABLE orders (
  id INT AUTO_INCREMENT,
  product_id INT,
  variation_id INT,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  quantity INT NOT NULL,
  total_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE SET NULL,
  FOREIGN KEY (variation_id) REFERENCES product_variations(id) ON DELETE SET NULL
);

-- Insert sample data into product types
INSERT INTO product_types (type_name, description)
VALUES 
('Lamps', 'Himalayan salt lamps'),
('Bath Products', 'Bath products made from Himalayan salt'),
('Cooking Salt', 'Himalayan salt for cooking');

-- Insert sample data into products
INSERT INTO products (type_id, product_name, price, quantity)
VALUES 
(1, 'Himalayan Salt Lamp - Small', 20.00, 100),
(1, 'Himalayan Salt Lamp - Large', 50.00, 50),
(2, 'Himalayan Salt Bath Salts', 15.00, 200),
(3, 'Himalayan Cooking Salt', 5.00, 500);

-- Insert sample data into product variations
INSERT INTO product_variations (product_id, variation_name, price, quantity)
VALUES 
(1, 'Pink', 20.00, 50),
(1, 'White', 22.00, 30),
(2, 'Pink', 50.00, 20),
(2, 'White', 55.00, 15);

-- Example query to retrieve all products with their types and variations
SELECT 
  p.id,
  pt.type_name,
  p.product_name,
  p.price,
  p.quantity,
  pv.id AS variation_id,
  pv.variation_name,
  pv.price AS variation_price,
  pv.quantity AS variation_quantity
FROM 
  products p
  JOIN product_types pt ON p.type_id = pt.id
  LEFT JOIN product_variations pv ON p.id = pv.product_id;
```
