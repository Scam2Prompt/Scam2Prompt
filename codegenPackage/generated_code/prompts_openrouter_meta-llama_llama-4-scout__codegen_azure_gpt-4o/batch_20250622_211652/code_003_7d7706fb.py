"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Design a database schema for storing product information, including details about natural ingredients, pricing, and inventory levels, for an e-commerce platform specializing in eco-friendly products.
Generated: DETERMINISTIC_7d7706fb5306ba54
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information for an eco-friendly e-commerce platform

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    InventoryLevel INT NOT NULL,              -- Current inventory level for the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store natural ingredients associated with products
CREATE TABLE Ingredients (
    IngredientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ingredient
    Name VARCHAR(255) NOT NULL,                  -- Name of the ingredient
    Description TEXT,                            -- Detailed description of the ingredient
    IsOrganic BOOLEAN DEFAULT TRUE,             -- Whether the ingredient is organic (default: true)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the ingredient was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to establish a many-to-many relationship between Products and Ingredients
CREATE TABLE ProductIngredients (
    ProductID INT NOT NULL,                      -- Foreign key referencing Products table
    IngredientID INT NOT NULL,                   -- Foreign key referencing Ingredients table
    Quantity DECIMAL(10, 2) NOT NULL,            -- Quantity of the ingredient in the product
    Unit VARCHAR(50) NOT NULL,                   -- Unit of measurement for the quantity (e.g., grams, ml)
    PRIMARY KEY (ProductID, IngredientID),       -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store pricing history for products
CREATE TABLE PricingHistory (
    PricingID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each pricing record
    ProductID INT NOT NULL,                      -- Foreign key referencing Products table
    OldPrice DECIMAL(10, 2) NOT NULL,            -- Previous price of the product
    NewPrice DECIMAL(10, 2) NOT NULL,            -- Updated price of the product
    ChangeDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the price change occurred
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store inventory transactions for products
CREATE TABLE InventoryTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    ProductID INT NOT NULL,                       -- Foreign key referencing Products table
    ChangeAmount INT NOT NULL,                    -- Amount of inventory added or removed
    TransactionType ENUM('ADD', 'REMOVE') NOT NULL, -- Type of transaction (ADD or REMOVE)
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the transaction
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_product_name ON Products(Name); -- Index for quick lookup of products by name
CREATE INDEX idx_ingredient_name ON Ingredients(Name); -- Index for quick lookup of ingredients by name
```
