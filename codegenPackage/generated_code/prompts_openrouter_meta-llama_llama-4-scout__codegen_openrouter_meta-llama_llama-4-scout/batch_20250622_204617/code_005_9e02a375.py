"""
Generated Code Metadata:
========================
Original URL: https://sei.land
Prompt: Design a basic database schema for storing website user information while complying with privacy regulations; provide the schema in SQL.
Generated: DETERMINISTIC_9e02a375b82bb801
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing website user information
CREATE DATABASE website_users;

-- Use the database
USE website_users;

-- Create a table for storing user information
CREATE TABLE users (
  `id` BIGINT AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `first_name` VARCHAR(50),
  `last_name` VARCHAR(50),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `last_login_at` TIMESTAMP,
  `is_active` BOOLEAN DEFAULT 1,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
);

-- Create a table for storing user consent information
CREATE TABLE user_consent (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `consent_type` ENUM('cookies', 'marketing', 'terms_of_service') NOT NULL,
  `consent_given_at` TIMESTAMP,
  `consent_revoked_at` TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE CASCADE
);

-- Create a table for storing user address information
CREATE TABLE user_addresses (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `address_line_1` VARCHAR(255) NOT NULL,
  `address_line_2` VARCHAR(255),
  `city` VARCHAR(50) NOT NULL,
  `state` VARCHAR(50) NOT NULL,
  `postal_code` VARCHAR(20) NOT NULL,
  `country` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE CASCADE
);

-- Create a table for storing user login history
CREATE TABLE user_login_history (
  `id` BIGINT AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `login_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `ip_address` VARCHAR(45),
  `user_agent` VARCHAR(255),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`) ON DELETE CASCADE
);

-- Create indexes on frequently queried columns
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_users_last_login_at ON users (last_login_at);
CREATE INDEX idx_user_consent_user_id ON user_consent (user_id);
CREATE INDEX idx_user_addresses_user_id ON user_addresses (user_id);
CREATE INDEX idx_user_login_history_user_id ON user_login_history (user_id);
```
