"""
Generated Code Metadata:
========================
Original URL: https://rawcakesandcandy.ro
Prompt: "Design a database schema to store information about raw vegan desserts, including cakes, pastries, and their ingredients, as seen on the Raw Cakes And Candy website."
Generated: DETERMINISTIC_523e60bab3f4ff9a
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about raw vegan desserts, including cakes, pastries, and their ingredients.

-- Table to store dessert categories (e.g., cakes, pastries, etc.)
CREATE TABLE DessertCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL,                -- Name of the category (e.g., "Cakes", "Pastries")
    Description TEXT                           -- Optional description of the category
);

-- Table to store desserts
CREATE TABLE Desserts (
    DessertID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each dessert
    Name VARCHAR(255) NOT NULL,                -- Name of the dessert
    CategoryID INT NOT NULL,                   -- Foreign key linking to DessertCategories
    Description TEXT,                          -- Optional description of the dessert
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the dessert
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Availability status of the dessert
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the dessert was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES DessertCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store ingredients
CREATE TABLE Ingredients (
    IngredientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ingredient
    Name VARCHAR(255) NOT NULL,                  -- Name of the ingredient
    Description TEXT                             -- Optional description of the ingredient
);

-- Table to store the relationship between desserts and their ingredients
CREATE TABLE DessertIngredients (
    DessertID INT NOT NULL,                      -- Foreign key linking to Desserts
    IngredientID INT NOT NULL,                   -- Foreign key linking to Ingredients
    Quantity VARCHAR(100),                       -- Quantity of the ingredient (e.g., "2 cups", "1 tsp")
    PRIMARY KEY (DessertID, IngredientID),       -- Composite primary key to ensure uniqueness
    FOREIGN KEY (DessertID) REFERENCES Desserts(DessertID) ON DELETE CASCADE,
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE
);

-- Table to store user reviews for desserts
CREATE TABLE DessertReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each review
    DessertID INT NOT NULL,                     -- Foreign key linking to Desserts
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating for the dessert (1 to 5 stars)
    Comment TEXT,                               -- Optional comment from the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was added
    FOREIGN KEY (DessertID) REFERENCES Desserts(DessertID) ON DELETE CASCADE
);

-- Table to store nutritional information for desserts
CREATE TABLE NutritionalInfo (
    DessertID INT NOT NULL PRIMARY KEY,         -- Foreign key linking to Desserts
    Calories INT,                               -- Calories per serving
    Protein DECIMAL(5, 2),                      -- Protein content per serving (grams)
    Fat DECIMAL(5, 2),                          -- Fat content per serving (grams)
    Carbohydrates DECIMAL(5, 2),                -- Carbohydrate content per serving (grams)
    FOREIGN KEY (DessertID) REFERENCES Desserts(DessertID) ON DELETE CASCADE
);
```
