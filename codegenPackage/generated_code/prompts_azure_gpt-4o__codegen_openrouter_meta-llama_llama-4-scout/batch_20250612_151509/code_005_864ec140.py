"""
Generated Code Metadata:
========================
Original URL: https://bitmixr.biz
Prompt: Create a database schema for managing slot game providers, player accounts, and transaction records for a site like KONTAN88.
Generated: DETERMINISTIC_864ec140be5fd960
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for KONTAN88-like site

-- Create database
CREATE DATABASE kontan88;

-- Use database
USE kontan88;

-- Create table for slot game providers
CREATE TABLE providers (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_name` (`name`)
);

-- Create table for player accounts
CREATE TABLE players (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `balance` DECIMAL(10, 2) DEFAULT 0.00,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_username` (`username`),
  UNIQUE KEY `uk_email` (`email`)
);

-- Create table for transaction records
CREATE TABLE transactions (
  `id` INT AUTO_INCREMENT,
  `player_id` INT NOT NULL,
  `provider_id` INT NOT NULL,
  `transaction_type` ENUM('deposit', 'withdrawal', 'bet', 'win') NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_player_id` (`player_id`),
  KEY `fk_provider_id` (`provider_id`),
  CONSTRAINT `fk_player_id` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_provider_id` FOREIGN KEY (`provider_id`) REFERENCES `providers` (`id`) ON DELETE CASCADE
);

-- Create table for game sessions
CREATE TABLE game_sessions (
  `id` INT AUTO_INCREMENT,
  `player_id` INT NOT NULL,
  `provider_id` INT NOT NULL,
  `game_id` VARCHAR(255) NOT NULL,
  `session_data` JSON,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_player_id` (`player_id`),
  KEY `fk_provider_id` (`provider_id`),
  CONSTRAINT `fk_player_id_game_sessions` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_provider_id_game_sessions` FOREIGN KEY (`provider_id`) REFERENCES `providers` (`id`) ON DELETE CASCADE
);

-- Create table for player login history
CREATE TABLE player_login_history (
  `id` INT AUTO_INCREMENT,
  `player_id` INT NOT NULL,
  `login_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `ip_address` VARCHAR(255) NOT NULL,
  `user_agent` TEXT,
  PRIMARY KEY (`id`),
  KEY `fk_player_id_login_history` (`player_id`),
  CONSTRAINT `fk_player_id_login_history` FOREIGN KEY (`player_id`) REFERENCES `players` (`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_players_username ON players (username);
CREATE INDEX idx_players_email ON players (email);
CREATE INDEX idx_transactions_player_id ON transactions (player_id);
CREATE INDEX idx_transactions_provider_id ON transactions (provider_id);
```

```sql
-- Sample data for testing
INSERT INTO providers (name, description) VALUES
  ('Provider 1', 'This is provider 1'),
  ('Provider 2', 'This is provider 2');

INSERT INTO players (username, email, password, balance) VALUES
  ('player1', 'player1@example.com', 'password123', 100.00),
  ('player2', 'player2@example.com', 'password123', 50.00);

INSERT INTO transactions (player_id, provider_id, transaction_type, amount, status) VALUES
  (1, 1, 'deposit', 50.00, 'success'),
  (1, 1, 'bet', 10.00, 'pending'),
  (2, 2, 'deposit', 20.00, 'success');

INSERT INTO game_sessions (player_id, provider_id, game_id, session_data) VALUES
  (1, 1, 'game1', '{"game_state": "started"}'),
  (2, 2, 'game2', '{"game_state": "ended"}');

INSERT INTO player_login_history (player_id, ip_address, user_agent) VALUES
  (1, '192.168.1.100', 'Mozilla/5.0'),
  (2, '192.168.1.200', 'Chrome/74.0.3729.169');
```
