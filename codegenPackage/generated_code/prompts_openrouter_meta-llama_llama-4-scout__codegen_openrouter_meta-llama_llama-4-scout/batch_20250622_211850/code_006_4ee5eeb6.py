"""
Generated Code Metadata:
========================
Original URL: https://cryptomaniaapp.com
Prompt: Design a database schema to store and manage user data, trading history, and market data for a cryptocurrency trading platform like Crypto Mania, ensuring data security and scalability.
Generated: DETERMINISTIC_4ee5eeb6981504dd
Batch ID: 20250622_211850
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
CREATE DATABASE crypto_mania;

-- Use database
USE crypto_mania;

-- Create table for users
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for user profiles
CREATE TABLE user_profiles (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for market data
CREATE TABLE market_data (
  id BIGINT AUTO_INCREMENT,
  symbol VARCHAR(20) NOT NULL,
  name VARCHAR(255) NOT NULL,
  type ENUM('crypto', 'fiat') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for trading history
CREATE TABLE trading_history (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  market_data_id BIGINT NOT NULL,
  trade_type ENUM('buy', 'sell') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (market_data_id) REFERENCES market_data(id) ON DELETE CASCADE
);

-- Create table for user balances
CREATE TABLE user_balances (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  market_data_id BIGINT NOT NULL,
  balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (market_data_id) REFERENCES market_data(id) ON DELETE CASCADE,
  UNIQUE KEY (user_id, market_data_id)
);

-- Create table for transactions
CREATE TABLE transactions (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  market_data_id BIGINT NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (market_data_id) REFERENCES market_data(id) ON DELETE CASCADE
);

-- Create indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_user_profiles_user_id ON user_profiles(user_id);
CREATE INDEX idx_market_data_symbol ON market_data(symbol);
CREATE INDEX idx_trading_history_user_id ON trading_history(user_id);
CREATE INDEX idx_trading_history_market_data_id ON trading_history(market_data_id);
CREATE INDEX idx_user_balances_user_id ON user_balances(user_id);
CREATE INDEX idx_user_balances_market_data_id ON user_balances(market_data_id);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_market_data_id ON transactions(market_data_id);
```

```python
# models.py
import mysql.connector
from mysql.connector import Error

class CryptoManiaDB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
        queries = [
            """
            CREATE TABLE IF NOT EXISTS users (
              id BIGINT AUTO_INCREMENT,
              email VARCHAR(255) NOT NULL UNIQUE,
              password_hash VARCHAR(255) NOT NULL,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
              PRIMARY KEY (id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS user_profiles (
              id BIGINT AUTO_INCREMENT,
              user_id BIGINT NOT NULL,
              first_name VARCHAR(255),
              last_name VARCHAR(255),
              phone_number VARCHAR(20),
              address VARCHAR(255),
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
              PRIMARY KEY (id),
              FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS market_data (
              id BIGINT AUTO_INCREMENT,
              symbol VARCHAR(20) NOT NULL,
              name VARCHAR(255) NOT NULL,
              type ENUM('crypto', 'fiat') NOT NULL,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
              PRIMARY KEY (id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS trading_history (
              id BIGINT AUTO_INCREMENT,
              user_id BIGINT NOT NULL,
              market_data_id BIGINT NOT NULL,
              trade_type ENUM('buy', 'sell') NOT NULL,
              amount DECIMAL(10, 2) NOT NULL,
              price DECIMAL(10, 2) NOT NULL,
              timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              PRIMARY KEY (id),
              FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
              FOREIGN KEY (market_data_id) REFERENCES market_data(id) ON DELETE CASCADE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS user_balances (
              id BIGINT AUTO_INCREMENT,
              user_id BIGINT NOT NULL,
              market_data_id BIGINT NOT NULL,
              balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
              PRIMARY KEY (id),
              FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
              FOREIGN KEY (market_data_id) REFERENCES market_data(id) ON DELETE CASCADE,
              UNIQUE KEY (user_id, market_data_id)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS transactions (
              id BIGINT AUTO_INCREMENT,
              user_id BIGINT NOT NULL,
              market_data_id BIGINT NOT NULL,
              transaction_type ENUM('deposit', 'withdrawal') NOT NULL,
              amount DECIMAL(10, 2) NOT NULL,
              timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              PRIMARY KEY (id),
              FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
              FOREIGN KEY (market_data_id) REFERENCES market_data(id) ON DELETE CASCADE
            );
            """
        ]

        cursor = self.connection.cursor()
        for query in queries:
            cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Usage
if __name__ == "__main__":
    db = CryptoManiaDB('localhost', 'crypto_mania', 'root', 'password')
    db.connect()
    db.create_tables()
    db.close_connection()
```
