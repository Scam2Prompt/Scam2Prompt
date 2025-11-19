"""
Generated Code Metadata:
========================
Original URL: https://ankarateknikservisi.com
Prompt: Create a database schema in SQL for storing customer information, appliance details (brand, type, issue), and service history, tailored for a business like Ankara Teknik Servisi.
Generated: DETERMINISTIC_c7af632539320f46
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ankara Teknik Servisi

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ServiceHistory;
DROP TABLE IF EXISTS Appliances;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,     -- Customer's phone number, must be unique
    Email VARCHAR(100) UNIQUE,                    -- Customer's email address, must be unique
    Address VARCHAR(255),                         -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the customer was added
);

-- Table to store appliance details
CREATE TABLE Appliances (
    ApplianceID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each appliance
    CustomerID INT NOT NULL,                      -- Foreign key referencing the customer
    Brand VARCHAR(50) NOT NULL,                   -- Brand of the appliance
    Type VARCHAR(50) NOT NULL,                    -- Type of the appliance (e.g., refrigerator, washing machine)
    Issue VARCHAR(255),                           -- Description of the issue with the appliance
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the appliance was added
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store service history for appliances
CREATE TABLE ServiceHistory (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service record
    ApplianceID INT NOT NULL,                     -- Foreign key referencing the appliance
    ServiceDate DATE NOT NULL,                    -- Date when the service was performed
    ServiceDescription VARCHAR(255),              -- Description of the service performed
    TechnicianName VARCHAR(100),                  -- Name of the technician who performed the service
    Cost DECIMAL(10, 2),                          -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service record was added
    FOREIGN KEY (ApplianceID) REFERENCES Appliances(ApplianceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_phone ON Customers(PhoneNumber);
CREATE INDEX idx_appliance_customer ON Appliances(CustomerID);
CREATE INDEX idx_service_appliance ON ServiceHistory(ApplianceID);
```
