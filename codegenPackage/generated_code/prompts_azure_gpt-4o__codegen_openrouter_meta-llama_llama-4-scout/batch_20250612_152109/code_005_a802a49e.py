"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Create a database schema in SQL for managing a catalog of flip-flop products, including fields for product name, category, material type, and customization options.
Generated: DETERMINISTIC_a802a49eb2817f7a
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for managing flip-flop products
CREATE DATABASE FlipFlopCatalog;

-- Use the FlipFlopCatalog database
USE FlipFlopCatalog;

-- Create a table for product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create a table for material types
CREATE TABLE Materials (
    MaterialID INT AUTO_INCREMENT,
    MaterialName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MaterialID)
);

-- Create a table for customization options
CREATE TABLE CustomizationOptions (
    OptionID INT AUTO_INCREMENT,
    OptionName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OptionID)
);

-- Create a table for product customization option mappings
CREATE TABLE ProductCustomizationOptions (
    ProductID INT,
    OptionID INT,
    PRIMARY KEY (ProductID, OptionID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (OptionID) REFERENCES CustomizationOptions(OptionID)
);

-- Create a table for flip-flop products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    CategoryID INT,
    MaterialID INT,
    Price DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProductID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID)
);

-- Create indexes for foreign key columns
CREATE INDEX idx_CategoryID ON Products(CategoryID);
CREATE INDEX idx_MaterialID ON Products(MaterialID);
CREATE INDEX idx_ProductID ON ProductCustomizationOptions(ProductID);
CREATE INDEX idx_OptionID ON ProductCustomizationOptions(OptionID);

-- Example insert statements
INSERT INTO Categories (CategoryName, Description)
VALUES 
('Beach Flip Flops', 'Flip flops for beach activities'),
('Casual Flip Flops', 'Flip flops for everyday wear');

INSERT INTO Materials (MaterialName, Description)
VALUES 
('Rubber', 'Durable and water-resistant rubber material'),
('EVA', 'Lightweight and cushioned EVA material');

INSERT INTO CustomizationOptions (OptionName, Description)
VALUES 
('Color', 'Choose from various colors'),
('Size', 'Choose from various sizes');

INSERT INTO Products (ProductName, CategoryID, MaterialID, Price, Description)
VALUES 
('Beach Buddy', 1, 1, 9.99, 'A pair of beach flip flops made from rubber'),
('Casual Cruiser', 2, 2, 12.99, 'A pair of casual flip flops made from EVA');

INSERT INTO ProductCustomizationOptions (ProductID, OptionID)
VALUES 
(1, 1),
(1, 2),
(2, 1);
```
