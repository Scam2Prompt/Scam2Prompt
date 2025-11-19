"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Create a database schema in MySQL to manage user accounts, deposits, and withdrawals for an online betting platform like VZ99.
Generated: DETERMINISTIC_2a2fb2a6306bce14
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for online betting platform

-- Create the database
CREATE DATABASE IF NOT EXISTS betting_platform;
USE betting_platform;

-- Users table to store account information
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    account_status ENUM('active', 'suspended', 'closed') DEFAULT 'active',
    balance DECIMAL(15, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    verification_status ENUM('verified', 'pending', 'unverified') DEFAULT 'unverified',
    kyc_status ENUM('approved', 'pending', 'rejected', 'not_submitted') DEFAULT 'not_submitted',
    INDEX idx_account_status (account_status),
    INDEX idx_verification_status (verification_status)
) ENGINE=InnoDB;

-- User verification documents for KYC
CREATE TABLE IF NOT EXISTS user_documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    document_type ENUM('id_proof', 'address_proof', 'selfie', 'other') NOT NULL,
    document_number VARCHAR(100),
    file_path VARCHAR(255) NOT NULL,
    status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reviewed_at TIMESTAMP NULL,
    reviewed_by INT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_user_documents (user_id, status)
) ENGINE=InnoDB;

-- Transactions table for deposits and withdrawals
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    transaction_type ENUM('deposit', 'withdrawal') NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    status ENUM('pending', 'completed', 'failed', 'cancelled') DEFAULT 'pending',
    payment_method ENUM('credit_card', 'bank_transfer', 'ewallet', 'crypto') NOT NULL,
    payment_reference VARCHAR(255),
    transaction_fee DECIMAL(10, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP NULL,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_transaction_user (user_id),
    INDEX idx_transaction_status (status),
    INDEX idx_transaction_type (transaction_type)
) ENGINE=InnoDB;

-- User bank accounts for withdrawals
CREATE TABLE IF NOT EXISTS user_bank_accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_holder_name VARCHAR(100) NOT NULL,
    bank_name VARCHAR(100) NOT NULL,
    account_number VARCHAR(50) NOT NULL,
    iban VARCHAR(50),
    swift_code VARCHAR(20),
    branch_code VARCHAR(20),
    is_primary BOOLEAN DEFAULT FALSE,
    verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_user_bank_accounts (user_id, is_primary)
) ENGINE=InnoDB;

-- User login history for security
CREATE TABLE IF NOT EXISTS login_history (
    login_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    user_agent TEXT,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    success BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_login_history (user_id, login_time)
) ENGINE=InnoDB;

-- Account activity log
CREATE TABLE IF NOT EXISTS activity_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    activity_type VARCHAR(50) NOT NULL,
    description TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_activity_log (user_id, created_at)
) ENGINE=InnoDB;

-- System settings table
CREATE TABLE IF NOT EXISTS system_settings (
    setting_id INT AUTO_INCREMENT PRIMARY KEY,
    setting_key VARCHAR(50) NOT NULL UNIQUE,
    setting_value TEXT NOT NULL,
    description TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Initial system settings
INSERT INTO system_settings (setting_key, setting_value, description) VALUES
('min_deposit', '10.00', 'Minimum deposit amount'),
('max_deposit', '10000.00', 'Maximum deposit amount'),
('min_withdrawal', '20.00', 'Minimum withdrawal amount'),
('max_withdrawal', '5000.00', 'Maximum withdrawal amount'),
('deposit_fee_percent', '0.00', 'Percentage fee for deposits'),
('withdrawal_fee_fixed', '5.00', 'Fixed fee for withdrawals'),
('currency', 'USD', 'Default currency'),
('maintenance_mode', '0', 'Is platform in maintenance mode (1/0)');
```
