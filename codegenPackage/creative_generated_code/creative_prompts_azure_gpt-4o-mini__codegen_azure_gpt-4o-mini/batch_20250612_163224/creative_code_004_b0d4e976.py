"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgtcom.com
Prompt: Design a database schema for an online store that includes tables for premium fabrics and customer reviews, based on JGT's product categories.
Generated: DETERMINISTIC_b0d4e97685b05445
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an online store including tables for premium fabrics and customer reviews

-- Create database
CREATE DATABASE IF NOT EXISTS OnlineStore;
USE OnlineStore;

-- Table for product categories
CREATE TABLE IF NOT EXISTS ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL, -- Name of the product category
    Description TEXT, -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table for premium fabrics
CREATE TABLE IF NOT EXISTS PremiumFabrics (
    FabricID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each fabric
    FabricName VARCHAR(255) NOT NULL, -- Name of the fabric
    CategoryID INT NOT NULL, -- Foreign key to ProductCategories
    Price DECIMAL(10, 2) NOT NULL, -- Price of the fabric
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0), -- Quantity in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the fabric was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the fabric was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table for customer reviews
CREATE TABLE IF NOT EXISTS CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    FabricID INT NOT NULL, -- Foreign key to PremiumFabrics
    CustomerName VARCHAR(255) NOT NULL, -- Name of the customer
    ReviewText TEXT NOT NULL, -- Text of the review
    Rating INT NOT NULL CHECK (Rating >= 1 AND Rating <= 5), -- Rating given by the customer (1 to 5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the review was last updated
    FOREIGN KEY (FabricID) REFERENCES PremiumFabrics(FabricID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Example of adding a product category
INSERT INTO ProductCategories (CategoryName, Description)
VALUES ('Cotton', 'High-quality cotton fabrics suitable for various uses.');

-- Example of adding a premium fabric
INSERT INTO PremiumFabrics (FabricName, CategoryID, Price, StockQuantity)
VALUES ('Organic Cotton', 1, 15.99, 100);

-- Example of adding a customer review
INSERT INTO CustomerReviews (FabricID, CustomerName, ReviewText, Rating)
VALUES (1, 'John Doe', 'Great quality fabric, very soft!', 5);
```
