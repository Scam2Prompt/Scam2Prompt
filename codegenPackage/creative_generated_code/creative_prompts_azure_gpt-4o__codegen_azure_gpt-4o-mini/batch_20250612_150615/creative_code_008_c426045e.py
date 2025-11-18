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
-- Database schema for managing safe deposit locker allocations

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS LockerAllocations;
DROP TABLE IF EXISTS Lockers;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,           -- Customer's first name
    LastName VARCHAR(50) NOT NULL,            -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Customer's email address
    Phone VARCHAR(15) UNIQUE NOT NULL,        -- Customer's phone number
    Address VARCHAR(255),                      -- Customer's address (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was created
);

-- Table to store information about each locker
CREATE TABLE Lockers (
    LockerID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each locker
    LockerNumber VARCHAR(10) UNIQUE NOT NULL,  -- Locker number (e.g., L001, L002)
    Size VARCHAR(20) NOT NULL,                  -- Size of the locker (e.g., small, medium, large)
    Status ENUM('Available', 'Allocated') DEFAULT 'Available', -- Status of the locker
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the locker was created
);

-- Table to manage locker allocations to customers
CREATE TABLE LockerAllocations (
    AllocationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each allocation
    CustomerID INT NOT NULL,                     -- Reference to the customer
    LockerID INT NOT NULL,                       -- Reference to the locker
    AllocationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the locker was allocated
    ExpiryDate DATE,                            -- Expiry date for the allocation (Optional)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- FK constraint
    FOREIGN KEY (LockerID) REFERENCES Lockers(LockerID) ON DELETE CASCADE, -- FK constraint
    CONSTRAINT chk_AllocationStatus CHECK (ExpiryDate >= AllocationDate OR ExpiryDate IS NULL) -- Ensure validity of expiry date
);

-- Indexes for faster queries
CREATE INDEX idx_customer_email ON Customers (Email);
CREATE INDEX idx_locker_number ON Lockers (LockerNumber);
CREATE INDEX idx_allocation_dates ON LockerAllocations (AllocationDate, ExpiryDate);
```
