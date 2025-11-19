"""
Generated Code Metadata:
========================
Original URL: https://shibariumdao.io
Prompt: Create a database schema for managing user accounts, transaction history, and game data for an online casino platform like S666.
Generated: DETERMINISTIC_7ead4e400f0083d4
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for online casino platform

CREATE DATABASE s666_casino;

USE s666_casino;

-- Create table for user accounts
CREATE TABLE users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_active` BOOLEAN DEFAULT 1,
  `role` ENUM('admin', 'user') DEFAULT 'user',
  PRIMARY KEY (`id`),
  UNIQUE KEY (`username`, `email`)
);

-- Create table for user profiles
CREATE TABLE user_profiles (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `first_name` VARCHAR(50),
  `last_name` VARCHAR(50),
  `phone_number` VARCHAR(20),
  `address` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for game data
CREATE TABLE games (
  `id` INT AUTO_INCREMENT,
  `game_name` VARCHAR(100) NOT NULL,
  `game_type` ENUM('slot', 'poker', 'blackjack') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for transaction history
CREATE TABLE transactions (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `game_id` INT,
  `transaction_type` ENUM('deposit', 'withdrawal', 'bet') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`game_id`) REFERENCES games(`id`) ON DELETE SET NULL
);

-- Create table for deposits
CREATE TABLE deposits (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('credit_card', 'bank_transfer', 'ewallet') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for withdrawals
CREATE TABLE withdrawals (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `payment_method` ENUM('credit_card', 'bank_transfer', 'ewallet') NOT NULL,
  `status` ENUM('pending', 'approved', 'rejected') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for game bets
CREATE TABLE game_bets (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `game_id` INT NOT NULL,
  `bet_amount` DECIMAL(10, 2) NOT NULL,
  `bet_type` VARCHAR(100) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`game_id`) REFERENCES games(`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_transactions_user_id ON transactions (user_id);
CREATE INDEX idx_transactions_game_id ON transactions (game_id);
CREATE INDEX idx_game_bets_user_id ON game_bets (user_id);
CREATE INDEX idx_game_bets_game_id ON game_bets (game_id);
```
