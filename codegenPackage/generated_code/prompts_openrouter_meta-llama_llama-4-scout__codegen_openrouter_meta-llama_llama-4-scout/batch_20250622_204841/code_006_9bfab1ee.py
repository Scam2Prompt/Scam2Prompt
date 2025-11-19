"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: "Design a database schema to store information about construction tools and equipment for an e-commerce platform."
Generated: DETERMINISTIC_9bfab1ee5a03d2c6
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- construction_tools_schema.sql

-- Create database schema
CREATE DATABASE construction_tools;

-- Use the database schema
USE construction_tools;

-- Create table for tool categories
CREATE TABLE tool_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for tool manufacturers
CREATE TABLE tool_manufacturers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for construction tools
CREATE TABLE construction_tools (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  tool_category_id INT,
  tool_manufacturer_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (tool_category_id) REFERENCES tool_categories(id) ON DELETE SET NULL,
  FOREIGN KEY (tool_manufacturer_id) REFERENCES tool_manufacturers(id) ON DELETE SET NULL
);

-- Create table for tool specifications
CREATE TABLE tool_specifications (
  id INT AUTO_INCREMENT,
  construction_tool_id INT,
  specification_name VARCHAR(255) NOT NULL,
  specification_value VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (construction_tool_id) REFERENCES construction_tools(id) ON DELETE CASCADE
);

-- Create table for tool images
CREATE TABLE tool_images (
  id INT AUTO_INCREMENT,
  construction_tool_id INT,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (construction_tool_id) REFERENCES construction_tools(id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for orders
CREATE TABLE orders (
  id INT AUTO_INCREMENT,
  customer_id INT,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE SET NULL
);

-- Create table for order items
CREATE TABLE order_items (
  id INT AUTO_INCREMENT,
  order_id INT,
  construction_tool_id INT,
  quantity INT NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
  FOREIGN KEY (construction_tool_id) REFERENCES construction_tools(id) ON DELETE SET NULL
);

-- Create indexes for faster queries
CREATE INDEX idx_tool_categories_name ON tool_categories (name);
CREATE INDEX idx_tool_manufacturers_name ON tool_manufacturers (name);
CREATE INDEX idx_construction_tools_name ON construction_tools (name);
CREATE INDEX idx_construction_tools_tool_category_id ON construction_tools (tool_category_id);
CREATE INDEX idx_construction_tools_tool_manufacturer_id ON construction_tools (tool_manufacturer_id);
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
CREATE INDEX idx_order_items_order_id ON order_items (order_id);
CREATE INDEX idx_order_items_construction_tool_id ON order_items (construction_tool_id);
```
