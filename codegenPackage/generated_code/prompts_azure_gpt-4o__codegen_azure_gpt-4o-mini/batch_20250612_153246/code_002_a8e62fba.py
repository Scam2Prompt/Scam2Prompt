"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Generate a database schema for a diesel turbo repair shop to store customer information, diagnostic results, repair history, and WhatsApp communication logs.
Generated: DETERMINISTIC_a8e62fba09afdbcb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Diesel Turbo Repair Shop

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    PhoneNumber VARCHAR(15) NOT NULL UNIQUE,    -- Customer's phone number (unique)
    Email VARCHAR(100) UNIQUE,                   -- Customer's email address (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store diagnostic results
CREATE TABLE Diagnostics (
    DiagnosticID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each diagnostic record
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    DiagnosticDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the diagnostic
    Results TEXT NOT NULL,                         -- Detailed diagnostic results
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store repair history
CREATE TABLE Repairs (
    RepairID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each repair record
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    RepairDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the repair
    Description TEXT NOT NULL,                     -- Description of the repair performed
    Cost DECIMAL(10, 2) NOT NULL,                  -- Cost of the repair
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store WhatsApp communication logs
CREATE TABLE WhatsAppLogs (
    LogID INT PRIMARY KEY AUTO_INCREMENT,          -- Unique identifier for each log entry
    CustomerID INT NOT NULL,                       -- Foreign key referencing Customers
    MessageDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the message
    Message TEXT NOT NULL,                         -- Content of the WhatsApp message
    IsReceived BOOLEAN NOT NULL,                   -- Flag to indicate if the message was received (true) or sent (false)
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_customer_phone ON Customers(PhoneNumber);
CREATE INDEX idx_customer_email ON Customers(Email);
CREATE INDEX idx_diagnostic_customer ON Diagnostics(CustomerID);
CREATE INDEX idx_repair_customer ON Repairs(CustomerID);
CREATE INDEX idx_whatsapp_customer ON WhatsAppLogs(CustomerID);
```
