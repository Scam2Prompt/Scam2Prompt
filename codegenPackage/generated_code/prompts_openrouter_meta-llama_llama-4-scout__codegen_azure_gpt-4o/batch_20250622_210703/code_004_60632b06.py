"""
Generated Code Metadata:
========================
Original URL: https://bekon.rs
Prompt: Design a database schema to store information about meat products, including types (e.g., fresh meat, sausages, dry products) and recipes, inspired by Bekon Promet's product offerings.
Generated: DETERMINISTIC_60632b0620af7fba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about meat products and recipes

-- Table to store types of meat products
CREATE TABLE MeatProductTypes (
    TypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each type
    TypeName VARCHAR(100) NOT NULL,        -- Name of the meat product type (e.g., fresh meat, sausages, dry products)
    Description TEXT                       -- Optional description of the type
);

-- Table to store individual meat products
CREATE TABLE MeatProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,        -- Name of the meat product
    TypeID INT NOT NULL,                      -- Foreign key referencing MeatProductTypes
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Weight DECIMAL(10, 2) NOT NULL,           -- Weight of the product in kilograms
    Description TEXT,                         -- Optional description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    FOREIGN KEY (TypeID) REFERENCES MeatProductTypes(TypeID) ON DELETE CASCADE
);

-- Table to store recipes
CREATE TABLE Recipes (
    RecipeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each recipe
    RecipeName VARCHAR(100) NOT NULL,        -- Name of the recipe
    Instructions TEXT NOT NULL,              -- Cooking instructions for the recipe
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the recipe was added
);

-- Table to associate meat products with recipes
CREATE TABLE RecipeIngredients (
    RecipeIngredientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    RecipeID INT NOT NULL,                             -- Foreign key referencing Recipes
    ProductID INT NOT NULL,                            -- Foreign key referencing MeatProducts
    Quantity DECIMAL(10, 2) NOT NULL,                  -- Quantity of the product used in the recipe
    FOREIGN KEY (RecipeID) REFERENCES Recipes(RecipeID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES MeatProducts(ProductID) ON DELETE CASCADE
);

-- Example of error handling: Ensure all tables are created successfully
-- If any table creation fails, the transaction will roll back
START TRANSACTION;

-- Create tables
-- (Place the CREATE TABLE statements here)

-- Commit transaction if all tables are created successfully
COMMIT;

-- Rollback transaction in case of an error
ROLLBACK;
```
