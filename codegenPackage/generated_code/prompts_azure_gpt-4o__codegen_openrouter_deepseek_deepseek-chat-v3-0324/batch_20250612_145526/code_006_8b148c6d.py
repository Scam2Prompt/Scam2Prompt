"""
Generated Code Metadata:
========================
Original URL: https://aspjj.com
Prompt: "Create a database schema for managing slot game data, including game titles, RTP rates, and user bets, as described on สล็อตเว็บตรง."
Generated: DETERMINISTIC_8b148c6dfd89e436
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing slot game data

-- Create the database
CREATE DATABASE IF NOT EXISTS slot_games_db;
USE slot_games_db;

-- Users table to store player information
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_balance CHECK (balance >= 0)
) ENGINE=InnoDB;

-- Game providers table
CREATE TABLE IF NOT EXISTS providers (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Games table
CREATE TABLE IF NOT EXISTS games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    provider_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    rtp DECIMAL(5, 2) NOT NULL COMMENT 'Return to Player percentage',
    volatility ENUM('Low', 'Medium', 'High') NOT NULL,
    min_bet DECIMAL(10, 2) NOT NULL,
    max_bet DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    release_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (provider_id) REFERENCES providers(provider_id),
    CONSTRAINT chk_rtp CHECK (rtp BETWEEN 0 AND 100),
    CONSTRAINT chk_bet_range CHECK (min_bet > 0 AND max_bet >= min_bet)
) ENGINE=InnoDB;

-- Game categories table
CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- Game to category mapping
CREATE TABLE IF NOT EXISTS game_categories (
    game_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (game_id, category_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Game features table
CREATE TABLE IF NOT EXISTS features (
    feature_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

-- Game to features mapping
CREATE TABLE IF NOT EXISTS game_features (
    game_id INT NOT NULL,
    feature_id INT NOT NULL,
    PRIMARY KEY (game_id, feature_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES features(feature_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- User bets table
CREATE TABLE IF NOT EXISTS bets (
    bet_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    game_id INT NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    win_amount DECIMAL(15, 2) DEFAULT 0.00,
    bet_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    result_time TIMESTAMP NULL,
    status ENUM('Pending', 'Won', 'Lost', 'Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    CONSTRAINT chk_amount CHECK (amount > 0),
    CONSTRAINT chk_win_amount CHECK (win_amount >= 0)
) ENGINE=InnoDB;

-- Transaction history table
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_type ENUM('Deposit', 'Withdrawal', 'Win', 'Bet', 'Bonus') NOT NULL,
    reference_id BIGINT NULL COMMENT 'Reference to bet_id or other relevant ID',
    status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',
    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
) ENGINE=InnoDB;

-- Game sessions table
CREATE TABLE IF NOT EXISTS game_sessions (
    session_id VARCHAR(64) PRIMARY KEY,
    user_id INT NOT NULL,
    game_id INT NOT NULL,
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP NULL,
    total_bets DECIMAL(15, 2) DEFAULT 0.00,
    total_wins DECIMAL(15, 2) DEFAULT 0.00,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id)
) ENGINE=InnoDB;

-- Game statistics table
CREATE TABLE IF NOT EXISTS game_statistics (
    stat_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    date DATE NOT NULL,
    total_bets INT DEFAULT 0,
    total_amount_bet DECIMAL(20, 2) DEFAULT 0.00,
    total_wins DECIMAL(20, 2) DEFAULT 0.00,
    unique_players INT DEFAULT 0,
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    UNIQUE KEY (game_id, date)
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_bets_user_id ON bets(user_id);
CREATE INDEX idx_bets_game_id ON bets(game_id);
CREATE INDEX idx_bets_status ON bets(status);
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_type_status ON transactions(transaction_type, status);
CREATE INDEX idx_game_sessions_user_id ON game_sessions(user_id);
```
