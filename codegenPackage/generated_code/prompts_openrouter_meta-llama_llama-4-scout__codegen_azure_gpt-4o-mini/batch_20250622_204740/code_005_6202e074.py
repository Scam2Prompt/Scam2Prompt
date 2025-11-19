"""
Generated Code Metadata:
========================
Original URL: https://karnatakaaromas.com
Prompt: Design a database schema to store Karnataka Aromas' product information, including fragrances, flavors, and essential oils.
Generated: DETERMINISTIC_6202e074986e3333
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Karnataka Aromas' product information

-- Create a database for Karnataka Aromas
CREATE DATABASE KarnatakaAromas;

-- Use the created database
USE KarnatakaAromas;

-- Table to store product categories (e.g., Fragrances, Flavors, Essential Oils)
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the product
    CategoryID INT NOT NULL,                      -- Foreign key referencing ProductCategories
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity in stock
    Description TEXT,                             -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store product ingredients (e.g., essential oils, flavor components)
CREATE TABLE Ingredients (
    IngredientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each ingredient
    IngredientName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the ingredient
    Description TEXT,                              -- Description of the ingredient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the ingredient was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to associate products with their ingredients
CREATE TABLE ProductIngredients (
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    IngredientID INT NOT NULL,                    -- Foreign key referencing Ingredients
    Quantity DECIMAL(10, 2) NOT NULL,            -- Quantity of the ingredient in the product
    PRIMARY KEY (ProductID, IngredientID),       -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each review
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    ReviewerName VARCHAR(100) NOT NULL,          -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating out of 5
    Comment TEXT,                                 -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_ingredient_name ON Ingredients(IngredientName);
```
