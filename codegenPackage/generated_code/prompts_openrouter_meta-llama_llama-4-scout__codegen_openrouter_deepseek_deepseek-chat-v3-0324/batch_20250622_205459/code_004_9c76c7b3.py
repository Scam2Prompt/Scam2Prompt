"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Design a basic database schema for storing character information, alliances, and survival supplies in a scenario like "The Cannibals," using SQL.
Generated: DETERMINISTIC_9c76c7b389d3810e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a survival scenario game with characters, alliances, and supplies

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Characters table - stores individual character information
CREATE TABLE IF NOT EXISTS characters (
    character_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER CHECK (age >= 0),
    gender TEXT,
    health_status TEXT CHECK (health_status IN ('healthy', 'injured', 'critical', 'dead')),
    strength INTEGER CHECK (strength BETWEEN 0 AND 10),
    intelligence INTEGER CHECK (intelligence BETWEEN 0 AND 10),
    charisma INTEGER CHECK (charisma BETWEEN 0 AND 10),
    is_cannibal BOOLEAN DEFAULT FALSE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Alliances table - stores group relationships between characters
CREATE TABLE IF NOT EXISTS alliances (
    alliance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    leader_id INTEGER,
    formation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (leader_id) REFERENCES characters(character_id) ON DELETE SET NULL
);

-- Alliance members junction table - tracks which characters belong to which alliances
CREATE TABLE IF NOT EXISTS alliance_members (
    alliance_id INTEGER,
    character_id INTEGER,
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    role TEXT CHECK (role IN ('leader', 'member', 'supporter')),
    PRIMARY KEY (alliance_id, character_id),
    FOREIGN KEY (alliance_id) REFERENCES alliances(alliance_id) ON DELETE CASCADE,
    FOREIGN KEY (character_id) REFERENCES characters(character_id) ON DELETE CASCADE
);

-- Supply categories table - defines types of supplies
CREATE TABLE IF NOT EXISTS supply_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Supplies table - tracks available resources
CREATE TABLE IF NOT EXISTS supplies (
    supply_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER,
    quantity INTEGER DEFAULT 0 CHECK (quantity >= 0),
    unit TEXT,
    perishable BOOLEAN DEFAULT FALSE,
    expiration_date TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES supply_categories(category_id) ON DELETE SET NULL
);

-- Character inventory junction table - tracks which characters possess which supplies
CREATE TABLE IF NOT EXISTS character_inventory (
    character_id INTEGER,
    supply_id INTEGER,
    quantity INTEGER DEFAULT 1 CHECK (quantity >= 0),
    acquisition_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (character_id, supply_id),
    FOREIGN KEY (character_id) REFERENCES characters(character_id) ON DELETE CASCADE,
    FOREIGN KEY (supply_id) REFERENCES supplies(supply_id) ON DELETE CASCADE
);

-- Alliance inventory junction table - tracks which alliances possess which supplies
CREATE TABLE IF NOT EXISTS alliance_inventory (
    alliance_id INTEGER,
    supply_id INTEGER,
    quantity INTEGER DEFAULT 1 CHECK (quantity >= 0),
    storage_location TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (alliance_id, supply_id),
    FOREIGN KEY (alliance_id) REFERENCES alliances(alliance_id) ON DELETE CASCADE,
    FOREIGN KEY (supply_id) REFERENCES supplies(supply_id) ON DELETE CASCADE
);

-- Events table - logs significant game events
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type TEXT NOT NULL CHECK (event_type IN ('supply_change', 'alliance_change', 'character_status', 'other')),
    description TEXT NOT NULL,
    affected_character_id INTEGER,
    affected_alliance_id INTEGER,
    affected_supply_id INTEGER,
    event_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (affected_character_id) REFERENCES characters(character_id) ON DELETE SET NULL,
    FOREIGN KEY (affected_alliance_id) REFERENCES alliances(alliance_id) ON DELETE SET NULL,
    FOREIGN KEY (affected_supply_id) REFERENCES supplies(supply_id) ON DELETE SET NULL
);

-- Create indexes for performance optimization
CREATE INDEX IF NOT EXISTS idx_characters_health ON characters(health_status);
CREATE INDEX IF NOT EXISTS idx_alliances_active ON alliances(is_active);
CREATE INDEX IF NOT EXISTS idx_supplies_category ON supplies(category_id);
CREATE INDEX IF NOT EXISTS idx_events_timestamp ON events(event_timestamp);
```
