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
-- Database schema for storing SIMemes player data

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS PlayerInteractions;
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Resources;
DROP TABLE IF EXISTS Chests;
DROP TABLE IF EXISTS Tokens;

-- Table to store player information
CREATE TABLE Players (
    player_id SERIAL PRIMARY KEY, -- Unique identifier for each player
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the player
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of player creation
    last_login TIMESTAMP -- Timestamp of the last login
);

-- Table to store various resources for players
CREATE TABLE Resources (
    resource_id SERIAL PRIMARY KEY, -- Unique identifier for each resource entry
    player_id INT NOT NULL, -- Foreign key referencing Players
    resource_type VARCHAR(50) NOT NULL, -- Type of resource (e.g., 'poop', 'tokens')
    quantity INT NOT NULL DEFAULT 0, -- Quantity of the resource
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store chests owned by players
CREATE TABLE Chests (
    chest_id SERIAL PRIMARY KEY, -- Unique identifier for each chest
    player_id INT NOT NULL, -- Foreign key referencing Players
    chest_type VARCHAR(50) NOT NULL, -- Type of chest (e.g., 'gold', 'silver')
    opened BOOLEAN DEFAULT FALSE, -- Indicates if the chest has been opened
    opened_at TIMESTAMP, -- Timestamp of when the chest was opened
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store tokens for players
CREATE TABLE Tokens (
    token_id SERIAL PRIMARY KEY, -- Unique identifier for each token entry
    player_id INT NOT NULL, -- Foreign key referencing Players
    token_type VARCHAR(50) NOT NULL, -- Type of token (e.g., 'gold', 'silver')
    quantity INT NOT NULL DEFAULT 0, -- Quantity of the token
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store player interactions
CREATE TABLE PlayerInteractions (
    interaction_id SERIAL PRIMARY KEY, -- Unique identifier for each interaction
    player_id INT NOT NULL, -- Foreign key referencing Players
    interacted_with INT NOT NULL, -- ID of the player interacted with
    interaction_type VARCHAR(50) NOT NULL, -- Type of interaction (e.g., 'trade', 'battle')
    interaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the interaction
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (interacted_with) REFERENCES Players(player_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_player_username ON Players(username);
CREATE INDEX idx_resources_player ON Resources(player_id);
CREATE INDEX idx_chests_player ON Chests(player_id);
CREATE INDEX idx_tokens_player ON Tokens(player_id);
CREATE INDEX idx_interactions_player ON PlayerInteractions(player_id);
CREATE INDEX idx_interactions_with ON PlayerInteractions(interacted_with);
```
