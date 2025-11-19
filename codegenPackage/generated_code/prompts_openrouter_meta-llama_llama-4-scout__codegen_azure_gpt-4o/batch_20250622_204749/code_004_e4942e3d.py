"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: "Create a database schema for managing electrical contractor services, including traffic signals, street lighting, and underground utilities."
Generated: DETERMINISTIC_e4942e3df39d6717
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Managing Electrical Contractor Services

-- Table to store information about contractors
CREATE TABLE Contractors (
    ContractorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contractor
    Name VARCHAR(255) NOT NULL,                  -- Name of the contractor
    PhoneNumber VARCHAR(15),                     -- Contact phone number
    Email VARCHAR(255),                          -- Contact email
    Address TEXT,                                -- Address of the contractor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service categories
CREATE TABLE ServiceCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service category
    CategoryName VARCHAR(255) NOT NULL,          -- Name of the service category (e.g., Traffic Signals, Street Lighting)
    Description TEXT,                            -- Description of the service category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store specific services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service
    CategoryID INT NOT NULL,                     -- Foreign key to ServiceCategories
    ServiceName VARCHAR(255) NOT NULL,           -- Name of the service
    Description TEXT,                            -- Description of the service
    Price DECIMAL(10, 2),                        -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CategoryID) REFERENCES ServiceCategories(CategoryID) ON DELETE CASCADE
);

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,                  -- Name of the client
    PhoneNumber VARCHAR(15),                     -- Contact phone number
    Email VARCHAR(255),                          -- Contact email
    Address TEXT,                                -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service request
    ClientID INT NOT NULL,                       -- Foreign key to Clients
    ContractorID INT,                            -- Foreign key to Contractors (optional, if assigned)
    ServiceID INT NOT NULL,                      -- Foreign key to Services
    RequestDate DATE NOT NULL,                   -- Date of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the request
    Notes TEXT,                                  -- Additional notes about the request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ContractorID) REFERENCES Contractors(ContractorID) ON DELETE SET NULL,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Table to store work logs for service requests
CREATE TABLE WorkLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each work log
    RequestID INT NOT NULL,                      -- Foreign key to ServiceRequests
    LogDate DATE NOT NULL,                       -- Date of the work log entry
    Description TEXT NOT NULL,                   -- Description of the work performed
    HoursWorked DECIMAL(5, 2) NOT NULL,          -- Number of hours worked
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE
);

-- Table to store invoices for completed service requests
CREATE TABLE Invoices (
    InvoiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each invoice
    RequestID INT NOT NULL,                      -- Foreign key to ServiceRequests
    InvoiceDate DATE NOT NULL,                   -- Date of the invoice
    TotalAmount DECIMAL(10, 2) NOT NULL,         -- Total amount for the invoice
    Paid BOOLEAN DEFAULT FALSE,                  -- Payment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE
);
```
