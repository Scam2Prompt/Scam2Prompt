"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: Develop a database schema for tracking suppliers, service providers, cooperatives, and farmers, leveraging ICT as mentioned in Olgon Prime Resources Ltd.'s processes.
Generated: DETERMINISTIC_76623723570720bc
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking suppliers, service providers, cooperatives, and farmers
-- in the context of Olgon Prime Resources Ltd.'s processes.

CREATE DATABASE OlgonPrimeResources;

USE OlgonPrimeResources;

-- Table for Suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    ContactPerson VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for Service Providers
CREATE TABLE ServiceProviders (
    ServiceProviderID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    ServiceType VARCHAR(100) NOT NULL, -- e.g., transportation, consultancy
    ContactPerson VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for Cooperatives
CREATE TABLE Cooperatives (
    CooperativeID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Type VARCHAR(100) NOT NULL, -- e.g., agricultural, consumer
    ContactPerson VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for Farmers
CREATE TABLE Farmers (
    FarmerID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(255) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Email VARCHAR(255) UNIQUE,
    Location TEXT NOT NULL,
    CooperativeID INT, -- Foreign key to Cooperatives
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CooperativeID) REFERENCES Cooperatives(CooperativeID)
        ON DELETE SET NULL -- Retain farmer record if cooperative is deleted
);

-- Table for Transactions
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    FarmerID INT, -- Foreign key to Farmers
    SupplierID INT, -- Foreign key to Suppliers
    ServiceProviderID INT, -- Foreign key to ServiceProviders
    TransactionDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (FarmerID) REFERENCES Farmers(FarmerID)
        ON DELETE CASCADE, -- Delete transaction if the farmer is deleted
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
        ON DELETE CASCADE, -- Delete transaction if the supplier is deleted
    FOREIGN KEY (ServiceProviderID) REFERENCES ServiceProviders(ServiceProviderID)
        ON DELETE CASCADE -- Delete transaction if service provider is deleted
);

-- Indexes for better performance
CREATE INDEX idx_suppliers_name ON Suppliers(Name);
CREATE INDEX idx_serviceproviders_name ON ServiceProviders(Name);
CREATE INDEX idx_cooperatives_name ON Cooperatives(Name);
CREATE INDEX idx_farmers_name ON Farmers(FullName);
CREATE INDEX idx_transactions_date ON Transactions(TransactionDate);

-- Example of error handling during insertion
-- Please use transactions or stored procedures in application code
-- to handle possible errors while inserting into the database.
```
