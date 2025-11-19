"""
Generated Code Metadata:
========================
Original URL: https://metis2020.com
Prompt: Create a database schema for managing user accounts, transaction history, and slot game statistics for a platform like Satria4D.
Generated: DETERMINISTIC_3986e73ff5b0086b
Batch ID: 20250612_152739
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
CREATE DATABASE satria4d;

-- Use database
USE satria4d;

-- Create table for user accounts
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for transaction history
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'bet') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for slot game statistics
CREATE TABLE slot_games (
  id INT AUTO_INCREMENT,
  game_name VARCHAR(255) NOT NULL,
  game_code VARCHAR(255) UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user slot game statistics
CREATE TABLE user_slot_game_stats (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  wins INT DEFAULT 0,
  losses INT DEFAULT 0,
  total_bets DECIMAL(10, 2) DEFAULT 0,
  total_winnings DECIMAL(10, 2) DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (game_id) REFERENCES slot_games(id) ON DELETE CASCADE
);

-- Create table for bet history
CREATE TABLE bet_history (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  bet_amount DECIMAL(10, 2) NOT NULL,
  bet_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  result ENUM('win', 'loss') NOT NULL,
  winnings DECIMAL(10, 2) DEFAULT 0,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (game_id) REFERENCES slot_games(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_user_id ON transactions (user_id);
CREATE INDEX idx_game_id ON user_slot_game_stats (game_id);
CREATE INDEX idx_user_id ON user_slot_game_stats (user_id);
CREATE INDEX idx_user_id ON bet_history (user_id);
CREATE INDEX idx_game_id ON bet_history (game_id);
```

```sql
-- stored_procedures.sql

DELIMITER //

CREATE PROCEDURE GetUserTransactionHistory(IN userId INT)
BEGIN
  SELECT * FROM transactions WHERE user_id = userId;
END //

CREATE PROCEDURE GetUserSlotGameStats(IN userId INT)
BEGIN
  SELECT * FROM user_slot_game_stats WHERE user_id = userId;
END //

CREATE PROCEDURE UpdateUserSlotGameStats(
  IN userId INT,
  IN gameId INT,
  IN wins INT,
  IN losses INT,
  IN totalBets DECIMAL(10, 2),
  IN totalWinnings DECIMAL(10, 2)
)
BEGIN
  INSERT INTO user_slot_game_stats (user_id, game_id, wins, losses, total_bets, total_winnings)
  VALUES (userId, gameId, wins, losses, totalBets, totalWinnings)
  ON DUPLICATE KEY UPDATE
    wins = wins + values(wins),
    losses = losses + values(losses),
    total_bets = total_bets + values(total_bets),
    total_winnings = total_winnings + values(total_winnings);
END //

DELIMITER ;
```

```sql
-- example_usage.sql

-- Insert a new user
INSERT INTO users (username, email, password_hash)
VALUES ('john_doe', 'john@example.com', 'password_hash');

-- Get user transaction history
CALL GetUserTransactionHistory(1);

-- Get user slot game statistics
CALL GetUserSlotGameStats(1);

-- Update user slot game statistics
CALL UpdateUserSlotGameStats(1, 1, 10, 5, 100.00, 50.00);
```
