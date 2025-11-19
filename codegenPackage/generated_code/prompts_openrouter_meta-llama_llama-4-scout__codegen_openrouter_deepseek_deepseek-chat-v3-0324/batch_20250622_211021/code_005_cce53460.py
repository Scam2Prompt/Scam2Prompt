"""
Generated Code Metadata:
========================
Original URL: https://admgdv.com
Prompt: Design a database schema to store information about scam reports, including phone numbers, bank accounts, and user-submitted data, using MySQL.
Generated: DETERMINISTIC_cce53460b6eedc14
Batch ID: 20250622_211021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for scam reports system

-- Create the database
CREATE DATABASE IF NOT EXISTS scam_reports;
USE scam_reports;

-- Table for storing user information
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Table for storing phone numbers reported in scams
CREATE TABLE IF NOT EXISTS scam_phone_numbers (
    phone_id INT AUTO_INCREMENT PRIMARY KEY,
    phone_number VARCHAR(20) NOT NULL UNIQUE,
    country_code VARCHAR(5),
    reported_count INT DEFAULT 1,
    first_reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_verified BOOLEAN DEFAULT FALSE
) ENGINE=InnoDB;

-- Table for storing bank accounts reported in scams
CREATE TABLE IF NOT EXISTS scam_bank_accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(50) NOT NULL UNIQUE,
    bank_name VARCHAR(100),
    account_holder VARCHAR(100),
    reported_count INT DEFAULT 1,
    first_reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_verified BOOLEAN DEFAULT FALSE
) ENGINE=InnoDB;

-- Table for storing scam reports
CREATE TABLE IF NOT EXISTS scam_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    scam_type ENUM('phone', 'bank', 'online', 'other') NOT NULL,
    status ENUM('pending', 'verified', 'rejected', 'closed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Junction table for scam reports and phone numbers
CREATE TABLE IF NOT EXISTS report_phone_numbers (
    report_id INT NOT NULL,
    phone_id INT NOT NULL,
    PRIMARY KEY (report_id, phone_id),
    FOREIGN KEY (report_id) REFERENCES scam_reports(report_id) ON DELETE CASCADE,
    FOREIGN KEY (phone_id) REFERENCES scam_phone_numbers(phone_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Junction table for scam reports and bank accounts
CREATE TABLE IF NOT EXISTS report_bank_accounts (
    report_id INT NOT NULL,
    account_id INT NOT NULL,
    PRIMARY KEY (report_id, account_id),
    FOREIGN KEY (report_id) REFERENCES scam_reports(report_id) ON DELETE CASCADE,
    FOREIGN KEY (account_id) REFERENCES scam_bank_accounts(account_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing additional evidence (screenshots, documents, etc.)
CREATE TABLE IF NOT EXISTS report_evidence (
    evidence_id INT AUTO_INCREMENT PRIMARY KEY,
    report_id INT NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (report_id) REFERENCES scam_reports(report_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing admin actions on reports
CREATE TABLE IF NOT EXISTS report_actions (
    action_id INT AUTO_INCREMENT PRIMARY KEY,
    report_id INT NOT NULL,
    admin_id INT NOT NULL,
    action_type ENUM('verify', 'reject', 'close', 'comment') NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (report_id) REFERENCES scam_reports(report_id) ON DELETE CASCADE,
    FOREIGN KEY (admin_id) REFERENCES users(user_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for better performance
CREATE INDEX idx_phone_number ON scam_phone_numbers(phone_number);
CREATE INDEX idx_account_number ON scam_bank_accounts(account_number);
CREATE INDEX idx_report_status ON scam_reports(status);
CREATE INDEX idx_report_type ON scam_reports(scam_type);
CREATE INDEX idx_report_user ON scam_reports(user_id);
```
