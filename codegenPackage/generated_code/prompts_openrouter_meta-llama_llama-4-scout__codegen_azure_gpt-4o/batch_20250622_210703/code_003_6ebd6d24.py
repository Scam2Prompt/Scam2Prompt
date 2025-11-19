"""
Generated Code Metadata:
========================
Original URL: https://ristorantelafenice.ch
Prompt: Design a database schema to store information about restaurant menus, including tables for dishes, prices, and ingredients, inspired by the offerings at Ristorante La Fenice.
Generated: DETERMINISTIC_6ebd6d24896b8c52
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing restaurant menu information

-- Table to store information about dishes
CREATE TABLE Dishes (
    DishID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each dish
    Name VARCHAR(255) NOT NULL,            -- Name of the dish
    Description TEXT,                      -- Description of the dish
    Category VARCHAR(100),                 -- Category of the dish (e.g., Appetizer, Main Course, Dessert)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the dish was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store prices for dishes
CREATE TABLE Prices (
    PriceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each price entry
    DishID INT NOT NULL,                    -- Foreign key referencing the Dishes table
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the dish
    Currency VARCHAR(10) DEFAULT 'USD',     -- Currency of the price (default is USD)
    EffectiveDate DATE NOT NULL,            -- Date when the price becomes effective
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the price was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (DishID) REFERENCES Dishes(DishID) ON DELETE CASCADE -- Cascade delete if dish is removed
);

-- Table to store ingredients for dishes
CREATE TABLE Ingredients (
    IngredientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ingredient
    Name VARCHAR(255) NOT NULL,                  -- Name of the ingredient
    Description TEXT,                            -- Description of the ingredient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the ingredient was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to associate dishes with their ingredients
CREATE TABLE DishIngredients (
    DishIngredientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    DishID INT NOT NULL,                             -- Foreign key referencing the Dishes table
    IngredientID INT NOT NULL,                       -- Foreign key referencing the Ingredients table
    Quantity VARCHAR(50),                            -- Quantity of the ingredient (e.g., "200g", "1 tsp")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the association was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (DishID) REFERENCES Dishes(DishID) ON DELETE CASCADE, -- Cascade delete if dish is removed
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE -- Cascade delete if ingredient is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_dish_name ON Dishes(Name); -- Index for quick lookup of dishes by name
CREATE INDEX idx_ingredient_name ON Ingredients(Name); -- Index for quick lookup of ingredients by name
CREATE INDEX idx_price_dish ON Prices(DishID); -- Index for quick lookup of prices by dish
CREATE INDEX idx_dishingredient_dish ON DishIngredients(DishID); -- Index for quick lookup of ingredients by dish
CREATE INDEX idx_dishingredient_ingredient ON DishIngredients(IngredientID); -- Index for quick lookup of dishes by ingredient
```
