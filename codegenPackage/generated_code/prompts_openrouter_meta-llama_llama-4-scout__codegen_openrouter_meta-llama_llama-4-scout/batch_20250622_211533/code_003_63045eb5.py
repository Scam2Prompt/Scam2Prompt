"""
Generated Code Metadata:
========================
Original URL: https://cashb90.net
Prompt: Design a database schema to store user information, game history, and transactions for an online casino platform similar to BaxBet.
Generated: DETERMINISTIC_63045eb512e884e4
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for online casino platform
CREATE DATABASE IF NOT EXISTS baxbet;

-- Use database
USE baxbet;

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  `id` BIGINT AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
);

-- Create table for game history
CREATE TABLE IF NOT EXISTS game_history (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `game_type` ENUM('slots', 'poker', 'blackjack', 'roulette') NOT NULL,
  `game_name` VARCHAR(100) NOT NULL,
  `bet_amount` DECIMAL(10, 2) NOT NULL,
  `win_amount` DECIMAL(10, 2),
  `game_result` ENUM('win', 'loss', 'draw') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE IF NOT EXISTS transactions (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `transaction_type` ENUM('deposit', 'withdrawal') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  `status` ENUM('pending', 'success', 'failed') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE CASCADE
);

-- Create table for user balances
CREATE TABLE IF NOT EXISTS user_balances (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `balance` DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE CASCADE,
  UNIQUE KEY `user_id` (`user_id`)
);

-- Create table for game bonuses
CREATE TABLE IF NOT EXISTS game_bonuses (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `game_type` ENUM('slots', 'poker', 'blackjack', 'roulette') NOT NULL,
  `bonus_type` ENUM('welcome', 'deposit', 'free_spin') NOT NULL,
  `bonus_amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_game_history_user_id ON game_history (user_id);
CREATE INDEX idx_transactions_user_id ON transactions (user_id);
CREATE INDEX idx_user_balances_user_id ON user_balances (user_id);
CREATE INDEX idx_game_bonuses_user_id ON game_bonuses (user_id);
```

```sql
-- sample_data.sql

-- Insert sample data into users table
INSERT INTO users (username, email, password_hash)
VALUES 
('john_doe', 'john@example.com', 'password_hash_1'),
('jane_doe', 'jane@example.com', 'password_hash_2');

-- Insert sample data into game_history table
INSERT INTO game_history (user_id, game_type, game_name, bet_amount, win_amount, game_result)
VALUES 
(1, 'slots', 'Slot Machine 1', 10.00, 50.00, 'win'),
(1, 'poker', 'Poker Game 1', 20.00, NULL, 'loss'),
(2, 'blackjack', 'Blackjack Game 1', 15.00, 30.00, 'win');

-- Insert sample data into transactions table
INSERT INTO transactions (user_id, transaction_type, amount, payment_method, status)
VALUES 
(1, 'deposit', 100.00, 'credit_card', 'success'),
(1, 'withdrawal', 50.00, 'paypal', 'pending'),
(2, 'deposit', 200.00, 'bank_transfer', 'success');

-- Insert sample data into user_balances table
INSERT INTO user_balances (user_id, balance)
VALUES 
(1, 150.00),
(2, 200.00);

-- Insert sample data into game_bonuses table
INSERT INTO game_bonuses (user_id, game_type, bonus_type, bonus_amount)
VALUES 
(1, 'slots', 'welcome', 10.00),
(2, 'poker', 'deposit', 20.00);
```
