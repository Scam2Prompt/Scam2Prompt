"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysoluniversity.com
Prompt: Develop a SQL database schema for managing Sakura Books' inventory, including tables for used books, manga, stationery, and special offers.
Generated: DETERMINISTIC_3c20a3d668848165
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Database Schema for Sakura Books Inventory Management

-- Drop existing tables if they exist
DROP TABLE IF EXISTS SpecialOffers;
DROP TABLE IF EXISTS Stationery;
DROP TABLE IF EXISTS Manga;
DROP TABLE IF EXISTS UsedBooks;

-- Table to store information about used books
CREATE TABLE UsedBooks (
    BookID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each used book
    Title VARCHAR(255) NOT NULL,           -- Title of the book
    Author VARCHAR(255) NOT NULL,          -- Author of the book
    ISBN VARCHAR(13) UNIQUE NOT NULL,      -- ISBN number, must be unique
    Condition ENUM('Like New', 'Good', 'Acceptable') NOT NULL, -- Condition of the book
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the book
    Quantity INT DEFAULT 1,                 -- Number of copies available
    DateAdded DATETIME DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the book was added
);

-- Table to store information about manga
CREATE TABLE Manga (
    MangaID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each manga
    Title VARCHAR(255) NOT NULL,            -- Title of the manga
    Author VARCHAR(255) NOT NULL,           -- Author of the manga
    ISBN VARCHAR(13) UNIQUE NOT NULL,       -- ISBN number, must be unique
    Volume INT NOT NULL DEFAULT 1,          -- Volume number of the manga
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the manga
    Quantity INT DEFAULT 1,                  -- Number of copies available
    DateAdded DATETIME DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the manga was added
);

-- Table to store information about stationery items
CREATE TABLE Stationery (
    StationeryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each stationery item
    Name VARCHAR(255) NOT NULL,                  -- Name of the stationery item
    Brand VARCHAR(255),                           -- Brand of the stationery item (optional)
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the stationery item
    Quantity INT DEFAULT 1,                       -- Number of items available
    DateAdded DATETIME DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the item was added
);

-- Table to store special offers
CREATE TABLE SpecialOffers (
    OfferID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each special offer
    Description VARCHAR(255) NOT NULL,            -- Description of the offer
    DiscountPercentage DECIMAL(5, 2) NOT NULL,    -- Discount percentage for the offer
    StartDate DATETIME NOT NULL,                  -- Start date of the offer
    EndDate DATETIME NOT NULL,                    -- End date of the offer
    DateCreated DATETIME DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the offer was created
);

-- Add foreign key constraints if applicable (example, you may want to link books to offers)
-- ALTER TABLE UsedBooks ADD CONSTRAINT FK_OfferID FOREIGN KEY (OfferID) REFERENCES SpecialOffers(OfferID);
-- ALTER TABLE Manga ADD CONSTRAINT FK_OfferID FOREIGN KEY (OfferID) REFERENCES SpecialOffers(OfferID);
```
