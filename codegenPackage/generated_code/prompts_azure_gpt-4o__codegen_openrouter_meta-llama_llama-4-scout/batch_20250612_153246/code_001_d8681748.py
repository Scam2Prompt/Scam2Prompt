"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Create a database schema for managing custom box orders, including fields for "Box Type," "Material," "Size," "Customization Details," and "Client Information."
Generated: DETERMINISTIC_d8681748157c517c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for custom box orders
CREATE DATABASE custom_box_orders;

-- Use the custom_box_orders database
USE custom_box_orders;

-- Create table for box types
CREATE TABLE box_types (
  id INT AUTO_INCREMENT,
  box_type_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for materials
CREATE TABLE materials (
  id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for box sizes
CREATE TABLE box_sizes (
  id INT AUTO_INCREMENT,
  size_name VARCHAR(255) NOT NULL,
  length DECIMAL(10, 2) NOT NULL,
  width DECIMAL(10, 2) NOT NULL,
  height DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for clients
CREATE TABLE clients (
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

-- Create table for custom box orders
CREATE TABLE custom_box_orders (
  id INT AUTO_INCREMENT,
  box_type_id INT NOT NULL,
  material_id INT NOT NULL,
  box_size_id INT NOT NULL,
  client_id INT NOT NULL,
  customization_details TEXT,
  order_date DATE NOT NULL,
  delivery_date DATE,
  status ENUM('pending', 'in_progress', 'delivered', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (box_type_id) REFERENCES box_types(id) ON DELETE CASCADE,
  FOREIGN KEY (material_id) REFERENCES materials(id) ON DELETE CASCADE,
  FOREIGN KEY (box_size_id) REFERENCES box_sizes(id) ON DELETE CASCADE,
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create index on foreign key columns
CREATE INDEX idx_box_type_id ON custom_box_orders (box_type_id);
CREATE INDEX idx_material_id ON custom_box_orders (material_id);
CREATE INDEX idx_box_size_id ON custom_box_orders (box_size_id);
CREATE INDEX idx_client_id ON custom_box_orders (client_id);

-- Example insert statements
INSERT INTO box_types (box_type_name, description) VALUES ('Custom Box', 'Custom box for various purposes');
INSERT INTO materials (material_name, description) VALUES ('Cardboard', 'Durable cardboard material');
INSERT INTO box_sizes (size_name, length, width, height) VALUES ('Large', 20.00, 15.00, 10.00);
INSERT INTO clients (first_name, last_name, email, phone_number) VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890');
INSERT INTO custom_box_orders (box_type_id, material_id, box_size_id, client_id, customization_details, order_date)
VALUES (1, 1, 1, 1, 'Custom design with logo', '2024-09-16');
```
