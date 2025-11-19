"""
Generated Code Metadata:
========================
Original URL: https://optionroom.finance
Prompt: "Design a basic database schema for managing user accounts, games, and transactions for an online betting platform like HUBET."
Generated: DETERMINISTIC_6f66424a58ed13f0
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for online betting platform
CREATE DATABASE hubet;

-- Use the database
USE hubet;

-- Create table for user accounts
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  balance DECIMAL(10, 2) DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for games
CREATE TABLE games (
  id INT AUTO_INCREMENT,
  game_name VARCHAR(100) NOT NULL,
  game_type ENUM('sports', 'casino', 'lottery') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  transaction_type ENUM('deposit', 'withdrawal', 'bet') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'success', 'failed') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
);

-- Create table for bets
CREATE TABLE bets (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  bet_amount DECIMAL(10, 2) NOT NULL,
  bet_details JSON,
  odds DECIMAL(5, 2) NOT NULL,
  status ENUM('pending', 'won', 'lost') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE
);

-- Create index on user_id and game_id for transactions and bets
CREATE INDEX idx_user_id ON transactions (user_id);
CREATE INDEX idx_game_id ON transactions (game_id);
CREATE INDEX idx_user_id_bets ON bets (user_id);
CREATE INDEX idx_game_id_bets ON bets (game_id);
```

```sql
-- procedures.sql

DELIMITER $$

-- Procedure to deposit funds into a user's account
CREATE PROCEDURE deposit_funds(IN user_id INT, IN amount DECIMAL(10, 2))
BEGIN
  IF amount <= 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid deposit amount';
  END IF;

  UPDATE users
  SET balance = balance + amount
  WHERE id = user_id;

  INSERT INTO transactions (user_id, game_id, transaction_type, amount, status)
  VALUES (user_id, NULL, 'deposit', amount, 'success');
END$$

-- Procedure to withdraw funds from a user's account
CREATE PROCEDURE withdraw_funds(IN user_id INT, IN amount DECIMAL(10, 2))
BEGIN
  IF amount <= 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid withdrawal amount';
  END IF;

  IF (SELECT balance FROM users WHERE id = user_id) < amount THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient balance';
  END IF;

  UPDATE users
  SET balance = balance - amount
  WHERE id = user_id;

  INSERT INTO transactions (user_id, game_id, transaction_type, amount, status)
  VALUES (user_id, NULL, 'withdrawal', amount, 'success');
END$$

-- Procedure to place a bet
CREATE PROCEDURE place_bet(IN user_id INT, IN game_id INT, IN bet_amount DECIMAL(10, 2), IN bet_details JSON, IN odds DECIMAL(5, 2))
BEGIN
  IF bet_amount <= 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid bet amount';
  END IF;

  IF (SELECT balance FROM users WHERE id = user_id) < bet_amount THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient balance';
  END IF;

  INSERT INTO bets (user_id, game_id, bet_amount, bet_details, odds)
  VALUES (user_id, game_id, bet_amount, bet_details, odds);

  UPDATE users
  SET balance = balance - bet_amount
  WHERE id = user_id;

  INSERT INTO transactions (user_id, game_id, transaction_type, amount, status)
  VALUES (user_id, game_id, 'bet', bet_amount, 'pending');
END$$

DELIMITER ;
```

```sql
-- triggers.sql

DELIMITER $$

-- Trigger to update user's balance after a bet is resolved
CREATE TRIGGER update_balance_after_bet
AFTER UPDATE ON bets
FOR EACH ROW
BEGIN
  IF NEW.status = 'won' THEN
    UPDATE users
    SET balance = balance + NEW.bet_amount * NEW.odds
    WHERE id = NEW.user_id;
  ELSEIF NEW.status = 'lost' THEN
    -- No action needed, bet amount already deducted
  END IF;
END$$

-- Trigger to update transaction status after a bet is resolved
CREATE TRIGGER update_transaction_status_after_bet
AFTER UPDATE ON bets
FOR EACH ROW
BEGIN
  IF NEW.status != OLD.status THEN
    UPDATE transactions
    SET status = CASE
      WHEN NEW.status = 'won' THEN 'success'
      WHEN NEW.status = 'lost' THEN 'failed'
      ELSE status
    END
    WHERE user_id = NEW.user_id AND game_id = NEW.game_id AND transaction_type = 'bet';
  END IF;
END$$

DELIMITER ;
```
