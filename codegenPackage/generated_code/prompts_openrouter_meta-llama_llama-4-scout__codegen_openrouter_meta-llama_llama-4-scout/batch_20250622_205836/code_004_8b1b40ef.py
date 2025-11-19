"""
Generated Code Metadata:
========================
Original URL: https://celinedionmerch.com
Prompt: Design a database schema to store information about Celine Dion's merchandise, including product categories, prices, and inventory levels.
Generated: DETERMINISTIC_8b1b40ef56bbb6aa
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- merchandise_schema.sql

-- Create a database schema for Celine Dion's merchandise
CREATE DATABASE celine_dion_merchandise;

-- Use the database schema
USE celine_dion_merchandise;

-- Create a table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE
);

-- Create a table for inventory levels
CREATE TABLE inventory_levels (
  inventory_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (inventory_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id)
);

-- Create a table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO product_categories (category_name, description)
VALUES
  ('T-Shirts', 'Celine Dion branded T-Shirts'),
  ('Hoodies', 'Celine Dion branded Hoodies'),
  ('CDs', 'Celine Dion music CDs');

INSERT INTO products (category_id, product_name, description, price)
VALUES
  (1, 'Celine Dion Tour T-Shirt', 'Official tour T-Shirt', 25.99),
  (1, 'Celine Dion Logo T-Shirt', 'Official logo T-Shirt', 22.99),
  (2, 'Celine Dion Tour Hoodie', 'Official tour Hoodie', 49.99),
  (3, 'Celine Dion Greatest Hits CD', 'Collection of greatest hits', 14.99);

INSERT INTO inventory_levels (product_id, quantity)
VALUES
  (1, 100),
  (2, 50),
  (3, 200),
  (4, 500);

-- Example query to retrieve product information with inventory levels
SELECT 
  p.product_name, 
  pc.category_name, 
  p.price, 
  il.quantity AS inventory_level
FROM 
  products p
  JOIN product_categories pc ON p.category_id = pc.category_id
  JOIN inventory_levels il ON p.product_id = il.product_id;
```
