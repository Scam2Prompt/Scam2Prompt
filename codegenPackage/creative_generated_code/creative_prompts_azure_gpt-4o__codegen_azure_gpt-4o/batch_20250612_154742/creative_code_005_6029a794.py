"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom.gifts
Prompt: Suggest a database schema for managing daily item rotations in an online shop, including item categories and prices, as seen on Phantom's "Item Shop Daily Rotation."
Generated: DETERMINISTIC_6029a794b2c2f67e
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing daily item rotations in an online shop
-- This schema includes tables for items, categories, daily rotations, and prices.
-- It is designed to handle item categorization, pricing, and daily rotation functionality.

-- Table to store item information
CREATE TABLE Items (
    ItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each item
    ItemName VARCHAR(255) NOT NULL,        -- Name of the item
    Description TEXT,                      -- Description of the item
    CategoryID INT NOT NULL,               -- Foreign key to link with Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) -- Establish relationship with Categories table
);

-- Table to store item categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store item prices (supports historical pricing)
CREATE TABLE ItemPrices (
    PriceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each price
    ItemID INT NOT NULL,                    -- Foreign key to link with Items table
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the item
    EffectiveDate DATE NOT NULL,            -- Date when the price is effective
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the price entry is created
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID) -- Establish relationship with Items table
);

-- Table to store daily rotations for the item shop
CREATE TABLE DailyRotations (
    RotationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each rotation
    RotationDate DATE NOT NULL,                -- Date of the daily rotation
    ItemID INT NOT NULL,                       -- Foreign key to link with Items table
    IsFeatured BOOLEAN DEFAULT FALSE,          -- Indicates whether the item is featured on the rotation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the rotation entry is created
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID) -- Establish relationship with Items table
);

-- Example indexes for optimization
CREATE INDEX IDX_Items_CategoryID ON Items(CategoryID); -- Index for faster lookups by category
CREATE INDEX IDX_ItemPrices_ItemID ON ItemPrices(ItemID); -- Index for faster lookups by item
CREATE INDEX IDX_DailyRotations_RotationDate ON DailyRotations(RotationDate); -- Index for faster lookups by rotation date

-- Example constraints
ALTER TABLE ItemPrices ADD CONSTRAINT CHK_Price_Positive CHECK (Price > 0); -- Ensure prices are positive
```
