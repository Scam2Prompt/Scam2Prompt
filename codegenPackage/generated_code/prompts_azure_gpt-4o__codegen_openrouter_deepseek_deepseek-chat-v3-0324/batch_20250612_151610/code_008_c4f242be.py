"""
Generated Code Metadata:
========================
Original URL: https://neftyartstudio.com
Prompt: Generate a SQL query to store and retrieve data about NFT collections from the Neftyartstudio marketplace, including fields like "highest bid," "category," and "sale type."
Generated: DETERMINISTIC_c4f242be32e8f7d8
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a table for storing NFT collections from Neftyartstudio marketplace
-- Includes fields for highest bid, category, and sale type

CREATE TABLE nft_collections (
    id SERIAL PRIMARY KEY,
    collection_name VARCHAR(255) NOT NULL,
    collection_id VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    creator VARCHAR(255) NOT NULL,
    highest_bid DECIMAL(18, 8) DEFAULT 0.0,
    currency VARCHAR(10) DEFAULT 'NEFTY',
    category VARCHAR(100) NOT NULL,
    sale_type VARCHAR(50) NOT NULL CHECK (sale_type IN ('auction', 'fixed_price', 'bundle')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    metadata JSONB
);

-- Create an index for faster queries on frequently accessed fields
CREATE INDEX idx_nft_collections_category ON nft_collections(category);
CREATE INDEX idx_nft_collections_sale_type ON nft_collections(sale_type);
CREATE INDEX idx_nft_collections_highest_bid ON nft_collections(highest_bid);

-- Trigger to update the updated_at timestamp when a record is modified
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_timestamp
BEFORE UPDATE ON nft_collections
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

-- Query to retrieve NFT collections with pagination and filtering
-- Example usage: Get active auctions in 'art' category sorted by highest bid
/*
SELECT 
    id,
    collection_name,
    creator,
    highest_bid,
    currency,
    category,
    sale_type,
    created_at
FROM 
    nft_collections
WHERE 
    is_active = TRUE
    AND category = 'art'
    AND sale_type = 'auction'
ORDER BY 
    highest_bid DESC
LIMIT 20 OFFSET 0;
*/

-- Query to update the highest bid for a collection
/*
UPDATE nft_collections
SET 
    highest_bid = 10.5,
    updated_at = CURRENT_TIMESTAMP
WHERE 
    collection_id = 'collection123';
*/

-- Query to get statistics by category
/*
SELECT 
    category,
    COUNT(*) as total_collections,
    AVG(highest_bid) as avg_highest_bid,
    MAX(highest_bid) as max_highest_bid
FROM 
    nft_collections
WHERE 
    is_active = TRUE
GROUP BY 
    category
ORDER BY 
    avg_highest_bid DESC;
*/
```
