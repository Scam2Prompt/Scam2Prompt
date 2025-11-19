"""
Generated Code Metadata:
========================
Original URL: https://moneygrowthway.com
Prompt: "Generate a SQL database schema to manage user accounts, investment plans, and transactions on a financial investment platform, ensuring data security and integrity."
Generated: DETERMINISTIC_0b36059510624285
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the financial investment platform
CREATE DATABASE financial_investment_platform;

-- Use the created database
USE financial_investment_platform;

-- Create a table for user accounts
CREATE TABLE users (
    id INT AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
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

-- Create a table for user investment plans
CREATE TABLE user_investment_plans (
    id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    investment_plan_id INT NOT NULL,
    invested_amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (investment_plan_id) REFERENCES investment_plans(id) ON DELETE CASCADE
);

-- Create a table for transactions
CREATE TABLE transactions (
    id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    investment_plan_id INT NOT NULL,
    transaction_type ENUM('deposit', 'withdrawal', 'interest') NOT NULL,
    transaction_amount DECIMAL(10, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (investment_plan_id) REFERENCES investment_plans(id) ON DELETE CASCADE
);

-- Create a table for user sessions
CREATE TABLE user_sessions (
    id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    session_token VARCHAR(255) NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_investment_plans_plan_name ON investment_plans (plan_name);
CREATE INDEX idx_user_investment_plans_user_id ON user_investment_plans (user_id);
CREATE INDEX idx_user_investment_plans_investment_plan_id ON user_investment_plans (investment_plan_id);
CREATE INDEX idx_transactions_user_id ON transactions (user_id);
CREATE INDEX idx_transactions_investment_plan_id ON transactions (investment_plan_id);

-- Add constraints for data integrity
ALTER TABLE users
ADD CONSTRAINT chk_password CHECK (LENGTH(password_hash) > 0);

ALTER TABLE investment_plans
ADD CONSTRAINT chk_min_investment CHECK (min_investment > 0),
ADD CONSTRAINT chk_max_investment CHECK (max_investment > 0),
ADD CONSTRAINT chk_interest_rate CHECK (interest_rate >= 0);

ALTER TABLE user_investment_plans
ADD CONSTRAINT chk_invested_amount CHECK (invested_amount > 0);

ALTER TABLE transactions
ADD CONSTRAINT chk_transaction_amount CHECK (transaction_amount > 0);
```
