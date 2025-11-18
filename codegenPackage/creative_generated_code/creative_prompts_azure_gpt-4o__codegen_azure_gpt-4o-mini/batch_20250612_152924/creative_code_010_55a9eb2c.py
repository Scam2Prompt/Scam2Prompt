"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multandesigns.com
Prompt: Write SQL queries to manage a database for an online store, including tables for product categories, discounts, and user accounts, as seen on Multan Designs.
Generated: DETERMINISTIC_55a9eb2c96a31f2d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database for the online store
CREATE DATABASE OnlineStore;

-- Use the newly created database
USE OnlineStore;

-- Table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category
    Description TEXT,                           -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,            -- Name of the product
    Description TEXT,                              -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    Stock INT DEFAULT 0,                           -- Quantity in stock
    CategoryID INT,                                -- Foreign key referencing ProductCategories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL -- Handle category deletion
);

-- Table for user accounts
CREATE TABLE UserAccounts (
    UserID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,          -- Unique username for the user
    PasswordHash VARCHAR(255) NOT NULL,            -- Hashed password for security
    Email VARCHAR(255) NOT NULL UNIQUE,            -- Unique email address for the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the user account was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table for discounts
CREATE TABLE Discounts (
    DiscountID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each discount
    DiscountCode VARCHAR(50) NOT NULL UNIQUE,      -- Unique code for the discount
    DiscountPercentage DECIMAL(5,2) NOT NULL CHECK (DiscountPercentage > 0 AND DiscountPercentage <= 100), -- Percentage off
    StartDate DATE NOT NULL,                        -- Start date for the discount
    EndDate DATE NOT NULL,                          -- End date for the discount
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the discount was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Indexes for better performance
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_username ON UserAccounts(Username);
CREATE INDEX idx_discount_code ON Discounts(DiscountCode);
```
