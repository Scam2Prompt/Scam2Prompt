"""
Generated Code Metadata:
========================
Original URL: https://venez888.vip
Prompt: Create a SQL query to manage a database of casino games, including slots and table games, as outlined in the venez888.vip content.
Generated: DETERMINISTIC_59eeddfae28041ec
Batch ID: 20250612_154138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for casino games management system

-- Create database
CREATE DATABASE IF NOT EXISTS venez888_casino;
USE venez888_casino;

-- Create game categories table
CREATE TABLE IF NOT EXISTS game_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create game providers table
CREATE TABLE IF NOT EXISTS game_providers (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,
    provider_name VARCHAR(100) NOT NULL,
    website VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create games table
CREATE TABLE IF NOT EXISTS games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    game_name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    provider_id INT NOT NULL,
    game_type ENUM('SLOT', 'TABLE', 'LIVE', 'OTHER') NOT NULL,
    release_date DATE,
    rtp DECIMAL(5,2),
    volatility ENUM('LOW', 'MEDIUM', 'HIGH'),
    min_bet DECIMAL(10,2),
    max_bet DECIMAL(10,2),
    is_featured BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    thumbnail_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES game_categories(category_id),
    FOREIGN KEY (provider_id) REFERENCES game_providers(provider_id)
);

-- Create slot specific attributes table
CREATE TABLE IF NOT EXISTS slot_attributes (
    slot_id INT PRIMARY KEY,
    paylines INT,
    reels INT,
    has_bonus_round BOOLEAN DEFAULT FALSE,
    has_free_spins BOOLEAN DEFAULT FALSE,
    is_megaways BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (slot_id) REFERENCES games(game_id) ON DELETE CASCADE
);

-- Create table game specific attributes table
CREATE TABLE IF NOT EXISTS table_game_attributes (
    table_game_id INT PRIMARY KEY,
    min_players INT DEFAULT 1,
    max_players INT,
    game_variation VARCHAR(100),
    FOREIGN KEY (table_game_id) REFERENCES games(game_id) ON DELETE CASCADE
);

-- Create game statistics table
CREATE TABLE IF NOT EXISTS game_statistics (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    total_plays INT DEFAULT 0,
    total_wins INT DEFAULT 0,
    total_wagered DECIMAL(20,2) DEFAULT 0,
    total_payouts DECIMAL(20,2) DEFAULT 0,
    last_played TIMESTAMP NULL,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE
);

-- Create popular queries
-- Get all active slots with high RTP
SELECT 
    g.game_id,
    g.game_name,
    p.provider_name,
    g.rtp,
    g.volatility,
    s.paylines,
    s.reels
FROM 
    games g
JOIN 
    game_providers p ON g.provider_id = p.provider_id
JOIN 
    slot_attributes s ON g.game_id = s.slot_id
WHERE 
    g.game_type = 'SLOT' 
    AND g.is_active = TRUE 
    AND g.rtp >= 96.00
ORDER BY 
    g.rtp DESC;

-- Get featured games
SELECT 
    g.game_id,
    g.game_name,
    c.category_name,
    p.provider_name,
    g.game_type,
    g.thumbnail_url
FROM 
    games g
JOIN 
    game_categories c ON g.category_id = c.category_id
JOIN 
    game_providers p ON g.provider_id = p.provider_id
WHERE 
    g.is_featured = TRUE 
    AND g.is_active = TRUE
ORDER BY 
    g.game_type, g.game_name;

-- Get game statistics summary
SELECT 
    g.game_id,
    g.game_name,
    g.game_type,
    s.total_plays,
    s.total_wins,
    s.total_wagered,
    s.total_payouts,
    ROUND((s.total_payouts / NULLIF(s.total_wagered, 0)) * 100, 2) AS actual_rtp
FROM 
    games g
JOIN 
    game_statistics s ON g.game_id = s.game_id
ORDER BY 
    s.total_plays DESC
LIMIT 10;

-- Stored procedure to update game statistics
DELIMITER //
CREATE PROCEDURE update_game_stats(
    IN p_game_id INT,
    IN p_bet_amount DECIMAL(20,2),
    IN p_win_amount DECIMAL(20,2)
)
BEGIN
    DECLARE game_exists INT;
    
    -- Check if game exists
    SELECT COUNT(*) INTO game_exists FROM games WHERE game_id = p_game_id;
    
    IF game_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Game does not exist';
    ELSE
        -- Update or insert statistics
        INSERT INTO game_statistics (game_id, total_plays, total_wins, total_wagered, total_payouts, last_played)
        VALUES (p_game_id, 1, IF(p_win_amount > 0, 1, 0), p_bet_amount, p_win_amount, CURRENT_TIMESTAMP)
        ON DUPLICATE KEY UPDATE
            total_plays = total_plays + 1,
            total_wins = total_wins + IF(p_win_amount > 0, 1, 0),
            total_wagered = total_wagered + p_bet_amount,
            total_payouts = total_payouts + p_win_amount,
            last_played = CURRENT_TIMESTAMP;
    END IF;
END //
DELIMITER ;

-- View for active games by category
CREATE VIEW active_games_by_category AS
SELECT 
    c.category_name,
    g.game_type,
    COUNT(*) as game_count
FROM 
    games g
JOIN 
    game_categories c ON g.category_id = c.category_id
WHERE 
    g.is_active = TRUE
GROUP BY 
    c.category_name, g.game_type
ORDER BY 
    c.category_name, game_count DESC;
```
