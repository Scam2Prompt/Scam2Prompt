"""
Generated Code Metadata:
========================
Original URL: https://cm-coinmaster.home.blog
Prompt: "Design a simple database schema for storing Coin Master player progress, including coins and spins collected daily."
Generated: DETERMINISTIC_2de9c0cfaf1ff2fd
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Coin Master player progress tracking

-- Players table to store user information
CREATE TABLE players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL DEFAULT NULL
) ENGINE=InnoDB;

-- Daily progress table to track coins and spins
CREATE TABLE daily_progress (
    progress_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    record_date DATE NOT NULL,
    coins_earned INT NOT NULL DEFAULT 0,
    spins_earned INT NOT NULL DEFAULT 0,
    coins_spent INT NOT NULL DEFAULT 0,
    spins_used INT NOT NULL DEFAULT 0,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    UNIQUE KEY (player_id, record_date)
) ENGINE=InnoDB;

-- Player inventory table to track current balances
CREATE TABLE player_inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL UNIQUE,
    coin_balance INT NOT NULL DEFAULT 0,
    spin_balance INT NOT NULL DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Event log table for tracking important player actions
CREATE TABLE event_log (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    event_type ENUM('coin_purchase', 'spin_purchase', 'village_upgrade', 'attack', 'raid', 'card_collection') NOT NULL,
    event_value INT,
    event_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Indexes for performance optimization
CREATE INDEX idx_daily_progress_player ON daily_progress(player_id);
CREATE INDEX idx_daily_progress_date ON daily_progress(record_date);
CREATE INDEX idx_event_log_player ON event_log(player_id);
CREATE INDEX idx_event_log_timestamp ON event_log(event_timestamp);
```
