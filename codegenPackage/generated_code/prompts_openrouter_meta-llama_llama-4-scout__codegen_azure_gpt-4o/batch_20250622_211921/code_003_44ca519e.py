"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: "Design a database schema for storing information about various natural stone bracelets, their collections (e.g., The Earth Series, Statement Stones), and their respective prices and discounts."
Generated: DETERMINISTIC_44ca519e7c4cb5a7
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about natural stone bracelets, collections, prices, and discounts.

-- Create a table to store information about collections
CREATE TABLE Collections (
    CollectionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each collection
    Name VARCHAR(255) NOT NULL,                  -- Name of the collection (e.g., "The Earth Series")
    Description TEXT,                            -- Optional description of the collection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the collection was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store information about bracelets
CREATE TABLE Bracelets (
    BraceletID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each bracelet
    Name VARCHAR(255) NOT NULL,                  -- Name of the bracelet
    CollectionID INT NOT NULL,                   -- Foreign key linking to the Collections table
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the bracelet
    Discount DECIMAL(5, 2) DEFAULT 0.00,         -- Discount percentage (e.g., 10.00 for 10%)
    Stock INT DEFAULT 0,                         -- Number of bracelets available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the bracelet was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CollectionID) REFERENCES Collections(CollectionID) ON DELETE CASCADE -- Cascade delete if collection is removed
);

-- Create a table to store logs for price and discount changes (optional for tracking history)
CREATE TABLE PriceDiscountLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each log entry
    BraceletID INT NOT NULL,                     -- Foreign key linking to the Bracelets table
    OldPrice DECIMAL(10, 2),                     -- Previous price of the bracelet
    NewPrice DECIMAL(10, 2),                     -- Updated price of the bracelet
    OldDiscount DECIMAL(5, 2),                   -- Previous discount percentage
    NewDiscount DECIMAL(5, 2),                   -- Updated discount percentage
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the change occurred
    FOREIGN KEY (BraceletID) REFERENCES Bracelets(BraceletID) ON DELETE CASCADE -- Cascade delete if bracelet is removed
);

-- Indexes for faster queries
CREATE INDEX idx_collection_name ON Collections(Name); -- Index for collection name
CREATE INDEX idx_bracelet_name ON Bracelets(Name);     -- Index for bracelet name
CREATE INDEX idx_bracelet_price ON Bracelets(Price);   -- Index for bracelet price
CREATE INDEX idx_bracelet_discount ON Bracelets(Discount); -- Index for bracelet discount
```
