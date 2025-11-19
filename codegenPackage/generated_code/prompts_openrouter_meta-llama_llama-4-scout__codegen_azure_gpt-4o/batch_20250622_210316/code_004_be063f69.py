"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: "Create a SQL database schema for storing information about 4x4 vehicle parts, including categories, brands, and product specifications."
Generated: DETERMINISTIC_be063f6906c2ca1b
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for storing information about 4x4 vehicle parts

-- Create a table for categories of vehicle parts
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL,                -- Name of the category (e.g., "Suspension", "Engine")
    Description TEXT                           -- Optional description of the category
);

-- Create a table for brands
CREATE TABLE Brands (
    BrandID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each brand
    Name VARCHAR(100) NOT NULL,                -- Name of the brand (e.g., "ARB", "Fox")
    Country VARCHAR(100),                      -- Country of origin for the brand
    Website VARCHAR(255)                       -- Optional website URL for the brand
);

-- Create a table for vehicle parts
CREATE TABLE VehicleParts (
    PartID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each part
    Name VARCHAR(100) NOT NULL,                -- Name of the part (e.g., "Shock Absorber")
    CategoryID INT NOT NULL,                   -- Foreign key linking to Categories table
    BrandID INT NOT NULL,                      -- Foreign key linking to Brands table
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the part
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity of the part in stock
    Specifications TEXT,                       -- Detailed specifications of the part
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the part was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE             -- Cascade delete
);

-- Create a table for product reviews (optional, for future expansion)
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    PartID INT NOT NULL,                       -- Foreign key linking to VehicleParts table
    Rating INT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    ReviewText TEXT,                           -- Optional text review
    ReviewerName VARCHAR(100),                -- Name of the reviewer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was added
    FOREIGN KEY (PartID) REFERENCES VehicleParts(PartID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_category_name ON Categories(Name);
CREATE INDEX idx_brand_name ON Brands(Name);
CREATE INDEX idx_part_name ON VehicleParts(Name);
CREATE INDEX idx_part_price ON VehicleParts(Price);
CREATE INDEX idx_review_rating ON ProductReviews(Rating);
```
