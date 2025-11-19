"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Develop a database schema to manage packaging product inventories and export destinations, inspired by Osku's wide portfolio and global distribution.
Generated: DETERMINISTIC_3bbaa902592bb883
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for packaging product inventories and export destinations
CREATE DATABASE packaging_inventory;

-- Use the created database
USE packaging_inventory;

-- Create table for product categories
CREATE TABLE product_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for packaging products
CREATE TABLE packaging_products (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  product_code VARCHAR(50) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  unit_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES product_categories(id) ON DELETE CASCADE
);

-- Create table for export destinations
CREATE TABLE export_destinations (
  id INT AUTO_INCREMENT,
  country VARCHAR(100) NOT NULL,
  city VARCHAR(100),
  address VARCHAR(255),
  postal_code VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for inventory transactions
CREATE TABLE inventory_transactions (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  transaction_type ENUM('IN', 'OUT') NOT NULL,
  quantity INT NOT NULL,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES packaging_products(id) ON DELETE CASCADE
);

-- Create table for export orders
CREATE TABLE export_orders (
  id INT AUTO_INCREMENT,
  destination_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_quantity INT NOT NULL,
  total_value DECIMAL(10, 2) NOT NULL,
  status ENUM('PENDING', 'SHIPPED', 'DELIVERED') NOT NULL DEFAULT 'PENDING',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (destination_id) REFERENCES export_destinations(id) ON DELETE CASCADE
);

-- Create table for export order items
CREATE TABLE export_order_items (
  id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (order_id) REFERENCES export_orders(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES packaging_products(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_packaging_products_category_id ON packaging_products (category_id);
CREATE INDEX idx_inventory_transactions_product_id ON inventory_transactions (product_id);
CREATE INDEX idx_export_orders_destination_id ON export_orders (destination_id);
CREATE INDEX idx_export_order_items_order_id ON export_order_items (order_id);
CREATE INDEX idx_export_order_items_product_id ON export_order_items (product_id);
```

```sql
-- sample_data.sql

-- Insert sample data into product categories
INSERT INTO product_categories (name, description)
VALUES
  ('Paper Products', 'Paper-based packaging products'),
  ('Plastic Products', 'Plastic-based packaging products'),
  ('Cardboard Products', 'Cardboard-based packaging products');

-- Insert sample data into packaging products
INSERT INTO packaging_products (category_id, product_name, product_code, quantity, unit_price)
VALUES
  (1, 'Paper Cups', 'PC-001', 1000, 0.50),
  (1, 'Paper Plates', 'PP-001', 500, 0.25),
  (2, 'Plastic Bottles', 'PB-001', 2000, 1.00),
  (3, 'Cardboard Boxes', 'CB-001', 1500, 1.50);

-- Insert sample data into export destinations
INSERT INTO export_destinations (country, city, address, postal_code)
VALUES
  ('United States', 'New York', '123 Main St', '10001'),
  ('Canada', 'Toronto', '456 Maple St', 'M5V 1A1'),
  ('Mexico', 'Mexico City', '789 Reforma St', '01000');

-- Insert sample data into inventory transactions
INSERT INTO inventory_transactions (product_id, transaction_type, quantity)
VALUES
  (1, 'IN', 500),
  (1, 'OUT', 200),
  (2, 'IN', 300),
  (3, 'IN', 1000);

-- Insert sample data into export orders
INSERT INTO export_orders (destination_id, total_quantity, total_value)
VALUES
  (1, 100, 50.00),
  (2, 200, 100.00),
  (3, 300, 150.00);

-- Insert sample data into export order items
INSERT INTO export_order_items (order_id, product_id, quantity, unit_price)
VALUES
  (1, 1, 50, 0.50),
  (1, 2, 50, 0.25),
  (2, 3, 100, 1.00),
  (3, 4, 150, 1.50);
```
