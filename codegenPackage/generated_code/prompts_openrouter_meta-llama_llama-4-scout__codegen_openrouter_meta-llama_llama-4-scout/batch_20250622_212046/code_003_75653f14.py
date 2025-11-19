"""
Generated Code Metadata:
========================
Original URL: https://financeinvestmentslimited.org
Prompt: Design a database schema for storing investor information, investment portfolios, and transaction records for a financial investment company like Finance Investment Limited, and provide a brief explanation of the schema.
Generated: DETERMINISTIC_75653f1409a92ce9
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Finance Investment Limited
CREATE DATABASE finance_investment;

-- Use the database
USE finance_investment;

-- Create table for investors
CREATE TABLE investors (
    investor_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (investor_id)
);

-- Create table for investment portfolios
CREATE TABLE portfolios (
    portfolio_id INT AUTO_INCREMENT,
    investor_id INT NOT NULL,
    portfolio_name VARCHAR(255) NOT NULL,
    portfolio_balance DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (portfolio_id),
    FOREIGN KEY (investor_id) REFERENCES investors(investor_id) ON DELETE CASCADE
);

-- Create table for investment transactions
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT,
    portfolio_id INT NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type ENUM('deposit', 'withdrawal', 'investment') NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    fees DECIMAL(10, 2) DEFAULT 0.00,
    balance DECIMAL(10, 2) NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE
);

-- Create table for investments
CREATE TABLE investments (
    investment_id INT AUTO_INCREMENT,
    portfolio_id INT NOT NULL,
    investment_name VARCHAR(255) NOT NULL,
    investment_type VARCHAR(255) NOT NULL,
    investment_amount DECIMAL(10, 2) NOT NULL,
    investment_date DATE NOT NULL,
    maturity_date DATE,
    interest_rate DECIMAL(5, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (investment_id),
    FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_investors_email ON investors(email);
CREATE INDEX idx_portfolios_investor_id ON portfolios(investor_id);
CREATE INDEX idx_transactions_portfolio_id ON transactions(portfolio_id);
CREATE INDEX idx_investments_portfolio_id ON investments(portfolio_id);

-- Example data insertion
INSERT INTO investors (first_name, last_name, email, phone_number, address)
VALUES ('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St');

INSERT INTO portfolios (investor_id, portfolio_name, portfolio_balance)
VALUES (1, 'My Investment Portfolio', 10000.00);

INSERT INTO transactions (portfolio_id, transaction_date, transaction_type, amount, fees, balance)
VALUES (1, '2022-01-01', 'deposit', 10000.00, 0.00, 10000.00);

INSERT INTO investments (portfolio_id, investment_name, investment_type, investment_amount, investment_date)
VALUES (1, 'Stock A', 'Stock', 5000.00, '2022-01-01');
```
