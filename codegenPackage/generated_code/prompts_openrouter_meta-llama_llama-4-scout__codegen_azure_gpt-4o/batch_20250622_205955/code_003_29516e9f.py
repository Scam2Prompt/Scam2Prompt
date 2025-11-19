"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Design a basic database schema to store information about Eclat's products, including nail polish colors, gel polish sets, and eyelash extension types.
Generated: DETERMINISTIC_29516e9f7c390a32
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Eclat's products

-- Table to store general product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Category VARCHAR(50) NOT NULL,            -- Category of the product (e.g., Nail Polish, Gel Polish Set, Eyelash Extension)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store nail polish colors
CREATE TABLE NailPolishColors (
    ColorID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each color
    ProductID INT NOT NULL,                  -- Foreign key referencing Products table
    ColorName VARCHAR(100) NOT NULL,         -- Name of the nail polish color
    HexCode VARCHAR(7),                      -- Hexadecimal color code (e.g., #FF5733)
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Table to store gel polish sets
CREATE TABLE GelPolishSets (
    SetID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each gel polish set
    ProductID INT NOT NULL,                  -- Foreign key referencing Products table
    SetName VARCHAR(255) NOT NULL,           -- Name of the gel polish set
    NumberOfColors INT NOT NULL,             -- Number of colors included in the set
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Table to store eyelash extension types
CREATE TABLE EyelashExtensions (
    ExtensionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each eyelash extension type
    ProductID INT NOT NULL,                     -- Foreign key referencing Products table
    Length VARCHAR(50) NOT NULL,                -- Length of the eyelash extension (e.g., "8mm", "10mm")
    CurlType VARCHAR(50) NOT NULL,              -- Curl type of the eyelash extension (e.g., "C", "D")
    Thickness VARCHAR(50) NOT NULL,             -- Thickness of the eyelash extension (e.g., "0.07mm", "0.10mm")
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Indexes for faster querying
CREATE INDEX idx_category ON Products(Category); -- Index on the Category column for faster filtering
CREATE INDEX idx_colorname ON NailPolishColors(ColorName); -- Index on the ColorName column for faster searching
CREATE INDEX idx_setname ON GelPolishSets(SetName); -- Index on the SetName column for faster searching
CREATE INDEX idx_curltype ON EyelashExtensions(CurlType); -- Index on the CurlType column for faster searching
```
