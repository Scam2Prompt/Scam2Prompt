"""
Generated Code Metadata:
========================
Original URL: https://venez888.vip
Prompt: Design a database schema to store user information, game records, and transactions for an online casino website like venez888.
Generated: DETERMINISTIC_a1b858507a0ac0da
Batch ID: 20250622_211418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for online casino website

CREATE DATABASE venez888;

USE venez888;

-- Create table for users
CREATE TABLE Users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `dob` DATE,
  `country` VARCHAR(50),
  `city` VARCHAR(50),
  `address` VARCHAR(200),
  `phone` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`username`),
  UNIQUE KEY (`email`)
);

-- Create table for game records
CREATE TABLE GameRecords (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `game_type` ENUM('slots', 'poker', 'blackjack', 'roulette') NOT NULL,
  `game_name` VARCHAR(100) NOT NULL,
  `bet_amount` DECIMAL(10, 2) NOT NULL,
  `win_amount` DECIMAL(10, 2),
  `loss_amount` DECIMAL(10, 2),
  `result` ENUM('win', 'loss', 'draw') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE Transactions (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `transaction_type` ENUM('deposit', 'withdrawal') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  `status` ENUM('pending', 'success', 'failed') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Create table for deposits
CREATE TABLE Deposits (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  `status` ENUM('pending', 'success', 'failed') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Create table for withdrawals
CREATE TABLE Withdrawals (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  `status` ENUM('pending', 'success', 'failed') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Create table for bonuses
CREATE TABLE Bonuses (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `bonus_type` ENUM('welcome', 'deposit') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'claimed') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Create table for user sessions
CREATE TABLE Sessions (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `session_token` VARCHAR(255) NOT NULL,
  `ip_address` VARCHAR(50) NOT NULL,
  `user_agent` VARCHAR(200) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `expired_at` TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Create indexes on frequently used columns
CREATE INDEX idx_user_id ON GameRecords (user_id);
CREATE INDEX idx_user_id ON Transactions (user_id);
CREATE INDEX idx_user_id ON Deposits (user_id);
CREATE INDEX idx_user_id ON Withdrawals (user_id);
CREATE INDEX idx_user_id ON Bonuses (user_id);
CREATE INDEX idx_session_token ON Sessions (session_token);
```

```sql
-- Sample data for testing
INSERT INTO Users (username, email, password, name, dob, country, city, address, phone)
VALUES 
('testuser', 'test@example.com', 'password123', 'John Doe', '1990-01-01', 'USA', 'New York', '123 Main St', '1234567890');

INSERT INTO GameRecords (user_id, game_type, game_name, bet_amount, win_amount, result)
VALUES 
(1, 'slots', 'Wheel of Fortune', 10.00, 50.00, 'win');

INSERT INTO Transactions (user_id, transaction_type, amount, payment_method, status)
VALUES 
(1, 'deposit', 100.00, 'credit_card', 'success');

INSERT INTO Deposits (user_id, amount, payment_method, status)
VALUES 
(1, 100.00, 'credit_card', 'success');

INSERT INTO Withdrawals (user_id, amount, payment_method, status)
VALUES 
(1, 50.00, 'paypal', 'pending');

INSERT INTO Bonuses (user_id, bonus_type, amount, status)
VALUES 
(1, 'welcome', 20.00, 'pending');

INSERT INTO Sessions (user_id, session_token, ip_address, user_agent)
VALUES 
(1, 'session_token_123', '192.168.1.100', 'Mozilla/5.0');
```
