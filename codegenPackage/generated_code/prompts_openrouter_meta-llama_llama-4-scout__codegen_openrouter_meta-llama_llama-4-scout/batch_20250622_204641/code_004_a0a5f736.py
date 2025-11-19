"""
Generated Code Metadata:
========================
Original URL: https://inceptiontrades.net
Prompt: Design a database schema to manage client information, investment portfolios, and transaction history for a multi-asset management firm like Inception Trades.
Generated: DETERMINISTIC_a0a5f7362ad6963b
Batch ID: 20250622_204641
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Inception Trades
CREATE DATABASE inception_trades;

-- Use inception_trades database
USE inception_trades;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for investment portfolios
CREATE TABLE portfolios (
  portfolio_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  portfolio_name VARCHAR(255) NOT NULL,
  portfolio_type VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (portfolio_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for assets
CREATE TABLE assets (
  asset_id INT AUTO_INCREMENT,
  asset_name VARCHAR(255) NOT NULL,
  asset_type VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (asset_id)
);

-- Create table for portfolio assets
CREATE TABLE portfolio_assets (
  portfolio_id INT NOT NULL,
  asset_id INT NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  purchase_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (portfolio_id, asset_id),
  FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE,
  FOREIGN KEY (asset_id) REFERENCES assets(asset_id) ON DELETE CASCADE
);

-- Create table for transactions
CREATE TABLE transactions (
  transaction_id INT AUTO_INCREMENT,
  portfolio_id INT NOT NULL,
  asset_id INT NOT NULL,
  transaction_type VARCHAR(100) NOT NULL CHECK (transaction_type IN ('BUY', 'SELL')),
  quantity DECIMAL(10, 2) NOT NULL,
  transaction_price DECIMAL(10, 2) NOT NULL,
  transaction_date TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE,
  FOREIGN KEY (asset_id) REFERENCES assets(asset_id) ON DELETE CASCADE
);

-- Create table for fees
CREATE TABLE fees (
  fee_id INT AUTO_INCREMENT,
  portfolio_id INT NOT NULL,
  fee_type VARCHAR(100) NOT NULL CHECK (fee_type IN ('MANAGEMENT', 'ADMINISTRATION')),
  fee_amount DECIMAL(10, 2) NOT NULL,
  fee_date TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (fee_id),
  FOREIGN KEY (portfolio_id) REFERENCES portfolios(portfolio_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_clients_email ON clients(email);
CREATE INDEX idx_portfolios_client_id ON portfolios(client_id);
CREATE INDEX idx_portfolio_assets_portfolio_id ON portfolio_assets(portfolio_id);
CREATE INDEX idx_portfolio_assets_asset_id ON portfolio_assets(asset_id);
CREATE INDEX idx_transactions_portfolio_id ON transactions(portfolio_id);
CREATE INDEX idx_transactions_asset_id ON transactions(asset_id);
CREATE INDEX idx_fees_portfolio_id ON fees(portfolio_id);
```

```python
# models.py

import mysql.connector
from mysql.connector import Error

class Database:
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

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error executing query: {e}")

    def execute_read_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Error executing read query: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

class Client:
    def __init__(self, client_id, first_name, last_name, email, phone_number, address):
        self.client_id = client_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address

class Portfolio:
    def __init__(self, portfolio_id, client_id, portfolio_name, portfolio_type):
        self.portfolio_id = portfolio_id
        self.client_id = client_id
        self.portfolio_name = portfolio_name
        self.portfolio_type = portfolio_type

class Asset:
    def __init__(self, asset_id, asset_name, asset_type):
        self.asset_id = asset_id
        self.asset_name = asset_name
        self.asset_type = asset_type

class Transaction:
    def __init__(self, transaction_id, portfolio_id, asset_id, transaction_type, quantity, transaction_price, transaction_date):
        self.transaction_id = transaction_id
        self.portfolio_id = portfolio_id
        self.asset_id = asset_id
        self.transaction_type = transaction_type
        self.quantity = quantity
        self.transaction_price = transaction_price
        self.transaction_date = transaction_date

class Fee:
    def __init__(self, fee_id, portfolio_id, fee_type, fee_amount, fee_date):
        self.fee_id = fee_id
        self.portfolio_id = portfolio_id
        self.fee_type = fee_type
        self.fee_amount = fee_amount
        self.fee_date = fee_date

# Example usage
if __name__ == "__main__":
    db = Database("localhost", "inception_trades", "root", "password")
    db.connect()

    # Create client
    query = """
        INSERT INTO clients (first_name, last_name, email, phone_number, address)
        VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St')
    """
    db.execute_query(query)

    # Get client
    query = "SELECT * FROM clients WHERE email = 'john.doe@example.com'"
    result = db.execute_read_query(query)
    client = Client(*result[0])

    # Create portfolio
    query = f"""
        INSERT INTO portfolios (client_id, portfolio_name, portfolio_type)
        VALUES ({client.client_id}, 'My Portfolio', 'STOCK')
    """
    db.execute_query(query)

    # Get portfolio
    query = f"SELECT * FROM portfolios WHERE client_id = {client.client_id}"
    result = db.execute_read_query(query)
    portfolio = Portfolio(*result[0])

    # Create asset
    query = """
        INSERT INTO assets (asset_name, asset_type)
        VALUES ('Apple Stock', 'STOCK')
    """
    db.execute_query(query)

    # Get asset
    query = "SELECT * FROM assets WHERE asset_name = 'Apple Stock'"
    result = db.execute_read_query(query)
    asset = Asset(*result[0])

    # Create transaction
    query = f"""
        INSERT INTO transactions (portfolio_id, asset_id, transaction_type, quantity, transaction_price, transaction_date)
        VALUES ({portfolio.portfolio_id}, {asset.asset_id}, 'BUY', 10.0, 100.0, NOW())
    """
    db.execute_query(query)

    db.close_connection()
```
