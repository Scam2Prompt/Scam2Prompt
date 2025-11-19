"""
Generated Code Metadata:
========================
Original URL: https://longtradegroup.com
Prompt: "Design a database schema to store user investments, daily profits, and referral bonuses for a cryptocurrency staking platform like LongTradeGroup."
Generated: DETERMINISTIC_cd2652e051d9fd1f
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for LongTradeGroup cryptocurrency staking platform

-- Create database
CREATE DATABASE IF NOT EXISTS long_trade_group;

-- Use database
USE long_trade_group;

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  `id` BIGINT AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `referral_code` VARCHAR(255) UNIQUE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`email`)
);

-- Create table for investments
CREATE TABLE IF NOT EXISTS investments (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `investment_plan` ENUM('low', 'medium', 'high') NOT NULL,
  `principal_amount` DECIMAL(18, 8) NOT NULL,
  `staking_duration` INT NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  `status` ENUM('active', 'matured', 'withdrawn') NOT NULL DEFAULT 'active',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE CASCADE
);

-- Create table for daily profits
CREATE TABLE IF NOT EXISTS daily_profits (
  `id` BIGINT AUTO_INCREMENT,
  `investment_id` BIGINT NOT NULL,
  `profit_date` DATE NOT NULL,
  `profit_amount` DECIMAL(18, 8) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`investment_id`) REFERENCES investments (`id`) ON DELETE CASCADE
);

-- Create table for referral bonuses
CREATE TABLE IF NOT EXISTS referral_bonuses (
  `id` BIGINT AUTO_INCREMENT,
  `referrer_id` BIGINT NOT NULL,
  `referred_user_id` BIGINT NOT NULL,
  `bonus_amount` DECIMAL(18, 8) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`referrer_id`) REFERENCES users (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`referred_user_id`) REFERENCES users (`id`) ON DELETE CASCADE
);

-- Create table for withdrawals
CREATE TABLE IF NOT EXISTS withdrawals (
  `id` BIGINT AUTO_INCREMENT,
  `investment_id` BIGINT NOT NULL,
  `withdrawal_date` DATE NOT NULL,
  `withdrawal_amount` DECIMAL(18, 8) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`investment_id`) REFERENCES investments (`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_investments_user_id ON investments (user_id);
CREATE INDEX idx_daily_profits_investment_id ON daily_profits (investment_id);
CREATE INDEX idx_referral_bonuses_referrer_id ON referral_bonuses (referrer_id);
CREATE INDEX idx_referral_bonuses_referred_user_id ON referral_bonuses (referred_user_id);
CREATE INDEX idx_withdrawals_investment_id ON withdrawals (investment_id);
```
