"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: "Design a database schema to store information about different types of fibers, including fiberglass, ceramic fiber, and carbon fiber chopped, and their applications."
Generated: DETERMINISTIC_05108fbb8afc7340
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema to store information about different types of fibers and their applications

-- Create a database
CREATE DATABASE FiberDatabase;

-- Use the database
USE FiberDatabase;

-- Create a table to store fiber types
CREATE TABLE FiberTypes (
    FiberTypeID INT AUTO_INCREMENT,
    FiberTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (FiberTypeID)
);

-- Create a table to store fiber properties
CREATE TABLE FiberProperties (
    FiberPropertyID INT AUTO_INCREMENT,
    FiberTypeID INT NOT NULL,
    TensileStrength DECIMAL(10, 2),
    ElasticModulus DECIMAL(10, 2),
    ThermalConductivity DECIMAL(10, 2),
    MaxTemperature DECIMAL(10, 2),
    PRIMARY KEY (FiberPropertyID),
    FOREIGN KEY (FiberTypeID) REFERENCES FiberTypes(FiberTypeID)
);

-- Create a table to store applications
CREATE TABLE Applications (
    ApplicationID INT AUTO_INCREMENT,
    ApplicationName VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (ApplicationID)
);

-- Create a table to store fiber applications
CREATE TABLE FiberApplications (
    FiberApplicationID INT AUTO_INCREMENT,
    FiberTypeID INT NOT NULL,
    ApplicationID INT NOT NULL,
    PRIMARY KEY (FiberApplicationID),
    FOREIGN KEY (FiberTypeID) REFERENCES FiberTypes(FiberTypeID),
    FOREIGN KEY (ApplicationID) REFERENCES Applications(ApplicationID)
);

-- Create a table to store manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT,
    ManufacturerName VARCHAR(255) NOT NULL,
    PRIMARY KEY (ManufacturerID)
);

-- Create a table to store fiber products
CREATE TABLE FiberProducts (
    FiberProductID INT AUTO_INCREMENT,
    FiberTypeID INT NOT NULL,
    ManufacturerID INT NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    PRIMARY KEY (FiberProductID),
    FOREIGN KEY (FiberTypeID) REFERENCES FiberTypes(FiberTypeID),
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID)
);

-- Insert sample data
INSERT INTO FiberTypes (FiberTypeName, Description)
VALUES 
('Fiberglass', 'A type of fiber made from glass'),
('Ceramic Fiber', 'A type of fiber made from ceramic materials'),
('Carbon Fiber Chopped', 'A type of fiber made from chopped carbon fibers');

INSERT INTO FiberProperties (FiberTypeID, TensileStrength, ElasticModulus, ThermalConductivity, MaxTemperature)
VALUES 
(1, 1000.00, 5000.00, 0.05, 600.00),
(2, 800.00, 4000.00, 0.03, 1000.00),
(3, 2000.00, 10000.00, 0.01, 800.00);

INSERT INTO Applications (ApplicationName, Description)
VALUES 
('Composites', 'Used in composite materials'),
('Insulation', 'Used in insulation applications'),
('Aerospace', 'Used in aerospace industry');

INSERT INTO FiberApplications (FiberTypeID, ApplicationID)
VALUES 
(1, 1),
(1, 2),
(2, 2),
(3, 3);

INSERT INTO Manufacturers (ManufacturerName)
VALUES 
('Owens Corning'),
('3M'),
('Toray Industries');

INSERT INTO FiberProducts (FiberTypeID, ManufacturerID, ProductName)
VALUES 
(1, 1, 'Fiberglass Chopped Strand'),
(2, 2, 'Ceramic Fiber Blanket'),
(3, 3, 'Carbon Fiber Chopped Strand');
```
