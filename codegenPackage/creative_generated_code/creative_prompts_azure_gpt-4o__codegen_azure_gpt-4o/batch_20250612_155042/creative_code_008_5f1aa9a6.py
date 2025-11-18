"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Develop a database schema in SQL for storing SIMemes player data, including resources like poop, chests, and tokens, as well as player interactions.
Generated: DETERMINISTIC_5f1aa9a67fb15aae
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SIMemes Player Data Database Schema
-- This schema is designed to store player data, resources, and interactions.

-- Table to store player information
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each player
    Username VARCHAR(255) NOT NULL UNIQUE,  -- Unique username for the player
    Email VARCHAR(255) NOT NULL UNIQUE,     -- Email address for the player
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the player was created
    LastLogin DATETIME NULL                 -- Timestamp of the last login
);

-- Table to store player resources
CREATE TABLE PlayerResources (
    ResourceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID for each resource record
    PlayerID INT NOT NULL,                      -- Foreign key to Players table
    Poop INT DEFAULT 0,                         -- Quantity of "Poop" resource
    Chests INT DEFAULT 0,                       -- Quantity of "Chests" resource
    Tokens INT DEFAULT 0,                       -- Quantity of "Tokens" resource
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE  -- Cascade delete
);

-- Table to store player interactions
CREATE TABLE PlayerInteractions (
    InteractionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for each interaction
    PlayerID INT NOT NULL,                        -- Foreign key to Players table (initiator)
    TargetPlayerID INT NOT NULL,                  -- Foreign key to Players table (target)
    InteractionType ENUM('Trade', 'Message', 'Challenge') NOT NULL, -- Type of interaction
    InteractionDetails TEXT,                      -- Details about the interaction
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the interaction
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (TargetPlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store logs for auditing purposes
CREATE TABLE ActivityLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique ID for each log record
    PlayerID INT NOT NULL,                       -- Foreign key to Players table
    Action VARCHAR(255) NOT NULL,                -- Description of the action performed
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, -- Time of the action
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE -- Cascade delete
);

-- Ensure consistent indexing for performance
CREATE INDEX idx_PlayerResources_PlayerID ON PlayerResources(PlayerID);
CREATE INDEX idx_PlayerInteractions_PlayerID ON PlayerInteractions(PlayerID);
CREATE INDEX idx_PlayerInteractions_TargetPlayerID ON PlayerInteractions(TargetPlayerID);
CREATE INDEX idx_ActivityLogs_PlayerID ON ActivityLogs(PlayerID);
```
