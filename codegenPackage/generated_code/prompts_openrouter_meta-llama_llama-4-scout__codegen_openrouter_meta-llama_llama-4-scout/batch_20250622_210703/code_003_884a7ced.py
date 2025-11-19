"""
Generated Code Metadata:
========================
Original URL: https://abiliatrading.co.za
Prompt: "Design a database schema for an online auction platform like Abilia Trading, including tables for users, auctions, bids, and payments."
Generated: DETERMINISTIC_884a7cedf9d9e319
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for online auction platform
CREATE DATABASE online_auction;

-- Use the database
USE online_auction;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for auctions
CREATE TABLE auctions (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT NOT NULL,
  start_price DECIMAL(10, 2) NOT NULL,
  current_price DECIMAL(10, 2) NOT NULL,
  end_price DECIMAL(10, 2) NOT NULL,
  start_date TIMESTAMP NOT NULL,
  end_date TIMESTAMP NOT NULL,
  user_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for bids
CREATE TABLE bids (
  id INT AUTO_INCREMENT,
  auction_id INT NOT NULL,
  user_id INT NOT NULL,
  bid_amount DECIMAL(10, 2) NOT NULL,
  bid_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (auction_id) REFERENCES auctions(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE (auction_id, user_id)
);

-- Create table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  auction_id INT NOT NULL,
  user_id INT NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (auction_id) REFERENCES auctions(id) ON DELETE CASCADE,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create index on foreign key columns
CREATE INDEX idx_auctions_user_id ON auctions (user_id);
CREATE INDEX idx_bids_auction_id ON bids (auction_id);
CREATE INDEX idx_bids_user_id ON bids (user_id);
CREATE INDEX idx_payments_auction_id ON payments (auction_id);
CREATE INDEX idx_payments_user_id ON payments (user_id);

-- Create trigger to update current price of auction when a new bid is placed
DELIMITER $$
CREATE TRIGGER update_current_price
AFTER INSERT ON bids
FOR EACH ROW
BEGIN
  UPDATE auctions
  SET current_price = NEW.bid_amount
  WHERE id = NEW.auction_id;
END$$
DELIMITER ;

-- Create trigger to prevent bids after auction end date
DELIMITER $$
CREATE TRIGGER prevent_bids_after_end_date
BEFORE INSERT ON bids
FOR EACH ROW
BEGIN
  IF (SELECT end_date FROM auctions WHERE id = NEW.auction_id) < NEW.bid_date THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Bidding has ended for this auction';
  END IF;
END$$
DELIMITER ;
```
