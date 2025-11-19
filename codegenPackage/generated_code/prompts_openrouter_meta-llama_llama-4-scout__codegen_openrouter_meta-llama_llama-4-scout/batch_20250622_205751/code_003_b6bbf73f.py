"""
Generated Code Metadata:
========================
Original URL: https://casinovlad.com
Prompt: "Design a simple database schema for storing user information, game records, and transactions for an online casino like Cazino Vlad, using SQL."
Generated: DETERMINISTIC_b6bbf73f5f4c2de2
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the online casino
CREATE DATABASE cazino_vlad;

-- Use the cazino_vlad database
USE cazino_vlad;

-- Create a table for storing user information
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for storing game records
CREATE TABLE game_records (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_name VARCHAR(255) NOT NULL,
  game_type ENUM('slot', 'poker', 'blackjack', 'roulette') NOT NULL,
  bet_amount DECIMAL(10, 2) NOT NULL,
  win_amount DECIMAL(10, 2),
  game_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for storing transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  payment_method VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create a table for storing user balances
CREATE TABLE user_balances (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id) (user_id)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_game_records_user_id ON game_records (user_id);
CREATE INDEX idx_transactions_user_id ON transactions (user_id);
CREATE INDEX idx_user_balances_user_id ON user_balances (user_id);

-- Example insert statements
INSERT INTO users (username, email, password_hash, first_name, last_name, date_of_birth)
VALUES ('john_doe', 'john@example.com', 'password_hash', 'John', 'Doe', '1990-01-01');

INSERT INTO game_records (user_id, game_name, game_type, bet_amount, win_amount)
VALUES (1, 'Slot Machine', 'slot', 10.00, 50.00);

INSERT INTO transactions (user_id, transaction_type, amount, payment_method)
VALUES (1, 'deposit', 100.00, 'credit_card');

INSERT INTO user_balances (user_id, balance)
VALUES (1, 100.00);
```
