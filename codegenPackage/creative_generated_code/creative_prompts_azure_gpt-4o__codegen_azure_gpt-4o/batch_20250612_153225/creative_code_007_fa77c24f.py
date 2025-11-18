"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Write a database schema for storing product details, including categories, sizes, and warranty information, based on the diverse product offerings mentioned on the TDKCO website.
Generated: DETERMINISTIC_fa77c24f81ab91a6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for storing product details, categories, sizes, and warranty information
-- This schema is designed to be normalized and follows best practices.

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                 -- Category name (e.g., Electronics, Furniture)
    Description TEXT                            -- Optional description of the category
);

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,                 -- Product name
    Description TEXT,                           -- Optional detailed product description
    Price DECIMAL(10, 2) NOT NULL,              -- The price of the product
    StockQuantity INT DEFAULT 0,                -- Number of items available in stock
    CategoryID INT NOT NULL,                    -- Foreign key for the category the product belongs to
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for product creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

-- Table to store available sizes for products
CREATE TABLE Sizes (
    SizeID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each size entry
    Name VARCHAR(255) NOT NULL,                 -- Name of the size (e.g., Small, Medium, Large)
    Description TEXT                            -- Optional description of the size
);

-- Table to associate products with their available sizes
CREATE TABLE ProductSizes (
    ProductID INT NOT NULL,                     -- Foreign key referencing the product
    SizeID INT NOT NULL,                        -- Foreign key referencing the size
    PRIMARY KEY (ProductID, SizeID),            -- Composite primary key to ensure uniqueness for product-size pairs
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SizeID) REFERENCES Sizes(SizeID) ON DELETE CASCADE
);

-- Table to store warranty information for products
CREATE TABLE Warranties (
    WarrantyID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each warranty entry
    ProductID INT NOT NULL,                     -- Foreign key referencing the product
    WarrantyPeriod INT NOT NULL,                -- Warranty period in months
    Terms TEXT NOT NULL,                        -- Full terms and conditions of the warranty
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Example indexes for optimizing queries
CREATE INDEX idx_products_category ON Products(CategoryID); -- Index for faster category-based lookups
CREATE INDEX idx_product_sizes ON ProductSizes(ProductID);  -- Index for faster product-size queries
CREATE INDEX idx_warranties_product ON Warranties(ProductID); -- Index for faster warranty lookup by product
```
