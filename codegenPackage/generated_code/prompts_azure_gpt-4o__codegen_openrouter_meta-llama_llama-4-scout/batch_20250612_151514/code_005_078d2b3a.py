"""
Generated Code Metadata:
========================
Original URL: https://bolehshop.id
Prompt: Create a database schema in SQL for managing lottery game results, user accounts, and payment transactions, inspired by the HONGTOGEL platform.
Generated: DETERMINISTIC_078d2b3a960e1199
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for lottery game management
CREATE DATABASE hongtogellotto;

-- Use the created database
USE hongtogellotto;

-- Create table for user accounts
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (username),
  UNIQUE KEY (email)
);

-- Create table for lottery game results
CREATE TABLE lottery_results (
  id INT AUTO_INCREMENT,
  game_date DATE NOT NULL,
  game_type ENUM('2D', '3D', '4D') NOT NULL,
  winning_numbers JSON NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user lottery game tickets
CREATE TABLE user_tickets (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_date DATE NOT NULL,
  game_type ENUM('2D', '3D', '4D') NOT NULL,
  ticket_numbers JSON NOT NULL,
  bet_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create table for payment transactions
CREATE TABLE payment_transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  transaction_type ENUM('deposit', 'withdrawal', 'bet') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('bank_transfer', 'online_payment') NOT NULL,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create table for user account balances
CREATE TABLE user_balances (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  UNIQUE KEY (user_id)
);

-- Create table for lottery game types
CREATE TABLE game_types (
  id INT AUTO_INCREMENT,
  game_type ENUM('2D', '3D', '4D') NOT NULL,
  game_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_user_tickets_user_id ON user_tickets (user_id);
CREATE INDEX idx_lottery_results_game_date ON lottery_results (game_date);
CREATE INDEX idx_payment_transactions_user_id ON payment_transactions (user_id);
CREATE INDEX idx_user_balances_user_id ON user_balances (user_id);
```
