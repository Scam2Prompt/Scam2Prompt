"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: "Design a database schema to store information about roofing services, including client details, service types (e.g., roof inspection, repair, installation), and insurance claim status, inspired by JaraEs Construction LLC's services."
Generated: DETERMINISTIC_e04462a0288f2737
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for roofing services management

-- Create a table to store client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,             -- Name of the service (e.g., inspection, repair)
    Description TEXT,                               -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store insurance claim statuses
CREATE TABLE InsuranceClaims (
    ClaimID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each claim
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    ServiceTypeID INT NOT NULL,                     -- Foreign key referencing ServiceTypes
    ClaimStatus ENUM('Pending', 'Approved', 'Denied') NOT NULL,  -- Status of the insurance claim
    ClaimAmount DECIMAL(10, 2),                    -- Amount claimed
    ClaimDate DATE NOT NULL,                        -- Date of the claim
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store service records
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each service record
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    ServiceTypeID INT NOT NULL,                     -- Foreign key referencing ServiceTypes
    ServiceDate DATE NOT NULL,                      -- Date when the service was performed
    ServiceCost DECIMAL(10, 2) NOT NULL,           -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
