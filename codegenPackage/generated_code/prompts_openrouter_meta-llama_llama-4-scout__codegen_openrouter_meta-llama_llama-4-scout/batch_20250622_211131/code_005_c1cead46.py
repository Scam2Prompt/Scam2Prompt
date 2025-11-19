"""
Generated Code Metadata:
========================
Original URL: https://a-brk.pages.dev
Prompt: Design a database schema to store Notcoin user data and airdrop claims efficiently.
Generated: DETERMINISTIC_c1cead460a0d7105
Batch ID: 20250622_211131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- notcoin_schema.sql

-- Create a database schema for Notcoin user data and airdrop claims

CREATE DATABASE notcoin;

USE notcoin;

-- Create a table to store user data
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT,
  wallet_address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (wallet_address)
) COMMENT 'Stores Notcoin user data';

-- Create a table to store airdrop claims
CREATE TABLE airdrop_claims (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  claim_amount DECIMAL(38, 0) NOT NULL,
  claimed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  transaction_hash VARCHAR(255) UNIQUE,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) COMMENT 'Stores Notcoin airdrop claims';

-- Create a table to store airdrop claim history
CREATE TABLE airdrop_claim_history (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  claim_amount DECIMAL(38, 0) NOT NULL,
  claimed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  transaction_hash VARCHAR(255) UNIQUE,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) COMMENT 'Stores historical Notcoin airdrop claims';

-- Create indexes for efficient querying
CREATE INDEX idx_users_wallet_address ON users(wallet_address);
CREATE INDEX idx_airdrop_claims_user_id ON airdrop_claims(user_id);
CREATE INDEX idx_airdrop_claim_history_user_id ON airdrop_claim_history(user_id);

-- Stored procedure to claim airdrop
DELIMITER //
CREATE PROCEDURE claim_airdrop(
  IN p_wallet_address VARCHAR(255),
  IN p_claim_amount DECIMAL(38, 0),
  IN p_transaction_hash VARCHAR(255)
)
BEGIN
  DECLARE user_id BIGINT;
  DECLARE existing_claim BIGINT;

  -- Get the user ID
  SELECT id INTO user_id FROM users WHERE wallet_address = p_wallet_address;

  -- Check if user exists
  IF user_id IS NULL THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User not found';
  END IF;

  -- Check if airdrop claim already exists
  SELECT COUNT(*) INTO existing_claim
  FROM airdrop_claims
  WHERE user_id = user_id AND transaction_hash = p_transaction_hash;

  IF existing_claim > 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Airdrop claim already exists';
  END IF;

  -- Insert airdrop claim
  INSERT INTO airdrop_claims (user_id, claim_amount, transaction_hash)
  VALUES (user_id, p_claim_amount, p_transaction_hash);

  -- Insert airdrop claim history
  INSERT INTO airdrop_claim_history (user_id, claim_amount, transaction_hash)
  VALUES (user_id, p_claim_amount, p_transaction_hash);
END//
DELIMITER ;

-- Example usage:
-- CALL claim_airdrop('0x1234567890', 1000, '0x9876543210');
```
