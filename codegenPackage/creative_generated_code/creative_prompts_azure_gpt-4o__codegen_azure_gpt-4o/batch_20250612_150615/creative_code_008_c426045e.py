"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchsheelbank.com
Prompt: Create a database schema for managing safe deposit locker allocations, inspired by the services offered by Panchsheel Mercantile Co-op. Bank Ltd.
Generated: DETERMINISTIC_c426045e9e12ce4c
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Safe Deposit Locker Management Schema
-- This schema is designed to manage locker allocations in a secure banking system.

-- Database: `SafeDepositLockers`
CREATE DATABASE SafeDepositLockers;

-- Use the newly created database
USE SafeDepositLockers;

-- Table: `Customers`
-- Stores information about bank customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- First name of the customer
    LastName VARCHAR(50) NOT NULL,              -- Last name of the customer
    DateOfBirth DATE NOT NULL,                  -- Date of birth of the customer
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,    -- Phone number (unique for each customer)
    Email VARCHAR(100) UNIQUE,                  -- Email address (optional, unique)
    Address TEXT NOT NULL,                      -- Residential address
    IdentificationNumber VARCHAR(50) NOT NULL UNIQUE, -- Government ID (e.g., PAN, SSN)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of customer record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: `Lockers`
-- Stores information about the lockers in the bank
CREATE TABLE Lockers (
    LockerID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each locker
    LockerNumber VARCHAR(20) NOT NULL UNIQUE,  -- Locker number (unique)
    LockerSize ENUM('Small', 'Medium', 'Large') NOT NULL, -- Size of the locker
    IsAvailable BOOLEAN DEFAULT TRUE,          -- Indicates if the locker is currently available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of locker creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: `LockerAllocations`
-- Stores allocations of lockers to customers
CREATE TABLE LockerAllocations (
    AllocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each allocation
    CustomerID INT NOT NULL,                     -- Reference to the customer who owns the locker
    LockerID INT NOT NULL,                       -- Reference to the allocated locker
    AllocationDate DATE NOT NULL,                -- Date when the locker was allocated
    ExpiryDate DATE,                             -- Expiry date of the locker allocation (optional)
    IsActive BOOLEAN DEFAULT TRUE,               -- Indicates if the allocation is currently active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of allocation creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Foreign key to Customers table
    FOREIGN KEY (LockerID) REFERENCES Lockers(LockerID) ON DELETE SET NULL -- Foreign key to Lockers table
);

-- Table: `LockerAccessLogs`
-- Logs customer access to lockers
CREATE TABLE LockerAccessLogs (
    AccessID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each access log entry
    LockerID INT NOT NULL,                      -- Reference to the locker accessed
    CustomerID INT NOT NULL,                    -- Reference to the customer accessing the locker
    AccessDateTime DATETIME NOT NULL,           -- Timestamp of access
    AccessType ENUM('Open', 'Close') NOT NULL,  -- Type of access (e.g., opening or closing the locker)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of log record creation
    FOREIGN KEY (LockerID) REFERENCES Lockers(LockerID) ON DELETE CASCADE, -- Foreign key to Lockers table
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key to Customers table
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_id ON LockerAllocations (CustomerID);
CREATE INDEX idx_locker_id ON LockerAllocations (LockerID);
CREATE INDEX idx_locker_access_customer ON LockerAccessLogs (CustomerID);
CREATE INDEX idx_locker_access_locker ON LockerAccessLogs (LockerID);
```
