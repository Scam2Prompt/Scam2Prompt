"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Construct a SQL database schema to store information about various food items, their dietary options, and packaging details, inspired by the menu structure of Perfect Food Corner.
Generated: DETERMINISTIC_ad72e5577a0d3489
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for Perfect Food Corner's menu structure

-- Create a database for Perfect Food Corner
CREATE DATABASE PerfectFoodCorner;

-- Use the newly created database
USE PerfectFoodCorner;

-- Table to store food items
CREATE TABLE FoodItems (
    FoodID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each food item
    Name VARCHAR(255) NOT NULL,            -- Name of the food item
    Description TEXT,                      -- Description of the food item
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the food item
    Category VARCHAR(100),                 -- Category of the food item (e.g., Appetizer, Main Course, Dessert)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the food item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store dietary options
CREATE TABLE DietaryOptions (
    OptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each dietary option
    Name VARCHAR(100) NOT NULL UNIQUE,       -- Name of the dietary option (e.g., Vegan, Gluten-Free, Nut-Free)
    Description TEXT                         -- Description of the dietary option
);

-- Table to store packaging details
CREATE TABLE PackagingDetails (
    PackagingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each packaging type
    Type VARCHAR(100) NOT NULL UNIQUE,          -- Type of packaging (e.g., Box, Bag, Wrapper)
    Material VARCHAR(100),                      -- Material used for packaging (e.g., Plastic, Paper, Biodegradable)
    IsReusable BOOLEAN DEFAULT FALSE,           -- Indicates if the packaging is reusable
    Description TEXT                             -- Additional details about the packaging
);

-- Table to associate food items with dietary options (many-to-many relationship)
CREATE TABLE FoodDietaryOptions (
    FoodID INT NOT NULL,                         -- Foreign key referencing FoodItems
    OptionID INT NOT NULL,                       -- Foreign key referencing DietaryOptions
    PRIMARY KEY (FoodID, OptionID),              -- Composite primary key
    FOREIGN KEY (FoodID) REFERENCES FoodItems(FoodID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (OptionID) REFERENCES DietaryOptions(OptionID) ON DELETE CASCADE -- Cascade delete
);

-- Table to associate food items with packaging details (one-to-many relationship)
CREATE TABLE FoodPackaging (
    FoodID INT NOT NULL,                         -- Foreign key referencing FoodItems
    PackagingID INT NOT NULL,                    -- Foreign key referencing PackagingDetails
    PRIMARY KEY (FoodID, PackagingID),           -- Composite primary key
    FOREIGN KEY (FoodID) REFERENCES FoodItems(FoodID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (PackagingID) REFERENCES PackagingDetails(PackagingID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for faster querying
CREATE INDEX idx_food_category ON FoodItems(Category); -- Index on food category
CREATE INDEX idx_dietary_name ON DietaryOptions(Name); -- Index on dietary option name
CREATE INDEX idx_packaging_type ON PackagingDetails(Type); -- Index on packaging type
```
