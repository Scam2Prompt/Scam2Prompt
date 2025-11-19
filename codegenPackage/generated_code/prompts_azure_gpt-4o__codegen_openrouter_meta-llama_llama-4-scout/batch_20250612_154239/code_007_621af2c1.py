"""
Generated Code Metadata:
========================
Original URL: https://cashb90.net
Prompt: Create a database schema to manage user accounts, transaction history, and loyalty rewards for a casino platform like BaxBet.
Generated: DETERMINISTIC_621af2c117f2c88a
Batch ID: 20250612_154239
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
CREATE DATABASE IF NOT EXISTS baxbet;

-- Use database
USE baxbet;

-- Create table for user accounts
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user profiles
CREATE TABLE IF NOT EXISTS user_profiles (
  user_id INT NOT NULL,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  date_of_birth DATE,
  address VARCHAR(255),
  phone_number VARCHAR(20),
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for transaction history
CREATE TABLE IF NOT EXISTS transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'bet') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for loyalty rewards
CREATE TABLE IF NOT EXISTS loyalty_rewards (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  reward_type ENUM('bonus', 'free_bet', 'comp_point') NOT NULL,
  reward_value DECIMAL(10, 2) NOT NULL,
  expiration_date DATE,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for loyalty program tiers
CREATE TABLE IF NOT EXISTS loyalty_tiers (
  id INT AUTO_INCREMENT,
  tier_name VARCHAR(255) NOT NULL,
  min_points INT NOT NULL,
  max_points INT NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for user loyalty points
CREATE TABLE IF NOT EXISTS user_loyalty_points (
  user_id INT NOT NULL,
  points INT NOT NULL DEFAULT 0,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for user login history
CREATE TABLE IF NOT EXISTS user_login_history (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  login_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  ip_address VARCHAR(45),
  user_agent TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for performance optimization
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_transactions_user_id ON transactions (user_id);
CREATE INDEX idx_loyalty_rewards_user_id ON loyalty_rewards (user_id);
CREATE INDEX idx_user_loyalty_points_user_id ON user_loyalty_points (user_id);
```

```sql
-- sample_data.sql

-- Insert sample data into users table
INSERT INTO users (username, email, password_hash)
VALUES 
('john_doe', 'john@example.com', 'password_hash_1'),
('jane_doe', 'jane@example.com', 'password_hash_2');

-- Insert sample data into user_profiles table
INSERT INTO user_profiles (user_id, first_name, last_name, date_of_birth, address, phone_number)
VALUES 
(1, 'John', 'Doe', '1990-01-01', '123 Main St', '123-456-7890'),
(2, 'Jane', 'Doe', '1995-06-01', '456 Elm St', '987-654-3210');

-- Insert sample data into transactions table
INSERT INTO transactions (user_id, transaction_type, amount)
VALUES 
(1, 'deposit', 100.00),
(1, 'bet', 50.00),
(2, 'deposit', 200.00);

-- Insert sample data into loyalty_rewards table
INSERT INTO loyalty_rewards (user_id, reward_type, reward_value, expiration_date)
VALUES 
(1, 'bonus', 20.00, '2024-12-31'),
(2, 'free_bet', 10.00, '2025-06-30');

-- Insert sample data into loyalty_tiers table
INSERT INTO loyalty_tiers (tier_name, min_points, max_points)
VALUES 
('Bronze', 0, 99),
('Silver', 100, 499),
('Gold', 500, 999);

-- Insert sample data into user_loyalty_points table
INSERT INTO user_loyalty_points (user_id, points)
VALUES 
(1, 50),
(2, 200);

-- Insert sample data into user_login_history table
INSERT INTO user_login_history (user_id, ip_address, user_agent)
VALUES 
(1, '192.168.1.100', 'Mozilla/5.0'),
(2, '192.168.1.200', 'Chrome/74.0.3729.169');
```
