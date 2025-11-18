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
-- Database Schema for Suzuki Capital Motors' Certified Used Car Program

-- Table: CarModels
-- Stores information about the car models available in the program
CREATE TABLE CarModels (
    ModelID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each car model
    Make VARCHAR(50) NOT NULL,              -- Manufacturer (e.g., Suzuki)
    Model VARCHAR(50) NOT NULL,             -- Model name of the car
    Year INT NOT NULL,                      -- Manufacturing year
    BodyType VARCHAR(50),                   -- Type of body (e.g., Sedan, SUV)
    EngineType VARCHAR(50),                 -- Type of engine (e.g., Petrol, Diesel, Hybrid)
    Transmission VARCHAR(50),               -- Type of transmission (e.g., Manual, Automatic)
    Color VARCHAR(50)                       -- Color of the car
);

-- Table: Evaluations
-- Stores details about the evaluation of certified used cars
CREATE TABLE Evaluations (
    EvaluationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the evaluation
    ModelID INT NOT NULL,                        -- Foreign key linking to CarModels
    Mileage INT NOT NULL,                        -- Mileage of the car in kilometers
    Condition VARCHAR(50) NOT NULL,             -- Condition of the car (e.g., Excellent, Good, Average)
    EvaluationDate DATE NOT NULL,               -- Date of evaluation
    EvaluatorName VARCHAR(100),                 -- Name of the evaluator
    FOREIGN KEY (ModelID) REFERENCES CarModels(ModelID) -- Ensures integrity between tables
);

-- Table: WarrantyInfo
-- Stores warranty details for certified used cars
CREATE TABLE WarrantyInfo (
    WarrantyID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for the warranty
    ModelID INT NOT NULL,                          -- Foreign key linking to CarModels
    WarrantyPeriod INT NOT NULL,                  -- Warranty period in months
    WarrantyCoverage VARCHAR(255) NOT NULL,       -- Coverage details (e.g., Engine, Transmission)
    FOREIGN KEY (ModelID) REFERENCES CarModels(ModelID) -- Ensures integrity between tables
);

-- Table: CustomerTransactions
-- Stores details of transactions with customers
CREATE TABLE CustomerTransactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for the transaction
    CustomerName VARCHAR(100) NOT NULL,           -- Name of the customer
    ContactInfo VARCHAR(100) NOT NULL,            -- Contact information (e.g., phone or email)
    ModelID INT NOT NULL,                         -- Foreign key linking to CarModels
    PurchaseDate DATE NOT NULL,                   -- Date of purchase
    Price DECIMAL(10, 2) NOT NULL,                -- Price paid for the car
    WarrantyID INT,                               -- Foreign key linking to WarrantyInfo
    FOREIGN KEY (ModelID) REFERENCES CarModels(ModelID), -- Ensures integrity between tables
    FOREIGN KEY (WarrantyID) REFERENCES WarrantyInfo(WarrantyID) -- Ensures integrity between tables
);

-- Adding indexes for faster querying
CREATE INDEX idx_CarModels_Make ON CarModels(Make);
CREATE INDEX idx_CarModels_Model ON CarModels(Model);
CREATE INDEX idx_Evaluations_ModelID ON Evaluations(ModelID);
CREATE INDEX idx_WarrantyInfo_ModelID ON WarrantyInfo(ModelID);
CREATE INDEX idx_CustomerTransactions_CustomerName ON CustomerTransactions(CustomerName);
CREATE INDEX idx_CustomerTransactions_ModelID ON CustomerTransactions(ModelID);
```
