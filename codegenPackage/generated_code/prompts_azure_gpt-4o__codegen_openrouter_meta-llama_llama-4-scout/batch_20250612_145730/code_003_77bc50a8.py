"""
Generated Code Metadata:
========================
Original URL: https://pansos4dz.com
Prompt: Create a database schema in SQL to store and manage user transactions, including deposits via bank transfers, e-wallets, and pulsa, as outlined on PANSOS4D.
Generated: DETERMINISTIC_77bc50a89e619789
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for PANSOS4D transactions
CREATE DATABASE IF NOT EXISTS pansos4d_transactions;

-- Use the pansos4d_transactions database
USE pansos4d_transactions;

-- Create table for users
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for transaction types
CREATE TABLE IF NOT EXISTS transaction_types (
  id INT AUTO_INCREMENT,
  type_name VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Insert initial transaction types
INSERT INTO transaction_types (type_name, description)
VALUES 
('bank_transfer', 'Deposit via bank transfer'),
('e_wallet', 'Deposit via e-wallet'),
('pulsa', 'Deposit via pulsa');

-- Create table for transactions
CREATE TABLE IF NOT EXISTS transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  transaction_type_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  transaction_code VARCHAR(255) UNIQUE,
  status ENUM('pending', 'success', 'failed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (transaction_type_id) REFERENCES transaction_types(id)
);

-- Create table for bank transfers
CREATE TABLE IF NOT EXISTS bank_transfers (
  id INT AUTO_INCREMENT,
  transaction_id INT NOT NULL,
  bank_name VARCHAR(100) NOT NULL,
  transfer_date DATE NOT NULL,
  transfer_amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);

-- Create table for e-wallets
CREATE TABLE IF NOT EXISTS e_wallets (
  id INT AUTO_INCREMENT,
  transaction_id INT NOT NULL,
  e_wallet_name VARCHAR(100) NOT NULL,
  wallet_number VARCHAR(255) NOT NULL,
  transfer_date DATE NOT NULL,
  transfer_amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);

-- Create table for pulsa transactions
CREATE TABLE IF NOT EXISTS pulsa_transactions (
  id INT AUTO_INCREMENT,
  transaction_id INT NOT NULL,
  pulsa_provider VARCHAR(100) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  transfer_date DATE NOT NULL,
  transfer_amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);

-- Create trigger to update transaction status
DELIMITER $$
CREATE TRIGGER update_transaction_status
AFTER UPDATE ON bank_transfers
FOR EACH ROW
BEGIN
  IF NEW.transfer_amount > 0 THEN
    UPDATE transactions
    SET status = 'success'
    WHERE id = NEW.transaction_id;
  END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_e_wallet_status
AFTER UPDATE ON e_wallets
FOR EACH ROW
BEGIN
  IF NEW.transfer_amount > 0 THEN
    UPDATE transactions
    SET status = 'success'
    WHERE id = NEW.transaction_id;
  END IF;
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER update_pulsa_status
AFTER UPDATE ON pulsa_transactions
FOR EACH ROW
BEGIN
  IF NEW.transfer_amount > 0 THEN
    UPDATE transactions
    SET status = 'success'
    WHERE id = NEW.transaction_id;
  END IF;
END$$
DELIMITER ;
```
