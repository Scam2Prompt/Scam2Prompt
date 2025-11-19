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
-- Database schema for RJB Moving Company

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Table to store moving services offered
CREATE TABLE MovingServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the moving service
    Description TEXT,                           -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the service was added
);

-- Table to store storage facilities information
CREATE TABLE StorageFacilities (
    FacilityID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each storage facility
    FacilityName VARCHAR(100) NOT NULL,        -- Name of the storage facility
    Location VARCHAR(255) NOT NULL,            -- Address of the storage facility
    Capacity INT NOT NULL,                      -- Total capacity of the facility (in cubic feet)
    AvailableSpace INT NOT NULL,                -- Available space in the facility (in cubic feet)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the facility was added
);

-- Table to link clients with their selected moving services
CREATE TABLE ClientServices (
    ClientServiceID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each client-service relationship
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                         -- Foreign key referencing MovingServices
    ServiceDate DATE NOT NULL,                      -- Date when the service is scheduled
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ServiceID) REFERENCES MovingServices(ServiceID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to link clients with their selected storage facilities
CREATE TABLE ClientStorage (
    ClientStorageID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each client-storage relationship
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    FacilityID INT NOT NULL,                        -- Foreign key referencing StorageFacilities
    StartDate DATE NOT NULL,                       -- Start date of storage
    EndDate DATE,                                  -- End date of storage (nullable)
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (FacilityID) REFERENCES StorageFacilities(FacilityID) ON DELETE CASCADE -- Ensures referential integrity
);
```
