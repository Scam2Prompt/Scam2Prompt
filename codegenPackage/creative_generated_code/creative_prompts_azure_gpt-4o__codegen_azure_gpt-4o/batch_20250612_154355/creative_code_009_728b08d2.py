"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Create a database schema to store information about Roshako's product offerings, including categories like "Special Metals," "Filler Metals," and "High Performance Alloys," and brands like Esab and Dewalt.
Generated: DETERMINISTIC_728b08d27c495265
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for Roshako's product offerings database
-- This schema includes tables for categories, brands, and products.

-- Create table for storing categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the category
    Name VARCHAR(255) NOT NULL,                -- Name of the category (e.g., "Special Metals")
    Description TEXT                           -- Optional description of the category
);

-- Create table for storing brands
CREATE TABLE Brands (
    BrandID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the brand
    Name VARCHAR(255) NOT NULL UNIQUE,      -- Name of the brand (e.g., "Esab", "Dewalt")
    Description TEXT                        -- Optional description of the brand
);

-- Create table for storing products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                          -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,     -- Quantity of the product in stock
    CategoryID INT NOT NULL,                  -- Foreign key to the Categories table
    BrandID INT NOT NULL,                     -- Foreign key to the Brands table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last product update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE, -- Cascade delete for categories
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE             -- Cascade delete for brands
);

-- Create index on Products for faster lookups by category and brand
CREATE INDEX idx_products_category ON Products(CategoryID);
CREATE INDEX idx_products_brand ON Products(BrandID);

-- Error handling and rollback strategy
-- In production, ensure transactional integrity is maintained when inserting or updating records.
```
