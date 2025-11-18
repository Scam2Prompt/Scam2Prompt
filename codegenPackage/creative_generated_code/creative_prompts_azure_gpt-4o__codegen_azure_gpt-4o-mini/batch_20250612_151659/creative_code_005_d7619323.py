"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Create a database schema to store metadata for NFTs with over 600 unique traits and link them to their respective families (e.g., Fire, Ice, Earth, Meta, Electric) for a P2E game.
Generated: DETERMINISTIC_d76193233ba970c1
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for NFT metadata storage

-- Drop existing tables if they exist to avoid conflicts during re-creation
DROP TABLE IF EXISTS Traits;
DROP TABLE IF EXISTS Families;
DROP TABLE IF EXISTS NFTs;

-- Create Families table to categorize NFTs into different elemental families
CREATE TABLE Families (
    FamilyID SERIAL PRIMARY KEY,
    FamilyName VARCHAR(100) NOT NULL UNIQUE,  -- Unique name for each family
    Description TEXT,                          -- Description of the family
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Create Traits table to store unique traits of NFTs
CREATE TABLE Traits (
    TraitID SERIAL PRIMARY KEY,
    TraitName VARCHAR(100) NOT NULL,          -- Name of the trait
    TraitType VARCHAR(100),                    -- Type/category of the trait (e.g., Color, Size)
    Rarity DECIMAL(5, 2) CHECK (Rarity >= 0 AND Rarity <= 100),  -- Rarity percentage (0-100)
    FamilyID INT REFERENCES Families(FamilyID) ON DELETE CASCADE,  -- Link to Families table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Create NFTs table to store NFT metadata and link to traits
CREATE TABLE NFTs (
    NFTID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,                -- Name of the NFT
    Description TEXT,                          -- Description of the NFT
    ImageURL VARCHAR(255),                     -- URL for the NFT's image
    FamilyID INT REFERENCES Families(FamilyID) ON DELETE SET NULL,  -- Link to Families table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

-- Create a junction table to associate NFTs with their traits
CREATE TABLE NFTTraits (
    NFTID INT REFERENCES NFTs(NFTID) ON DELETE CASCADE,  -- Link to NFTs table
    TraitID INT REFERENCES Traits(TraitID) ON DELETE CASCADE,  -- Link to Traits table
    PRIMARY KEY (NFTID, TraitID)  -- Composite primary key to ensure unique NFT-Trait relationships
);

-- Ensure all tables are properly indexed for performance improvement
CREATE INDEX idx_families_name ON Families (FamilyName);
CREATE INDEX idx_traits_name ON Traits (TraitName);
CREATE INDEX idx_nfts_name ON NFTs (Name);
```
