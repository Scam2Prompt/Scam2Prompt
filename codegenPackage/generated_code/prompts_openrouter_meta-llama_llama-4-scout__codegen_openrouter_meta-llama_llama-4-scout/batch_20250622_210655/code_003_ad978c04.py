"""
Generated Code Metadata:
========================
Original URL: https://thoinayadv.com
Prompt: "Design a database schema for managing orders and services for a company like Quảng cáo Thời Nay that offers custom signage and printing."
Generated: DETERMINISTIC_ad978c041f895966
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for managing orders and services

CREATE DATABASE signage_printing;

USE signage_printing;

-- Define tables

CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  service_id INT NOT NULL,
  quantity INT NOT NULL,
  unit_cost DECIMAL(10, 2) NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_method ENUM('cash', 'credit_card', 'bank_transfer') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying

CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_service_id ON order_items(service_id);
CREATE INDEX idx_payments_order_id ON payments(order_id);

-- Insert sample data

INSERT INTO customers (company_name, contact_name, email, phone_number, address)
VALUES
  ('Quảng cáo Thời Nay', 'John Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
  ('ABC Corporation', 'Jane Smith', 'jane.smith@example.com', '9876543210', '456 Elm St');

INSERT INTO services (service_name, description, price)
VALUES
  ('Custom Signage', 'Design and production of custom signs', 100.00),
  ('Printing Services', 'Digital printing services for various materials', 50.00);

INSERT INTO orders (customer_id, order_date, total_cost)
VALUES
  (1, '2022-01-01', 500.00),
  (2, '2022-01-15', 200.00);

INSERT INTO order_items (order_id, service_id, quantity, unit_cost, total_cost)
VALUES
  (1, 1, 2, 150.00, 300.00),
  (1, 2, 1, 50.00, 50.00),
  (2, 1, 1, 100.00, 100.00);

INSERT INTO payments (order_id, payment_date, payment_method, amount)
VALUES
  (1, '2022-01-01', 'bank_transfer', 500.00),
  (2, '2022-01-15', 'cash', 200.00);
```
