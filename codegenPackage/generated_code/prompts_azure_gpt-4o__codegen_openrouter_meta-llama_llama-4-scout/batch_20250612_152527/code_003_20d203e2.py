"""
Generated Code Metadata:
========================
Original URL: https://shubaswap.com
Prompt: Create a database schema for storing user accounts, game history, and jackpot winnings, modeled after the MESIN128 platform.
Generated: DETERMINISTIC_20d203e2f42924f3
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for MESIN128 platform

CREATE DATABASE mesin128;

USE mesin128;

-- Create table for user accounts
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (username),
  UNIQUE KEY (email)
);

-- Create table for game history
CREATE TABLE game_history (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_name VARCHAR(100) NOT NULL,
  game_date DATE NOT NULL,
  bet_amount DECIMAL(10, 2) NOT NULL,
  winnings DECIMAL(10, 2) NOT NULL,
  game_result VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for jackpot winnings
CREATE TABLE jackpot_winnings (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  jackpot_name VARCHAR(100) NOT NULL,
  winning_date DATE NOT NULL,
  winning_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create index on user_id in game_history table
CREATE INDEX idx_user_id_game_history ON game_history (user_id);

-- Create index on user_id in jackpot_winnings table
CREATE INDEX idx_user_id_jackpot_winnings ON jackpot_winnings (user_id);

-- Create stored procedure to insert new user account
DELIMITER //
CREATE PROCEDURE insert_user(
  IN p_username VARCHAR(50),
  IN p_email VARCHAR(100),
  IN p_password_hash VARCHAR(255)
)
BEGIN
  INSERT INTO users (username, email, password_hash)
  VALUES (p_username, p_email, p_password_hash);
END//
DELIMITER ;

-- Create stored procedure to insert new game history
DELIMITER //
CREATE PROCEDURE insert_game_history(
  IN p_user_id INT,
  IN p_game_name VARCHAR(100),
  IN p_game_date DATE,
  IN p_bet_amount DECIMAL(10, 2),
  IN p_winnings DECIMAL(10, 2),
  IN p_game_result VARCHAR(100)
)
BEGIN
  INSERT INTO game_history (user_id, game_name, game_date, bet_amount, winnings, game_result)
  VALUES (p_user_id, p_game_name, p_game_date, p_bet_amount, p_winnings, p_game_result);
END//
DELIMITER ;

-- Create stored procedure to insert new jackpot winnings
DELIMITER //
CREATE PROCEDURE insert_jackpot_winnings(
  IN p_user_id INT,
  IN p_jackpot_name VARCHAR(100),
  IN p_winning_date DATE,
  IN p_winning_amount DECIMAL(10, 2)
)
BEGIN
  INSERT INTO jackpot_winnings (user_id, jackpot_name, winning_date, winning_amount)
  VALUES (p_user_id, p_jackpot_name, p_winning_date, p_winning_amount);
END//
DELIMITER ;
```
