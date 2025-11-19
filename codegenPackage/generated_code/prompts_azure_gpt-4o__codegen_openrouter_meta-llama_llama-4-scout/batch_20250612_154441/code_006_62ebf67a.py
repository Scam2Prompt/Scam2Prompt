"""
Generated Code Metadata:
========================
Original URL: https://ethopt.io
Prompt: Create a database schema for managing diverse casino games, user accounts, and transaction histories for a platform like 2QCOM.
Generated: DETERMINISTIC_62ebf67a6f62fdc9
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
CREATE DATABASE casino_platform;

-- Use database
USE casino_platform;

-- Create table for games
CREATE TABLE games (
  game_id INT AUTO_INCREMENT,
  game_name VARCHAR(255) NOT NULL,
  game_type ENUM('slot', 'poker', 'roulette', 'blackjack') NOT NULL,
  min_bet DECIMAL(10, 2) NOT NULL,
  max_bet DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (game_id)
);

-- Create table for users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  role ENUM('admin', 'user') NOT NULL DEFAULT 'user',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id)
);

-- Create table for transactions
CREATE TABLE transactions (
  transaction_id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'bet', 'win') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (game_id) REFERENCES games(game_id)
);

-- Create table for game sessions
CREATE TABLE game_sessions (
  session_id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  end_time TIMESTAMP NULL,
  bet_amount DECIMAL(10, 2) NOT NULL,
  win_amount DECIMAL(10, 2) NULL,
  PRIMARY KEY (session_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id),
  FOREIGN KEY (game_id) REFERENCES games(game_id)
);

-- Create table for user login history
CREATE TABLE user_login_history (
  login_id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  ip_address VARCHAR(255) NOT NULL,
  user_agent TEXT NOT NULL,
  PRIMARY KEY (login_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_user_id ON transactions (user_id);
CREATE INDEX idx_game_id ON transactions (game_id);
CREATE INDEX idx_user_id ON game_sessions (user_id);
CREATE INDEX idx_game_id ON game_sessions (game_id);
```

```sql
-- stored_procedures.sql

DELIMITER $$

-- Procedure to create a new user account
CREATE PROCEDURE create_user(
  IN p_username VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_password_hash VARCHAR(255)
)
BEGIN
  INSERT INTO users (username, email, password_hash)
  VALUES (p_username, p_email, p_password_hash);
END$$

-- Procedure to deposit funds into a user's account
CREATE PROCEDURE deposit_funds(
  IN p_user_id INT,
  IN p_amount DECIMAL(10, 2)
)
BEGIN
  UPDATE users
  SET balance = balance + p_amount
  WHERE user_id = p_user_id;
  
  INSERT INTO transactions (user_id, game_id, transaction_type, amount)
  VALUES (p_user_id, NULL, 'deposit', p_amount);
END$$

-- Procedure to record a bet
CREATE PROCEDURE record_bet(
  IN p_user_id INT,
  IN p_game_id INT,
  IN p_bet_amount DECIMAL(10, 2)
)
BEGIN
  IF (SELECT balance FROM users WHERE user_id = p_user_id) >= p_bet_amount THEN
    UPDATE users
    SET balance = balance - p_bet_amount
    WHERE user_id = p_user_id;
    
    INSERT INTO transactions (user_id, game_id, transaction_type, amount)
    VALUES (p_user_id, p_game_id, 'bet', p_bet_amount);
    
    INSERT INTO game_sessions (user_id, game_id, bet_amount)
    VALUES (p_user_id, p_game_id, p_bet_amount);
  ELSE
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Insufficient balance';
  END IF;
END$$

-- Procedure to record a win
CREATE PROCEDURE record_win(
  IN p_session_id INT,
  IN p_win_amount DECIMAL(10, 2)
)
BEGIN
  UPDATE game_sessions
  SET end_time = CURRENT_TIMESTAMP, win_amount = p_win_amount
  WHERE session_id = p_session_id;
  
  UPDATE users
  SET balance = balance + p_win_amount
  WHERE user_id = (SELECT user_id FROM game_sessions WHERE session_id = p_session_id);
  
  INSERT INTO transactions (user_id, game_id, transaction_type, amount)
  VALUES (
    (SELECT user_id FROM game_sessions WHERE session_id = p_session_id),
    (SELECT game_id FROM game_sessions WHERE session_id = p_session_id),
    'win',
    p_win_amount
  );
END$$

DELIMITER ;
```
