"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectfoodcorner.com
Prompt: Construct a SQL database schema to store information about various food items, their dietary options, and packaging details, inspired by the menu structure of Perfect Food Corner.
Generated: DETERMINISTIC_ad72e5577a0d3489
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for storing food items and their details
CREATE DATABASE PerfectFoodCorner;

-- Use the created database
USE PerfectFoodCorner;

-- Table to store different food items
CREATE TABLE FoodItems (
    FoodID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each food item
    Name VARCHAR(255) NOT NULL,              -- Name of the food item
    Description TEXT,                         -- Description of the food item
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the food item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store dietary options
CREATE TABLE DietaryOptions (
    OptionID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each dietary option
    OptionName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the dietary option (e.g., Vegan, Gluten-Free)
    Description TEXT                          -- Description of the dietary option
);

-- Linking table to associate food items with dietary options (many-to-many relationship)
CREATE TABLE FoodItemDietaryOptions (
    FoodID INT,                               -- Identifier for the food item
    OptionID INT,                             -- Identifier for the dietary option
    PRIMARY KEY (FoodID, OptionID),          -- Composite primary key
    FOREIGN KEY (FoodID) REFERENCES FoodItems(FoodID) ON DELETE CASCADE,  -- Foreign key constraint
    FOREIGN KEY (OptionID) REFERENCES DietaryOptions(OptionID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store packaging details
CREATE TABLE PackagingDetails (
    PackagingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each packaging type
    PackagingType VARCHAR(100) NOT NULL UNIQUE,  -- Type of packaging (e.g., Box, Bag)
    Description TEXT                             -- Description of the packaging
);

-- Linking table to associate food items with packaging details (one-to-many relationship)
CREATE TABLE FoodItemPackaging (
    FoodID INT,                                 -- Identifier for the food item
    PackagingID INT,                            -- Identifier for the packaging type
    PRIMARY KEY (FoodID, PackagingID),         -- Composite primary key
    FOREIGN KEY (FoodID) REFERENCES FoodItems(FoodID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (PackagingID) REFERENCES PackagingDetails(PackagingID) ON DELETE CASCADE -- Foreign key constraint
);

-- Index for quick search on food item name
CREATE INDEX idx_food_name ON FoodItems(Name);

-- Index for quick search on dietary option name
CREATE INDEX idx_option_name ON DietaryOptions(OptionName);
```
