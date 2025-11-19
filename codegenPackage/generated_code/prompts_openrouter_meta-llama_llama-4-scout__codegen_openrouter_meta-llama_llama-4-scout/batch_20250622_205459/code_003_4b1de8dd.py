"""
Generated Code Metadata:
========================
Original URL: https://baochuanco.com
Prompt: "Design a database schema for a wire mesh products company, including tables for products, customers, orders, and suppliers, using MySQL."
Generated: DETERMINISTIC_4b1de8dde69fbd1b
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database
CREATE DATABASE wire_mesh_products;

-- Use database
USE wire_mesh_products;

-- Create table for suppliers
CREATE TABLE suppliers (
  supplier_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_title VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(100),
  region VARCHAR(100),
  postal_code VARCHAR(20),
  country VARCHAR(100),
  phone VARCHAR(20),
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (supplier_id)
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  description TEXT,
  material VARCHAR(100) NOT NULL,
  mesh_size DECIMAL(10, 2) NOT NULL,
  wire_diameter DECIMAL(10, 2) NOT NULL,
  sheet_size DECIMAL(10, 2) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  supplier_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE SET NULL
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_title VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(100),
  region VARCHAR(100),
  postal_code VARCHAR(20),
  country VARCHAR(100),
  phone VARCHAR(20),
  email VARCHAR(100) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  required_date DATE,
  shipped_date DATE,
  ship_via INT,
  freight DECIMAL(10, 2),
  ship_name VARCHAR(255),
  ship_address VARCHAR(255),
  ship_city VARCHAR(100),
  ship_region VARCHAR(100),
  ship_postal_code VARCHAR(20),
  ship_country VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create table for order details
CREATE TABLE order_details (
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  quantity INT NOT NULL,
  discount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create index on supplier_id in products table
CREATE INDEX idx_supplier_id ON products (supplier_id);

-- Create index on customer_id in orders table
CREATE INDEX idx_customer_id ON orders (customer_id);

-- Create index on order_id and product_id in order_details table
CREATE INDEX idx_order_id_product_id ON order_details (order_id, product_id);
```
