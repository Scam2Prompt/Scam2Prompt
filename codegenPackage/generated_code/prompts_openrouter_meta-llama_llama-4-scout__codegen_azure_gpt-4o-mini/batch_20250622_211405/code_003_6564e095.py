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
    player_id SERIAL PRIMARY KEY,          -- Unique identifier for each player
    username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for the player
    email VARCHAR(100) NOT NULL UNIQUE,     -- Unique email for the player
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of player creation
    last_login TIMESTAMP                     -- Timestamp of last login
);

-- Table to store player progress
CREATE TABLE PlayerProgress (
    progress_id SERIAL PRIMARY KEY,         -- Unique identifier for each progress record
    player_id INT NOT NULL,                 -- Foreign key referencing Players
    level INT NOT NULL DEFAULT 1,           -- Current level of the player
    experience INT NOT NULL DEFAULT 0,      -- Experience points of the player
    achievements JSONB DEFAULT '{}'::JSONB, -- JSONB to store achievements
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store inventory items
CREATE TABLE InventoryItems (
    item_id SERIAL PRIMARY KEY,             -- Unique identifier for each inventory item
    item_name VARCHAR(100) NOT NULL,        -- Name of the item
    item_type VARCHAR(50) NOT NULL,         -- Type of the item (e.g., weapon, armor, collectible)
    rarity VARCHAR(50) NOT NULL,             -- Rarity of the item (e.g., common, rare, epic)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of item creation
);

-- Table to store player inventory
CREATE TABLE PlayerInventory (
    inventory_id SERIAL PRIMARY KEY,        -- Unique identifier for each inventory record
    player_id INT NOT NULL,                 -- Foreign key referencing Players
    item_id INT NOT NULL,                   -- Foreign key referencing InventoryItems
    quantity INT NOT NULL DEFAULT 1,        -- Quantity of the item in the inventory
    equipped BOOLEAN DEFAULT FALSE,          -- Indicates if the item is equipped
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (item_id) REFERENCES InventoryItems(item_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store workshop information
CREATE TABLE Workshops (
    workshop_id SERIAL PRIMARY KEY,         -- Unique identifier for each workshop
    workshop_name VARCHAR(100) NOT NULL,    -- Name of the workshop
    description TEXT,                        -- Description of the workshop
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of workshop creation
);

-- Table to store player workshop progress
CREATE TABLE PlayerWorkshops (
    workshop_progress_id SERIAL PRIMARY KEY, -- Unique identifier for each workshop progress record
    player_id INT NOT NULL,                  -- Foreign key referencing Players
    workshop_id INT NOT NULL,                -- Foreign key referencing Workshops
    progress_level INT NOT NULL DEFAULT 0,   -- Current progress level in the workshop
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (workshop_id) REFERENCES Workshops(workshop_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store collectibles
CREATE TABLE Collectibles (
    collectible_id SERIAL PRIMARY KEY,       -- Unique identifier for each collectible
    collectible_name VARCHAR(100) NOT NULL,  -- Name of the collectible
    description TEXT,                        -- Description of the collectible
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of collectible creation
);

-- Table to store player collectibles
CREATE TABLE PlayerCollectibles (
    collectible_progress_id SERIAL PRIMARY KEY, -- Unique identifier for each collectible progress record
    player_id INT NOT NULL,                     -- Foreign key referencing Players
    collectible_id INT NOT NULL,                -- Foreign key referencing Collectibles
    acquired BOOLEAN DEFAULT FALSE,              -- Indicates if the collectible has been acquired
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (collectible_id) REFERENCES Collectibles(collectible_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
