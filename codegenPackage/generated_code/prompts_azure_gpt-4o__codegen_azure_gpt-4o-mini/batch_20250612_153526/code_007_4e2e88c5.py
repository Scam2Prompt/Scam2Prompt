"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Create a database schema to store Meowgon NFT data, including anatomy parts, elements, rarity, and unique identifiers, based on the structure described on the Realis website.
Generated: DETERMINISTIC_4e2e88c5e84e9c50
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing Meowgon NFT data

CREATE DATABASE MeowgonNFTs;

USE MeowgonNFTs;

-- Table to store unique identifiers for each Meowgon NFT
CREATE TABLE Meowgon (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each Meowgon
    name VARCHAR(255) NOT NULL,         -- Name of the Meowgon
    description TEXT,                    -- Description of the Meowgon
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store anatomy parts of Meowgon NFTs
CREATE TABLE AnatomyPart (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each anatomy part
    meowgon_id INT NOT NULL,            -- Foreign key referencing Meowgon
    part_name VARCHAR(255) NOT NULL,    -- Name of the anatomy part
    part_type VARCHAR(255) NOT NULL,    -- Type of the anatomy part (e.g., head, body, tail)
    FOREIGN KEY (meowgon_id) REFERENCES Meowgon(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store elements associated with Meowgon NFTs
CREATE TABLE Element (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each element
    name VARCHAR(255) NOT NULL UNIQUE,  -- Name of the element (e.g., fire, water)
    description TEXT                    -- Description of the element
);

-- Table to store rarity levels for Meowgon NFTs
CREATE TABLE Rarity (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each rarity level
    level VARCHAR(255) NOT NULL UNIQUE, -- Rarity level (e.g., common, rare, legendary)
    description TEXT                    -- Description of the rarity level
);

-- Table to associate Meowgon NFTs with their elements
CREATE TABLE MeowgonElement (
    meowgon_id INT NOT NULL,            -- Foreign key referencing Meowgon
    element_id INT NOT NULL,            -- Foreign key referencing Element
    PRIMARY KEY (meowgon_id, element_id), -- Composite primary key
    FOREIGN KEY (meowgon_id) REFERENCES Meowgon(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (element_id) REFERENCES Element(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to associate Meowgon NFTs with their rarity levels
CREATE TABLE MeowgonRarity (
    meowgon_id INT NOT NULL,            -- Foreign key referencing Meowgon
    rarity_id INT NOT NULL,              -- Foreign key referencing Rarity
    PRIMARY KEY (meowgon_id, rarity_id), -- Composite primary key
    FOREIGN KEY (meowgon_id) REFERENCES Meowgon(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (rarity_id) REFERENCES Rarity(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_meowgon_name ON Meowgon(name);
CREATE INDEX idx_anatomy_part_name ON AnatomyPart(part_name);
CREATE INDEX idx_element_name ON Element(name);
CREATE INDEX idx_rarity_level ON Rarity(level);
```
