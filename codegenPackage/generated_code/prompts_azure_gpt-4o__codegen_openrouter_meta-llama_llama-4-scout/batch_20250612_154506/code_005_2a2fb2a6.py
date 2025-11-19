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
-- vz99_database_schema.sql

-- Create database
CREATE DATABASE vz99;

-- Use database
USE vz99;

-- Create table for user accounts
CREATE TABLE users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
);

-- Create table for user accounts status
CREATE TABLE user_status (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `status` ENUM('active', 'inactive', 'suspended') NOT NULL DEFAULT 'active',
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for deposits
CREATE TABLE deposits (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('bank_transfer', 'e_wallet', 'credit_card') NOT NULL,
  `transaction_id` VARCHAR(100),
  `status` ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for withdrawals
CREATE TABLE withdrawals (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('bank_transfer', 'e_wallet', 'credit_card') NOT NULL,
  `transaction_id` VARCHAR(100),
  `status` ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for user balance history
CREATE TABLE balance_history (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `transaction_type` ENUM('deposit', 'withdrawal', 'bet') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `balance` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for bets
CREATE TABLE bets (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `bet_amount` DECIMAL(10, 2) NOT NULL,
  `bet_type` ENUM('sports', 'casino') NOT NULL,
  `bet_status` ENUM('pending', 'won', 'lost') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);
```
