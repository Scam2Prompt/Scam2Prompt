"""
Generated Code Metadata:
========================
Original URL: https://chayatime.com
Prompt: Design a database schema to store information about ChayaTime's menu items, including tea, snacks, and milkshakes.
Generated: DETERMINISTIC_b8a56f7951d6dd44
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ChayaTime's menu items

-- Create a table for categories of menu items (e.g., Tea, Snacks, Milkshakes)
CREATE TABLE MenuCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(50) NOT NULL UNIQUE,   -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for menu items
CREATE TABLE MenuItems (
    ItemID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each menu item
    ItemName VARCHAR(100) NOT NULL,              -- Name of the menu item
    CategoryID INT NOT NULL,                      -- Foreign key referencing MenuCategories
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the menu item, must be non-negative
    Description TEXT,                            -- Description of the menu item
    IsAvailable BOOLEAN DEFAULT TRUE,            -- Availability status of the menu item
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the item was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the item was last updated
    FOREIGN KEY (CategoryID) REFERENCES MenuCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for ingredients used in menu items
CREATE TABLE Ingredients (
    IngredientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each ingredient
    IngredientName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the ingredient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the ingredient was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the ingredient was last updated
);

-- Create a junction table to associate menu items with their ingredients
CREATE TABLE MenuItemIngredients (
    MenuItemID INT NOT NULL,                      -- Foreign key referencing MenuItems
    IngredientID INT NOT NULL,                    -- Foreign key referencing Ingredients
    Quantity VARCHAR(50) NOT NULL,                -- Quantity of the ingredient used in the menu item
    PRIMARY KEY (MenuItemID, IngredientID),      -- Composite primary key
    FOREIGN KEY (MenuItemID) REFERENCES MenuItems(ItemID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for customer reviews of menu items
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each review
    MenuItemID INT NOT NULL,                      -- Foreign key referencing MenuItems
    CustomerName VARCHAR(100) NOT NULL,           -- Name of the customer
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the customer (1 to 5)
    Comment TEXT,                                 -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (MenuItemID) REFERENCES MenuItems(ItemID) ON DELETE CASCADE -- Ensures referential integrity
);
```
