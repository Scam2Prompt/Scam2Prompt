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
-- Database schema for Meowgon NFT data

-- Enable UUID extension for unique identifiers
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Table to store NFT collections
CREATE TABLE collections (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    contract_address VARCHAR(42) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(contract_address)
);

-- Table to store NFT categories (e.g., background, body, eyes, etc.)
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    display_order INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

-- Table to store possible traits within each category
CREATE TABLE traits (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category_id UUID NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    image_url VARCHAR(255),
    rarity DECIMAL(5,2) NOT NULL CHECK (rarity >= 0 AND rarity <= 100),
    element VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(category_id, name)
);

-- Table to store individual NFTs
CREATE TABLE nfts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    collection_id UUID NOT NULL REFERENCES collections(id) ON DELETE CASCADE,
    token_id VARCHAR(100) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    image_url VARCHAR(255),
    external_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(collection_id, token_id)
);

-- Junction table to link NFTs with their traits
CREATE TABLE nft_traits (
    nft_id UUID NOT NULL REFERENCES nfts(id) ON DELETE CASCADE,
    trait_id UUID NOT NULL REFERENCES traits(id) ON DELETE CASCADE,
    PRIMARY KEY (nft_id, trait_id)
);

-- Table to store rarity scores for NFTs
CREATE TABLE nft_rarity_scores (
    nft_id UUID PRIMARY KEY REFERENCES nfts(id) ON DELETE CASCADE,
    overall_score DECIMAL(10,4) NOT NULL,
    trait_count INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table to store element types
CREATE TABLE elements (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) NOT NULL,
    color VARCHAR(7) NOT NULL, -- Hex color code
    icon_url VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name)
);

-- Function to update timestamp on record update
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for automatic timestamp updates
CREATE TRIGGER update_collections_timestamp
BEFORE UPDATE ON collections
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_nfts_timestamp
BEFORE UPDATE ON nfts
FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Indexes for performance optimization
CREATE INDEX idx_traits_category_id ON traits(category_id);
CREATE INDEX idx_nfts_collection_id ON nfts(collection_id);
CREATE INDEX idx_nft_traits_nft_id ON nft_traits(nft_id);
CREATE INDEX idx_nft_traits_trait_id ON nft_traits(trait_id);
```
