"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thechampionsshop.com
Prompt: Recommend a database schema for storing product information for a website selling replica wrestling belts, including fields for categories like NXT Belts, Impact Belts, and Fantasy Belts.
Generated: DETERMINISTIC_3099832546b64e74
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script for creating a database schema to store product information 
-- for a website selling replica wrestling belts.

-- Create the main database
CREATE DATABASE ReplicaWrestlingBelts;

-- Use the created database
USE ReplicaWrestlingBelts;

-- Table for storing categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category, e.g., "NXT Belts", "Impact Belts", "Fantasy Belts"
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the category was created
);

-- Table for storing product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to Categories table
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT DEFAULT 0,                       -- Number of items available in inventory
    Description TEXT,                          -- Detailed description of the product
    ImageURL VARCHAR(2083),                    -- URL to the product image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Table for tracking product reviews (optional, can be excluded if not required)
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each review
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    ReviewerName VARCHAR(255),                 -- Name of the person reviewing the product
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the product (1 to 5 stars)
    Comment TEXT,                              -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was submitted
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Example insertion of categories for testing
INSERT INTO Categories (CategoryName) VALUES 
('NXT Belts'),
('Impact Belts'),
('Fantasy Belts');

-- Ensure proper indexing for faster querying
CREATE INDEX idx_CategoryID ON Products(CategoryID);
CREATE INDEX idx_ProductID ON Reviews(ProductID);
```
