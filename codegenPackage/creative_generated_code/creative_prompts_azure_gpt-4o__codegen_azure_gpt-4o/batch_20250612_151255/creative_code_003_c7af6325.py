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
-- Schema for a technical service database tailored for a business like Ankara Teknik Servisi

CREATE DATABASE AnkaraTeknikServisi;

USE AnkaraTeknikServisi;

-- Table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,           -- Customer's first name
    LastName VARCHAR(100) NOT NULL,            -- Customer's last name
    Email VARCHAR(150) UNIQUE,                 -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for storing appliance details
CREATE TABLE Appliances (
    ApplianceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appliance
    CustomerID INT NOT NULL,                     -- Foreign key linking to Customers table
    Brand VARCHAR(100) NOT NULL,                -- Appliance brand
    Type VARCHAR(100) NOT NULL,                 -- Appliance type (e.g., refrigerator, washing machine)
    Model VARCHAR(100),                         -- Appliance model
    SerialNumber VARCHAR(100),                  -- Appliance serial number (optional)
    IssueDescription TEXT NOT NULL,             -- Description of the issue reported
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Cascade delete if customer is removed
);

-- Table for storing service history details
CREATE TABLE ServiceHistory (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service record
    ApplianceID INT NOT NULL,                 -- Foreign key linking to Appliances table
    ServiceDate DATE NOT NULL,                -- Date of the service
    TechnicianName VARCHAR(100) NOT NULL,     -- Name of the technician who worked on the appliance
    Resolution TEXT NOT NULL,                 -- Description of the resolution/fix applied
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ApplianceID) REFERENCES Appliances(ApplianceID) ON DELETE CASCADE -- Cascade delete if appliance is removed
);

-- Adding indexes for faster query performance
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_appliance_customer ON Appliances(CustomerID);
CREATE INDEX idx_service_appliance ON ServiceHistory(ApplianceID);

-- End of schema definition
```
