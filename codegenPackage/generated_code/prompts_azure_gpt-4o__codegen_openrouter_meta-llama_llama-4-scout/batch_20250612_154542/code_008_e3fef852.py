"""
Generated Code Metadata:
========================
Original URL: https://mcoinners.com
Prompt: Create a SQL database schema to manage user accounts, deposits, withdrawals, and referral bonuses for a cryptocurrency investment platform like mcoinners.com.
Generated: DETERMINISTIC_e3fef852f8380b51
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for cryptocurrency investment platform

CREATE DATABASE IF NOT EXISTS crypto_investment_platform;

USE crypto_investment_platform;

-- Create table for user accounts
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user accounts' balances
CREATE TABLE IF NOT EXISTS user_balances (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  balance DECIMAL(18, 8) NOT NULL DEFAULT 0.0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for deposits
CREATE TABLE IF NOT EXISTS deposits (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  amount DECIMAL(18, 8) NOT NULL,
  transaction_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for withdrawals
CREATE TABLE IF NOT EXISTS withdrawals (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  amount DECIMAL(18, 8) NOT NULL,
  transaction_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for referral bonuses
CREATE TABLE IF NOT EXISTS referral_bonuses (
  id INT AUTO_INCREMENT,
  referrer_id INT NOT NULL,
  referred_id INT NOT NULL,
  bonus DECIMAL(18, 8) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (referrer_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (referred_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (referrer_id, referred_id)
);

-- Create table for user referrals
CREATE TABLE IF NOT EXISTS user_referrals (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  referral_code VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id)
);

-- Create trigger to update user balance after deposit
DELIMITER $$
CREATE TRIGGER update_balance_after_deposit
AFTER INSERT ON deposits
FOR EACH ROW
BEGIN
  UPDATE user_balances
  SET balance = balance + NEW.amount
  WHERE user_id = NEW.user_id;
END$$
DELIMITER ;

-- Create trigger to update user balance after withdrawal
DELIMITER $$
CREATE TRIGGER update_balance_after_withdrawal
AFTER INSERT ON withdrawals
FOR EACH ROW
BEGIN
  UPDATE user_balances
  SET balance = balance - NEW.amount
  WHERE user_id = NEW.user_id;
END$$
DELIMITER ;

-- Create stored procedure to add new user
DELIMITER $$
CREATE PROCEDURE add_new_user(
  IN p_email VARCHAR(255),
  IN p_password_hash VARCHAR(255),
  IN p_name VARCHAR(255)
)
BEGIN
  INSERT INTO users (email, password_hash, name)
  VALUES (p_email, p_password_hash, p_name);
  
  INSERT INTO user_balances (user_id)
  VALUES (LAST_INSERT_ID());
END$$
DELIMITER ;

-- Create stored procedure to make deposit
DELIMITER $$
CREATE PROCEDURE make_deposit(
  IN p_user_id INT,
  IN p_amount DECIMAL(18, 8),
  IN p_transaction_hash VARCHAR(255)
)
BEGIN
  INSERT INTO deposits (user_id, amount, transaction_hash)
  VALUES (p_user_id, p_amount, p_transaction_hash);
END$$
DELIMITER ;

-- Create stored procedure to make withdrawal
DELIMITER $$
CREATE PROCEDURE make_withdrawal(
  IN p_user_id INT,
  IN p_amount DECIMAL(18, 8),
  IN p_transaction_hash VARCHAR(255)
)
BEGIN
  IF (SELECT balance FROM user_balances WHERE user_id = p_user_id) >= p_amount THEN
    INSERT INTO withdrawals (user_id, amount, transaction_hash)
    VALUES (p_user_id, p_amount, p_transaction_hash);
  ELSE
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient balance';
  END IF;
END$$
DELIMITER ;

-- Create stored procedure to give referral bonus
DELIMITER $$
CREATE PROCEDURE give_referral_bonus(
  IN p_referrer_id INT,
  IN p_referred_id INT,
  IN p_bonus DECIMAL(18, 8)
)
BEGIN
  IF NOT EXISTS (SELECT 1 FROM user_referrals WHERE user_id = p_referred_id) THEN
    INSERT INTO referral_bonuses (referrer_id, referred_id, bonus)
    VALUES (p_referrer_id, p_referred_id, p_bonus);
    
    UPDATE user_balances
    SET balance = balance + p_bonus
    WHERE user_id = p_referrer_id;
  ELSE
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Referred user already exists';
  END IF;
END$$
DELIMITER ;
```
