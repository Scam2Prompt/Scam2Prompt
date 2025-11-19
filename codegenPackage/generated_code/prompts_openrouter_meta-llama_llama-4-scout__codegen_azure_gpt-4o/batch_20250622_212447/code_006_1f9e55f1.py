"""
Generated Code Metadata:
========================
Original URL: https://connectsupporthelpdesk.org
Prompt: Design a database schema to store information about domain registrations, parking status, and owner details, based on the structure implied by connectsupporthelpdesk.org.
Generated: DETERMINISTIC_1f9e55f1184a3299
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing domain registration information, parking status, and owner details

-- Table to store domain information
CREATE TABLE Domains (
    DomainID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each domain
    DomainName VARCHAR(255) NOT NULL UNIQUE, -- Fully qualified domain name (e.g., example.com)
    RegistrationDate DATE NOT NULL,          -- Date the domain was registered
    ExpirationDate DATE NOT NULL,            -- Date the domain registration expires
    IsParked BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the domain is parked (true/false)
    OwnerID INT NOT NULL,                    -- Foreign key referencing the owner of the domain
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store owner information
CREATE TABLE Owners (
    OwnerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each owner
    FullName VARCHAR(255) NOT NULL,         -- Full name of the domain owner
    Email VARCHAR(255) NOT NULL UNIQUE,     -- Email address of the owner
    PhoneNumber VARCHAR(20),                -- Phone number of the owner (optional)
    Address TEXT,                           -- Physical address of the owner (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store parking status details (optional, for more granular parking information)
CREATE TABLE ParkingStatus (
    ParkingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for parking status
    DomainID INT NOT NULL,                    -- Foreign key referencing the domain
    ParkingStartDate DATE,                    -- Date the domain was parked
    ParkingEndDate DATE,                      -- Date the domain was unparked (if applicable)
    Notes TEXT,                               -- Additional notes about the parking status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (DomainID) REFERENCES Domains(DomainID) ON DELETE CASCADE -- Cascade delete if domain is removed
);

-- Add foreign key constraint to link Domains table to Owners table
ALTER TABLE Domains
ADD CONSTRAINT FK_Domain_Owner
FOREIGN KEY (OwnerID) REFERENCES Owners(OwnerID) ON DELETE CASCADE; -- Cascade delete if owner is removed

-- Indexes for performance optimization
CREATE INDEX IDX_DomainName ON Domains(DomainName); -- Index for quick domain name lookups
CREATE INDEX IDX_OwnerEmail ON Owners(Email);       -- Index for quick owner email lookups
CREATE INDEX IDX_IsParked ON Domains(IsParked);     -- Index for filtering parked domains
```
