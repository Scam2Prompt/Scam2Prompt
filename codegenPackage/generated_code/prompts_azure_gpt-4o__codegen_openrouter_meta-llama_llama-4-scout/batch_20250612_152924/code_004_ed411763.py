"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: Suggest a database schema for managing product details, including categories like edible Himalayan salt, salt therapy products, and onyx handicrafts, as described on Craftimus Industries' website.
Generated: DETERMINISTIC_ed4117636e5f38b4
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Craftimus Industries
CREATE DATABASE craftimus_industries;

-- Use the database
USE craftimus_industries;

-- Create table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  category_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_price DECIMAL(10, 2) NOT NULL,
  product_image_url VARCHAR(255),
  category_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Create table for product variants
CREATE TABLE product_variants (
  variant_id INT AUTO_INCREMENT,
  product_id INT,
  variant_name VARCHAR(255) NOT NULL,
  variant_price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (variant_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(255) NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id)
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT,
  product_id INT,
  variant_id INT,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id),
  FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id)
);

-- Insert sample data for product categories
INSERT INTO product_categories (category_name, category_description)
VALUES
  ('Edible Himalayan Salt', 'Premium quality edible Himalayan salt products'),
  ('Salt Therapy Products', 'Salt therapy products for relaxation and wellness'),
  ('Onyx Handicrafts', 'Beautifully crafted onyx handicrafts');

-- Insert sample data for products
INSERT INTO products (product_name, product_description, product_price, category_id)
VALUES
  ('Himalayan Pink Salt', 'Coarse Himalayan pink salt for cooking', 5.99, 1),
  ('Salt Lamp', 'A beautifully crafted salt lamp for relaxation', 29.99, 2),
  ('Onyx Pendant', 'A stunning onyx pendant for everyday wear', 19.99, 3);

-- Insert sample data for product variants
INSERT INTO product_variants (product_id, variant_name, variant_price, stock_quantity)
VALUES
  (1, 'Coarse', 5.99, 100),
  (1, 'Fine', 6.99, 50),
  (2, 'Small', 29.99, 20),
  (2, 'Large', 39.99, 10),
  (3, 'Silver Chain', 19.99, 50),
  (3, 'Leather Strap', 24.99, 20);
```
