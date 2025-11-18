"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Develop a database schema for managing customs clearance processes in Indonesia, referencing Uniair Cargo's customs services.
Generated: DETERMINISTIC_c0aa45367d233272
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing customs clearance processes in Indonesia
-- This schema is designed to handle customs processes efficiently, referencing Uniair Cargo's services.

-- Table to store user information (e.g., staff, clients)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for each user
    FullName VARCHAR(255) NOT NULL,                     -- Full name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,                 -- Unique email for communication
    PhoneNumber VARCHAR(20),                            -- Contact phone number
    Role ENUM('Admin', 'Staff', 'Client') NOT NULL,     -- Role of the user within the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP       -- When the user was added to the system
);

-- Table to store import/export shipments information
CREATE TABLE Shipments (
    ShipmentID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each shipment
    UserID INT NOT NULL,                                -- Reference to the user who owns the shipment
    ShipmentReference VARCHAR(255) UNIQUE NOT NULL,     -- Unique reference for the shipment
    Description TEXT,                                   -- Description of the shipment contents
    OriginCountry VARCHAR(255) NOT NULL,               -- Country of origin
    DestinationCountry VARCHAR(255) NOT NULL,          -- Destination country
    Weight DECIMAL(10,2) NOT NULL,                     -- Weight of the shipment in kilograms
    Value DECIMAL(15,2) NOT NULL,                      -- Value of the shipment in local currency
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- When the shipment was registered
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID)      -- Foreign key linking to Users table
);

-- Table to store customs clearance status and progress
CREATE TABLE CustomsClearance (
    ClearanceID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each clearance process
    ShipmentID INT NOT NULL,                            -- Reference to the shipment being cleared
    Status ENUM('Pending', 'In Progress', 'Completed', 'Rejected') NOT NULL DEFAULT 'Pending', -- Clearance status
    AgentName VARCHAR(255),                             -- Name of the customs clearance agent
    Notes TEXT,                                         -- Notes related to the clearance process
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- When the clearance process was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) -- Foreign key linking to Shipments table
);

-- Table to store customs duty and tax information
CREATE TABLE CustomsDuty (
    DutyID INT AUTO_INCREMENT PRIMARY KEY,              -- Unique identifier for duty record
    ShipmentID INT NOT NULL,                            -- Reference to the shipment this duty applies to
    DutyAmount DECIMAL(15,2) NOT NULL,                  -- Customs duty amount in local currency
    TaxAmount DECIMAL(15,2) NOT NULL,                   -- Customs tax amount in local currency
    TotalAmount DECIMAL(15,2) AS (DutyAmount + TaxAmount) STORED, -- Total customs amount (calculated)
    PaidStatus ENUM('Unpaid', 'Paid') NOT NULL DEFAULT 'Unpaid', -- Payment status for the duty/tax
    PaymentDate TIMESTAMP NULL,                         -- Date of payment (null if unpaid)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- When the duty record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID) -- Foreign key linking to Shipments table
);

-- Table to log actions performed during customs clearance
CREATE TABLE ClearanceLog (
    LogID INT AUTO_INCREMENT PRIMARY KEY,               -- Unique identifier for the log entry
    ClearanceID INT NOT NULL,                           -- Reference to the clearance process
    Action VARCHAR(255) NOT NULL,                       -- Description of the action performed
    PerformedBy INT NOT NULL,                           -- Reference to the user who performed the action
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp of the action
    FOREIGN KEY (ClearanceID) REFERENCES CustomsClearance(ClearanceID), -- Foreign key linking to CustomsClearance table
    FOREIGN KEY (PerformedBy) REFERENCES Users(UserID)  -- Foreign key linking to Users table
);

-- Indexes for better query performance
CREATE INDEX idx_user_email ON Users(Email);
CREATE INDEX idx_shipment_reference ON Shipments(ShipmentReference);
CREATE INDEX idx_clearance_status ON CustomsClearance(Status);
CREATE INDEX idx_duty_paid_status ON CustomsDuty(PaidStatus);
CREATE INDEX idx_log_timestamp ON ClearanceLog(Timestamp);
```
