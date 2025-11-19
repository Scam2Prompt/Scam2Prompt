"""
Generated Code Metadata:
========================
Original URL: https://degenroyale.com
Prompt: Create a SQL database schema to store user accounts, game history, and transaction data for an online casino platform like Royal Reels.
Generated: DETERMINISTIC_39eeacdc855795ae
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Royal Reels online casino platform
CREATE DATABASE royal_reels;

-- Use the royal_reels database
USE royal_reels;

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

-- Create table for game history
CREATE TABLE game_history (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `game_name` VARCHAR(100) NOT NULL,
  `game_type` ENUM('slot', 'poker', 'blackjack', 'roulette') NOT NULL,
  `bet_amount` DECIMAL(10, 2) NOT NULL,
  `win_amount` DECIMAL(10, 2),
  `game_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE transactions (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `transaction_type` ENUM('deposit', 'withdrawal') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `transaction_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `status` ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for deposits
CREATE TABLE deposits (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  `transaction_id` INT,
  `status` ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`transaction_id`) REFERENCES transactions(`id`) ON DELETE SET NULL
);

-- Create table for withdrawals
CREATE TABLE withdrawals (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  `transaction_id` INT,
  `status` ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`transaction_id`) REFERENCES transactions(`id`) ON DELETE SET NULL
);

-- Create indexes for faster queries
CREATE INDEX idx_user_id ON game_history (user_id);
CREATE INDEX idx_user_id ON transactions (user_id);
CREATE INDEX idx_user_id ON deposits (user_id);
CREATE INDEX idx_user_id ON withdrawals (user_id);
```

```sql
-- Example usage:
-- Insert a new user
INSERT INTO users (username, email, password_hash)
VALUES ('john_doe', 'john@example.com', 'password_hash');

-- Insert a new game history entry
INSERT INTO game_history (user_id, game_name, game_type, bet_amount, win_amount)
VALUES (1, 'Slot Machine', 'slot', 10.00, 50.00);

-- Insert a new transaction
INSERT INTO transactions (user_id, transaction_type, amount)
VALUES (1, 'deposit', 100.00);

-- Get all game history for a user
SELECT * FROM game_history WHERE user_id = 1;

-- Get all transactions for a user
SELECT * FROM transactions WHERE user_id = 1;
```
