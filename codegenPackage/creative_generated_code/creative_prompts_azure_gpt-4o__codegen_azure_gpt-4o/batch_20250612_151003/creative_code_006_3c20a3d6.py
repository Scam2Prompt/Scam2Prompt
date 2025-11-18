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
-- Sakura Books Inventory Management SQL Schema

-- Table for storing data about used books
CREATE TABLE UsedBooks (
    BookID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each book
    Title VARCHAR(255) NOT NULL,           -- Title of the book
    Author VARCHAR(255) NOT NULL,          -- Author of the book
    Genre VARCHAR(100),                    -- Genre/category of the book
    PublicationYear INT,                   -- Year the book was published
    ISBN VARCHAR(13),                      -- ISBN number (optional for older books)
    Condition ENUM('Poor', 'Fair', 'Good', 'Excellent') DEFAULT 'Good', -- Condition of the book
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the book
    Quantity INT NOT NULL DEFAULT 0,       -- Number of copies available
    AddedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the book was added to inventory
);

-- Table for storing data about manga
CREATE TABLE Manga (
    MangaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each manga
    Title VARCHAR(255) NOT NULL,            -- Title of the manga
    Author VARCHAR(255) NOT NULL,           -- Author or creator of the manga
    Genre VARCHAR(100),                     -- Genre/category of the manga
    Volume INT NOT NULL,                    -- Volume number
    ISBN VARCHAR(13),                       -- ISBN number (optional)
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the manga
    Quantity INT NOT NULL DEFAULT 0,        -- Number of copies available
    AddedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the manga was added to inventory
);

-- Table for storing data about stationery items
CREATE TABLE Stationery (
    ItemID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each stationery item
    Name VARCHAR(255) NOT NULL,             -- Name of the stationery item
    Category VARCHAR(100),                  -- Category/type of stationery item (e.g., pens, notebooks)
    Brand VARCHAR(100),                     -- Brand of the stationery item
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the stationery item
    Quantity INT NOT NULL DEFAULT 0,        -- Number of items available
    AddedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the item was added to inventory
);

-- Table for storing data about special offers
CREATE TABLE SpecialOffers (
    OfferID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each offer
    Description TEXT NOT NULL,              -- Description of the offer
    DiscountPercentage DECIMAL(5, 2) NOT NULL, -- Discount percentage for the offer
    StartDate DATE NOT NULL,                -- Start date of the offer
    EndDate DATE NOT NULL,                  -- End date of the offer
    ApplicableTo ENUM('UsedBooks', 'Manga', 'Stationery', 'All') DEFAULT 'All', -- Which category the offer applies to
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the offer was created
);

-- Enforce referential integrity and data quality where applicable
-- Foreign key relationships could be added if tables reference each other
-- Example: Adding relationships if special offers apply only to specific items
```
