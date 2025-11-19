"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Create a database schema to manage customer orders, equipment rentals, and repair services for a company like SARL VERDIER, which specializes in agricultural and irrigation equipment.
Generated: DETERMINISTIC_b9994a7a72503b8d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for SARL VERDIER
CREATE DATABASE sarl_verdier;

-- Use the database
USE sarl_verdier;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  country VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for equipment
CREATE TABLE equipment (
  equipment_id INT AUTO_INCREMENT,
  equipment_type VARCHAR(100) NOT NULL,
  equipment_model VARCHAR(100) NOT NULL,
  equipment_description TEXT,
  rental_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (equipment_id)
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  equipment_id INT NOT NULL,
  quantity INT NOT NULL,
  rental_duration INT NOT NULL,
  unit_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE
);

-- Create table for repair services
CREATE TABLE repair_services (
  repair_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  equipment_id INT NOT NULL,
  repair_date DATE NOT NULL,
  description TEXT NOT NULL,
  cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (repair_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT,
  repair_id INT,
  payment_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'credit_card', 'bank_transfer') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (repair_id) REFERENCES repair_services(repair_id) ON DELETE CASCADE,
  CHECK ((order_id IS NOT NULL AND repair_id IS NULL) OR (order_id IS NULL AND repair_id IS NOT NULL))
);

-- Create indexes for foreign keys
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_equipment_id ON order_items(equipment_id);
CREATE INDEX idx_repair_services_customer_id ON repair_services(customer_id);
CREATE INDEX idx_repair_services_equipment_id ON repair_services(equipment_id);
CREATE INDEX idx_payments_order_id ON payments(order_id);
CREATE INDEX idx_payments_repair_id ON payments(repair_id);
```
