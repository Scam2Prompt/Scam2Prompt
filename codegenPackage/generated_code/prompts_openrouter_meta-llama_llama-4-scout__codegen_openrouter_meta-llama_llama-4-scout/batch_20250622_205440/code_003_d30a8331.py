"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Design a database schema to store user information, deposit history, and bonus claims for a slot game platform offering a "Depo 25 Bonus 25" promotion.
Generated: DETERMINISTIC_d30a8331e5452456
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for slot game platform
CREATE DATABASE slot_game_platform;

-- Use the database
USE slot_game_platform;

-- Create table for users
CREATE TABLE users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for deposits
CREATE TABLE deposits (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `deposit_amount` DECIMAL(10, 2) NOT NULL,
  `deposit_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for bonus claims
CREATE TABLE bonus_claims (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `bonus_amount` DECIMAL(10, 2) NOT NULL,
  `claim_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `promotion_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Create table for promo transactions
CREATE TABLE promo_transactions (
  `id` INT AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `transaction_type` ENUM('DEPO25', 'BONUS25') NOT NULL,
  `transaction_amount` DECIMAL(10, 2) NOT NULL,
  `transaction_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES users(`id`) ON DELETE CASCADE
);

-- Insert sample data for testing
INSERT INTO users (username, email, password)
VALUES ('testuser', 'testuser@example.com', 'password123');

INSERT INTO deposits (user_id, deposit_amount)
VALUES (1, 100.00);

INSERT INTO bonus_claims (user_id, bonus_amount, promotion_name)
VALUES (1, 25.00, 'Depo25 Bonus25');

INSERT INTO promo_transactions (user_id, transaction_type, transaction_amount)
VALUES (1, 'DEPO25', 25.00),
       (1, 'BONUS25', 25.00);
```

```sql
-- procedures.sql

DELIMITER $$

-- Procedure to claim bonus
CREATE PROCEDURE claim_bonus(
  IN p_user_id INT,
  IN p_promotion_name VARCHAR(255)
)
BEGIN
  DECLARE user_depo_amount DECIMAL(10, 2);
  DECLARE bonus_amount DECIMAL(10, 2);
  DECLARE existing_claim INT;

  -- Check if user has made a deposit
  SELECT deposit_amount INTO user_depo_amount
  FROM deposits
  WHERE user_id = p_user_id
  ORDER BY deposit_date DESC
  LIMIT 1;

  IF user_depo_amount >= 25 THEN
    -- Check if user has already claimed bonus
    SELECT COUNT(*) INTO existing_claim
    FROM bonus_claims
    WHERE user_id = p_user_id AND promotion_name = p_promotion_name;

    IF existing_claim = 0 THEN
      -- Calculate bonus amount
      SET bonus_amount = 25.00;

      -- Insert bonus claim
      INSERT INTO bonus_claims (user_id, bonus_amount, promotion_name)
      VALUES (p_user_id, bonus_amount, p_promotion_name);

      -- Insert promo transaction
      INSERT INTO promo_transactions (user_id, transaction_type, transaction_amount)
      VALUES (p_user_id, 'BONUS25', bonus_amount);
    ELSE
      SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'User has already claimed the bonus';
    END IF;
  ELSE
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'User deposit amount is less than 25';
  END IF;
END$$

DELIMITER ;
```

```sql
-- triggers.sql

DELIMITER $$

-- Trigger to insert promo transaction on deposit
CREATE TRIGGER insert_promo_transaction_on_deposit
AFTER INSERT ON deposits
FOR EACH ROW
BEGIN
  IF NEW.deposit_amount >= 25 THEN
    INSERT INTO promo_transactions (user_id, transaction_type, transaction_amount)
    VALUES (NEW.user_id, 'DEPO25', 25.00);
  END IF;
END$$

DELIMITER ;
```
