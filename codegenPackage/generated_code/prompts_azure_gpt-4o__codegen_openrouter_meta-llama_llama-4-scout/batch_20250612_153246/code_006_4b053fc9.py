"""
Generated Code Metadata:
========================
Original URL: https://blogdotrabalhadordigital.com
Prompt: Create a database schema for managing user accounts, game statistics, and bonus claims for an online gaming platform similar to Pelangi189.
Generated: DETERMINISTIC_4b053fc91ad4d9d0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the online gaming platform
CREATE DATABASE pelangi189;

-- Use the created database
USE pelangi189;

-- Create a table for user accounts
CREATE TABLE users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
);

-- Create a table for game statistics
CREATE TABLE game_statistics (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `game_name` VARCHAR(100) NOT NULL,
  `wins` INT DEFAULT 0,
  `losses` INT DEFAULT 0,
  `draws` INT DEFAULT 0,
  `total_games` INT DEFAULT 0,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create a table for bonus claims
CREATE TABLE bonus_claims (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `bonus_type` ENUM('signup', 'deposit', 'referral') NOT NULL,
  `claim_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `status` ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create a table for user login history
CREATE TABLE user_login_history (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `login_date` DATE NOT NULL,
  `login_time` TIME NOT NULL,
  `ip_address` VARCHAR(50) NOT NULL,
  `device_info` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create a table for game transactions
CREATE TABLE game_transactions (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `game_name` VARCHAR(100) NOT NULL,
  `transaction_date` DATE NOT NULL,
  `amount` DECIMAL(10, 2) NOT NULL,
  `transaction_type` ENUM('bet', 'win', 'refund') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_game_statistics_user_id ON game_statistics (user_id);
CREATE INDEX idx_bonus_claims_user_id ON bonus_claims (user_id);
CREATE INDEX idx_user_login_history_user_id ON user_login_history (user_id);
CREATE INDEX idx_game_transactions_user_id ON game_transactions (user_id);
```

```sql
-- Sample stored procedure for inserting a new user
DELIMITER //
CREATE PROCEDURE sp_insert_user(
  IN p_username VARCHAR(50),
  IN p_email VARCHAR(100),
  IN p_password VARCHAR(255)
)
BEGIN
  INSERT INTO users (username, email, password)
  VALUES (p_username, p_email, p_password);
END//
DELIMITER ;

-- Sample stored procedure for updating game statistics
DELIMITER //
CREATE PROCEDURE sp_update_game_statistics(
  IN p_user_id INT,
  IN p_game_name VARCHAR(100),
  IN p_wins INT,
  IN p_losses INT,
  IN p_draws INT,
  IN p_total_games INT
)
BEGIN
  UPDATE game_statistics
  SET wins = p_wins, losses = p_losses, draws = p_draws, total_games = p_total_games
  WHERE user_id = p_user_id AND game_name = p_game_name;
END//
DELIMITER ;
```

```sql
-- Sample trigger for updating updated_at timestamp
DELIMITER //
CREATE TRIGGER tr_update_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;
```
