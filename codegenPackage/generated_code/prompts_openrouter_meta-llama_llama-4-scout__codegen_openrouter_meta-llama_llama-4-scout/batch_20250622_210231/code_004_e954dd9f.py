"""
Generated Code Metadata:
========================
Original URL: https://missions3nyanheroescom.pages.dev
Prompt: Design a basic database schema for storing user missions, referrals, and $NYAN rewards on a platform like Nyan Heroes.
Generated: DETERMINISTIC_e954dd9f66f04442
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- nyan_heroes_schema.sql

-- Create database schema for Nyan Heroes platform
CREATE DATABASE nyan_heroes;

-- Use the nyan_heroes database
USE nyan_heroes;

-- Create table for users
CREATE TABLE users (
  id BIGINT AUTO_INCREMENT,
  wallet_address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (wallet_address)
);

-- Create table for user missions
CREATE TABLE user_missions (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  mission_id INT NOT NULL,
  completed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for referrals
CREATE TABLE referrals (
  id BIGINT AUTO_INCREMENT,
  referrer_id BIGINT NOT NULL,
  referred_id BIGINT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (referrer_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (referred_id) REFERENCES users(id) ON DELETE CASCADE,
  UNIQUE KEY (referrer_id, referred_id)
);

-- Create table for $NYAN rewards
CREATE TABLE nyan_rewards (
  id BIGINT AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  reward_amount DECIMAL(38, 18) NOT NULL,
  reward_type ENUM('mission', 'referral') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Create table for missions
CREATE TABLE missions (
  id INT AUTO_INCREMENT,
  mission_name VARCHAR(255) NOT NULL,
  mission_description TEXT,
  reward_amount DECIMAL(38, 18) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create index on user_id in user_missions table
CREATE INDEX idx_user_id ON user_missions(user_id);

-- Create index on referrer_id and referred_id in referrals table
CREATE INDEX idx_referrer_id ON referrals(referrer_id);
CREATE INDEX idx_referred_id ON referrals(referred_id);

-- Create index on user_id in nyan_rewards table
CREATE INDEX idx_user_id ON nyan_rewards(user_id);
```

```sql
-- Example usage:

-- Insert a new user
INSERT INTO users (wallet_address) VALUES ('0x1234567890');

-- Insert a new mission
INSERT INTO missions (mission_name, mission_description, reward_amount) 
VALUES ('Mission 1', 'Complete task 1', 100.00);

-- Assign a mission to a user
INSERT INTO user_missions (user_id, mission_id) 
VALUES (1, 1);

-- Mark mission as completed
UPDATE user_missions SET completed = TRUE WHERE id = 1;

-- Insert a referral
INSERT INTO referrals (referrer_id, referred_id) 
VALUES (1, 2);

-- Give $NYAN reward to a user
INSERT INTO nyan_rewards (user_id, reward_amount, reward_type) 
VALUES (1, 50.00, 'mission');
```
