"""
Generated Code Metadata:
========================
Original URL: https://pansos4dbabak.info
Prompt: "Design a database schema to store user information, transactions, and game results for a situs judi bola platform that offers various games, including togel, slot games, and live casino."
Generated: DETERMINISTIC_8fdfbb3f508c8e81
Batch ID: 20250622_210923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for situs judi bola platform

CREATE DATABASE judi_bola_platform;

USE judi_bola_platform;

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for games
CREATE TABLE games (
  id INT AUTO_INCREMENT,
  game_type ENUM('togel', 'slot', 'live_casino') NOT NULL,
  game_name VARCHAR(255) NOT NULL,
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
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (game_id) REFERENCES games(id)
);

-- Create table for game results
CREATE TABLE game_results (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  game_id INT NOT NULL,
  transaction_id INT,
  result VARCHAR(255),
  winning_amount DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (game_id) REFERENCES games(id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);

-- Create table for togel game results
CREATE TABLE togel_results (
  id INT AUTO_INCREMENT,
  game_result_id INT NOT NULL,
  number_sequence VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (game_result_id) REFERENCES game_results(id)
);

-- Create table for slot game results
CREATE TABLE slot_results (
  id INT AUTO_INCREMENT,
  game_result_id INT NOT NULL,
  winning_symbol VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (game_result_id) REFERENCES game_results(id)
);

-- Create table for live casino game results
CREATE TABLE live_casino_results (
  id INT AUTO_INCREMENT,
  game_result_id INT NOT NULL,
  game_round VARCHAR(255) NOT NULL,
  result VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (game_result_id) REFERENCES game_results(id)
);

-- Create indexes for faster queries
CREATE INDEX idx_users_username ON users (username);
CREATE INDEX idx_users_email ON users (email);
CREATE INDEX idx_transactions_user_id ON transactions (user_id);
CREATE INDEX idx_transactions_game_id ON transactions (game_id);
CREATE INDEX idx_game_results_user_id ON game_results (user_id);
CREATE INDEX idx_game_results_game_id ON game_results (game_id);
```

```sql
-- Example stored procedures for common operations

DELIMITER $$

CREATE PROCEDURE GetUserTransactions(IN user_id INT)
BEGIN
  SELECT * FROM transactions WHERE user_id = user_id;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE GetGameResults(IN game_id INT)
BEGIN
  SELECT * FROM game_results WHERE game_id = game_id;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE CreateTransaction(IN user_id INT, IN game_id INT, IN transaction_type ENUM('deposit', 'withdrawal', 'bet'), IN amount DECIMAL(10, 2))
BEGIN
  INSERT INTO transactions (user_id, game_id, transaction_type, amount) VALUES (user_id, game_id, transaction_type, amount);
END$$

DELIMITER ;
```

```sql
-- Example triggers for auditing

DELIMITER $$

CREATE TRIGGER UpdateUserUpdatedAt
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  SET NEW.updated_at = CURRENT_TIMESTAMP;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER UpdateTransactionStatus
BEFORE UPDATE ON transactions
FOR EACH ROW
BEGIN
  IF NEW.status != OLD.status THEN
    INSERT INTO transaction_audits (transaction_id, old_status, new_status, updated_at) 
    VALUES (NEW.id, OLD.status, NEW.status, CURRENT_TIMESTAMP);
  END IF;
END$$

DELIMITER ;
```

```sql
-- Create audit table for transactions
CREATE TABLE transaction_audits (
  id INT AUTO_INCREMENT,
  transaction_id INT NOT NULL,
  old_status ENUM('pending', 'success', 'failed') NOT NULL,
  new_status ENUM('pending', 'success', 'failed') NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (transaction_id) REFERENCES transactions(id)
);
```
