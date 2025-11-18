"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luattrungcuong.com
Prompt: Develop a SQL database schema to store client information and service details for a legal consultancy firm, referencing the diverse legal services offered by Luật Trung Cường.
Generated: DETERMINISTIC_dd60c7a136f48bb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Schema for Legal Consultancy Firm: Luật Trung Cường

-- Create a database for the legal consultancy firm
CREATE DATABASE LegalConsultancy;

-- Switch to the newly created database
USE LegalConsultancy;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store legal services offered
CREATE TABLE LegalServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name describing the legal service
    Description TEXT,                         -- Detailed description of the service
    Cost DECIMAL(10, 2) NOT NULL,             -- Service cost
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store the relationship between clients and services
CREATE TABLE ClientServices (
    ClientServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for client-service relationship
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                         -- Foreign key referencing LegalServices table
    ServiceDate DATE NOT NULL,                      -- Date when the service was provided
    Notes TEXT,                                     -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for clients
    FOREIGN KEY (ServiceID) REFERENCES LegalServices(ServiceID) ON DELETE CASCADE -- Cascade delete for services
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for email lookups
CREATE INDEX idx_service_name ON LegalServices(ServiceName); -- Index for service name lookups
CREATE INDEX idx_client_service ON ClientServices(ClientID, ServiceID); -- Composite index for client-service lookups

-- Error handling in case of execution issues
BEGIN;
-- Additional schema setup or constraints can be added here.
COMMIT;
```
