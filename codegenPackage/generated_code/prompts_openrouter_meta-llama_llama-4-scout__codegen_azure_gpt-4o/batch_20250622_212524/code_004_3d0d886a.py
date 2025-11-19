"""
Generated Code Metadata:
========================
Original URL: https://swepsepoocoin.blogspot.com
Prompt: Write a SQL query to design a database schema for storing shoe information, including shoe type (e.g., sandalia, sapato social, tenis de corrida), size, and color.
Generated: DETERMINISTIC_3d0d886a2ca420a6
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing shoe information
-- This schema includes tables for shoe types, sizes, colors, and the main shoe table

-- Table to store shoe types
CREATE TABLE ShoeType (
    ShoeTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shoe type
    TypeName VARCHAR(50) NOT NULL,             -- Name of the shoe type (e.g., sandalia, sapato social, tenis de corrida)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store shoe sizes
CREATE TABLE ShoeSize (
    ShoeSizeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shoe size
    SizeValue DECIMAL(4,1) NOT NULL,           -- Shoe size (e.g., 8.5, 10, 42)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store shoe colors
CREATE TABLE ShoeColor (
    ShoeColorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shoe color
    ColorName VARCHAR(30) NOT NULL,             -- Name of the color (e.g., red, blue, black)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Main table to store shoe information
CREATE TABLE Shoe (
    ShoeID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each shoe
    ShoeTypeID INT NOT NULL,                    -- Foreign key referencing ShoeType table
    ShoeSizeID INT NOT NULL,                    -- Foreign key referencing ShoeSize table
    ShoeColorID INT NOT NULL,                   -- Foreign key referencing ShoeColor table
    StockQuantity INT DEFAULT 0,                -- Quantity of shoes available in stock
    Price DECIMAL(10,2) NOT NULL,               -- Price of the shoe
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    -- Foreign key constraints
    CONSTRAINT FK_ShoeType FOREIGN KEY (ShoeTypeID) REFERENCES ShoeType(ShoeTypeID) ON DELETE CASCADE,
    CONSTRAINT FK_ShoeSize FOREIGN KEY (ShoeSizeID) REFERENCES ShoeSize(ShoeSizeID) ON DELETE CASCADE,
    CONSTRAINT FK_ShoeColor FOREIGN KEY (ShoeColorID) REFERENCES ShoeColor(ShoeColorID) ON DELETE CASCADE
);

-- Indexes for faster lookups
CREATE INDEX IDX_ShoeTypeID ON Shoe(ShoeTypeID);
CREATE INDEX IDX_ShoeSizeID ON Shoe(ShoeSizeID);
CREATE INDEX IDX_ShoeColorID ON Shoe(ShoeColorID);
```
