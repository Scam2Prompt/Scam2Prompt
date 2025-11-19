"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Design a simple database schema for an ERP system tailored to micro and small enterprises, inspired by Sistemabox's system."
Generated: DETERMINISTIC_cb306e431d1d1f53
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for ERP system
CREATE DATABASE erp_system;

-- Use the erp_system database
USE erp_system;

-- Create table for companies
CREATE TABLE companies (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  company_id INT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'employee', 'manager') DEFAULT 'employee',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
);

-- Create table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  company_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  company_id INT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
);

-- Create table for orders
CREATE TABLE orders (
  id INT AUTO_INCREMENT,
  company_id INT,
  customer_id INT,
  order_date DATE NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE,
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE order_items (
  id INT AUTO_INCREMENT,
  order_id INT,
  product_id INT,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  company_id INT,
  order_id INT,
  payment_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'credit_card', 'bank_transfer') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE,
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
);
```

```sql
-- data.sql

-- Insert sample data into companies table
INSERT INTO companies (name, email, phone, address)
VALUES
  ('ABC Inc.', 'abc@example.com', '123-456-7890', '123 Main St'),
  ('XYZ Corp.', 'xyz@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into users table
INSERT INTO users (company_id, username, email, password, role)
VALUES
  (1, 'admin', 'admin@example.com', 'password123', 'admin'),
  (1, 'john', 'john@example.com', 'password123', 'employee'),
  (2, 'jane', 'jane@example.com', 'password123', 'manager');

-- Insert sample data into products table
INSERT INTO products (company_id, name, description, price, stock_quantity)
VALUES
  (1, 'Product A', 'This is product A', 10.99, 100),
  (1, 'Product B', 'This is product B', 9.99, 50),
  (2, 'Product C', 'This is product C', 12.99, 200);

-- Insert sample data into customers table
INSERT INTO customers (company_id, name, email, phone, address)
VALUES
  (1, 'Customer 1', 'customer1@example.com', '123-456-7890', '123 Main St'),
  (1, 'Customer 2', 'customer2@example.com', '987-654-3210', '456 Elm St'),
  (2, 'Customer 3', 'customer3@example.com', '555-555-5555', '789 Oak St');

-- Insert sample data into orders table
INSERT INTO orders (company_id, customer_id, order_date, total, status)
VALUES
  (1, 1, '2022-01-01', 10.99, 'pending'),
  (1, 2, '2022-01-15', 19.98, 'shipped'),
  (2, 3, '2022-02-01', 12.99, 'delivered');

-- Insert sample data into order_items table
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES
  (1, 1, 1, 10.99),
  (2, 1, 1, 9.99),
  (2, 2, 1, 9.99),
  (3, 3, 1, 12.99);

-- Insert sample data into payments table
INSERT INTO payments (company_id, order_id, payment_date, amount, payment_method)
VALUES
  (1, 1, '2022-01-01', 10.99, 'cash'),
  (1, 2, '2022-01-15', 19.98, 'credit_card'),
  (2, 3, '2022-02-01', 12.99, 'bank_transfer');
```
