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

# Database Schema for Finance Investment Limited

```sql
-- Database creation
CREATE DATABASE finance_investment_limited;
USE finance_investment_limited;

-- Investors table
CREATE TABLE investors (
    investor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE NOT NULL,
    tax_id VARCHAR(30) UNIQUE NOT NULL,
    address_line1 VARCHAR(100) NOT NULL,
    address_line2 VARCHAR(100),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    account_status ENUM('active', 'inactive', 'suspended') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_email (email),
    INDEX idx_tax_id (tax_id)
) ENGINE=InnoDB;

-- Investment accounts table
CREATE TABLE investment_accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    investor_id INT NOT NULL,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    account_type ENUM('individual', 'joint', 'corporate', 'retirement') NOT NULL,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    currency VARCHAR(3) DEFAULT 'USD',
    opened_date DATE NOT NULL,
    closed_date DATE,
    status ENUM('active', 'closed', 'frozen') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (investor_id) REFERENCES investors(investor_id) ON DELETE CASCADE,
    INDEX idx_account_number (account_number),
    INDEX idx_investor_id (investor_id)
) ENGINE=InnoDB;

-- Securities table (stocks, bonds, ETFs, etc.)
CREATE TABLE securities (
    security_id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    type ENUM('stock', 'bond', 'etf', 'mutual_fund', 'option', 'future') NOT NULL,
    exchange VARCHAR(50),
    currency VARCHAR(3) DEFAULT 'USD',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_symbol (symbol),
    INDEX idx_type (type)
) ENGINE=InnoDB;

-- Portfolio holdings table
CREATE TABLE portfolio_holdings (
    holding_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    security_id INT NOT NULL,
    quantity DECIMAL(15, 6) NOT NULL,
    average_cost DECIMAL(15, 4) NOT NULL,
    current_value DECIMAL(15, 2) NOT NULL,
    unrealized_gain DECIMAL(15, 2) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES investment_accounts(account_id) ON DELETE CASCADE,
    FOREIGN KEY (security_id) REFERENCES securities(security_id) ON DELETE CASCADE,
    UNIQUE KEY unique_holding (account_id, security_id),
    INDEX idx_account_id (account_id),
    INDEX idx_security_id (security_id)
) ENGINE=InnoDB;

-- Transactions table
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    security_id INT NOT NULL,
    type ENUM('buy', 'sell', 'dividend', 'interest', 'deposit', 'withdrawal', 'transfer') NOT NULL,
    quantity DECIMAL(15, 6),
    price DECIMAL(15, 4),
    amount DECIMAL(15, 2) NOT NULL,
    fee DECIMAL(10, 2) DEFAULT 0.00,
    tax DECIMAL(10, 2) DEFAULT 0.00,
    transaction_date TIMESTAMP NOT NULL,
    settlement_date TIMESTAMP,
    status ENUM('pending', 'completed', 'failed', 'cancelled') DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES investment_accounts(account_id) ON DELETE CASCADE,
    FOREIGN KEY (security_id) REFERENCES securities(security_id) ON DELETE CASCADE,
    INDEX idx_account_id (account_id),
    INDEX idx_security_id (security_id),
    INDEX idx_transaction_date (transaction_date),
    INDEX idx_type (type)
) ENGINE=InnoDB;

-- Historical prices table
CREATE TABLE historical_prices (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    security_id INT NOT NULL,
    price_date DATE NOT NULL,
    open_price DECIMAL(15, 4),
    high_price DECIMAL(15, 4),
    low_price DECIMAL(15, 4),
    close_price DECIMAL(15, 4) NOT NULL,
    adjusted_close DECIMAL(15, 4),
    volume BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (security_id) REFERENCES securities(security_id) ON DELETE CASCADE,
    UNIQUE KEY unique_price (security_id, price_date),
    INDEX idx_security_id (security_id),
    INDEX idx_price_date (price_date)
) ENGINE=InnoDB;

-- User authentication table
CREATE TABLE user_authentication (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    investor_id INT UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    last_login TIMESTAMP,
    failed_attempts INT DEFAULT 0,
    locked_until TIMESTAMP,
    reset_token VARCHAR(100),
    reset_token_expiry TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (investor_id) REFERENCES investors(investor_id) ON DELETE CASCADE,
    INDEX idx_username (username)
) ENGINE=InnoDB;

-- Audit log table
CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    entity_id INT,
    old_value TEXT,
    new_value TEXT,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_action (action),
    INDEX idx_entity (entity_type, entity_id),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB;
```
