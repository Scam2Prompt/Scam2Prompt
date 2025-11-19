"""
Generated Code Metadata:
========================
Original URL: https://puroworldclub.com
Prompt: Develop a simple database schema to store information about cigar products, including origin, type, and pricing, inspired by the Puro World Club's product offerings.
Generated: DETERMINISTIC_b26638472193518c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for cigar products

-- Create a database
CREATE DATABASE CigarDatabase;

-- Use the database
USE CigarDatabase;

-- Create a table for countries of origin
CREATE TABLE Countries (
    CountryID INT AUTO_INCREMENT,
    CountryName VARCHAR(255) NOT NULL,
    PRIMARY KEY (CountryID)
);

-- Create a table for cigar types
CREATE TABLE CigarTypes (
    CigarTypeID INT AUTO_INCREMENT,
    CigarTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (CigarTypeID)
);

-- Create a table for cigar products
CREATE TABLE CigarProducts (
    CigarID INT AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    CountryID INT,
    CigarTypeID INT,
    Price DECIMAL(10, 2) NOT NULL,
    Size VARCHAR(50),
    Wrapper VARCHAR(50),
    Binder VARCHAR(50),
    Filler VARCHAR(50),
    PRIMARY KEY (CigarID),
    FOREIGN KEY (CountryID) REFERENCES Countries(CountryID),
    FOREIGN KEY (CigarTypeID) REFERENCES CigarTypes(CigarTypeID)
);

-- Create a table for product ratings
CREATE TABLE ProductRatings (
    RatingID INT AUTO_INCREMENT,
    CigarID INT,
    Rating TINYINT NOT NULL,
    Review TEXT,
    PRIMARY KEY (RatingID),
    FOREIGN KEY (CigarID) REFERENCES CigarProducts(CigarID),
    CHECK (Rating BETWEEN 1 AND 5)
);

-- Create a table for product inventory
CREATE TABLE ProductInventory (
    InventoryID INT AUTO_INCREMENT,
    CigarID INT,
    Quantity INT NOT NULL DEFAULT 0,
    PRIMARY KEY (InventoryID),
    FOREIGN KEY (CigarID) REFERENCES CigarProducts(CigarID)
);

-- Insert sample data
INSERT INTO Countries (CountryName) 
VALUES 
('Cuba'),
('Dominican Republic'),
('Nicaragua'),
('Honduras'),
('Mexico');

INSERT INTO CigarTypes (CigarTypeName, Description) 
VALUES 
('Robusto', 'A classic robusto cigar'),
('Toro', 'A toro cigar with a rich flavor'),
('Corona', 'A corona cigar with a smooth taste');

INSERT INTO CigarProducts (ProductName, CountryID, CigarTypeID, Price, Size, Wrapper, Binder, Filler) 
VALUES 
('Cigar 1', 1, 1, 10.99, '5 x 50', 'Natural', 'Tobacco', 'Tobacco'),
('Cigar 2', 2, 2, 12.99, '6 x 52', 'Maduro', 'Tobacco', 'Tobacco'),
('Cigar 3', 3, 3, 9.99, '5 x 42', 'Natural', 'Tobacco', 'Tobacco');

INSERT INTO ProductRatings (CigarID, Rating, Review) 
VALUES 
(1, 5, 'Excellent cigar'),
(2, 4, 'Good but not great'),
(3, 5, 'Love this cigar');

INSERT INTO ProductInventory (CigarID, Quantity) 
VALUES 
(1, 100),
(2, 50),
(3, 200);
```
