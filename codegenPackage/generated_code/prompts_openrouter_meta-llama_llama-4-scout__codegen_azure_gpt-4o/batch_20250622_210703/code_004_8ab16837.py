"""
Generated Code Metadata:
========================
Original URL: https://rjbmudanzas.es
Prompt: Design a simple database schema to store information about clients, moving services, and storage facilities for a company like RJB Moving, and provide a brief explanation of the schema.
Generated: DETERMINISTIC_8ab16837a1ca1e2a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for RJB Moving Company

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the client record was created
);

-- Table to store moving services information
CREATE TABLE MovingServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ServiceDate DATE NOT NULL,                -- Date of the moving service
    StartLocation TEXT NOT NULL,              -- Starting location of the move
    EndLocation TEXT NOT NULL,                -- Ending location of the move
    ServiceType ENUM('Residential', 'Commercial') NOT NULL, -- Type of moving service
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the moving service
    Notes TEXT,                               -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service record was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store storage facility information
CREATE TABLE StorageFacilities (
    FacilityID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each storage facility
    Name VARCHAR(100) NOT NULL,                -- Name of the storage facility
    Location TEXT NOT NULL,                    -- Location of the storage facility
    Capacity INT NOT NULL,                     -- Maximum capacity of the facility (in units)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the facility record was created
);

-- Table to store client storage rentals
CREATE TABLE StorageRentals (
    RentalID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each rental
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    FacilityID INT NOT NULL,                   -- Foreign key referencing StorageFacilities table
    StartDate DATE NOT NULL,                   -- Start date of the rental
    EndDate DATE,                              -- End date of the rental (nullable for ongoing rentals)
    MonthlyRate DECIMAL(10, 2) NOT NULL,       -- Monthly rental rate
    Notes TEXT,                                -- Additional notes about the rental
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the rental record was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (FacilityID) REFERENCES StorageFacilities(FacilityID) ON DELETE CASCADE -- Cascade delete if facility is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_clients_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_movingservices_clientid ON MovingServices(ClientID); -- Index for quick lookup by client ID
CREATE INDEX idx_storagerentals_clientid ON StorageRentals(ClientID); -- Index for quick lookup by client ID
CREATE INDEX idx_storagerentals_facilityid ON StorageRentals(FacilityID); -- Index for quick lookup by facility ID
```

This schema is designed to store information about clients, moving services, and storage facilities for a moving company. It includes proper relationships, constraints, and indexes for efficient data management.
