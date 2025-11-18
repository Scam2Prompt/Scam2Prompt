"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realis.pages.dev
Prompt: Create a database schema to store Meowgon NFT data, including anatomy parts, elements, rarity, and unique identifiers, based on the structure described on the Realis website.
Generated: DETERMINISTIC_4e2e88c5e84e9c50
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing Meowgon NFT data

-- Table to store information about Meowgon NFTs
CREATE TABLE Meowgon_NFTs (
    id SERIAL PRIMARY KEY, -- Auto-incrementing unique identifier for each NFT
    nft_id UUID NOT NULL UNIQUE, -- Unique identifier for the NFT
    name VARCHAR(255) NOT NULL, -- Name of the Meowgon
    description TEXT, -- Optional description of the Meowgon
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store anatomy parts of Meowgons
CREATE TABLE Anatomy_Parts (
    id SERIAL PRIMARY KEY, -- Auto-incrementing unique identifier for each anatomy part
    name VARCHAR(255) NOT NULL, -- Name of the anatomy part (e.g., "Wings", "Tail")
    nft_id UUID NOT NULL, -- The Meowgon NFT associated with this anatomy part
    rarity VARCHAR(50) NOT NULL, -- Rarity of the anatomy part (e.g., "Common", "Rare", "Epic")
    FOREIGN KEY (nft_id) REFERENCES Meowgon_NFTs (nft_id) ON DELETE CASCADE -- Foreign key linking to Meowgon_NFTs
);

-- Table to store elemental attributes of Meowgons
CREATE TABLE Elements (
    id SERIAL PRIMARY KEY, -- Auto-incrementing unique identifier for each element
    name VARCHAR(255) NOT NULL, -- Element name (e.g., "Fire", "Water", "Earth")
    strength INTEGER NOT NULL CHECK (strength >= 0), -- Strength level of the element
    nft_id UUID NOT NULL, -- The Meowgon NFT associated with this element
    FOREIGN KEY (nft_id) REFERENCES Meowgon_NFTs (nft_id) ON DELETE CASCADE -- Foreign key linking to Meowgon_NFTs
);

-- Table to store rarity information
CREATE TABLE Rarity (
    id SERIAL PRIMARY KEY, -- Auto-incrementing unique identifier for rarity levels
    rarity_level VARCHAR(50) NOT NULL UNIQUE, -- Rarity level (e.g., "Common", "Rare", "Epic")
    description TEXT -- Optional description for the rarity level
);

-- Associating Meowgons with a specific rarity level
ALTER TABLE Meowgon_NFTs 
ADD COLUMN rarity_id INTEGER,
ADD CONSTRAINT fk_rarity
FOREIGN KEY (rarity_id) REFERENCES Rarity (id) ON DELETE SET NULL; -- Foreign key linking to Rarity table
```
