"""
Generated Code Metadata:
========================
Original URL: https://www.ledger-live-ledger.org
Prompt: Design a database schema to store user information, bets, and transactions for a Vavada-like sports betting platform.
Generated: DETERMINISTIC_b520f7936b4e9a90
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Vavada-like sports betting platform

-- Create database
CREATE DATABASE vavada_betting_platform;

-- Use database
USE vavada_betting_platform;

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

-- Create table for sports
CREATE TABLE sports (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  sport_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  start_time TIMESTAMP NOT NULL,
  end_time TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE
);

-- Create table for bets
CREATE TABLE bets (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  event_id INT NOT NULL,
  bet_type ENUM('win', 'lose', 'draw') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  odds DECIMAL(5, 2) NOT NULL,
  status ENUM('pending', 'won', 'lost', 'canceled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  bet_id INT,
  transaction_type ENUM('deposit', 'withdrawal', 'bet_placed', 'bet_won', 'bet_lost') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (bet_id) REFERENCES bets(id) ON DELETE SET NULL
);

-- Create table for deposits
CREATE TABLE deposits (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  status ENUM('pending', 'success', 'failed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for withdrawals
CREATE TABLE withdrawals (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
  status ENUM('pending', 'success', 'failed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_bets_user_id ON bets (user_id);
CREATE INDEX idx_bets_event_id ON bets (event_id);
CREATE INDEX idx_transactions_user_id ON transactions (user_id);
CREATE INDEX idx_deposits_user_id ON deposits (user_id);
CREATE INDEX idx_withdrawals_user_id ON withdrawals (user_id);
```
