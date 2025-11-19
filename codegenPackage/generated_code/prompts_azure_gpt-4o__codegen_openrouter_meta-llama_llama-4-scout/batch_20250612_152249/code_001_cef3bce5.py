"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Create a database schema for managing inventory and production data for a textile company specializing in 100% acrylic yarns, including tables for yarn types, machinery details, and customer orders.
Generated: DETERMINISTIC_cef3bce514e7db0c
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for textile company
CREATE DATABASE textile_company;

-- Use the database
USE textile_company;

-- Create table for yarn types
CREATE TABLE yarn_types (
  yarn_type_id INT AUTO_INCREMENT,
  yarn_color VARCHAR(50) NOT NULL,
  yarn_weight DECIMAL(4, 2) NOT NULL,
  yarn_length DECIMAL(6, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (yarn_type_id)
);

-- Create table for machinery details
CREATE TABLE machinery_details (
  machine_id INT AUTO_INCREMENT,
  machine_type VARCHAR(100) NOT NULL,
  machine_model VARCHAR(100) NOT NULL,
  production_capacity DECIMAL(6, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (machine_id)
);

-- Create table for customer orders
CREATE TABLE customer_orders (
  order_id INT AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  order_date DATE NOT NULL,
  yarn_type_id INT,
  quantity DECIMAL(6, 2) NOT NULL,
  machine_id INT,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (yarn_type_id) REFERENCES yarn_types(yarn_type_id),
  FOREIGN KEY (machine_id) REFERENCES machinery_details(machine_id)
);

-- Create table for production data
CREATE TABLE production_data (
  production_id INT AUTO_INCREMENT,
  machine_id INT NOT NULL,
  yarn_type_id INT NOT NULL,
  production_date DATE NOT NULL,
  quantity_produced DECIMAL(6, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (production_id),
  FOREIGN KEY (machine_id) REFERENCES machinery_details(machine_id),
  FOREIGN KEY (yarn_type_id) REFERENCES yarn_types(yarn_type_id)
);

-- Create table for inventory
CREATE TABLE inventory (
  inventory_id INT AUTO_INCREMENT,
  yarn_type_id INT NOT NULL,
  quantity DECIMAL(6, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (inventory_id),
  FOREIGN KEY (yarn_type_id) REFERENCES yarn_types(yarn_type_id)
);

-- Insert some sample data
INSERT INTO yarn_types (yarn_color, yarn_weight, yarn_length)
VALUES 
('Red', 2.50, 1000.00),
('Blue', 3.00, 1200.00),
('Green', 2.00, 900.00);

INSERT INTO machinery_details (machine_type, machine_model, production_capacity)
VALUES 
('Spinning Machine', 'Model 1', 500.00),
('Winding Machine', 'Model 2', 600.00),
('Twisting Machine', 'Model 3', 400.00);

INSERT INTO customer_orders (customer_name, order_date, yarn_type_id, quantity, machine_id)
VALUES 
('John Doe', '2022-01-01', 1, 100.00, 1),
('Jane Doe', '2022-01-15', 2, 200.00, 2),
('Bob Smith', '2022-02-01', 3, 300.00, 3);

INSERT INTO production_data (machine_id, yarn_type_id, production_date, quantity_produced)
VALUES 
(1, 1, '2022-01-05', 50.00),
(2, 2, '2022-01-20', 100.00),
(3, 3, '2022-02-10', 150.00);

INSERT INTO inventory (yarn_type_id, quantity)
VALUES 
(1, 500.00),
(2, 600.00),
(3, 700.00);
```
