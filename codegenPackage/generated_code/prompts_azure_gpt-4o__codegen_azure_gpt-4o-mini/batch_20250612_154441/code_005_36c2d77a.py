"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Create a database schema to store information about various rubber flooring products (e.g., Eva Mats, EPDM) and their applications in areas like parking lots and sports fields, based on Rubber Flooring Indonesia's offerings.
Generated: DETERMINISTIC_36c2d77a4679e445
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about rubber flooring products

CREATE DATABASE RubberFlooringDB;

USE RubberFlooringDB;

-- Table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store rubber flooring products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100) NOT NULL,
    CategoryID INT,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL
);

-- Table to store applications of the products
CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY,
    ApplicationName VARCHAR(100) NOT NULL UNIQUE,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to link products to their applications
CREATE TABLE ProductApplications (
    ProductApplicationID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT,
    ApplicationID INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (ApplicationID) REFERENCES Applications(ApplicationID) ON DELETE CASCADE,
    UNIQUE (ProductID, ApplicationID) -- Prevent duplicate entries
);

-- Table to store product reviews
CREATE TABLE ProductReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT,
    ReviewText TEXT,
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating must be between 1 and 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Sample data insertion for categories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Eva Mats', 'High-density foam mats suitable for various applications.'),
('EPDM', 'Durable rubber flooring ideal for outdoor use.');

-- Sample data insertion for applications
INSERT INTO Applications (ApplicationName, Description) VALUES
('Parking Lots', 'Rubber flooring suitable for vehicle traffic.'),
('Sports Fields', 'Durable flooring for athletic activities.');

-- Sample data insertion for products
INSERT INTO Products (ProductName, CategoryID, Description, Price, StockQuantity) VALUES
('Eva Mat - Standard', 1, 'Standard Eva mat for indoor use.', 25.00, 100),
('EPDM - Outdoor', 2, 'EPDM flooring for outdoor sports fields.', 50.00, 50);

-- Sample data insertion for product applications
INSERT INTO ProductApplications (ProductID, ApplicationID) VALUES
(1, 1), -- Eva Mat - Standard for Parking Lots
(2, 2); -- EPDM - Outdoor for Sports Fields
```
