"""
Generated Code Metadata:
========================
Original URL: https://carehelpers.pt
Prompt: "Design a database schema to store information about clients, caregivers, and services provided by a home care company like CARE HELPERS."
Generated: DETERMINISTIC_16875a7cdd155ffd
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a home care company "CARE HELPERS"

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    DateOfBirth DATE NOT NULL,                 -- Client's date of birth
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Email VARCHAR(100),                        -- Client's email address
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store caregiver information
CREATE TABLE Caregivers (
    CaregiverID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each caregiver
    FirstName VARCHAR(50) NOT NULL,              -- Caregiver's first name
    LastName VARCHAR(50) NOT NULL,               -- Caregiver's last name
    PhoneNumber VARCHAR(15),                      -- Caregiver's phone number
    Email VARCHAR(100),                           -- Caregiver's email address
    HireDate DATE NOT NULL,                       -- Date the caregiver was hired
    Specialization VARCHAR(100),                  -- Caregiver's area of specialization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store services provided
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the service
    Description TEXT,                             -- Description of the service
    Cost DECIMAL(10, 2) NOT NULL,                -- Cost of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to link clients and caregivers with the services they receive
CREATE TABLE ClientCaregiverServices (
    ID INT PRIMARY KEY AUTO_INCREMENT,            -- Unique identifier for each record
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients
    CaregiverID INT NOT NULL,                     -- Foreign key referencing Caregivers
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    ServiceDate DATE NOT NULL,                    -- Date the service was provided
    Notes TEXT,                                   -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
