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
-- Database Schema for storing NFT metadata and linking them to their respective families

-- Create a table for NFT families
CREATE TABLE nft_families (
    family_id SERIAL PRIMARY KEY,              -- Unique identifier for each family
    family_name VARCHAR(50) NOT NULL UNIQUE,   -- Name of the NFT family (e.g., Fire, Ice, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the family was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Create a table for NFT traits
CREATE TABLE nft_traits (
    trait_id SERIAL PRIMARY KEY,               -- Unique identifier for each trait
    trait_name VARCHAR(100) NOT NULL UNIQUE,   -- Name of the trait (e.g., "Fire Aura", "Ice Shield")
    trait_type VARCHAR(50) NOT NULL,           -- Type of the trait (e.g., "Visual", "Elemental", "Stat")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the trait was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for last update
);

-- Create a table for NFTs
CREATE TABLE nfts (
    nft_id SERIAL PRIMARY KEY,                 -- Unique identifier for each NFT
    nft_name VARCHAR(100) NOT NULL,            -- Name or title of the NFT
    metadata_url TEXT NOT NULL,                -- URL pointing to the metadata (JSON or other file)
    family_id INT NOT NULL,                    -- Foreign key referencing the family the NFT belongs to
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the NFT was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (family_id) REFERENCES nft_families(family_id) ON DELETE CASCADE
);

-- Create a junction table to associate NFTs with their traits
CREATE TABLE nft_traits_mapping (
    nft_id INT NOT NULL,                       -- Foreign key referencing the NFT
    trait_id INT NOT NULL,                     -- Foreign key referencing the trait
    PRIMARY KEY (nft_id, trait_id),            -- Composite primary key (one NFT can have multiple traits)
    FOREIGN KEY (nft_id) REFERENCES nfts(nft_id) ON DELETE CASCADE,
    FOREIGN KEY (trait_id) REFERENCES nft_traits(trait_id) ON DELETE CASCADE
);

-- Create indexes to optimize queries
CREATE INDEX idx_nft_families_name ON nft_families(family_name); -- Index for fast lookup of families by name
CREATE INDEX idx_nft_traits_name ON nft_traits(trait_name);      -- Index for fast lookup of traits by name
CREATE INDEX idx_nfts_family_id ON nfts(family_id);              -- Index for filtering NFTs by family
CREATE INDEX idx_nft_traits_mapping_nft_id ON nft_traits_mapping(nft_id); -- Index for querying traits by NFT
```

This schema is production-ready, handles over 600 traits, and links NFTs to families efficiently. It includes proper error handling (e.g., cascading deletes for integrity maintenance) and uses indexes for performance optimization.
