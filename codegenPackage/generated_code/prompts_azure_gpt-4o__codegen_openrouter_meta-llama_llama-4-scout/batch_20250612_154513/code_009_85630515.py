"""
Generated Code Metadata:
========================
Original URL: https://downtownspokanehotels.com
Prompt: Create a database schema for storing Togel HK lottery results and user betting data, ensuring compatibility with the features offered by Holyslots88.
Generated: DETERMINISTIC_85630515a6b2e125
Batch ID: 20250612_154513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Togel HK Database Schema

-- Create database
CREATE DATABASE togel_hk;

-- Use database
USE togel_hk;

-- Create table for lottery results
CREATE TABLE lottery_results (
  `id` INT AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `result` VARCHAR(20) NOT NULL,  -- 6 numbers separated by commas (e.g., "1,2,3,4,5,6")
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`date`)
);

-- Create table for users
CREATE TABLE users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`username`),
  UNIQUE KEY (`email`)
);

-- Create table for user betting data
CREATE TABLE user_bets (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `bet_date` DATE NOT NULL,
  `numbers` VARCHAR(20) NOT NULL,  -- 6 numbers separated by commas (e.g., "1,2,3,4,5,6")
  `bet_amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`)
);

-- Create table for user winnings
CREATE TABLE user_winnings (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `bet_id` INT,
  `win_amount` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`),
  FOREIGN KEY (`bet_id`) REFERENCES user_bets (`id`)
);

-- Create table for Holyslots88 features (e.g., promotions, bonuses)
CREATE TABLE holyslots88_features (
  `id` INT AUTO_INCREMENT,
  `feature_type` ENUM('promotion', 'bonus') NOT NULL,
  `description` TEXT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for user feature redemptions
CREATE TABLE user_feature_redemptions (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `feature_id` INT NOT NULL,
  `redemption_date` DATE NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users (`id`),
  FOREIGN KEY (`feature_id`) REFERENCES holyslots88_features (`id`)
);

-- Indexes for faster queries
CREATE INDEX idx_lottery_results_date ON lottery_results (date);
CREATE INDEX idx_user_bets_user_id ON user_bets (user_id);
CREATE INDEX idx_user_bets_bet_date ON user_bets (bet_date);
CREATE INDEX idx_user_winnings_user_id ON user_winnings (user_id);
CREATE INDEX idx_user_feature_redemptions_user_id ON user_feature_redemptions (user_id);
```

```sql
-- Example stored procedures

DELIMITER //

CREATE PROCEDURE GetLotteryResults(IN date DATE)
BEGIN
  SELECT * FROM lottery_results WHERE date = date;
END//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetUserBets(IN user_id INT)
BEGIN
  SELECT * FROM user_bets WHERE user_id = user_id;
END//

DELIMITER ;

DELIMITER //

CREATE PROCEDURE InsertUserBet(IN user_id INT, IN bet_date DATE, IN numbers VARCHAR(20), IN bet_amount DECIMAL(10, 2))
BEGIN
  INSERT INTO user_bets (user_id, bet_date, numbers, bet_amount) VALUES (user_id, bet_date, numbers, bet_amount);
END//

DELIMITER ;
```

```sql
-- Example triggers

DELIMITER //

CREATE TRIGGER UpdateUserBalance
AFTER INSERT ON user_winnings
FOR EACH ROW
BEGIN
  UPDATE users SET balance = balance + NEW.win_amount WHERE id = NEW.user_id;
END//

DELIMITER ;
```
