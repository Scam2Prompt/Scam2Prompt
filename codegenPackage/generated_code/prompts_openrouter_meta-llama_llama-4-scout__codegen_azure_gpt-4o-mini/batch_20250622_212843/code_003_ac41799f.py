"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Develop a SQL database schema to store information about clients, service requests, and door types for a company like Trimatic Puertas Automáticas that offers repair and installation services for automatic doors in Madrid.
Generated: DETERMINISTIC_ac41799f78382a1b
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Trimatic Puertas Automáticas

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ServiceRequests;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS DoorTypes;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    Phone VARCHAR(15),                         -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store different types of doors
CREATE TABLE DoorTypes (
    DoorTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each door type
    DoorTypeName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the door type (e.g., sliding, swinging)
    Description TEXT,                            -- Description of the door type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store service requests made by clients
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each service request
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients table
    DoorTypeID INT NOT NULL,                     -- Foreign key referencing DoorTypes table
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the service request
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',  -- Status of the service request
    Notes TEXT,                                  -- Additional notes regarding the service request
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (DoorTypeID) REFERENCES DoorTypes(DoorTypeID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_door_type_name ON DoorTypes(DoorTypeName);
CREATE INDEX idx_request_status ON ServiceRequests(Status);
```
