"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Design a database schema to store Karnataka Aromas' product information, including fragrances, flavors, and essential oils.
Generated: DETERMINISTIC_6202e074986e3333
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Karnataka Aromas
CREATE DATABASE karnataka_aromas;

-- Use the database
USE karnataka_aromas;

-- Create a table for fragrances
CREATE TABLE fragrances (
  fragrance_id INT AUTO_INCREMENT,
  fragrance_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (fragrance_id)
);

-- Create a table for flavors
CREATE TABLE flavors (
  flavor_id INT AUTO_INCREMENT,
  flavor_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (flavor_id)
);

-- Create a table for essential oils
CREATE TABLE essential_oils (
  oil_id INT AUTO_INCREMENT,
  oil_name VARCHAR(255) NOT NULL,
  oil_type VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (oil_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  fragrance_id INT,
  flavor_id INT,
  oil_id INT,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (fragrance_id) REFERENCES fragrances(fragrance_id) ON DELETE SET NULL,
  FOREIGN KEY (flavor_id) REFERENCES flavors(flavor_id) ON DELETE SET NULL,
  FOREIGN KEY (oil_id) REFERENCES essential_oils(oil_id) ON DELETE SET NULL
);

-- Create a table for product inventory
CREATE TABLE product_inventory (
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
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
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

-- Insert sample data into fragrances table
INSERT INTO fragrances (fragrance_name, description)
VALUES 
('Lavender', 'A calming and soothing fragrance'),
('Jasmine', 'A sweet and floral fragrance'),
('Rose', 'A classic and romantic fragrance');

-- Insert sample data into flavors table
INSERT INTO flavors (flavor_name, description)
VALUES 
('Vanilla', 'A sweet and creamy flavor'),
('Strawberry', 'A sweet and fruity flavor'),
('Mint', 'A cool and refreshing flavor');

-- Insert sample data into essential_oils table
INSERT INTO essential_oils (oil_name, oil_type, description)
VALUES 
('Lavender Oil', 'Calming', 'Used for relaxation and stress relief'),
('Tea Tree Oil', 'Antimicrobial', 'Used for skin care and acne treatment'),
('Eucalyptus Oil', 'Decongestant', 'Used for relieving respiratory issues');

-- Insert sample data into products table
INSERT INTO products (product_name, fragrance_id, flavor_id, oil_id, description, price)
VALUES 
('Lavender Dream', 1, 1, 1, 'A calming and soothing product', 19.99),
('Jasmine Delight', 2, 2, 2, 'A sweet and floral product', 14.99),
('Rose Petal', 3, 3, 3, 'A classic and romantic product', 24.99);

-- Insert sample data into product_inventory table
INSERT INTO product_inventory (product_id, quantity)
VALUES 
(1, 100),
(2, 50),
(3, 200);

-- Insert sample data into orders table
INSERT INTO orders (order_date, total, status)
VALUES 
('2022-01-01 12:00:00', 19.99, 'pending'),
('2022-01-15 14:00:00', 29.98, 'shipped');

-- Insert sample data into order_items table
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES 
(1, 1, 1, 19.99),
(2, 2, 2, 14.99);
```
