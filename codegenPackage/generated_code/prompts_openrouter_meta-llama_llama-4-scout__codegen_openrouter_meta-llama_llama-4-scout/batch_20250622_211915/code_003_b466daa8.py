"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Design a database schema for storing user information, game data, and transaction records for a betting platform like VZ99.
Generated: DETERMINISTIC_b466daa8a6fbfde0
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for VZ99 betting platform

-- Create database
CREATE DATABASE vz99_betting_platform;

-- Use database
USE vz99_betting_platform;

-- Create table for users
CREATE TABLE Users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for games
CREATE TABLE Games (
  `id` INT AUTO_INCREMENT,
  `game_name` VARCHAR(255) NOT NULL,
  `game_type` ENUM('sports', 'casino', 'lottery') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for game data
CREATE TABLE Game_Data (
  `id` INT AUTO_INCREMENT,
  `game_id` INT NOT NULL,
  `game_state` ENUM('pending', 'in_progress', 'completed') NOT NULL,
  `start_time` TIMESTAMP,
  `end_time` TIMESTAMP,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`game_id`) REFERENCES Games(`id`)
);

-- Create table for transactions
CREATE TABLE Transactions (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `game_id` INT,
  `transaction_type` ENUM('bet', 'withdrawal', 'deposit') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `transaction_state` ENUM('pending', 'completed', 'failed') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`),
  FOREIGN KEY (`game_id`) REFERENCES Games(`id`)
);

-- Create table for bet records
CREATE TABLE Bet_Records (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `game_id` INT NOT NULL,
  `bet_amount` DECIMAL(10, 2) NOT NULL,
  `bet_state` ENUM('pending', 'won', 'lost') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`),
  FOREIGN KEY (`game_id`) REFERENCES Games(`id`)
);

-- Create index on user_id in Transactions and Bet_Records tables
CREATE INDEX idx_user_id_transactions ON Transactions (user_id);
CREATE INDEX idx_user_id_bet_records ON Bet_Records (user_id);

-- Create index on game_id in Game_Data, Transactions and Bet_Records tables
CREATE INDEX idx_game_id_game_data ON Game_Data (game_id);
CREATE INDEX idx_game_id_transactions ON Transactions (game_id);
CREATE INDEX idx_game_id_bet_records ON Bet_Records (game_id);
```
