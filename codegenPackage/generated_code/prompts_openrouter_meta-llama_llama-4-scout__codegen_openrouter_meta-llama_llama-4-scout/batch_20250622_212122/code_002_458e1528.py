"""
Generated Code Metadata:
========================
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Generate a SQL database schema for a wholesale kitchen supply store like Varejão das Louças that sells to restaurants and hotels.
Generated: DETERMINISTIC_458e1528e876aed6
Batch ID: 20250622_212122
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
CREATE DATABASE wholesale_kitchen_supply;

-- Use database
USE wholesale_kitchen_supply;

-- Create tables
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  country VARCHAR(100),
  zip_code VARCHAR(10),
  PRIMARY KEY (customer_id)
);

CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  unit_price DECIMAL(10, 2) NOT NULL,
  unit_of_measurement VARCHAR(20) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  PRIMARY KEY (product_id)
);

CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_method ENUM('cash', 'credit_card', 'bank_transfer') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Create indexes
CREATE INDEX idx_customers_contact_email ON customers (contact_email);
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
CREATE INDEX idx_order_items_order_id ON order_items (order_id);
CREATE INDEX idx_order_items_product_id ON order_items (product_id);
CREATE INDEX idx_payments_order_id ON payments (order_id);

-- Create views
CREATE VIEW customer_order_summary AS
SELECT 
  c.company_name, 
  COUNT(o.order_id) AS total_orders, 
  SUM(o.total_cost) AS total_spent
FROM 
  customers c
  LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY 
  c.company_name;

CREATE VIEW product_sales_summary AS
SELECT 
  p.product_name, 
  SUM(oi.quantity) AS total_quantity_sold, 
  SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM 
  products p
  LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY 
  p.product_name;
```
