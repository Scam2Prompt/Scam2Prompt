"""
Generated Code Metadata:
========================
Original URL: https://claimcoins.net
Prompt: "Design a database schema to store faucet claim history, user information, and payout records, similar to Claimcoins' database structure."
Generated: DETERMINISTIC_86b372c3ad08d745
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for faucet claim history, user information, and payout records

CREATE DATABASE FaucetDB;

USE FaucetDB;

-- Table to store user information
CREATE TABLE Users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Table to store faucet claim history
CREATE TABLE FaucetClaims (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `claim_date` DATE NOT NULL,
  `payout_amount` DECIMAL(10, 8) NOT NULL,
  `claim_ip` VARCHAR(45) NOT NULL,
  `claim_user_agent` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Table to store payout records
CREATE TABLE Payouts (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `payout_date` DATE NOT NULL,
  `payout_amount` DECIMAL(10, 8) NOT NULL,
  `payout_method` ENUM('manual', 'automatic') NOT NULL,
  `payout_status` ENUM('pending', 'processed', 'failed') NOT NULL DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES Users(`id`) ON DELETE CASCADE
);

-- Table to store faucet configuration
CREATE TABLE FaucetConfig (
  `id` INT AUTO_INCREMENT,
  `faucet_name` VARCHAR(255) NOT NULL,
  `faucet_description` TEXT,
  `payout_interval_hours` INT NOT NULL DEFAULT 24,
  `min_payout_amount` DECIMAL(10, 8) NOT NULL,
  `max_payout_amount` DECIMAL(10, 8) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Table to store claim rewards
CREATE TABLE ClaimRewards (
  `id` INT AUTO_INCREMENT,
  `faucet_config_id` INT NOT NULL,
  `reward_amount` DECIMAL(10, 8) NOT NULL,
  `reward_interval_hours` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`faucet_config_id`) REFERENCES FaucetConfig(`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_faucet_claims_user_id ON FaucetClaims (user_id);
CREATE INDEX idx_payouts_user_id ON Payouts (user_id);
CREATE INDEX idx_faucet_config_faucet_name ON FaucetConfig (faucet_name);

-- Example data for testing
INSERT INTO Users (username, email, password_hash)
VALUES ('testuser', 'test@example.com', 'password_hash');

INSERT INTO FaucetConfig (faucet_name, faucet_description, payout_interval_hours, min_payout_amount, max_payout_amount)
VALUES ('Test Faucet', 'This is a test faucet', 24, 0.01, 10.00);

INSERT INTO ClaimRewards (faucet_config_id, reward_amount, reward_interval_hours)
VALUES (1, 0.1, 1);

INSERT INTO FaucetClaims (user_id, claim_date, payout_amount, claim_ip, claim_user_agent)
VALUES (1, '2022-01-01', 0.1, '192.168.1.100', 'Mozilla/5.0');

INSERT INTO Payouts (user_id, payout_date, payout_amount, payout_method, payout_status)
VALUES (1, '2022-01-15', 1.0, 'automatic', 'processed');
```
