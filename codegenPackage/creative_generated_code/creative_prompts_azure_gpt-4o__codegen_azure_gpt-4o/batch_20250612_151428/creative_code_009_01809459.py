"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Design a database schema in SQL for storing Marant's skincare product details, including categories like exfoliants, peels, active ingredients, and target skin conditions.
Generated: DETERMINISTIC_018094593b7b0d64
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for storing Marant's skincare product details

-- Create table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,        -- Name of the category (e.g., Exfoliants, Peels)
    Description TEXT                           -- Optional description of the category
);

-- Create table for active ingredients
CREATE TABLE ActiveIngredients (
    IngredientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each ingredient
    IngredientName VARCHAR(100) NOT NULL,        -- Name of the active ingredient
    Description TEXT,                            -- Optional description of the ingredient
    PotentialBenefits TEXT                       -- Information on benefits of the ingredient
);

-- Create table for target skin conditions
CREATE TABLE SkinConditions (
    ConditionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each skin condition
    ConditionName VARCHAR(100) NOT NULL,        -- Name of the skin condition (e.g., Acne, Dryness)
    Description TEXT                            -- Optional description of the condition
);

-- Create main table for skincare products
CREATE TABLE SkincareProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each product
    ProductName VARCHAR(150) NOT NULL,          -- Name of the product
    CategoryID INT NOT NULL,                    -- Foreign key linking to ProductCategories
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    Description TEXT,                           -- Optional description of the product
    StockQuantity INT NOT NULL,                 -- Quantity of the product in stock
    -- Foreign key constraint to ensure valid category IDs
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE
);

-- Create table to link products and active ingredients (many-to-many relationship)
CREATE TABLE ProductIngredients (
    ProductID INT NOT NULL,                     -- Foreign key referencing SkincareProducts
    IngredientID INT NOT NULL,                  -- Foreign key referencing ActiveIngredients
    ConcentrationPercentage DECIMAL(5, 2),      -- Optional concentration percentage of the ingredient in the product
    -- Foreign key constraints to ensure valid product and ingredient IDs
    FOREIGN KEY (ProductID) REFERENCES SkincareProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (IngredientID) REFERENCES ActiveIngredients(IngredientID) ON DELETE CASCADE,
    PRIMARY KEY (ProductID, IngredientID)       -- Composite primary key for unique product-ingredient pairs
);

-- Create table to link products and target skin conditions (many-to-many relationship)
CREATE TABLE ProductSkinConditions (
    ProductID INT NOT NULL,                     -- Foreign key referencing SkincareProducts
    ConditionID INT NOT NULL,                   -- Foreign key referencing SkinConditions
    -- Foreign key constraints to ensure valid product and condition IDs
    FOREIGN KEY (ProductID) REFERENCES SkincareProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (ConditionID) REFERENCES SkinConditions(ConditionID) ON DELETE CASCADE,
    PRIMARY KEY (ProductID, ConditionID)        -- Composite primary key for unique product-condition pairs
);

-- Create indexes for faster query performance
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_ingredient_name ON ActiveIngredients(IngredientName);
CREATE INDEX idx_condition_name ON SkinConditions(ConditionName);
CREATE INDEX idx_product_name ON SkincareProducts(ProductName);

-- End of database schema definition
```
