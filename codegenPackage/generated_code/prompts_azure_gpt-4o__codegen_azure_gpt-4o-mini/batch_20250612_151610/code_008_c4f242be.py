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
-- Create a table to store NFT collection data
CREATE TABLE nft_collections (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each NFT collection
    name VARCHAR(255) NOT NULL,           -- Name of the NFT collection
    highest_bid DECIMAL(10, 2) NOT NULL,  -- Highest bid amount for the collection
    category VARCHAR(100) NOT NULL,       -- Category of the NFT collection
    sale_type VARCHAR(50) NOT NULL,       -- Type of sale (e.g., auction, fixed price)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Insert a new NFT collection into the table
INSERT INTO nft_collections (name, highest_bid, category, sale_type)
VALUES ('CryptoArt Collection', 1500.00, 'Art', 'Auction')
ON CONFLICT (name) DO UPDATE SET
    highest_bid = EXCLUDED.highest_bid,
    category = EXCLUDED.category,
    sale_type = EXCLUDED.sale_type,
    updated_at = CURRENT_TIMESTAMP; -- Update the record if it already exists

-- Retrieve all NFT collections from the table
SELECT * FROM nft_collections;

-- Retrieve NFT collections filtered by category
SELECT * FROM nft_collections
WHERE category = 'Art';

-- Retrieve the NFT collection with the highest bid
SELECT * FROM nft_collections
ORDER BY highest_bid DESC
LIMIT 1;

-- Error handling for potential issues during data manipulation
DO $$
BEGIN
    -- Example of a transaction block for inserting data
    BEGIN
        INSERT INTO nft_collections (name, highest_bid, category, sale_type)
        VALUES ('New NFT Collection', 2000.00, 'Collectibles', 'Fixed Price');
    EXCEPTION
        WHEN unique_violation THEN
            RAISE NOTICE 'Collection already exists, updating highest bid.';
            UPDATE nft_collections
            SET highest_bid = GREATEST(highest_bid, 2000.00),
                updated_at = CURRENT_TIMESTAMP
            WHERE name = 'New NFT Collection';
    END;
END $$;
```
