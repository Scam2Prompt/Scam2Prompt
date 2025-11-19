"""
Generated Code Metadata:
========================
Original URL: https://rehemacare.com
Prompt: Develop a basic database schema to store information about clients, services, and caregivers for a healthcare organization offering HCBS, DDD, and Behavioral Health Services.
Generated: DETERMINISTIC_e4581b0b9c9ea9b0
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a healthcare organization offering HCBS, DDD, and Behavioral Health Services

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Caregivers;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    ClientID SERIAL PRIMARY KEY,          -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,      -- Client's first name
    LastName VARCHAR(50) NOT NULL,       -- Client's last name
    DateOfBirth DATE NOT NULL,            -- Client's date of birth
    PhoneNumber VARCHAR(15),               -- Client's phone number
    Email VARCHAR(100),                    -- Client's email address
    Address VARCHAR(255),                  -- Client's residential address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service information
CREATE TABLE Services (
    ServiceID SERIAL PRIMARY KEY,         -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,   -- Name of the service
    Description TEXT,                     -- Description of the service
    ServiceType VARCHAR(50) NOT NULL,     -- Type of service (e.g., HCBS, DDD, Behavioral Health)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store caregiver information
CREATE TABLE Caregivers (
    CaregiverID SERIAL PRIMARY KEY,       -- Unique identifier for each caregiver
    FirstName VARCHAR(50) NOT NULL,      -- Caregiver's first name
    LastName VARCHAR(50) NOT NULL,       -- Caregiver's last name
    PhoneNumber VARCHAR(15),               -- Caregiver's phone number
    Email VARCHAR(100),                    -- Caregiver's email address
    Qualifications TEXT,                  -- Caregiver's qualifications
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to link clients with services they are receiving
CREATE TABLE ClientServices (
    ClientServiceID SERIAL PRIMARY KEY,   -- Unique identifier for each client-service relationship
    ClientID INT NOT NULL,                 -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                -- Foreign key referencing Services
    CaregiverID INT,                       -- Optional foreign key referencing Caregivers
    StartDate DATE NOT NULL,               -- Start date of the service
    EndDate DATE,                          -- End date of the service (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID) ON DELETE SET NULL -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_lastname ON Clients(LastName);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_caregiver_lastname ON Caregivers(LastName);
CREATE INDEX idx_client_service ON ClientServices(ClientID, ServiceID);
```
