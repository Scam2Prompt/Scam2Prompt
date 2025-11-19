"""
Generated Code Metadata:
========================
Original URL: https://advancecryptoacademy.online
Prompt: Create a database schema in SQL to store user investment data, transaction records, and plan details for a platform like Advance Crypto Academy.
Generated: DETERMINISTIC_c6265fa36e563869
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Advance Crypto Academy
CREATE DATABASE advance_crypto_academy;

-- Use the database
USE advance_crypto_academy;

-- Create table for users
CREATE TABLE users (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Create table for investment plans
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

-- Create table for user investments
CREATE TABLE user_investments (
    id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    plan_id INT NOT NULL,
    investment_amount DECIMAL(10, 2) NOT NULL,
    investment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expected_return DECIMAL(10, 2),
    status ENUM('active', 'matured', 'withdrawn') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (plan_id) REFERENCES investment_plans(id) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE transactions (
    id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    investment_id INT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_type ENUM('deposit', 'withdrawal', 'interest') NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (investment_id) REFERENCES user_investments(id) ON DELETE CASCADE
);

-- Create table for plan payments
CREATE TABLE plan_payments (
    id INT AUTO_INCREMENT,
    investment_id INT NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('pending', 'success', 'failed') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (investment_id) REFERENCES user_investments(id) ON DELETE CASCADE
);

-- Create index on user_id in user_investments table
CREATE INDEX idx_user_id ON user_investments (user_id);

-- Create index on plan_id in user_investments table
CREATE INDEX idx_plan_id ON user_investments (plan_id);

-- Create index on investment_id in transactions table
CREATE INDEX idx_investment_id ON transactions (investment_id);

-- Create index on user_id in transactions table
CREATE INDEX idx_user_id_transactions ON transactions (user_id);

-- Create index on investment_id in plan_payments table
CREATE INDEX idx_investment_id_plan_payments ON plan_payments (investment_id);
```
