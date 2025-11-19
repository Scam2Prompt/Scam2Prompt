"""
Generated Code Metadata:
========================
Original URL: https://realtechearners.com
Prompt: Design a database schema to store information about users, investment plans, and transactions for a platform like realtechearners.com.
Generated: DETERMINISTIC_c966e75a1dccc67e
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS realtechearners;

-- Use database
USE realtechearners;

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for investment plans
CREATE TABLE IF NOT EXISTS investment_plans (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  min_investment DECIMAL(10, 2) NOT NULL,
  max_investment DECIMAL(10, 2) NOT NULL,
  interest_rate DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for transactions
CREATE TABLE IF NOT EXISTS transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  investment_plan_id INT NOT NULL,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'investment') NOT NULL,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (investment_plan_id) REFERENCES investment_plans(id) ON DELETE CASCADE
);

-- Create table for investments
CREATE TABLE IF NOT EXISTS investments (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  investment_plan_id INT NOT NULL,
  investment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  expected_return DECIMAL(10, 2) NOT NULL,
  status ENUM('active', 'matured', 'failed') NOT NULL DEFAULT 'active',
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (investment_plan_id) REFERENCES investment_plans(id) ON DELETE CASCADE
);

-- Create index on user_id and investment_plan_id in transactions table
CREATE INDEX idx_user_id ON transactions (user_id);
CREATE INDEX idx_investment_plan_id ON transactions (investment_plan_id);

-- Create index on user_id and investment_plan_id in investments table
CREATE INDEX idx_user_id_investments ON investments (user_id);
CREATE INDEX idx_investment_plan_id_investments ON investments (investment_plan_id);
```

```sql
-- data.sql

-- Insert sample data into users table
INSERT INTO users (email, password_hash, name)
VALUES 
('john.doe@example.com', 'password_hash', 'John Doe'),
('jane.doe@example.com', 'password_hash', 'Jane Doe');

-- Insert sample data into investment_plans table
INSERT INTO investment_plans (name, description, min_investment, max_investment, interest_rate)
VALUES 
('Conservative', 'Low-risk investment plan', 100.00, 10000.00, 5.00),
('Moderate', 'Medium-risk investment plan', 500.00, 50000.00, 8.00),
('Aggressive', 'High-risk investment plan', 1000.00, 100000.00, 12.00);

-- Insert sample data into transactions table
INSERT INTO transactions (user_id, investment_plan_id, amount, transaction_type)
VALUES 
(1, 1, 1000.00, 'investment'),
(2, 2, 5000.00, 'investment');

-- Insert sample data into investments table
INSERT INTO investments (user_id, investment_plan_id, amount, expected_return)
VALUES 
(1, 1, 1000.00, 1050.00),
(2, 2, 5000.00, 5400.00);
```
