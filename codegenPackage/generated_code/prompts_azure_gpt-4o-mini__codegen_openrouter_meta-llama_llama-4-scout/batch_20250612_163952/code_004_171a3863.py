"""
Generated Code Metadata:
========================
Original URL: https://11tesorosibericos.com
Prompt: Design a database schema for an online store that includes tables for products like wines and gift baskets, as seen on 11 Tesoros Ibéricos, ensuring it supports various product categories and pricing.
Generated: DETERMINISTIC_171a386377ce54e4
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for online store
CREATE DATABASE online_store;

-- Use online store database
USE online_store;

-- Create table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  category_id INT,
  product_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Create table for wine products
CREATE TABLE wines (
  wine_id INT AUTO_INCREMENT,
  product_id INT,
  wine_type VARCHAR(100) NOT NULL,
  vintage INT,
  grape_variety VARCHAR(100),
  region VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (wine_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for gift basket products
CREATE TABLE gift_baskets (
  gift_basket_id INT AUTO_INCREMENT,
  product_id INT,
  basket_type VARCHAR(100) NOT NULL,
  contents TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (gift_basket_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_cost DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id)
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT,
  product_id INT,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_product_categories_category_id ON products (category_id);
CREATE INDEX idx_products_product_id ON wines (product_id);
CREATE INDEX idx_products_product_id ON gift_baskets (product_id);
CREATE INDEX idx_orders_order_id ON order_items (order_id);
CREATE INDEX idx_order_items_product_id ON order_items (product_id);
```

```sql
-- sample_data.sql

-- Insert sample data into product categories
INSERT INTO product_categories (category_name, description)
VALUES
  ('Wines', 'Selection of fine wines'),
  ('Gift Baskets', 'Thoughtfully curated gift baskets');

-- Insert sample data into products
INSERT INTO products (category_id, product_name, description, price, stock_quantity)
VALUES
  (1, 'Rioja Reserva', 'A rich and complex Rioja', 25.00, 100),
  (1, 'Ribera del Duero', 'A full-bodied Spanish red', 30.00, 50),
  (2, 'Tesoros Ibéricos Gift Basket', 'A selection of Iberian delicacies', 50.00, 20);

-- Insert sample data into wines
INSERT INTO wines (product_id, wine_type, vintage, grape_variety, region)
VALUES
  (1, 'Red', 2015, 'Tempranillo', 'La Rioja'),
  (2, 'Red', 2018, 'Tempranillo', 'Ribera del Duero');

-- Insert sample data into gift baskets
INSERT INTO gift_baskets (product_id, basket_type, contents)
VALUES
  (3, 'Standard', 'Selection of cured meats, cheeses, and crackers');

-- Insert sample data into orders
INSERT INTO orders (customer_name, total_cost)
VALUES
  ('John Doe', 50.00),
  ('Jane Smith', 100.00);

-- Insert sample data into order items
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
  (1, 1, 2, 25.00),
  (2, 3, 1, 50.00);
```
