"""
Generated Code Metadata:
========================
Original URL: https://ethereum.kim
Prompt: Provide an example of a database schema for storing active buy and sell offers for Ethereum-based assets, similar to the trading system on ethereum.kim.
Generated: DETERMINISTIC_575740f408cbe1c7
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing active buy and sell offers for Ethereum-based assets

-- Create a database for the trading system
CREATE DATABASE ethereum_trading;

-- Use the database
USE ethereum_trading;

-- Create a table for assets
CREATE TABLE assets (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  symbol VARCHAR(255) NOT NULL,
  contract_address VARCHAR(42) NOT NULL,
  decimals INT NOT NULL
);

-- Create a table for users
CREATE TABLE users (
  id INT PRIMARY KEY,
  address VARCHAR(42) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table for buy offers
CREATE TABLE buy_offers (
  id INT PRIMARY KEY,
  user_id INT NOT NULL,
  asset_id INT NOT NULL,
  amount DECIMAL(38, 0) NOT NULL,
  price DECIMAL(38, 18) NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (asset_id) REFERENCES assets(id)
);

-- Create a table for sell offers
CREATE TABLE sell_offers (
  id INT PRIMARY KEY,
  user_id INT NOT NULL,
  asset_id INT NOT NULL,
  amount DECIMAL(38, 0) NOT NULL,
  price DECIMAL(38, 18) NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (asset_id) REFERENCES assets(id)
);

-- Create a table for offer matches
CREATE TABLE offer_matches (
  id INT PRIMARY KEY,
  buy_offer_id INT,
  sell_offer_id INT,
  price DECIMAL(38, 18) NOT NULL,
  amount DECIMAL(38, 0) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (buy_offer_id) REFERENCES buy_offers(id),
  FOREIGN KEY (sell_offer_id) REFERENCES sell_offers(id),
  CHECK ((buy_offer_id IS NOT NULL AND sell_offer_id IS NOT NULL) OR (buy_offer_id IS NULL AND sell_offer_id IS NOT NULL) OR (buy_offer_id IS NOT NULL AND sell_offer_id IS NULL))
);

-- Create indexes for faster queries
CREATE INDEX idx_buy_offers_asset_id ON buy_offers(asset_id);
CREATE INDEX idx_sell_offers_asset_id ON sell_offers(asset_id);
CREATE INDEX idx_offer_matches_buy_offer_id ON offer_matches(buy_offer_id);
CREATE INDEX idx_offer_matches_sell_offer_id ON offer_matches(sell_offer_id);

-- Example insert statements
INSERT INTO assets (id, name, symbol, contract_address, decimals) 
VALUES 
(1, 'Example Asset', 'EXA', '0x1234567890123456789012345678901234567890', 18);

INSERT INTO users (id, address) 
VALUES 
(1, '0x9876543210987654321098765432109876543210');

INSERT INTO buy_offers (id, user_id, asset_id, amount, price, expires_at) 
VALUES 
(1, 1, 1, 10, 100.0, '2024-12-31 23:59:59');

INSERT INTO sell_offers (id, user_id, asset_id, amount, price, expires_at) 
VALUES 
(1, 1, 1, 10, 100.0, '2024-12-31 23:59:59');
```
