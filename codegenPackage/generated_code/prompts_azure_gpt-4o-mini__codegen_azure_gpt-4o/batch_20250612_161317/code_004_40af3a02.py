"""
Generated Code Metadata:
========================
Original URL: https://uniair.id
Prompt: Construct a sample database schema for managing logistics services like trucking, warehousing, and distribution, based on the offerings of Uniair Cargo.
Generated: DETERMINISTIC_40af3a0200158197
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Managing Logistics Services

-- Table to store information about customers
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    Name VARCHAR(255) NOT NULL,                -- Customer's name
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(20),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store trucking services
CREATE TABLE TruckingServices (
    TruckingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each trucking service
    TruckNumber VARCHAR(50) NOT NULL,          -- Unique truck number
    DriverName VARCHAR(255) NOT NULL,          -- Name of the driver
    CapacityInTons DECIMAL(10, 2) NOT NULL,    -- Truck capacity in tons
    Status ENUM('Available', 'In Transit', 'Under Maintenance') DEFAULT 'Available', -- Truck status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store warehousing services
CREATE TABLE Warehouses (
    WarehouseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each warehouse
    Location VARCHAR(255) NOT NULL,             -- Warehouse location
    CapacityInCubicMeters DECIMAL(10, 2) NOT NULL, -- Warehouse capacity in cubic meters
    CurrentOccupancy DECIMAL(10, 2) DEFAULT 0,  -- Current occupancy in cubic meters
    ManagerName VARCHAR(255),                   -- Name of the warehouse manager
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store distribution services
CREATE TABLE DistributionServices (
    DistributionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each distribution service
    CustomerID INT NOT NULL,                       -- Reference to the customer
    Origin VARCHAR(255) NOT NULL,                  -- Origin location
    Destination VARCHAR(255) NOT NULL,             -- Destination location
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Distribution status
    EstimatedDeliveryDate DATE,                    -- Estimated delivery date
    ActualDeliveryDate DATE,                       -- Actual delivery date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to track trucking assignments for distribution services
CREATE TABLE TruckingAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    DistributionID INT NOT NULL,                 -- Reference to the distribution service
    TruckingID INT NOT NULL,                     -- Reference to the trucking service
    AssignedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the truck was assigned
    FOREIGN KEY (DistributionID) REFERENCES DistributionServices(DistributionID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (TruckingID) REFERENCES TruckingServices(TruckingID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to track warehouse storage for distribution services
CREATE TABLE WarehouseStorage (
    StorageID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each storage record
    DistributionID INT NOT NULL,              -- Reference to the distribution service
    WarehouseID INT NOT NULL,                 -- Reference to the warehouse
    StoredVolume DECIMAL(10, 2) NOT NULL,     -- Volume stored in cubic meters
    StorageStartDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Start date of storage
    StorageEndDate TIMESTAMP,                 -- End date of storage
    FOREIGN KEY (DistributionID) REFERENCES DistributionServices(DistributionID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (WarehouseID) REFERENCES Warehouses(WarehouseID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to log service transactions
CREATE TABLE ServiceTransactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each transaction
    CustomerID INT NOT NULL,                      -- Reference to the customer
    ServiceType ENUM('Trucking', 'Warehousing', 'Distribution') NOT NULL, -- Type of service
    ServiceID INT NOT NULL,                       -- Reference to the specific service
    Amount DECIMAL(10, 2) NOT NULL,               -- Transaction amount
    TransactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);
```
