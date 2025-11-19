"""
Generated Code Metadata:
========================
Original URL: https://pancakeswap.eu.com
Prompt: Create a database schema for managing user accounts, game history, and transaction logs as described in Sunwin's registration and payment processes.
Generated: DETERMINISTIC_9841731d32571ba2
Batch ID: 20250612_154441
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
CREATE DATABASE sunwin;

-- Use database
USE sunwin;

-- Create table for user accounts
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for game history
CREATE TABLE game_history (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_name VARCHAR(255) NOT NULL,
  game_type ENUM('slot', 'poker', 'lottery') NOT NULL,
  bet_amount DECIMAL(10, 2) NOT NULL,
  win_amount DECIMAL(10, 2),
  game_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for transaction logs
CREATE TABLE transaction_logs (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'bet', 'win') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  payment_method VARCHAR(255),
  transaction_status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for deposits
CREATE TABLE deposits (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(255) NOT NULL,
  deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for withdrawals
CREATE TABLE withdrawals (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(255) NOT NULL,
  withdrawal_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create index on user_id in game_history, transaction_logs, deposits, and withdrawals
CREATE INDEX idx_user_id ON game_history (user_id);
CREATE INDEX idx_user_id ON transaction_logs (user_id);
CREATE INDEX idx_user_id ON deposits (user_id);
CREATE INDEX idx_user_id ON withdrawals (user_id);

-- Insert sample data for testing
INSERT INTO users (username, email, password_hash, phone_number)
VALUES ('testuser', 'test@example.com', 'password_hash', '1234567890');

INSERT INTO game_history (user_id, game_name, game_type, bet_amount, win_amount)
VALUES (1, 'Slot Machine', 'slot', 10.00, 50.00);

INSERT INTO transaction_logs (user_id, transaction_type, amount, payment_method)
VALUES (1, 'deposit', 100.00, 'Credit Card');

INSERT INTO deposits (user_id, amount, payment_method)
VALUES (1, 100.00, 'Credit Card');

INSERT INTO withdrawals (user_id, amount, payment_method)
VALUES (1, 50.00, 'Bank Transfer');
```
