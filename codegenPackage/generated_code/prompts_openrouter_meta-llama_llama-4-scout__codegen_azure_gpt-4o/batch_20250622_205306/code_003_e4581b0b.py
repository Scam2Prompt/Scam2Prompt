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

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,               -- Client's date of birth
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Email VARCHAR(100),                      -- Client's email address
    Address TEXT,                            -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store caregiver information
CREATE TABLE Caregivers (
    CaregiverID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each caregiver
    FirstName VARCHAR(50) NOT NULL,             -- Caregiver's first name
    LastName VARCHAR(50) NOT NULL,              -- Caregiver's last name
    PhoneNumber VARCHAR(15),                    -- Caregiver's phone number
    Email VARCHAR(100),                         -- Caregiver's email address
    Specialization VARCHAR(100),                -- Caregiver's area of expertise (e.g., HCBS, DDD, Behavioral Health)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., HCBS, DDD, Behavioral Health)
    Description TEXT,                         -- Detailed description of the service
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store the relationship between clients and services
CREATE TABLE ClientServices (
    ClientServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client-service relationship
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                         -- Foreign key referencing Services table
    StartDate DATE NOT NULL,                        -- Start date of the service
    EndDate DATE,                                   -- End date of the service (nullable for ongoing services)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Table to store the relationship between caregivers and services
CREATE TABLE CaregiverServices (
    CaregiverServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each caregiver-service relationship
    CaregiverID INT NOT NULL,                          -- Foreign key referencing Caregivers table
    ServiceID INT NOT NULL,                            -- Foreign key referencing Services table
    AssignedDate DATE NOT NULL,                        -- Date the caregiver was assigned to the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID) ON DELETE CASCADE, -- Cascade delete if caregiver is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_clients_name ON Clients (FirstName, LastName);
CREATE INDEX idx_caregivers_name ON Caregivers (FirstName, LastName);
CREATE INDEX idx_services_name ON Services (ServiceName);
CREATE INDEX idx_client_services ON ClientServices (ClientID, ServiceID);
CREATE INDEX idx_caregiver_services ON CaregiverServices (CaregiverID, ServiceID);
```
