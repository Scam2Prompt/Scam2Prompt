"""
Generated Code Metadata:
========================
Original URL: https://betbax.net
Prompt: Generate a SQL database schema to manage user accounts, transactions, and game history for a sports betting platform like BaxBet's, with features for bonus distribution and cashback rewards.
Generated: DETERMINISTIC_e293d423b8938ca6
Batch ID: 20250622_211523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS sports_betting_platform;

-- Use database
USE sports_betting_platform;

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user accounts
CREATE TABLE IF NOT EXISTS user_accounts (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  balance DECIMAL(10, 2) DEFAULT 0.00,
  bonus_balance DECIMAL(10, 2) DEFAULT 0.00,
  cashback_balance DECIMAL(10, 2) DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE IF NOT EXISTS transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'bet', 'bonus', 'cashback') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for game history
CREATE TABLE IF NOT EXISTS game_history (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  game_type ENUM('sports', 'casino') NOT NULL,
  bet_amount DECIMAL(10, 2) NOT NULL,
  winnings DECIMAL(10, 2) DEFAULT 0.00,
  status ENUM('pending', 'won', 'lost') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for bonuses
CREATE TABLE IF NOT EXISTS bonuses (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  bonus_type ENUM('welcome', 'deposit', 'referral') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'claimed', 'expired') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for cashback rewards
CREATE TABLE IF NOT EXISTS cashback_rewards (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'claimed', 'expired') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create triggers for updating user account balances
DELIMITER $$
CREATE TRIGGER update_user_account_balance_after_transaction
AFTER UPDATE ON transactions
FOR EACH ROW
BEGIN
  IF NEW.status = 'success' THEN
    UPDATE user_accounts
    SET balance = balance + NEW.amount
    WHERE user_id = NEW.user_id;
  END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_user_account_bonus_balance_after_bonus_claim
AFTER UPDATE ON bonuses
FOR EACH ROW
BEGIN
  IF NEW.status = 'claimed' THEN
    UPDATE user_accounts
    SET bonus_balance = bonus_balance - NEW.amount
    WHERE user_id = NEW.user_id;
  END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_user_account_cashback_balance_after_cashback_claim
AFTER UPDATE ON cashback_rewards
FOR EACH ROW
BEGIN
  IF NEW.status = 'claimed' THEN
    UPDATE user_accounts
    SET cashback_balance = cashback_balance - NEW.amount
    WHERE user_id = NEW.user_id;
  END IF;
END$$
DELIMITER ;
```
