"""
Generated Code Metadata:
========================
Original URL: https://dadihonlineex.com
Prompt: Create a database schema to store transaction details for international and domestic remittances, inspired by the services offered by Dadih Online Exchange.
Generated: DETERMINISTIC_c767160e27fcc3c9
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- remittance_database_schema.sql

-- Create database
CREATE DATABASE remittance_db;

-- Use database
USE remittance_db;

-- Create table for countries
CREATE TABLE countries (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  code VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (code)
);

-- Create table for currencies
CREATE TABLE currencies (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  code VARCHAR(10) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (code)
);

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for sender accounts
CREATE TABLE sender_accounts (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  account_number VARCHAR(255) NOT NULL,
  account_type VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for recipient accounts
CREATE TABLE recipient_accounts (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  account_number VARCHAR(255) NOT NULL,
  account_type VARCHAR(50) NOT NULL,
  bank_name VARCHAR(255),
  bank_branch VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  sender_account_id INT NOT NULL,
  recipient_account_id INT NOT NULL,
  transaction_type ENUM('international', 'domestic') NOT NULL,
  currency_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  exchange_rate DECIMAL(10, 4) NOT NULL,
  transfer_fee DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (sender_account_id) REFERENCES sender_accounts(id) ON DELETE CASCADE,
  FOREIGN KEY (recipient_account_id) REFERENCES recipient_accounts(id) ON DELETE CASCADE,
  FOREIGN KEY (currency_id) REFERENCES currencies(id) ON DELETE RESTRICT
);

-- Create table for transaction history
CREATE TABLE transaction_history (
  id INT AUTO_INCREMENT,
  transaction_id INT NOT NULL,
  status ENUM('pending', 'success', 'failed') NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(id) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX idx_transactions_sender_account_id ON transactions(sender_account_id);
CREATE INDEX idx_transactions_recipient_account_id ON transactions(recipient_account_id);
CREATE INDEX idx_transactions_currency_id ON transactions(currency_id);
```

```sql
-- Example usage:
DELIMITER //
CREATE PROCEDURE add_transaction(
  IN p_sender_account_id INT,
  IN p_recipient_account_id INT,
  IN p_transaction_type ENUM('international', 'domestic'),
  IN p_currency_id INT,
  IN p_amount DECIMAL(10, 2),
  IN p_exchange_rate DECIMAL(10, 4),
  IN p_transfer_fee DECIMAL(10, 2)
)
BEGIN
  INSERT INTO transactions (
    sender_account_id,
    recipient_account_id,
    transaction_type,
    currency_id,
    amount,
    exchange_rate,
    transfer_fee
  ) VALUES (
    p_sender_account_id,
    p_recipient_account_id,
    p_transaction_type,
    p_currency_id,
    p_amount,
    p_exchange_rate,
    p_transfer_fee
  );
END//
DELIMITER ;
```

```sql
-- Insert example data:
INSERT INTO countries (name, code) VALUES ('United States', 'US');
INSERT INTO currencies (name, code) VALUES ('US Dollar', 'USD');
INSERT INTO users (first_name, last_name, email) VALUES ('John', 'Doe', 'john.doe@example.com');
INSERT INTO sender_accounts (user_id, account_number, account_type) VALUES (1, '1234567890', 'checking');
INSERT INTO recipient_accounts (first_name, last_name, account_number, account_type) VALUES ('Jane', 'Doe', '9876543210', 'savings');

CALL add_transaction(1, 1, 'domestic', 1, 100.00, 1.0000, 5.00);
```
