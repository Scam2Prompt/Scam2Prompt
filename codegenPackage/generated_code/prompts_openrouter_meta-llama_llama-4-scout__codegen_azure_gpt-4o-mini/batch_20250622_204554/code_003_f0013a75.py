"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: "Design a database schema to store information about ITACA CERAMIC's tile products, including product categories, sizes, materials, and features, and provide a SQL code snippet to populate the database with sample data."
Generated: DETERMINISTIC_f0013a759ad27848
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ITACA CERAMIC's tile products

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT
);

-- Create a table for materials
CREATE TABLE Materials (
    MaterialID INT PRIMARY KEY AUTO_INCREMENT,
    MaterialName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT
);

-- Create a table for sizes
CREATE TABLE Sizes (
    SizeID INT PRIMARY KEY AUTO_INCREMENT,
    SizeName VARCHAR(50) NOT NULL UNIQUE,
    Dimensions VARCHAR(50) NOT NULL
);

-- Create a table for features
CREATE TABLE Features (
    FeatureID INT PRIMARY KEY AUTO_INCREMENT,
    FeatureName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    CategoryID INT,
    MaterialID INT,
    SizeID INT,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID),
    FOREIGN KEY (MaterialID) REFERENCES Materials(MaterialID),
    FOREIGN KEY (SizeID) REFERENCES Sizes(SizeID)
);

-- Sample data insertion for ProductCategories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Ceramic', 'High-quality ceramic tiles suitable for various applications.'),
('Porcelain', 'Durable porcelain tiles with a variety of finishes.'),
('Glass', 'Elegant glass tiles for decorative purposes.');

-- Sample data insertion for Materials
INSERT INTO Materials (MaterialName, Description) VALUES
('Clay', 'Natural clay used for ceramic tiles.'),
('Stone', 'Natural stone materials for a rustic look.'),
('Recycled Glass', 'Eco-friendly tiles made from recycled glass.');

-- Sample data insertion for Sizes
INSERT INTO Sizes (SizeName, Dimensions) VALUES
('Small', '30x30 cm'),
('Medium', '60x60 cm'),
('Large', '120x60 cm');

-- Sample data insertion for Features
INSERT INTO Features (FeatureName, Description) VALUES
('Water Resistant', 'Tiles that resist water absorption.'),
('Slip Resistant', 'Tiles designed to prevent slipping.'),
('Frost Resistant', 'Tiles that withstand freezing temperatures.');

-- Sample data insertion for Products
INSERT INTO Products (ProductName, CategoryID, MaterialID, SizeID, Price, StockQuantity) VALUES
('Classic White Ceramic Tile', 1, 1, 1, 2.50, 100),
('Elegant Black Porcelain Tile', 2, 2, 2, 3.75, 50),
('Modern Glass Mosaic Tile', 3, 3, 1, 5.00, 200);
```
