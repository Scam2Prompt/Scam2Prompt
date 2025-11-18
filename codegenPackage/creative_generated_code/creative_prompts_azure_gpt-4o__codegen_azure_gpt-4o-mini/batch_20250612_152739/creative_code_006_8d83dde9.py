"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suzuki-capital.com
Prompt: Design a database schema in SQL for managing Suzuki Capital Motors' Certified Used Car Program, including tables for car models, evaluation details, warranty information, and customer transactions.
Generated: DETERMINISTIC_8d83dde97fa84b15
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing Suzuki Capital Motors' Certified Used Car Program

-- Create a schema for the program
CREATE SCHEMA SuzukiCertifiedUsedCars;

-- Table to store car models information
CREATE TABLE SuzukiCertifiedUsedCars.CarModels (
    ModelID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each car model
    ModelName VARCHAR(100) NOT NULL,                 -- Name of the car model
    Year INT CHECK(Year >= 1886 AND Year <= YEAR(CURDATE())), -- Year must be realistic
    Manufacturer VARCHAR(100) NOT NULL,              -- Manufacturer of the car
    EngineType VARCHAR(50),                           -- Type of engine (e.g., Petrol, Diesel, Electric)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);

-- Table to store evaluation details for each car
CREATE TABLE SuzukiCertifiedUsedCars.EvaluationDetails (
    EvaluationID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each evaluation
    ModelID INT NOT NULL,                             -- Foreign key reference to CarModels
    EvaluationDate DATE NOT NULL,                     -- Date of the evaluation
    ConditionRating INT CHECK(ConditionRating BETWEEN 1 AND 5), -- Rating of the car's condition
    Comments TEXT,                                    -- Additional comments about the evaluation
    FOREIGN KEY (ModelID) REFERENCES SuzukiCertifiedUsedCars.CarModels(ModelID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store warranty information for each certified car
CREATE TABLE SuzukiCertifiedUsedCars.WarrantyInfo (
    WarrantyID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each warranty
    ModelID INT NOT NULL,                             -- Foreign key reference to CarModels
    WarrantyPeriod INT NOT NULL,                      -- Warranty period in months
    WarrantyDetails TEXT,                             -- Description of warranty coverage
    ExpirationDate DATE,                              -- Expiration date of the warranty
    FOREIGN KEY (ModelID) REFERENCES SuzukiCertifiedUsedCars.CarModels(ModelID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer transactions related to car purchases
CREATE TABLE SuzukiCertifiedUsedCars.CustomerTransactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each transaction
    ModelID INT NOT NULL,                             -- Foreign key reference to CarModels
    CustomerID INT NOT NULL,                          -- Foreign key reference to Customers (assumed to be another table)
    PurchaseDate DATE NOT NULL,                       -- Date of the transaction
    SalePrice DECIMAL(10, 2) NOT NULL,               -- Sale price of the car
    PaymentMethod ENUM('Cash', 'Finance', 'Lease') NOT NULL, -- Payment method used
    FOREIGN KEY (ModelID) REFERENCES SuzukiCertifiedUsedCars.CarModels(ModelID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CustomerID) REFERENCES SuzukiCertifiedUsedCars.Customers(CustomerID) ON DELETE CASCADE -- Assuming Customers table exists
);

-- Assuming a table for customers would also be needed
CREATE TABLE SuzukiCertifiedUsedCars.Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,                   -- Customer's first name
    LastName VARCHAR(50) NOT NULL,                    -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,               -- Customer's email address
    PhoneNumber VARCHAR(15),                           -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for updates
);
```
