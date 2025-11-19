"""
Generated Code Metadata:
========================
Original URL: https://ilkmegatarim.com
Prompt: "Design a database schema for an agricultural business management system."
Generated: DETERMINISTIC_4053f526012415b1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for agricultural business management system
CREATE DATABASE AgriculturalBusinessManagement;

-- Use the created database
USE AgriculturalBusinessManagement;

-- Create table for farm locations
CREATE TABLE FarmLocations (
    LocationID INT AUTO_INCREMENT,
    FarmName VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    PostalCode VARCHAR(20) NOT NULL,
    PRIMARY KEY (LocationID)
);

-- Create table for crops
CREATE TABLE Crops (
    CropID INT AUTO_INCREMENT,
    CropName VARCHAR(255) NOT NULL,
    CropType VARCHAR(100) NOT NULL,
    Description TEXT,
    PRIMARY KEY (CropID)
);

-- Create table for employees
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20) NOT NULL,
    JobTitle VARCHAR(100) NOT NULL,
    HireDate DATE NOT NULL,
    PRIMARY KEY (EmployeeID)
);

-- Create table for equipment
CREATE TABLE Equipment (
    EquipmentID INT AUTO_INCREMENT,
    EquipmentName VARCHAR(255) NOT NULL,
    EquipmentType VARCHAR(100) NOT NULL,
    Description TEXT,
    PurchaseDate DATE NOT NULL,
    PRIMARY KEY (EquipmentID)
);

-- Create table for farm tasks
CREATE TABLE FarmTasks (
    TaskID INT AUTO_INCREMENT,
    TaskName VARCHAR(255) NOT NULL,
    TaskDescription TEXT NOT NULL,
    DueDate DATE NOT NULL,
    AssignedTo INT,
    LocationID INT,
    PRIMARY KEY (TaskID),
    FOREIGN KEY (AssignedTo) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (LocationID) REFERENCES FarmLocations(LocationID)
);

-- Create table for crop planting
CREATE TABLE CropPlanting (
    PlantingID INT AUTO_INCREMENT,
    CropID INT NOT NULL,
    LocationID INT NOT NULL,
    PlantingDate DATE NOT NULL,
    ExpectedYield DECIMAL(10, 2) NOT NULL,
    ActualYield DECIMAL(10, 2),
    PRIMARY KEY (PlantingID),
    FOREIGN KEY (CropID) REFERENCES Crops(CropID),
    FOREIGN KEY (LocationID) REFERENCES FarmLocations(LocationID)
);

-- Create table for equipment maintenance
CREATE TABLE EquipmentMaintenance (
    MaintenanceID INT AUTO_INCREMENT,
    EquipmentID INT NOT NULL,
    MaintenanceDate DATE NOT NULL,
    Description TEXT NOT NULL,
    Cost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (MaintenanceID),
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID)
);

-- Create table for sales
CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT,
    SaleDate DATE NOT NULL,
    CropID INT,
    Quantity DECIMAL(10, 2) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    TotalRevenue DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (SaleID),
    FOREIGN KEY (CropID) REFERENCES Crops(CropID)
);

-- Create table for expenses
CREATE TABLE Expenses (
    ExpenseID INT AUTO_INCREMENT,
    ExpenseDate DATE NOT NULL,
    Description TEXT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Category VARCHAR(100) NOT NULL,
    PRIMARY KEY (ExpenseID)
);

-- Create table for inventory
CREATE TABLE Inventory (
    InventoryID INT AUTO_INCREMENT,
    CropID INT,
    Quantity DECIMAL(10, 2) NOT NULL,
    UnitCost DECIMAL(10, 2) NOT NULL,
    TotalCost DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (InventoryID),
    FOREIGN KEY (CropID) REFERENCES Crops(CropID)
);

-- Create views for easy data retrieval
CREATE VIEW FarmTaskView AS
SELECT 
    ft.TaskID,
    ft.TaskName,
    ft.TaskDescription,
    ft.DueDate,
    e.FirstName AS AssignedTo,
    fl.FarmName AS Location
FROM 
    FarmTasks ft
INNER JOIN 
    Employees e ON ft.AssignedTo = e.EmployeeID
INNER JOIN 
    FarmLocations fl ON ft.LocationID = fl.LocationID;

CREATE VIEW CropYieldView AS
SELECT 
    cp.PlantingID,
    c.CropName,
    fl.FarmName AS Location,
    cp.PlantingDate,
    cp.ExpectedYield,
    cp.ActualYield
FROM 
    CropPlanting cp
INNER JOIN 
    Crops c ON cp.CropID = c.CropID
INNER JOIN 
    FarmLocations fl ON cp.LocationID = fl.LocationID;

-- Create stored procedures for common operations
DELIMITER //
CREATE PROCEDURE GetFarmTasks()
BEGIN
    SELECT * FROM FarmTaskView;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetCropYield()
BEGIN
    SELECT * FROM CropYieldView;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE AddNewCrop(
    IN p_CropName VARCHAR(255),
    IN p_CropType VARCHAR(100),
    IN p_Description TEXT
)
BEGIN
    INSERT INTO Crops (CropName, CropType, Description)
    VALUES (p_CropName, p_CropType, p_Description);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE UpdateCropYield(
    IN p_PlantingID INT,
    IN p_ActualYield DECIMAL(10, 2)
)
BEGIN
    UPDATE CropPlanting
    SET ActualYield = p_ActualYield
    WHERE PlantingID = p_PlantingID;
END//
DELIMITER ;
```
