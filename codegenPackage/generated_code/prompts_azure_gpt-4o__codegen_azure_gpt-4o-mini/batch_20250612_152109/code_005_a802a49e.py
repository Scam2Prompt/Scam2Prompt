"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Create a database schema in SQL for managing a catalog of flip-flop products, including fields for product name, category, material type, and customization options.
Generated: DETERMINISTIC_a802a49eb2817f7a
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing a catalog of flip-flop products

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category
    Description TEXT                             -- Description of the category
);

-- Create a table for material types
CREATE TABLE MaterialTypes (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each material type
    MaterialName VARCHAR(100) NOT NULL UNIQUE,   -- Name of the material type
    Description TEXT                             -- Description of the material type
);

-- Create a table for customization options
CREATE TABLE CustomizationOptions (
    CustomizationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customization option
    OptionName VARCHAR(100) NOT NULL UNIQUE,        -- Name of the customization option
    Description TEXT                                 -- Description of the customization option
);

-- Create a table for flip-flop products
CREATE TABLE FlipFlopProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,               -- Name of the flip-flop product
    CategoryID INT NOT NULL,                          -- Foreign key referencing ProductCategories
    MaterialID INT NOT NULL,                          -- Foreign key referencing MaterialTypes
    CustomizationID INT,                              -- Foreign key referencing CustomizationOptions (optional)
    Price DECIMAL(10, 2) NOT NULL,                   -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,            -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (MaterialID) REFERENCES MaterialTypes(MaterialID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CustomizationID) REFERENCES CustomizationOptions(CustomizationID) ON DELETE SET NULL -- Optional customization
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON FlipFlopProducts(ProductName);
CREATE INDEX idx_category ON FlipFlopProducts(CategoryID);
CREATE INDEX idx_material ON FlipFlopProducts(MaterialID);
CREATE INDEX idx_customization ON FlipFlopProducts(CustomizationID);
```
