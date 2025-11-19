"""
Generated Code Metadata:
========================
Original URL: https://www.suezlng.com
Prompt: "Design a database schema for an oil trading company to store information about customers, oil products, and transactions."
Generated: DETERMINISTIC_6dd13ad33d6fe8f4
Batch ID: 20250622_211852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for oil trading company
CREATE DATABASE oil_trading;

-- Use oil trading database
USE oil_trading;

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for oil products
CREATE TABLE oil_products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  unit_price DECIMAL(10, 2) NOT NULL,
  unit_of_measurement VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for transactions
CREATE TABLE transactions (
  transaction_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  product_id INT NOT NULL,
  transaction_date DATE NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit_price DECIMAL(10, 2) NOT NULL,
  total_amount DECIMAL(10, 2) NOT NULL,
  transaction_type ENUM('sale', 'purchase') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (product_id) REFERENCES oil_products(product_id)
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  transaction_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id)
);

-- Create indexes for faster queries
CREATE INDEX idx_customer_id ON transactions (customer_id);
CREATE INDEX idx_product_id ON transactions (product_id);
CREATE INDEX idx_transaction_id ON payments (transaction_id);
```

```sql
-- data.sql

-- Insert sample data into customers table
INSERT INTO customers (company_name, contact_name, contact_email, phone_number, address)
VALUES
  ('ABC Oil Company', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('XYZ Energy Inc.', 'Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into oil_products table
INSERT INTO oil_products (product_name, product_description, unit_price, unit_of_measurement)
VALUES
  ('Crude Oil', 'Heavy crude oil from the Middle East', 50.00, 'barrel'),
  ('Gasoline', 'Regular gasoline for vehicles', 2.50, 'gallon');

-- Insert sample data into transactions table
INSERT INTO transactions (customer_id, product_id, transaction_date, quantity, unit_price, total_amount, transaction_type)
VALUES
  (1, 1, '2022-01-01', 100, 50.00, 5000.00, 'sale'),
  (2, 2, '2022-01-15', 500, 2.50, 1250.00, 'purchase');

-- Insert sample data into payments table
INSERT INTO payments (transaction_id, payment_date, payment_amount, payment_method)
VALUES
  (1, '2022-01-05', 2500.00, 'bank transfer'),
  (2, '2022-01-20', 625.00, 'cash');
```
