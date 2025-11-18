"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dotcomachinery.co.tz
Prompt: Create a database schema to organize product categories such as "Garage Machines" and "Power Tools" based on the structure of Dotcom Machinery's website.
Generated: DETERMINISTIC_1e43878892e1e7bd
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for organizing product categories

-- Step 1: Create the main schema
CREATE SCHEMA IF NOT EXISTS DotcomMachinery;

-- Step 2: Create the table for product categories
CREATE TABLE IF NOT EXISTS DotcomMachinery.ProductCategories (
    CategoryID SERIAL PRIMARY KEY,                      -- Unique Identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,         -- Name of the category (e.g., "Garage Machines", "Power Tools")
    ParentCategoryID INT NULL,                         -- Self-referencing foreign key for hierarchical structure
    Description TEXT,                                  -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT FK_ParentCategory FOREIGN KEY (ParentCategoryID) 
        REFERENCES DotcomMachinery.ProductCategories (CategoryID)
        ON DELETE SET NULL                             -- If the parent is deleted, this category's parent becomes NULL
);

-- Step 3: Create the table for products
CREATE TABLE IF NOT EXISTS DotcomMachinery.Products (
    ProductID SERIAL PRIMARY KEY,                      -- Unique Identifier for each product
    CategoryID INT NOT NULL,                           -- Foreign key to reference the product category
    ProductName VARCHAR(255) NOT NULL,                -- Name of the product
    SKU VARCHAR(100) NOT NULL UNIQUE,                 -- Stock Keeping Unit for product identification
    Price DECIMAL(10, 2) NOT NULL,                    -- Product price
    Stock INT DEFAULT 0,                              -- Quantity available in stock
    Description TEXT,                                 -- Optional description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT FK_ProductCategory FOREIGN KEY (CategoryID) 
        REFERENCES DotcomMachinery.ProductCategories (CategoryID)
        ON DELETE CASCADE                              -- Delete products if the category is deleted
);

-- Step 4: Create an index for faster lookups on CategoryID
CREATE INDEX IDX_CategoryID ON DotcomMachinery.Products (CategoryID);

-- Sample data insertion for demonstration purposes (optional)
-- INSERT INTO DotcomMachinery.ProductCategories (CategoryName, ParentCategoryID, Description)
-- VALUES 
--     ('Garage Machines', NULL, 'Machines for garage use'),
--     ('Power Tools', NULL, 'Tools powered by electricity'),
--     ('Drills', (SELECT CategoryID FROM DotcomMachinery.ProductCategories WHERE CategoryName = 'Power Tools'), 'Various types of drills');
```
