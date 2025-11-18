"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ankarateknikservisi.com
Prompt: Create a database schema in SQL for storing customer information, appliance details (brand, type, issue), and service history, tailored for a business like Ankara Teknik Servisi.
Generated: DETERMINISTIC_c7af632539320f46
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Ankara Teknik Servisi

-- Drop existing tables if they exist
DROP TABLE IF EXISTS ServiceHistory;
DROP TABLE IF EXISTS Appliances;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    PhoneNumber VARCHAR(15) NOT NULL,           -- Customer's phone number
    Email VARCHAR(100),                         -- Customer's email address (optional)
    Address VARCHAR(255),                        -- Customer's address (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp of when the record was created
);

-- Table to store appliance details
CREATE TABLE Appliances (
    ApplianceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each appliance
    CustomerID INT NOT NULL,                     -- Foreign key to link to Customers
    Brand VARCHAR(50) NOT NULL,                  -- Brand of the appliance
    Type VARCHAR(50) NOT NULL,                   -- Type of appliance (e.g., refrigerator, washing machine)
    IssueDescription TEXT NOT NULL,              -- Description of the issue
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store service history
CREATE TABLE ServiceHistory (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service record
    ApplianceID INT NOT NULL,                     -- Foreign key to link to Appliances
    ServiceDate TIMESTAMP NOT NULL,               -- Date of the service performed
    ServiceDetails TEXT NOT NULL,                 -- Details about the service performed
    TechnicianName VARCHAR(50) NOT NULL,         -- Name of the technician who performed the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the record was created
    FOREIGN KEY (ApplianceID) REFERENCES Appliances(ApplianceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Ensure proper indexes for performance
CREATE INDEX idx_customer_phone ON Customers(PhoneNumber);
CREATE INDEX idx_appliance_brand ON Appliances(Brand);
CREATE INDEX idx_service_date ON ServiceHistory(ServiceDate);
```
