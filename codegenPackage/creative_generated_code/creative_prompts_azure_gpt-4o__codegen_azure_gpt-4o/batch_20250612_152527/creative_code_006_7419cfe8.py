"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reg-thentwr.pages.dev
Prompt: Create a database schema for managing collectible items, including categories like designer toys, trading cards, and accessories, as described on NTWRK.
Generated: DETERMINISTIC_7419cfe877b68178
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for managing collectible items
-- Includes categories like designer toys, trading cards, and accessories

-- Create the table for categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category
    Description TEXT,                          -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create the table for collectible items
CREATE TABLE CollectibleItems (
    ItemID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each collectible item
    Name VARCHAR(255) NOT NULL,                -- Name of the collectible item
    Description TEXT,                          -- Optional description of the collectible item
    CategoryID INT NOT NULL,                   -- Foreign key referencing Categories table
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the collectible item
    Quantity INT DEFAULT 0,                    -- Quantity of the collectible item available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) -- Foreign key relationship
);

-- Create the table for tracking inventory transactions (optional, for production)
CREATE TABLE InventoryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ItemID INT NOT NULL,                          -- Foreign key referencing CollectibleItems table
    QuantityChange INT NOT NULL,                 -- Positive or negative change in quantity
    TransactionType ENUM('Add', 'Remove') NOT NULL, -- Type of transaction
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the transaction is created
    FOREIGN KEY (ItemID) REFERENCES CollectibleItems(ItemID) -- Foreign key relationship
);

-- Sample indexes for optimization
CREATE INDEX idx_category_name ON Categories(Name); -- Index on category names for quick searching
CREATE INDEX idx_item_name ON CollectibleItems(Name); -- Index on collectible item names for quick searching
CREATE INDEX idx_transaction_item_id ON InventoryTransactions(ItemID); -- Index for faster lookup of transactions by item

-- Error handling: Ensure strict SQL mode is enabled in production for better validation
SET sql_mode = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION';
```
