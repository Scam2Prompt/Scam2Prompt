"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Design a database schema for a restaurant that includes tables for menus, wines, and reservations, taking cues from Bodega Jean Bousquet's structure.
Generated: DETERMINISTIC_5caa338f92f6e32b
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for restaurant
CREATE DATABASE RestaurantDB;

-- Use the created database
USE RestaurantDB;

-- Create table for menus
CREATE TABLE Menus (
    MenuID INT AUTO_INCREMENT,
    MenuName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MenuID)
);

-- Create table for menu items
CREATE TABLE MenuItems (
    MenuItemID INT AUTO_INCREMENT,
    MenuID INT NOT NULL,
    ItemName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MenuItemID),
    FOREIGN KEY (MenuID) REFERENCES Menus(MenuID) ON DELETE CASCADE
);

-- Create table for wines
CREATE TABLE Wines (
    WineID INT AUTO_INCREMENT,
    WineName VARCHAR(255) NOT NULL,
    Vintage INT,
    GrapeVariety VARCHAR(100),
    Region VARCHAR(100),
    Price DECIMAL(10, 2),
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (WineID)
);

-- Create table for wine list
CREATE TABLE WineList (
    WineListID INT AUTO_INCREMENT,
    MenuID INT NOT NULL,
    WineID INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (WineListID),
    FOREIGN KEY (MenuID) REFERENCES Menus(MenuID) ON DELETE CASCADE,
    FOREIGN KEY (WineID) REFERENCES Wines(WineID) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for reservations
CREATE TABLE Reservations (
    ReservationID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ReservationDate DATE NOT NULL,
    ReservationTime TIME NOT NULL,
    PartySize INT NOT NULL,
    SpecialRequests TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReservationID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Create table for tables
CREATE TABLE Tables (
    TableID INT AUTO_INCREMENT,
    TableNumber INT NOT NULL,
    Capacity INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TableID)
);

-- Create table for reservation assignments
CREATE TABLE ReservationAssignments (
    ReservationAssignmentID INT AUTO_INCREMENT,
    ReservationID INT NOT NULL,
    TableID INT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ReservationAssignmentID),
    FOREIGN KEY (ReservationID) REFERENCES Reservations(ReservationID) ON DELETE CASCADE,
    FOREIGN KEY (TableID) REFERENCES Tables(TableID) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO Menus (MenuName, Description, Price)
VALUES 
('Appetizers', 'Delicious starters', 10.99),
('Entrees', 'Tasty main courses', 19.99),
('Desserts', 'Sweet treats', 7.99);

INSERT INTO MenuItems (MenuID, ItemName, Description, Price)
VALUES 
(1, 'Bruschetta', 'Toasted bread with tomatoes', 6.99),
(1, 'Calamari', 'Fried squid rings', 8.99),
(2, 'Grilled Steak', 'Tender steak with roasted vegetables', 24.99),
(3, 'Tiramisu', 'Coffee-soaked ladyfingers', 8.99);

INSERT INTO Wines (WineName, Vintage, GrapeVariety, Region, Price, Description)
VALUES 
('Cabernet Sauvignon', 2015, 'Cabernet Sauvignon', 'Napa Valley', 49.99, 'Full-bodied red wine'),
('Merlot', 2018, 'Merlot', 'Bordeaux', 29.99, 'Smooth red wine'),
('Chardonnay', 2017, 'Chardonnay', 'Sonoma County', 39.99, 'Buttery white wine');

INSERT INTO WineList (MenuID, WineID)
VALUES 
(1, 1),
(1, 2),
(2, 3);

INSERT INTO Customers (FirstName, LastName, Email, Phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO Reservations (CustomerID, ReservationDate, ReservationTime, PartySize, SpecialRequests)
VALUES 
(1, '2024-09-17', '18:00:00', 4, 'Birthday celebration'),
(2, '2024-09-18', '19:00:00', 2, NULL);

INSERT INTO Tables (TableNumber, Capacity)
VALUES 
(1, 4),
(2, 6),
(3, 2);

INSERT INTO ReservationAssignments (ReservationID, TableID)
VALUES 
(1, 1),
(2, 3);
```
