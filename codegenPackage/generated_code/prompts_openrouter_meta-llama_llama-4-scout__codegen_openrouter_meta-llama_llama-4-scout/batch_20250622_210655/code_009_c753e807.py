"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: "Design a database schema to manage inventory and orders for a company specializing in concrete products that mimic wood, like Fortic."
Generated: DETERMINISTIC_c753e8078b1d2927
Batch ID: 20250622_210655
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
CREATE DATABASE concrete_products;

-- Use database
USE concrete_products;

-- Create table for product categories
CREATE TABLE product_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES product_categories(id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for orders
CREATE TABLE orders (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE order_items (
  id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create table for suppliers
CREATE TABLE suppliers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for product suppliers
CREATE TABLE product_suppliers (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  supplier_id INT NOT NULL,
  lead_time INT,
  cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE CASCADE
);

-- Create triggers to update stock quantity and order total
DELIMITER $$
CREATE TRIGGER update_stock_quantity_after_order
AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
  UPDATE products
  SET stock_quantity = stock_quantity - NEW.quantity
  WHERE id = NEW.product_id;
  
  UPDATE orders
  SET total = total + NEW.unit_price * NEW.quantity
  WHERE id = NEW.order_id;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_stock_quantity_after_order_update
AFTER UPDATE ON order_items
FOR EACH ROW
BEGIN
  IF NEW.quantity <> OLD.quantity THEN
    UPDATE products
    SET stock_quantity = stock_quantity + OLD.quantity - NEW.quantity
    WHERE id = NEW.product_id;
    
    UPDATE orders
    SET total = total + (NEW.unit_price * NEW.quantity) - (OLD.unit_price * OLD.quantity)
    WHERE id = NEW.order_id;
  END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER prevent_negative_stock
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
  IF NEW.stock_quantity < 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Cannot update stock quantity to a negative value';
  END IF;
END$$
DELIMITER ;
```

```sql
-- sample_data.sql

-- Insert sample data into product categories
INSERT INTO product_categories (name, description)
VALUES
  ('Wood Planks', 'Concrete products that mimic wood planks'),
  ('Wood Panels', 'Concrete products that mimic wood panels'),
  ('Decorative Items', 'Concrete products for decorative purposes');

-- Insert sample data into products
INSERT INTO products (category_id, name, description, price, stock_quantity)
VALUES
  (1, 'Wooden Plank 1', 'Concrete product that mimics a wooden plank', 10.99, 100),
  (1, 'Wooden Plank 2', 'Concrete product that mimics another wooden plank', 12.99, 50),
  (2, 'Wooden Panel 1', 'Concrete product that mimics a wooden panel', 20.99, 200),
  (3, 'Decorative Item 1', 'Concrete product for decorative purposes', 5.99, 500);

-- Insert sample data into customers
INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into orders
INSERT INTO orders (customer_id, order_date, total, status)
VALUES
  (1, '2022-01-01 12:00:00', 21.98, 'pending'),
  (2, '2022-01-15 14:00:00', 10.99, 'shipped');

-- Insert sample data into order items
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
  (1, 1, 2, 10.99),
  (1, 3, 1, 20.99),
  (2, 4, 1, 10.99);

-- Insert sample data into suppliers
INSERT INTO suppliers (name, email, phone_number, address)
VALUES
  ('Supplier 1', 'supplier1@example.com', '123-456-7890', '123 Main St'),
  ('Supplier 2', 'supplier2@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into product suppliers
INSERT INTO product_suppliers (product_id, supplier_id, lead_time, cost)
VALUES
  (1, 1, 7, 8.99),
  (2, 2, 10, 9.99),
  (3, 1, 14, 18.99);
```
