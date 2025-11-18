"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Create a database schema for storing product details, categories, and promotions for an e-commerce platform like "Mass Compras."
Generated: DETERMINISTIC_3db0d53f5a27bba2
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL schema for an e-commerce platform database

-- Create table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    StockQuantity INT NOT NULL,               -- Number of items available in stock
    CategoryID INT,                           -- Foreign key for the category the product belongs to
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create table to store categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(255) NOT NULL,                -- Name of the category
    Description TEXT,                          -- Description of the category
    ParentCategoryID INT,                      -- Self-referencing foreign key for parent category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create table to store promotions
CREATE TABLE Promotions (
    PromotionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each promotion
    Name VARCHAR(255) NOT NULL,                 -- Name of the promotion
    Description TEXT,                           -- Description of the promotion
    DiscountPercentage DECIMAL(5, 2) NOT NULL, -- Discount percentage (e.g., 20.00 for 20%)
    StartDate DATE NOT NULL,                    -- Start date of the promotion
    EndDate DATE NOT NULL,                      -- End date of the promotion
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the promotion was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create junction table to associate products with promotions (many-to-many relationship)
CREATE TABLE ProductPromotions (
    ProductPromotionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProductID INT NOT NULL,                             -- Foreign key referencing Products table
    PromotionID INT NOT NULL,                           -- Foreign key referencing Promotions table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp when the association was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (PromotionID) REFERENCES Promotions(PromotionID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Add foreign key to link Products table to Categories table
ALTER TABLE Products
ADD FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL ON UPDATE CASCADE;

-- Add foreign key to create hierarchy within Categories table
ALTER TABLE Categories
ADD FOREIGN KEY (ParentCategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL ON UPDATE CASCADE;
```
