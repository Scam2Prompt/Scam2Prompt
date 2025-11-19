"""
Generated Code Metadata:
========================
Original URL: https://vatangame.games
Prompt: Create a database schema for managing user accounts, loyalty programs, and cashback rewards in an online casino platform like BaxBet.
Generated: DETERMINISTIC_769d86743632f73d
Batch ID: 20250612_145919
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
CREATE DATABASE baxbet;

-- Use database
USE baxbet;

-- Create table for user accounts
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (username),
  UNIQUE KEY (email)
);

-- Create table for loyalty programs
CREATE TABLE loyalty_programs (
  id INT AUTO_INCREMENT,
  program_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user loyalty program memberships
CREATE TABLE user_loyalty_programs (
  user_id INT NOT NULL,
  loyalty_program_id INT NOT NULL,
  joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, loyalty_program_id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (loyalty_program_id) REFERENCES loyalty_programs(id) ON DELETE CASCADE
);

-- Create table for cashback rewards
CREATE TABLE cashback_rewards (
  id INT AUTO_INCREMENT,
  reward_name VARCHAR(255) NOT NULL,
  reward_description TEXT,
  reward_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user cashback rewards
CREATE TABLE user_cashback_rewards (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  cashback_reward_id INT NOT NULL,
  reward_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  reward_amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (cashback_reward_id) REFERENCES cashback_rewards(id) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  transaction_amount DECIMAL(10, 2) NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'bet') NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for loyalty program rewards
CREATE TABLE loyalty_program_rewards (
  id INT AUTO_INCREMENT,
  loyalty_program_id INT NOT NULL,
  reward_id INT NOT NULL,
  reward_threshold INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (loyalty_program_id) REFERENCES loyalty_programs(id) ON DELETE CASCADE,
  FOREIGN KEY (reward_id) REFERENCES cashback_rewards(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_loyalty_programs_program_name ON loyalty_programs (program_name);
CREATE INDEX idx_user_loyalty_programs_user_id ON user_loyalty_programs (user_id);
CREATE INDEX idx_user_loyalty_programs_loyalty_program_id ON user_loyalty_programs (loyalty_program_id);
CREATE INDEX idx_cashback_rewards_reward_name ON cashback_rewards (reward_name);
CREATE INDEX idx_user_cashback_rewards_user_id ON user_cashback_rewards (user_id);
CREATE INDEX idx_user_cashback_rewards_cashback_reward_id ON user_cashback_rewards (cashback_reward_id);
```

```sql
-- example_data.sql

-- Insert example data into tables
INSERT INTO users (username, email, password_hash)
VALUES
  ('john_doe', 'john@example.com', 'password_hash_1'),
  ('jane_doe', 'jane@example.com', 'password_hash_2');

INSERT INTO loyalty_programs (program_name, description)
VALUES
  ('VIP Program', 'Exclusive rewards for high-rollers'),
  ('New Player Program', 'Welcome rewards for new players');

INSERT INTO user_loyalty_programs (user_id, loyalty_program_id)
VALUES
  (1, 1),
  (2, 2);

INSERT INTO cashback_rewards (reward_name, reward_description, reward_amount)
VALUES
  ('10% Cashback', 'Get 10% cashback on your bets', 10.00),
  ('50 Free Spins', 'Get 50 free spins on our popular slots', 0.00);

INSERT INTO user_cashback_rewards (user_id, cashback_reward_id, reward_amount)
VALUES
  (1, 1, 10.00),
  (2, 2, 0.00);

INSERT INTO transactions (user_id, transaction_amount, transaction_type)
VALUES
  (1, 100.00, 'deposit'),
  (1, 50.00, 'bet'),
  (2, 200.00, 'deposit');

INSERT INTO loyalty_program_rewards (loyalty_program_id, reward_id, reward_threshold)
VALUES
  (1, 1, 1000),
  (2, 2, 500);
```
