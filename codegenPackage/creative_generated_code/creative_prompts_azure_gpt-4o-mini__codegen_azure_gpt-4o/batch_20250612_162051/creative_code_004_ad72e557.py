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
-- SQL Database Schema for Perfect Food Corner

-- Create a table to store information about food items
CREATE TABLE FoodItems (
    FoodItemID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for food items
    Name VARCHAR(100) NOT NULL,                -- Name of the food item
    Description TEXT,                          -- Description of the food item
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the food item
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the food item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the item was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the item was last updated
);

-- Create a table to store dietary options
CREATE TABLE DietaryOptions (
    DietaryOptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for dietary options
    Name VARCHAR(50) NOT NULL,                      -- Name of the dietary option (e.g., Vegan, Gluten-Free)
    Description TEXT                                -- Description of the dietary option
);

-- Create a table to store packaging details
CREATE TABLE PackagingDetails (
    PackagingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for packaging details
    Type VARCHAR(50) NOT NULL,                  -- Type of packaging (e.g., Box, Bag, Wrapper)
    IsEcoFriendly BOOLEAN DEFAULT FALSE,        -- Whether the packaging is eco-friendly
    Material VARCHAR(50),                       -- Material of the packaging (e.g., Plastic, Paper)
    Description TEXT                             -- Additional description for the packaging
);

-- Create a table to establish many-to-many relationships between FoodItems and DietaryOptions
CREATE TABLE FoodItemDietaryOptions (
    FoodItemID INT NOT NULL,                    -- Foreign key referencing FoodItems
    DietaryOptionID INT NOT NULL,               -- Foreign key referencing DietaryOptions
    PRIMARY KEY (FoodItemID, DietaryOptionID),  -- Composite primary key
    FOREIGN KEY (FoodItemID) REFERENCES FoodItems(FoodItemID) ON DELETE CASCADE,
    FOREIGN KEY (DietaryOptionID) REFERENCES DietaryOptions(DietaryOptionID) ON DELETE CASCADE
);

-- Create a table to establish one-to-many relationships between FoodItems and PackagingDetails
CREATE TABLE FoodItemPackaging (
    FoodItemID INT NOT NULL,                    -- Foreign key referencing FoodItems
    PackagingID INT NOT NULL,                   -- Foreign key referencing PackagingDetails
    PRIMARY KEY (FoodItemID, PackagingID),      -- Composite primary key
    FOREIGN KEY (FoodItemID) REFERENCES FoodItems(FoodItemID) ON DELETE CASCADE,
    FOREIGN KEY (PackagingID) REFERENCES PackagingDetails(PackagingID) ON DELETE CASCADE
);

-- Indexes for better query performance
CREATE INDEX idx_fooditem_name ON FoodItems(Name);
CREATE INDEX idx_dietaryoption_name ON DietaryOptions(Name);
CREATE INDEX idx_packaging_type ON PackagingDetails(Type);

-- Example error handling for transactions
-- Wrap inserts into a transaction to ensure data consistency
START TRANSACTION;

-- Insert example data
INSERT INTO DietaryOptions (Name, Description) VALUES ('Vegan', 'No animal products used.');
INSERT INTO PackagingDetails (Type, IsEcoFriendly, Material, Description) VALUES ('Box', TRUE, 'Paper', 'Recyclable cardboard box.');

-- Commit the transaction if no errors
COMMIT;
```
