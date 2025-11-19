"""
Generated Code Metadata:
========================
Original URL: https://poly-web-phi.vercel.app
Prompt: "Design a database schema to store user information, market data, and transaction history for a platform like Polymarket."
Generated: DETERMINISTIC_8b12fd4c11e15c7d
Batch ID: 20250622_212546
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
CREATE DATABASE polymarket;

-- Use database
USE polymarket;

-- Create table for users
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for markets
CREATE TABLE markets (
  id BIGINT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for market data
CREATE TABLE market_data (
  id BIGINT AUTO_INCREMENT,
  market_id BIGINT NOT NULL,
  data JSON,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (market_id) REFERENCES markets(id)
);

-- Create table for transactions
CREATE TABLE transactions (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  market_id BIGINT NOT NULL,
  transaction_type ENUM('buy', 'sell') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (market_id) REFERENCES markets(id)
);

-- Create table for transaction history
CREATE TABLE transaction_history (
  id BIGINT AUTO_INCREMENT,
  transaction_id BIGINT NOT NULL,
  status ENUM('pending', 'settled', 'cancelled') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);

-- Create index on market_id in market_data
CREATE INDEX idx_market_id ON market_data(market_id);

-- Create index on user_id in transactions
CREATE INDEX idx_user_id ON transactions(user_id);

-- Create index on market_id in transactions
CREATE INDEX idx_market_id_transactions ON transactions(market_id);

-- Create index on transaction_id in transaction_history
CREATE INDEX idx_transaction_id ON transaction_history(transaction_id);
```

```sql
-- data.sql

-- Insert sample data into users table
INSERT INTO users (username, email, password_hash)
VALUES 
('john_doe', 'john@example.com', 'password_hash'),
('jane_doe', 'jane@example.com', 'password_hash');

-- Insert sample data into markets table
INSERT INTO markets (name, description)
VALUES 
('Market 1', 'This is market 1'),
('Market 2', 'This is market 2');

-- Insert sample data into market_data table
INSERT INTO market_data (market_id, data)
VALUES 
(1, '{"price": 10.99, "volume": 100}'),
(2, '{"price": 5.99, "volume": 50}');

-- Insert sample data into transactions table
INSERT INTO transactions (user_id, market_id, transaction_type, amount, price)
VALUES 
(1, 1, 'buy', 10, 10.99),
(1, 2, 'sell', 5, 5.99),
(2, 1, 'buy', 20, 10.99);

-- Insert sample data into transaction_history table
INSERT INTO transaction_history (transaction_id, status)
VALUES 
(1, 'settled'),
(2, 'pending'),
(3, 'settled');
```
