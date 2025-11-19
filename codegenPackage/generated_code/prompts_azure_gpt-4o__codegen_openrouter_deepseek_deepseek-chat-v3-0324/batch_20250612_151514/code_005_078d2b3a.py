"""
Generated Code Metadata:
========================
Original URL: https://bolehshop.id
Prompt: Create a database schema in SQL for managing lottery game results, user accounts, and payment transactions, inspired by the HONGTOGEL platform.
Generated: DETERMINISTIC_078d2b3a960e1199
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for lottery management system
CREATE DATABASE IF NOT EXISTS lottery_management;
USE lottery_management;

-- User account table
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    phone_number VARCHAR(20),
    date_of_birth DATE,
    address TEXT,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    account_status ENUM('active', 'suspended', 'banned') DEFAULT 'active',
    verification_status ENUM('verified', 'unverified') DEFAULT 'unverified',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    INDEX idx_email (email),
    INDEX idx_username (username)
) ENGINE=InnoDB;

-- Lottery game types
CREATE TABLE game_types (
    game_type_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    draw_frequency ENUM('daily', 'weekly', 'monthly') NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Lottery draws
CREATE TABLE draws (
    draw_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    game_type_id INT NOT NULL,
    draw_date DATE NOT NULL,
    draw_time TIME NOT NULL,
    status ENUM('pending', 'completed', 'cancelled') DEFAULT 'pending',
    winning_numbers VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (game_type_id) REFERENCES game_types(game_type_id),
    INDEX idx_draw_date (draw_date),
    INDEX idx_game_type (game_type_id)
) ENGINE=InnoDB;

-- User tickets
CREATE TABLE tickets (
    ticket_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    draw_id BIGINT NOT NULL,
    numbers_played VARCHAR(100) NOT NULL,
    bet_amount DECIMAL(10, 2) NOT NULL,
    ticket_status ENUM('pending', 'won', 'lost', 'cancelled') DEFAULT 'pending',
    win_amount DECIMAL(15, 2) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (draw_id) REFERENCES draws(draw_id),
    INDEX idx_user_tickets (user_id),
    INDEX idx_draw_tickets (draw_id)
) ENGINE=InnoDB;

-- Prize tiers for each game type
CREATE TABLE prize_tiers (
    prize_tier_id INT PRIMARY KEY AUTO_INCREMENT,
    game_type_id INT NOT NULL,
    match_count INT NOT NULL,
    prize_amount DECIMAL(15, 2) NOT NULL,
    prize_description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (game_type_id) REFERENCES game_types(game_type_id),
    UNIQUE KEY uk_game_match (game_type_id, match_count)
) ENGINE=InnoDB;

-- Winning tickets
CREATE TABLE winning_tickets (
    winning_ticket_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    ticket_id BIGINT NOT NULL,
    prize_tier_id INT NOT NULL,
    claimed BOOLEAN DEFAULT FALSE,
    claimed_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id),
    FOREIGN KEY (prize_tier_id) REFERENCES prize_tiers(prize_tier_id),
    INDEX idx_ticket_win (ticket_id)
) ENGINE=InnoDB;

-- Payment methods
CREATE TABLE payment_methods (
    payment_method_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Transactions
CREATE TABLE transactions (
    transaction_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    payment_method_id INT,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_type ENUM('deposit', 'withdrawal', 'bet', 'win') NOT NULL,
    status ENUM('pending', 'completed', 'failed', 'cancelled') DEFAULT 'pending',
    reference_id VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(payment_method_id),
    INDEX idx_user_transactions (user_id),
    INDEX idx_transaction_type (transaction_type)
) ENGINE=InnoDB;

-- User sessions
CREATE TABLE user_sessions (
    session_id VARCHAR(255) PRIMARY KEY,
    user_id BIGINT NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    INDEX idx_user_sessions (user_id)
) ENGINE=InnoDB;

-- Audit log for important actions
CREATE TABLE audit_log (
    log_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT,
    action_type VARCHAR(50) NOT NULL,
    table_affected VARCHAR(50),
    record_id BIGINT,
    old_values TEXT,
    new_values TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    INDEX idx_audit_user (user_id),
    INDEX idx_audit_action (action_type)
) ENGINE=InnoDB;

-- System settings
CREATE TABLE system_settings (
    setting_id INT PRIMARY KEY AUTO_INCREMENT,
    setting_key VARCHAR(50) NOT NULL UNIQUE,
    setting_value TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;
```
