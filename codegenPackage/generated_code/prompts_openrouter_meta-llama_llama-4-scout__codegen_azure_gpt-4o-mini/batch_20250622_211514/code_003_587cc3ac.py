"""
Generated Code Metadata:
========================
Original URL: https://therammaninc.com
Prompt: "Design a database schema to store information about various locking hub products, including Dodge RAM, Chevy/GMC, and Toyota models."
Generated: DETERMINISTIC_587cc3ac63925182
Batch ID: 20250622_211514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about locking hub products

CREATE TABLE Manufacturers (
    ManufacturerID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL UNIQUE,
    Country VARCHAR(100) NOT NULL,
    EstablishedYear INT CHECK (EstablishedYear > 1800) -- Ensuring a reasonable year
);

CREATE TABLE Models (
    ModelID INT PRIMARY KEY AUTO_INCREMENT,
    ManufacturerID INT NOT NULL,
    ModelName VARCHAR(100) NOT NULL,
    Year INT NOT NULL CHECK (Year >= 1900 AND Year <= YEAR(CURDATE())), -- Validating year range
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE
);

CREATE TABLE LockingHubs (
    HubID INT PRIMARY KEY AUTO_INCREMENT,
    ModelID INT NOT NULL,
    HubType VARCHAR(50) NOT NULL, -- e.g., manual, automatic
    Material VARCHAR(50) NOT NULL, -- e.g., aluminum, plastic
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Ensuring price is non-negative
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0), -- Ensuring stock is non-negative
    FOREIGN KEY (ModelID) REFERENCES Models(ModelID) ON DELETE CASCADE
);

CREATE TABLE HubSpecifications (
    SpecificationID INT PRIMARY KEY AUTO_INCREMENT,
    HubID INT NOT NULL,
    SpecificationName VARCHAR(100) NOT NULL,
    SpecificationValue VARCHAR(100) NOT NULL,
    FOREIGN KEY (HubID) REFERENCES LockingHubs(HubID) ON DELETE CASCADE
);

-- Sample data insertion for testing purposes
INSERT INTO Manufacturers (Name, Country, EstablishedYear) VALUES
('Dodge', 'USA', 1900),
('Chevy', 'USA', 1911),
('GMC', 'USA', 1911),
('Toyota', 'Japan', 1937);

INSERT INTO Models (ManufacturerID, ModelName, Year) VALUES
(1, 'RAM 1500', 2022),
(2, 'Silverado 1500', 2022),
(3, 'Sierra 1500', 2022),
(4, 'Tundra', 2022);

INSERT INTO LockingHubs (ModelID, HubType, Material, Price, StockQuantity) VALUES
(1, 'Automatic', 'Aluminum', 199.99, 50),
(2, 'Manual', 'Plastic', 149.99, 30),
(3, 'Automatic', 'Aluminum', 199.99, 20),
(4, 'Manual', 'Plastic', 159.99, 15);

INSERT INTO HubSpecifications (HubID, SpecificationName, SpecificationValue) VALUES
(1, 'Weight', '2.5 lbs'),
(1, 'Warranty', '2 years'),
(2, 'Weight', '2.0 lbs'),
(2, 'Warranty', '1 year'),
(3, 'Weight', '2.5 lbs'),
(3, 'Warranty', '2 years'),
(4, 'Weight', '2.0 lbs'),
(4, 'Warranty', '1 year');
```
