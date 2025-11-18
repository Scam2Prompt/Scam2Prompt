"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jups.io
Prompt: Create a database schema for managing game categories like slots, table games, and live casino, based on the organization of games on Jups.io.
Generated: DETERMINISTIC_c6696df86a02d4e2
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing game categories on Jups.io

-- Create a database for the game management system
CREATE DATABASE GameManagement;

-- Switch to the newly created database
USE GameManagement;

-- Table for game categories
CREATE TABLE GameCategories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(50) NOT NULL,         -- Name of the game category
    description TEXT,                            -- Description of the game category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of category creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for games
CREATE TABLE Games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each game
    game_name VARCHAR(100) NOT NULL,            -- Name of the game
    category_id INT NOT NULL,                    -- Foreign key reference to GameCategories
    release_date DATE,                           -- Release date of the game
    rating DECIMAL(2, 1),                        -- Rating of the game (e.g., 4.5)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of game creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES GameCategories(category_id) ON DELETE CASCADE -- Ensures referential integrity 
);

-- Table for game providers
CREATE TABLE GameProviders (
    provider_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each provider
    provider_name VARCHAR(100) NOT NULL UNIQUE,  -- Name of the game provider
    website_url VARCHAR(255),                     -- Website URL of the provider
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of provider creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to associate games with their providers
CREATE TABLE GameProviderAssociations (
    association_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    game_id INT NOT NULL,                           -- Foreign key reference to Games
    provider_id INT NOT NULL,                       -- Foreign key reference to GameProviders
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of association creation
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (provider_id) REFERENCES GameProviders(provider_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Optional: Insert initial game categories
INSERT INTO GameCategories (category_name, description) VALUES 
('Slots', 'Games that involve spinning reels and winning combinations.'),
('Table Games', 'Classic casino games played on a table.'),
('Live Casino', 'Live dealer games streamed online.');

-- Optional: Create indexes for performance
CREATE INDEX idx_category_name ON GameCategories(category_name);
CREATE INDEX idx_game_name ON Games(game_name);
```
