"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Design a database schema in SQL for managing Suzuki Capital Motors' Certified Used Car Program, including tables for car models, evaluation details, warranty information, and customer transactions.
Generated: DETERMINISTIC_8d83dde97fa84b15
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Suzuki Capital Motors' Certified Used Car Program

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CustomerTransactions;
DROP TABLE IF EXISTS WarrantyInformation;
DROP TABLE IF EXISTS EvaluationDetails;
DROP TABLE IF EXISTS CarModels;

-- Table to store car model information
CREATE TABLE CarModels (
    ModelID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each car model
    Make VARCHAR(50) NOT NULL,              -- Manufacturer of the car
    Model VARCHAR(50) NOT NULL,             -- Model name of the car
    Year INT NOT NULL,                       -- Year of manufacture
    EngineType VARCHAR(50),                  -- Type of engine (e.g., petrol, diesel, electric)
    TransmissionType VARCHAR(50),            -- Type of transmission (e.g., automatic, manual)
    Color VARCHAR(30),                       -- Color of the car
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store evaluation details of the cars
CREATE TABLE EvaluationDetails (
    EvaluationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each evaluation
    ModelID INT NOT NULL,                        -- Foreign key referencing CarModels
    EvaluationDate DATE NOT NULL,                -- Date of evaluation
    ConditionRating INT CHECK (ConditionRating BETWEEN 1 AND 10), -- Condition rating (1-10 scale)
    Comments TEXT,                               -- Additional comments about the evaluation
    FOREIGN KEY (ModelID) REFERENCES CarModels(ModelID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store warranty information for the cars
CREATE TABLE WarrantyInformation (
    WarrantyID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each warranty
    ModelID INT NOT NULL,                        -- Foreign key referencing CarModels
    WarrantyPeriod INT NOT NULL,                 -- Warranty period in months
    StartDate DATE NOT NULL,                     -- Start date of the warranty
    EndDate DATE NOT NULL,                       -- End date of the warranty
    FOREIGN KEY (ModelID) REFERENCES CarModels(ModelID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer transactions
CREATE TABLE CustomerTransactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each transaction
    ModelID INT NOT NULL,                         -- Foreign key referencing CarModels
    CustomerName VARCHAR(100) NOT NULL,          -- Name of the customer
    TransactionDate DATE NOT NULL,                -- Date of the transaction
    SalePrice DECIMAL(10, 2) NOT NULL,           -- Sale price of the car
    PaymentMethod VARCHAR(50),                    -- Payment method (e.g., cash, financing)
    FOREIGN KEY (ModelID) REFERENCES CarModels(ModelID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_car_model ON CarModels (Make, Model);
CREATE INDEX idx_evaluation_model ON EvaluationDetails (ModelID);
CREATE INDEX idx_warranty_model ON WarrantyInformation (ModelID);
CREATE INDEX idx_transaction_model ON CustomerTransactions (ModelID);
```
