"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Develop a database schema in SQL for storing SIMemes player data, including resources like poop, chests, and tokens, as well as player interactions.
Generated: DETERMINISTIC_5f1aa9a67fb15aae
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SIMemes game player data

-- Create the database
CREATE DATABASE IF NOT EXISTS simemes_db;
USE simemes_db;

-- Players table
CREATE TABLE IF NOT EXISTS players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_username_length CHECK (CHAR_LENGTH(username) >= 3)
) ENGINE=InnoDB;

-- Player resources
CREATE TABLE IF NOT EXISTS player_resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    poop_amount INT DEFAULT 0,
    chests_amount INT DEFAULT 0,
    tokens_amount INT DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    CONSTRAINT chk_non_negative_resources CHECK (
        poop_amount >= 0 AND 
        chests_amount >= 0 AND 
        tokens_amount >= 0
    )
) ENGINE=InnoDB;

-- Player interactions
CREATE TABLE IF NOT EXISTS player_interactions (
    interaction_id INT AUTO_INCREMENT PRIMARY KEY,
    from_player_id INT NOT NULL,
    to_player_id INT NOT NULL,
    interaction_type ENUM('gift', 'trade', 'attack', 'message') NOT NULL,
    resource_type ENUM('poop', 'chest', 'token') NULL,
    amount INT NULL,
    interaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_player_id) REFERENCES players(player_id),
    FOREIGN KEY (to_player_id) REFERENCES players(player_id),
    CONSTRAINT chk_non_negative_amount CHECK (amount IS NULL OR amount >= 0),
    CONSTRAINT chk_not_self_interaction CHECK (from_player_id != to_player_id)
) ENGINE=InnoDB;

-- Player inventory items
CREATE TABLE IF NOT EXISTS player_inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT DEFAULT 1,
    acquired_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    CONSTRAINT chk_positive_quantity CHECK (quantity > 0)
) ENGINE=InnoDB;

-- Player achievements
CREATE TABLE IF NOT EXISTS player_achievements (
    achievement_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    achievement_name VARCHAR(100) NOT NULL,
    achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    progress INT DEFAULT 100,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    CONSTRAINT chk_valid_progress CHECK (progress BETWEEN 0 AND 100)
) ENGINE=InnoDB;

-- Player sessions
CREATE TABLE IF NOT EXISTS player_sessions (
    session_id VARCHAR(255) PRIMARY KEY,
    player_id INT NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_player_resources_player ON player_resources(player_id);
CREATE INDEX idx_interactions_from ON player_interactions(from_player_id);
CREATE INDEX idx_interactions_to ON player_interactions(to_player_id);
CREATE INDEX idx_inventory_player ON player_inventory(player_id);
CREATE INDEX idx_achievements_player ON player_achievements(player_id);
CREATE INDEX idx_sessions_player ON player_sessions(player_id);
CREATE INDEX idx_sessions_expiry ON player_sessions(expires_at);
```
