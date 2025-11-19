"""
Generated Code Metadata:
========================
Original URL: https://todaythegames.com
Prompt: Design a database schema for storing user data, game statistics, and leaderboard information for a social casino platform similar to todaythegames.com.
Generated: DETERMINISTIC_53d93363bbaccf3d
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for social casino platform
CREATE DATABASE social_casino;

-- Use social casino database
USE social_casino;

-- Create table for users
CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create table for games
CREATE TABLE games (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  game_name VARCHAR(255) NOT NULL,
  game_type ENUM('slot', 'poker', 'blackjack') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create table for user game statistics
CREATE TABLE user_game_stats (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  game_id BIGINT NOT NULL,
  wins INT DEFAULT 0,
  losses INT DEFAULT 0,
  draws INT DEFAULT 0,
  total_played INT DEFAULT 0,
  total_bet DECIMAL(10, 2) DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
);

-- Create table for leaderboard
CREATE TABLE leaderboard (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  game_id BIGINT NOT NULL,
  user_id BIGINT NOT NULL,
  score BIGINT DEFAULT 0,
  rank INT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for user sessions
CREATE TABLE user_sessions (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  session_token VARCHAR(255) NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_user_game_stats_user_id ON user_game_stats(user_id);
CREATE INDEX idx_user_game_stats_game_id ON user_game_stats(game_id);
CREATE INDEX idx_leaderboard_game_id ON leaderboard(game_id);
CREATE INDEX idx_leaderboard_user_id ON leaderboard(user_id);
CREATE INDEX idx_user_sessions_user_id ON user_sessions(user_id);

-- Create stored procedure to update user game statistics
DELIMITER //
CREATE PROCEDURE update_user_game_stats(
  IN p_user_id BIGINT,
  IN p_game_id BIGINT,
  IN p_win INT,
  IN p_loss INT,
  IN p_draw INT,
  IN p_total_played INT,
  IN p_total_bet DECIMAL(10, 2)
)
BEGIN
  INSERT INTO user_game_stats (user_id, game_id, wins, losses, draws, total_played, total_bet)
  VALUES (p_user_id, p_game_id, p_win, p_loss, p_draw, p_total_played, p_total_bet)
  ON DUPLICATE KEY UPDATE
    wins = wins + p_win,
    losses = losses + p_loss,
    draws = draws + p_draw,
    total_played = total_played + p_total_played,
    total_bet = total_bet + p_total_bet;
END//
DELIMITER ;

-- Create stored procedure to update leaderboard
DELIMITER //
CREATE PROCEDURE update_leaderboard(
  IN p_game_id BIGINT,
  IN p_user_id BIGINT,
  IN p_score BIGINT
)
BEGIN
  INSERT INTO leaderboard (game_id, user_id, score)
  VALUES (p_game_id, p_user_id, p_score)
  ON DUPLICATE KEY UPDATE
    score = p_score,
    rank = (SELECT COUNT(*) FROM leaderboard WHERE game_id = p_game_id AND score > p_score) + 1;
END//
DELIMITER ;
```
