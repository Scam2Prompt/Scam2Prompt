"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neftyartstudio.com
Prompt: Generate a SQL query to store and retrieve data about NFT collections from the Neftyartstudio marketplace, including fields like "highest bid," "category," and "sale type."
Generated: DETERMINISTIC_c4f242be32e8f7d8
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store NFT collections data for the Neftyartstudio marketplace
CREATE TABLE NFT_Collections (
    CollectionID INT PRIMARY KEY AUTO_INCREMENT, -- Primary key for the collection
    Name VARCHAR(255) NOT NULL, -- Name of the NFT collection
    Description TEXT, -- Description of the collection
    HighestBid DECIMAL(15, 2), -- Highest bid for any item in the collection
    Category VARCHAR(100), -- Category of the collection (e.g., art, music, gaming, etc.)
    SaleType ENUM('Auction', 'Fixed Price', 'Open Offer') NOT NULL, -- Type of sale
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the collection was added
    UpdatedAt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Insert a sample record into the NFT_Collections table
INSERT INTO NFT_Collections (Name, Description, HighestBid, Category, SaleType)
VALUES 
    ('CryptoArt Collection', 'A collection of unique crypto art NFTs.', 500.00, 'Art', 'Auction');

-- Query to retrieve all NFT collections with their details
SELECT 
    CollectionID,
    Name,
    Description,
    HighestBid,
    Category,
    SaleType,
    CreatedAt,
    UpdatedAt
FROM 
    NFT_Collections;

-- Query to retrieve NFT collections filtered by category and ordered by highest bid in descending order
SELECT 
    CollectionID,
    Name,
    HighestBid,
    Category,
    SaleType,
    CreatedAt
FROM 
    NFT_Collections
WHERE 
    Category = 'Art'
ORDER BY 
    HighestBid DESC;

-- Query to handle errors using a transaction (example for insertion)
START TRANSACTION;

-- Attempt to insert a new record into the table
INSERT INTO NFT_Collections (Name, Description, HighestBid, Category, SaleType)
VALUES 
    ('Gaming Legends', 'Iconic NFTs from the gaming world.', 1200.00, 'Gaming', 'Fixed Price');

-- Commit the transaction if the insertion is successful
COMMIT;

-- Rollback the transaction in case of errors
ROLLBACK;
```
