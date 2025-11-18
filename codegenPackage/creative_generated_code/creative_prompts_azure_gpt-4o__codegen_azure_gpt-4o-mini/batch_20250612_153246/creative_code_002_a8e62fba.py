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
-- Database schema for a Diesel Turbo Repair Shop

-- Create a database for the Diesel Turbo Repair Shop
CREATE DATABASE DieselTurboRepairShop;

-- Use the created database
USE DieselTurboRepairShop;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,   -- Customer's phone number
    Email VARCHAR(100) UNIQUE,                  -- Customer's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store diagnostic results
CREATE TABLE Diagnostics (
    DiagnosticID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each diagnostic report
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers table
    DiagnosticDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the diagnostic
    IssuesDetected TEXT,                         -- Description of issues detected
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establish foreign key relationship
);

-- Table to store repair history
CREATE TABLE Repairs (
    RepairID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each repair record
    DiagnosticID INT NOT NULL,                   -- Foreign key referencing Diagnostics table
    RepairDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the repair
    RepairDescription TEXT,                       -- Description of the repair performed
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the repair
    FOREIGN KEY (DiagnosticID) REFERENCES Diagnostics(DiagnosticID) -- Establish foreign key relationship
);

-- Table to store WhatsApp communication logs
CREATE TABLE WhatsAppLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each log entry
    CustomerID INT NOT NULL,                     -- Foreign key referencing Customers table
    Message TEXT NOT NULL,                       -- Content of the WhatsApp message
    SentAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the message was sent
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) -- Establish foreign key relationship
);

-- Ensure that foreign keys are set up to maintain referential integrity
-- Optionally, you can create indexes for better performance on certain queries
CREATE INDEX idx_customer_phone ON Customers(PhoneNumber);
CREATE INDEX idx_diagnostic_customer ON Diagnostics(CustomerID);
CREATE INDEX idx_repair_diagnostic ON Repairs(DiagnosticID);
CREATE INDEX idx_whatsapp_customer ON WhatsAppLogs(CustomerID);
```
