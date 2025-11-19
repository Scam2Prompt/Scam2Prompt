"""
Generated Code Metadata:
========================
Original URL: https://bitmixr.biz
Prompt: Design a database schema for a slot game platform with tables for users, games, bonuses, and transactions.
Generated: DETERMINISTIC_7c4b62df7a00d06d
Batch ID: 20250622_205042
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
CREATE DATABASE slot_game_platform;

-- Use database
USE slot_game_platform;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  balance DECIMAL(10, 2) DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for games
CREATE TABLE games (
  id INT AUTO_INCREMENT,
  game_name VARCHAR(255) NOT NULL,
  game_description TEXT,
  game_image_url VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for bonuses
CREATE TABLE bonuses (
  id INT AUTO_INCREMENT,
  bonus_name VARCHAR(255) NOT NULL,
  bonus_description TEXT,
  bonus_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT,
  bonus_id INT,
  transaction_type ENUM('deposit', 'withdrawal', 'bet', 'bonus') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE SET NULL,
  FOREIGN KEY (bonus_id) REFERENCES bonuses(id) ON DELETE SET NULL
);

-- Create table for user bonuses
CREATE TABLE user_bonuses (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  bonus_id INT NOT NULL,
  claimed_at TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (bonus_id) REFERENCES bonuses(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, bonus_id)
);

-- Create indexes
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_games_game_name ON games (game_name);
CREATE INDEX idx_bonuses_bonus_name ON bonuses (bonus_name);
CREATE INDEX idx_transactions_user_id ON transactions (user_id);
CREATE INDEX idx_transactions_game_id ON transactions (game_id);
CREATE INDEX idx_transactions_bonus_id ON transactions (bonus_id);
```

```sql
-- example_data.sql

-- Insert example data into users table
INSERT INTO users (username, email, password_hash, balance)
VALUES 
  ('john_doe', 'john@example.com', 'password_hash', 100.00),
  ('jane_doe', 'jane@example.com', 'password_hash', 50.00);

-- Insert example data into games table
INSERT INTO games (game_name, game_description, game_image_url)
VALUES 
  ('Slot Machine', 'A classic slot machine game', 'slot-machine.jpg'),
  ('Roulette', 'A game of chance', 'roulette.jpg');

-- Insert example data into bonuses table
INSERT INTO bonuses (bonus_name, bonus_description, bonus_amount)
VALUES 
  ('Welcome Bonus', 'A bonus for new users', 20.00),
  ('Deposit Bonus', 'A bonus for deposits', 10.00);

-- Insert example data into transactions table
INSERT INTO transactions (user_id, game_id, transaction_type, amount)
VALUES 
  (1, 1, 'bet', 10.00),
  (1, 1, 'bet', 20.00),
  (2, 2, 'bet', 5.00);

-- Insert example data into user_bonuses table
INSERT INTO user_bonuses (user_id, bonus_id, claimed_at)
VALUES 
  (1, 1, NOW()),
  (2, 2, NOW());
```
