"""
Generated Code Metadata:
========================
Original URL: https://acessanet.com.br
Prompt: Design a database schema to store information about internet plans, customers, and their respective subscriptions, similar to how Acessanet might organize its customer data.
Generated: DETERMINISTIC_0fb28817c334054e
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema
CREATE DATABASE accessnet;

-- Use database schema
USE accessnet;

-- Create table for internet plans
CREATE TABLE internet_plans (
  plan_id INT AUTO_INCREMENT,
  plan_name VARCHAR(255) NOT NULL,
  plan_description TEXT,
  speed DECIMAL(5, 2) NOT NULL,
  data_limit DECIMAL(10, 2) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (plan_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for subscriptions
CREATE TABLE subscriptions (
  subscription_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  plan_id INT NOT NULL,
  subscription_date DATE NOT NULL,
  expiration_date DATE,
  status ENUM('active', 'inactive', 'pending') NOT NULL DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (subscription_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  FOREIGN KEY (plan_id) REFERENCES internet_plans(plan_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  subscription_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'card', 'bank_transfer') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (subscription_id) REFERENCES subscriptions(subscription_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_customer_id ON subscriptions (customer_id);
CREATE INDEX idx_plan_id ON subscriptions (plan_id);
CREATE INDEX idx_subscription_id ON payments (subscription_id);

-- Example data insertion
INSERT INTO internet_plans (plan_name, plan_description, speed, data_limit, price)
VALUES 
('Basic', 'Basic internet plan', 10.00, 100.00, 20.00),
('Premium', 'Premium internet plan', 50.00, 1000.00, 50.00);

INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john@example.com', '1234567890', '123 Main St'),
('Jane', 'Doe', 'jane@example.com', '9876543210', '456 Elm St');

INSERT INTO subscriptions (customer_id, plan_id, subscription_date, expiration_date)
VALUES 
(1, 1, '2022-01-01', '2023-01-01'),
(2, 2, '2022-06-01', '2023-06-01');

INSERT INTO payments (subscription_id, payment_date, payment_amount, payment_method)
VALUES 
(1, '2022-01-15', 20.00, 'cash'),
(1, '2022-02-15', 20.00, 'cash'),
(2, '2022-06-15', 50.00, 'card');
```
