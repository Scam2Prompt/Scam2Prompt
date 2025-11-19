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
-- Database schema for storing scam reports

-- Create a database for scam reports
CREATE DATABASE IF NOT EXISTS scam_reports_db;

-- Use the created database
USE scam_reports_db;

-- Table to store user information
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    name VARCHAR(100) NOT NULL,               -- User's name
    email VARCHAR(100) NOT NULL UNIQUE,       -- User's email, must be unique
    phone_number VARCHAR(15) NOT NULL,        -- User's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the user was created
);

-- Table to store phone numbers associated with scam reports
CREATE TABLE IF NOT EXISTS phone_numbers (
    phone_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each phone number
    user_id INT NOT NULL,                       -- Foreign key referencing the user
    phone_number VARCHAR(15) NOT NULL,         -- Phone number reported
    report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the report
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store bank account information associated with scam reports
CREATE TABLE IF NOT EXISTS bank_accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each bank account
    user_id INT NOT NULL,                        -- Foreign key referencing the user
    bank_name VARCHAR(100) NOT NULL,            -- Name of the bank
    account_number VARCHAR(20) NOT NULL,        -- Bank account number
    report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the report
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store scam reports submitted by users
CREATE TABLE IF NOT EXISTS scam_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each scam report
    user_id INT NOT NULL,                        -- Foreign key referencing the user
    report_description TEXT NOT NULL,            -- Description of the scam
    report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the report
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_user_phone ON phone_numbers(phone_number);
CREATE INDEX idx_user_bank ON bank_accounts(account_number);
CREATE INDEX idx_report_user ON scam_reports(user_id);
```
