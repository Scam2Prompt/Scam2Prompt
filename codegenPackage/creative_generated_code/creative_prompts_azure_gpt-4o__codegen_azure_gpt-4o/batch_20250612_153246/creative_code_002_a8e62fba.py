"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reparaciondeturbo.cl
Prompt: Generate a database schema for a diesel turbo repair shop to store customer information, diagnostic results, repair history, and WhatsApp communication logs.
Generated: DETERMINISTIC_a8e62fba09afdbcb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for Diesel Turbo Repair Shop Database

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the customer
    FirstName VARCHAR(50) NOT NULL,            -- First name of the customer
    LastName VARCHAR(50) NOT NULL,             -- Last name of the customer
    Email VARCHAR(100) UNIQUE,                 -- Email address of the customer
    PhoneNumber VARCHAR(15),                   -- Phone number of the customer
    Address TEXT,                              -- Address of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the customer record was created
);

-- Create a table to store diagnostic results
CREATE TABLE Diagnostics (
    DiagnosticID INT AUTO_INCREMENT PRIMARY KEY, -- Unique ID for the diagnostic entry
    CustomerID INT NOT NULL,                     -- Reference to the customer
    VehicleModel VARCHAR(50) NOT NULL,           -- Model of the vehicle being diagnosed
    VehicleVIN VARCHAR(50),                      -- Vehicle Identification Number
    DiagnosticDetails TEXT NOT NULL,             -- Detailed diagnostic results
    DiagnosticDate DATE NOT NULL,                -- Date of the diagnostic
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the diagnostic record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Foreign key linking to Customers table
);

-- Create a table to store repair history
CREATE TABLE Repairs (
    RepairID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique ID for the repair entry
    CustomerID INT NOT NULL,                    -- Reference to the customer
    DiagnosticID INT,                           -- Reference to the diagnostic entry (optional)
    RepairDetails TEXT NOT NULL,                -- Detailed repair information
    RepairCost DECIMAL(10, 2) NOT NULL,         -- Cost of the repair
    RepairDate DATE NOT NULL,                   -- Date of the repair
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the repair record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID), -- Foreign key linking to Customers table
    FOREIGN KEY (DiagnosticID) REFERENCES Diagnostics(DiagnosticID) -- Foreign key linking to Diagnostics table
);

-- Create a table to store WhatsApp communication logs
CREATE TABLE WhatsAppLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique ID for the communication log
    CustomerID INT NOT NULL,                   -- Reference to the customer
    MessageContent TEXT NOT NULL,              -- Content of the WhatsApp message
    SentBy ENUM('Customer', 'Shop') NOT NULL,  -- Indicates who sent the message
    SentAt TIMESTAMP NOT NULL,                 -- Timestamp of when the message was sent
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the log record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Foreign key linking to Customers table
);

-- Ensure all tables are using InnoDB for transactional support
ENGINE=InnoDB;
```
