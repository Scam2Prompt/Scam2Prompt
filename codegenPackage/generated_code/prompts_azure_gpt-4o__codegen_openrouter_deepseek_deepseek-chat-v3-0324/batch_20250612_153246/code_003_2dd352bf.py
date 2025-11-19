"""
Generated Code Metadata:
========================
Original URL: https://diskonin.id
Prompt: Create a database schema to manage user accounts, transaction history, and game preferences for an online slot gaming platform like Maxslot88.
Generated: DETERMINISTIC_2dd352bfc1e34462
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for online slot gaming platform

-- Create the database
CREATE DATABASE IF NOT EXISTS slot_gaming_platform;
USE slot_gaming_platform;

-- Users table to store account information
CREATE TABLE users (
    user_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    salt VARCHAR(100) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    phone_number VARCHAR(20),
    country VARCHAR(50),
    currency VARCHAR(3) DEFAULT 'USD',
    balance DECIMAL(15, 2) DEFAULT 0.00,
    account_status ENUM('active', 'suspended', 'banned', 'pending') DEFAULT 'pending',
    verification_status ENUM('verified', 'unverified') DEFAULT 'unverified',
    last_login DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_account_status (account_status),
    INDEX idx_verification_status (verification_status)
) ENGINE=InnoDB;

-- User verification documents
CREATE TABLE user_verifications (
    verification_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    document_type ENUM('id_card', 'passport', 'driver_license', 'utility_bill') NOT NULL,
    document_number VARCHAR(50),
    document_front_url VARCHAR(255),
    document_back_url VARCHAR(255),
    selfie_url VARCHAR(255),
    verification_status ENUM('pending', 'approved', 'rejected') DEFAULT 'pending',
    reviewed_by BIGINT UNSIGNED,
    reviewed_at DATETIME,
    notes TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_verification_status (verification_status)
) ENGINE=InnoDB;

-- User sessions
CREATE TABLE user_sessions (
    session_id VARCHAR(255) PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    INDEX idx_expires_at (expires_at),
    INDEX idx_is_active (is_active)
) ENGINE=InnoDB;

-- Game providers
CREATE TABLE game_providers (
    provider_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Games catalog
CREATE TABLE games (
    game_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    provider_id INT UNSIGNED NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('slot', 'table', 'live', 'other') NOT NULL,
    thumbnail_url VARCHAR(255),
    game_url VARCHAR(255),
    min_bet DECIMAL(10, 2) DEFAULT 0.10,
    max_bet DECIMAL(10, 2) DEFAULT 100.00,
    rtp DECIMAL(5, 2) COMMENT 'Return to player percentage',
    volatility ENUM('low', 'medium', 'high') DEFAULT 'medium',
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (provider_id) REFERENCES game_providers(provider_id),
    INDEX idx_category (category),
    INDEX idx_is_active (is_active)
) ENGINE=InnoDB;

-- User game preferences
CREATE TABLE user_game_preferences (
    preference_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    game_id BIGINT UNSIGNED NOT NULL,
    favorite BOOLEAN DEFAULT FALSE,
    last_played DATETIME,
    play_count INT UNSIGNED DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    UNIQUE KEY unique_user_game (user_id, game_id),
    INDEX idx_favorite (favorite)
) ENGINE=InnoDB;

-- Transaction types
CREATE TABLE transaction_types (
    type_id TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    affects_balance BOOLEAN DEFAULT TRUE,
    is_deposit BOOLEAN DEFAULT FALSE,
    is_withdrawal BOOLEAN DEFAULT FALSE,
    is_bonus BOOLEAN DEFAULT FALSE
) ENGINE=InnoDB;

-- Transactions table
CREATE TABLE transactions (
    transaction_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    type_id TINYINT UNSIGNED NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    balance_before DECIMAL(15, 2) NOT NULL,
    balance_after DECIMAL(15, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    reference_id VARCHAR(100),
    status ENUM('pending', 'completed', 'failed', 'cancelled') DEFAULT 'pending',
    description TEXT,
    metadata JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (type_id) REFERENCES transaction_types(type_id),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at),
    INDEX idx_reference_id (reference_id)
) ENGINE=InnoDB;

-- Game sessions
CREATE TABLE game_sessions (
    session_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    game_id BIGINT UNSIGNED NOT NULL,
    start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    end_time DATETIME,
    initial_balance DECIMAL(15, 2) NOT NULL,
    final_balance DECIMAL(15, 2),
    total_bet DECIMAL(15, 2) DEFAULT 0.00,
    total_win DECIMAL(15, 2) DEFAULT 0.00,
    session_duration INT UNSIGNED COMMENT 'Duration in seconds',
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    INDEX idx_start_time (start_time),
    INDEX idx_user_game (user_id, game_id)
) ENGINE=InnoDB;

-- Game rounds (individual spins/bets)
CREATE TABLE game_rounds (
    round_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    session_id BIGINT UNSIGNED NOT NULL,
    transaction_id BIGINT UNSIGNED,
    round_number INT UNSIGNED NOT NULL,
    bet_amount DECIMAL(15, 2) NOT NULL,
    win_amount DECIMAL(15, 2) DEFAULT 0.00,
    result_data JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES game_sessions(session_id) ON DELETE CASCADE,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id) ON DELETE SET NULL,
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB;

-- Bonuses and promotions
CREATE TABLE bonuses (
    bonus_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    bonus_type ENUM('deposit', 'signup', 'loyalty', 'promo') NOT NULL,
    amount DECIMAL(15, 2),
    percentage DECIMAL(5, 2),
    min_deposit DECIMAL(15, 2),
    max_bonus DECIMAL(15, 2),
    wagering_requirement DECIMAL(5, 2) COMMENT 'Multiplier for wagering requirement',
    valid_from DATETIME,
    valid_to DATETIME,
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_validity (valid_from, valid_to),
    INDEX idx_is_active (is_active)
) ENGINE=InnoDB;

-- User bonuses
CREATE TABLE user_bonuses (
    user_bonus_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    bonus_id BIGINT UNSIGNED NOT NULL,
