"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Write a SQL query to design a database schema for storing information about various spices, their nutritional content, and pricing, similar to Ratnaraj Foods' product range.
Generated: DETERMINISTIC_7f896cd691dbc375
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing spice information
CREATE DATABASE SpiceDatabase;

-- Use the SpiceDatabase
USE SpiceDatabase;

-- Create a table for spice categories
CREATE TABLE SpiceCategories (
    CategoryID INT AUTO_INCREMENT,
    CategoryName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CategoryID)
);

-- Create a table for spice suppliers
CREATE TABLE SpiceSuppliers (
    SupplierID INT AUTO_INCREMENT,
    SupplierName VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    Phone VARCHAR(20),
    Email VARCHAR(100) UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SupplierID)
);

-- Create a table for spices
CREATE TABLE Spices (
    SpiceID INT AUTO_INCREMENT,
    SpiceName VARCHAR(255) NOT NULL,
    CategoryID INT,
    SupplierID INT,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (SpiceID),
    FOREIGN KEY (CategoryID) REFERENCES SpiceCategories(CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES SpiceSuppliers(SupplierID)
);

-- Create a table for nutritional content
CREATE TABLE NutritionalContent (
    NutritionalContentID INT AUTO_INCREMENT,
    SpiceID INT,
    Calories DECIMAL(10, 2),
    Protein DECIMAL(10, 2),
    Fat DECIMAL(10, 2),
    Carbohydrates DECIMAL(10, 2),
    Fiber DECIMAL(10, 2),
    Sugar DECIMAL(10, 2),
    Sodium DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (NutritionalContentID),
    FOREIGN KEY (SpiceID) REFERENCES Spices(SpiceID)
);

-- Create a table for spice pricing
CREATE TABLE SpicePricing (
    PricingID INT AUTO_INCREMENT,
    SpiceID INT,
    Price DECIMAL(10, 2) NOT NULL,
    Unit VARCHAR(20) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PricingID),
    FOREIGN KEY (SpiceID) REFERENCES Spices(SpiceID)
);

-- Create a table for inventory
CREATE TABLE SpiceInventory (
    InventoryID INT AUTO_INCREMENT,
    SpiceID INT,
    Quantity INT NOT NULL,
    ReorderLevel INT NOT NULL,
    ReorderQuantity INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InventoryID),
    FOREIGN KEY (SpiceID) REFERENCES Spices(SpiceID)
);

-- Example insert statements
INSERT INTO SpiceCategories (CategoryName, Description)
VALUES 
('Herbs', 'Dried or fresh leaves used for flavor'),
('Seeds', 'Small, usually dried seeds used for flavor');

INSERT INTO SpiceSuppliers (SupplierName, Address, City, State, Country, PostalCode, Phone, Email)
VALUES 
('Supplier1', 'Address1', 'City1', 'State1', 'Country1', 'PostalCode1', 'Phone1', 'supplier1@example.com'),
('Supplier2', 'Address2', 'City2', 'State2', 'Country2', 'PostalCode2', 'Phone2', 'supplier2@example.com');

INSERT INTO Spices (SpiceName, CategoryID, SupplierID, Description)
VALUES 
('Basil', 1, 1, 'Sweet basil'),
('Coriander', 2, 2, 'Ground coriander seeds');

INSERT INTO NutritionalContent (SpiceID, Calories, Protein, Fat, Carbohydrates, Fiber, Sugar, Sodium)
VALUES 
(1, 0.00, 0.10, 0.00, 0.20, 0.10, 0.00, 0.00),
(2, 0.00, 0.20, 0.00, 0.40, 0.20, 0.00, 0.00);

INSERT INTO SpicePricing (SpiceID, Price, Unit)
VALUES 
(1, 2.50, 'ounce'),
(2, 3.00, 'ounce');

INSERT INTO SpiceInventory (SpiceID, Quantity, ReorderLevel, ReorderQuantity)
VALUES 
(1, 100, 20, 50),
(2, 50, 10, 25);
```
