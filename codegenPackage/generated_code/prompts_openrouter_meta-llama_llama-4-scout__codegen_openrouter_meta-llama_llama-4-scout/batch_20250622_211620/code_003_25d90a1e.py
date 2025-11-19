"""
Generated Code Metadata:
========================
Original URL: https://redclayware.com
Prompt: Design a basic database schema for an online store, such as Red Clay Ware, that needs to manage products, inventory, and customer subscriptions.
Generated: DETERMINISTIC_25d90a1e648bbfd4
Batch ID: 20250622_211620
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
CREATE DATABASE red_clay_ware;

-- Use database
USE red_clay_ware;

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for inventory
CREATE TABLE inventory (
  inventory_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (inventory_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for subscriptions
CREATE TABLE subscriptions (
  subscription_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  product_id INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (subscription_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create table for order items
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

-- Create indexes for foreign keys
CREATE INDEX idx_inventory_product_id ON inventory (product_id);
CREATE INDEX idx_subscriptions_customer_id ON subscriptions (customer_id);
CREATE INDEX idx_subscriptions_product_id ON subscriptions (product_id);
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
CREATE INDEX idx_order_items_order_id ON order_items (order_id);
CREATE INDEX idx_order_items_product_id ON order_items (product_id);
```

```sql
-- sample_data.sql

-- Insert sample data into products table
INSERT INTO products (name, description, price)
VALUES
  ('Product A', 'This is product A', 19.99),
  ('Product B', 'This is product B', 9.99),
  ('Product C', 'This is product C', 29.99);

-- Insert sample data into inventory table
INSERT INTO inventory (product_id, quantity)
VALUES
  (1, 100),
  (2, 50),
  (3, 200);

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, password_hash)
VALUES
  ('John', 'Doe', 'john.doe@example.com', 'password_hash_1'),
  ('Jane', 'Doe', 'jane.doe@example.com', 'password_hash_2'),
  ('Bob', 'Smith', 'bob.smith@example.com', 'password_hash_3');

-- Insert sample data into subscriptions table
INSERT INTO subscriptions (customer_id, product_id, start_date, end_date)
VALUES
  (1, 1, '2022-01-01', '2023-01-01'),
  (2, 2, '2022-02-01', NULL),
  (3, 3, '2022-03-01', '2023-03-01');

-- Insert sample data into orders table
INSERT INTO orders (customer_id, total, status)
VALUES
  (1, 19.99, 'shipped'),
  (2, 9.99, 'pending'),
  (3, 29.99, 'delivered');

-- Insert sample data into order_items table
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES
  (1, 1, 1, 19.99),
  (2, 2, 1, 9.99),
  (3, 3, 1, 29.99);
```
