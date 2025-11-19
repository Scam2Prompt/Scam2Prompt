"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Design a database schema to store player progress and inventory in a game like Big Time, with features like workshops, armory, and collectibles.
Generated: DETERMINISTIC_6564e09525e51336
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing player progress and inventory in a game

-- Table to store player information
CREATE TABLE Players (
    PlayerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each player
    Username VARCHAR(50) NOT NULL UNIQUE,    -- Player's username
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Player's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    LastLogin TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last login timestamp
);

-- Table to store player progress
CREATE TABLE PlayerProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for progress entry
    PlayerID INT NOT NULL,                     -- Foreign key to Players table
    Level INT NOT NULL,                        -- Current level of the player
    ExperiencePoints INT NOT NULL,             -- Total experience points earned
    WorkshopLevel INT NOT NULL,                -- Level of the player's workshop
    ArmoryLevel INT NOT NULL,                  -- Level of the player's armory
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE -- Cascade delete on player removal
);

-- Table to store player inventory
CREATE TABLE PlayerInventory (
    InventoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for inventory entry
    PlayerID INT NOT NULL,                      -- Foreign key to Players table
    ItemID INT NOT NULL,                        -- Foreign key to Items table
    Quantity INT NOT NULL,                      -- Quantity of the item in inventory
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE, -- Cascade delete on player removal
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID) ON DELETE CASCADE -- Cascade delete on item removal
);

-- Table to store items available in the game
CREATE TABLE Items (
    ItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each item
    ItemName VARCHAR(100) NOT NULL,        -- Name of the item
    ItemType ENUM('Collectible', 'Weapon', 'Armor', 'Resource') NOT NULL, -- Type of the item
    Rarity ENUM('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary') NOT NULL, -- Rarity of the item
    Description TEXT                       -- Description of the item
);

-- Table to store collectibles
CREATE TABLE Collectibles (
    CollectibleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each collectible
    PlayerID INT NOT NULL,                        -- Foreign key to Players table
    CollectibleName VARCHAR(100) NOT NULL,        -- Name of the collectible
    AcquiredAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the collectible was acquired
    FOREIGN KEY (PlayerID) REFERENCES Players(PlayerID) ON DELETE CASCADE -- Cascade delete on player removal
);

-- Indexes for optimization
CREATE INDEX idx_PlayerProgress_PlayerID ON PlayerProgress(PlayerID);
CREATE INDEX idx_PlayerInventory_PlayerID ON PlayerInventory(PlayerID);
CREATE INDEX idx_PlayerInventory_ItemID ON PlayerInventory(ItemID);
CREATE INDEX idx_Collectibles_PlayerID ON Collectibles(PlayerID);
```
