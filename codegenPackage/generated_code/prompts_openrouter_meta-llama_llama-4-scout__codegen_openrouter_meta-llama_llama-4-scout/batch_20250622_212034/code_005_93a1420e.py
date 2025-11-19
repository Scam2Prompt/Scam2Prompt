"""
Generated Code Metadata:
========================
Original URL: https://welforcevestcapital.com
Prompt: Design a basic schema for a database to store user information, investment plans, and transactions on the Welforcevest Capital platform, ensuring data security and scalability.
Generated: DETERMINISTIC_93a1420e2662b397
Batch ID: 20250622_212034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Welforcevest Capital
CREATE DATABASE welforcevest_capital;

-- Use the database
USE welforcevest_capital;

-- Create a table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for investment plans
CREATE TABLE investment_plans (
  id INT AUTO_INCREMENT,
  plan_name VARCHAR(255) NOT NULL,
  plan_description TEXT,
  min_investment DECIMAL(10, 2) NOT NULL,
  max_investment DECIMAL(10, 2) NOT NULL,
  interest_rate DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for user accounts
CREATE TABLE user_accounts (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  account_balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  investment_plan_id INT,
  transaction_type ENUM('deposit', 'withdrawal', 'investment') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (investment_plan_id) REFERENCES investment_plans(id) ON DELETE SET NULL
);

-- Create a table for investment records
CREATE TABLE investment_records (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  investment_plan_id INT NOT NULL,
  investment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  expected_return DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (investment_plan_id) REFERENCES investment_plans(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_investment_plans_plan_name ON investment_plans(plan_name);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_investment_records_user_id ON investment_records(user_id);
CREATE INDEX idx_investment_records_investment_plan_id ON investment_records(investment_plan_id);

-- Stored procedure to add a new user
DELIMITER //
CREATE PROCEDURE add_user(
  IN p_email VARCHAR(255),
  IN p_password_hash VARCHAR(255),
  IN p_first_name VARCHAR(100),
  IN p_last_name VARCHAR(100),
  IN p_phone_number VARCHAR(20),
  IN p_address VARCHAR(255)
)
BEGIN
  INSERT INTO users (email, password_hash, first_name, last_name, phone_number, address)
  VALUES (p_email, p_password_hash, p_first_name, p_last_name, p_phone_number, p_address);
END//
DELIMITER ;

-- Stored procedure to create a new investment plan
DELIMITER //
CREATE PROCEDURE add_investment_plan(
  IN p_plan_name VARCHAR(255),
  IN p_plan_description TEXT,
  IN p_min_investment DECIMAL(10, 2),
  IN p_max_investment DECIMAL(10, 2),
  IN p_interest_rate DECIMAL(5, 2)
)
BEGIN
  INSERT INTO investment_plans (plan_name, plan_description, min_investment, max_investment, interest_rate)
  VALUES (p_plan_name, p_plan_description, p_min_investment, p_max_investment, p_interest_rate);
END//
DELIMITER ;

-- Stored procedure to record a transaction
DELIMITER //
CREATE PROCEDURE record_transaction(
  IN p_user_id INT,
  IN p_investment_plan_id INT,
  IN p_transaction_type ENUM('deposit', 'withdrawal', 'investment'),
  IN p_amount DECIMAL(10, 2)
)
BEGIN
  INSERT INTO transactions (user_id, investment_plan_id, transaction_type, amount)
  VALUES (p_user_id, p_investment_plan_id, p_transaction_type, p_amount);
END//
DELIMITER ;
```
