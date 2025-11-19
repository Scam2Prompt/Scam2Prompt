"""
Generated Code Metadata:
========================
Original URL: https://nansenportfolio.app
Prompt: Design a database schema to store client information and investment portfolios for a financial services company like Grade World Investment Limited, and provide an example SQL code snippet.
Generated: DETERMINISTIC_271d79aec8edacce
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Grade World Investment Limited
CREATE DATABASE grade_world_investment;

-- Use the created database
USE grade_world_investment;

-- Create a table to store client information
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table to store investment portfolios
CREATE TABLE investment_portfolios (
  portfolio_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  portfolio_name VARCHAR(255) NOT NULL,
  investment_goal VARCHAR(255),
  risk_tolerance VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (portfolio_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table to store investments
CREATE TABLE investments (
  investment_id INT AUTO_INCREMENT,
  portfolio_id INT NOT NULL,
  investment_name VARCHAR(255) NOT NULL,
  investment_type VARCHAR(100) NOT NULL,
  investment_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (investment_id),
  FOREIGN KEY (portfolio_id) REFERENCES investment_portfolios(portfolio_id) ON DELETE CASCADE
);

-- Create a table to store transactions
CREATE TABLE transactions (
  transaction_id INT AUTO_INCREMENT,
  investment_id INT NOT NULL,
  transaction_date DATE NOT NULL,
  transaction_type VARCHAR(50) NOT NULL,
  transaction_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (investment_id) REFERENCES investments(investment_id) ON DELETE CASCADE
);

-- Insert sample data into clients table
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into investment_portfolios table
INSERT INTO investment_portfolios (client_id, portfolio_name, investment_goal, risk_tolerance)
VALUES 
(1, 'John Doe Portfolio', 'Long-term growth', 'High'),
(2, 'Jane Doe Portfolio', 'Short-term income', 'Low');

-- Insert sample data into investments table
INSERT INTO investments (portfolio_id, investment_name, investment_type, investment_amount)
VALUES 
(1, 'Stocks', 'Equity', 10000.00),
(1, 'Bonds', 'Fixed Income', 5000.00),
(2, 'Real Estate', 'Alternative', 20000.00);

-- Insert sample data into transactions table
INSERT INTO transactions (investment_id, transaction_date, transaction_type, transaction_amount)
VALUES 
(1, '2022-01-01', 'Buy', 10000.00),
(2, '2022-01-15', 'Buy', 5000.00),
(3, '2022-02-01', 'Buy', 20000.00);

-- Query to retrieve client information and investment portfolios
SELECT 
  c.client_id,
  c.first_name,
  c.last_name,
  ip.portfolio_id,
  ip.portfolio_name,
  ip.investment_goal,
  ip.risk_tolerance
FROM 
  clients c
  INNER JOIN investment_portfolios ip ON c.client_id = ip.client_id;

-- Query to retrieve investment details
SELECT 
  i.investment_id,
  i.investment_name,
  i.investment_type,
  i.investment_amount,
  t.transaction_id,
  t.transaction_date,
  t.transaction_type,
  t.transaction_amount
FROM 
  investments i
  LEFT JOIN transactions t ON i.investment_id = t.investment_id;
```
