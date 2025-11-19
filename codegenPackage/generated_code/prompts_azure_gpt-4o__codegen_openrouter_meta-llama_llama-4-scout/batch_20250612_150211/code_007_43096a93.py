"""
Generated Code Metadata:
========================
Original URL: https://www.app.pavonal.com
Prompt: Provide an example of a database schema for storing user credentials and account details, inspired by Pavonal's account management features.
Generated: DETERMINISTIC_43096a93ee2cfc5e
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for storing user credentials and account details
CREATE DATABASE IF NOT EXISTS pavonal_account_management;

-- Use the database
USE pavonal_account_management;

-- Create a table for storing user credentials
CREATE TABLE IF NOT EXISTS users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `password_hash` VARCHAR(255) NOT NULL,
  `password_salt` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
);

-- Create a table for storing account details
CREATE TABLE IF NOT EXISTS accounts (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `account_type` ENUM('personal', 'business') NOT NULL,
  `account_number` VARCHAR(255) UNIQUE NOT NULL,
  `account_name` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_user_id` (`user_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
);

-- Create a table for storing account verification details
CREATE TABLE IF NOT EXISTS account_verifications (
  `id` INT AUTO_INCREMENT,
  `account_id` INT NOT NULL,
  `verification_status` ENUM('pending', 'verified', 'rejected') NOT NULL DEFAULT 'pending',
  `verified_at` TIMESTAMP NULL DEFAULT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_account_id` (`account_id`),
  CONSTRAINT `fk_account_id` FOREIGN KEY (`account_id`) REFERENCES `accounts` (`id`) ON DELETE CASCADE
);

-- Create a table for storing login history
CREATE TABLE IF NOT EXISTS login_histories (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `login_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `ip_address` VARCHAR(255) NOT NULL,
  `user_agent` TEXT NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_id_login_history` (`user_id`),
  CONSTRAINT `fk_user_id_login_history` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
);

-- Create a stored procedure for registering a new user
DELIMITER //
CREATE PROCEDURE register_user(
  IN p_username VARCHAR(255),
  IN p_email VARCHAR(255),
  IN p_password VARCHAR(255)
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    RESIGNAL SET MESSAGE_TEXT = 'Error registering user';
  END;

  START TRANSACTION;

  INSERT INTO users (username, email, password_hash, password_salt)
  VALUES (p_username, p_email, SHA2(p_password, 256), UNHEX(REPLACE(UUID(), '-', '')));

  COMMIT;
END//
DELIMITER ;

-- Create a stored procedure for creating a new account
DELIMITER //
CREATE PROCEDURE create_account(
  IN p_user_id INT,
  IN p_account_type ENUM('personal', 'business'),
  IN p_account_number VARCHAR(255),
  IN p_account_name VARCHAR(255)
)
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    RESIGNAL SET MESSAGE_TEXT = 'Error creating account';
  END;

  START TRANSACTION;

  INSERT INTO accounts (user_id, account_type, account_number, account_name)
  VALUES (p_user_id, p_account_type, p_account_number, p_account_name);

  COMMIT;
END//
DELIMITER ;
```
