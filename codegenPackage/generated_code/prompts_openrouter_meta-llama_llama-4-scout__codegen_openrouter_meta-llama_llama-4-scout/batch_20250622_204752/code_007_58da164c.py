"""
Generated Code Metadata:
========================
Original URL: https://hub-steth.org
Prompt: Design a simple database schema for storing personal finance data, including savings, checking, and investment accounts.
Generated: DETERMINISTIC_58da164caf0d0f5d
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for personal finance
CREATE DATABASE personal_finance;

-- Use the personal finance database
USE personal_finance;

-- Create a table for accounts
CREATE TABLE accounts (
  id INT AUTO_INCREMENT,
  account_type ENUM('savings', 'checking', 'investment') NOT NULL,
  account_name VARCHAR(255) NOT NULL,
  balance DECIMAL(10, 2) DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  account_id INT NOT NULL,
  transaction_date DATE NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'transfer') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  description VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

-- Create a table for investment accounts
CREATE TABLE investment_accounts (
  id INT AUTO_INCREMENT,
  account_id INT NOT NULL,
  investment_type VARCHAR(255) NOT NULL,
  investment_name VARCHAR(255) NOT NULL,
  shares DECIMAL(10, 2) NOT NULL,
  price_per_share DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

-- Create a table for savings goals
CREATE TABLE savings_goals (
  id INT AUTO_INCREMENT,
  account_id INT NOT NULL,
  goal_name VARCHAR(255) NOT NULL,
  target_amount DECIMAL(10, 2) NOT NULL,
  current_amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

-- Example data
INSERT INTO accounts (account_type, account_name, balance)
VALUES 
  ('savings', 'Emergency Fund', 1000.00),
  ('checking', 'Primary Checking', 5000.00),
  ('investment', 'Retirement Account', 20000.00);

INSERT INTO transactions (account_id, transaction_date, transaction_type, amount, description)
VALUES 
  (1, '2022-01-01', 'deposit', 500.00, 'Payroll deposit'),
  (2, '2022-01-05', 'withdrawal', 200.00, 'Groceries'),
  (3, '2022-01-10', 'transfer', 1000.00, 'Transfer from checking');

INSERT INTO investment_accounts (account_id, investment_type, investment_name, shares, price_per_share)
VALUES 
  (3, 'stock', 'Apple', 10.00, 150.00),
  (3, 'bond', 'US Treasury', 1000.00, 1000.00);

INSERT INTO savings_goals (account_id, goal_name, target_amount)
VALUES 
  (1, 'Vacation Fund', 5000.00),
  (2, 'Down Payment Fund', 20000.00);
```
