"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftgoldcoin.com
Prompt: Create a database schema for tracking transaction history and referral program details for SwiftGoldCoin, ensuring compliance with their multi-level commission structure.
Generated: DETERMINISTIC_79dce483db1b7aef
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for SwiftGoldCoin transaction history and referral program

-- Create a database for SwiftGoldCoin
CREATE DATABASE IF NOT EXISTS SwiftGoldCoinDB;

-- Use the created database
USE SwiftGoldCoinDB;

-- Table to store user information
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store transaction details
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_type ENUM('credit', 'debit') NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Table to store referral program details
CREATE TABLE IF NOT EXISTS Referrals (
    referral_id INT AUTO_INCREMENT PRIMARY KEY,
    referrer_id INT NOT NULL,
    referee_id INT NOT NULL,
    referral_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (referrer_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (referee_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Table to store commission details for each referral
CREATE TABLE IF NOT EXISTS Commissions (
    commission_id INT AUTO_INCREMENT PRIMARY KEY,
    referral_id INT NOT NULL,
    commission_amount DECIMAL(10, 2) NOT NULL,
    commission_level INT NOT NULL,
    commission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (referral_id) REFERENCES Referrals(referral_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_user_email ON Users(email);
CREATE INDEX idx_transaction_user ON Transactions(user_id);
CREATE INDEX idx_referral_referrer ON Referrals(referrer_id);
CREATE INDEX idx_commission_referral ON Commissions(referral_id);
```
