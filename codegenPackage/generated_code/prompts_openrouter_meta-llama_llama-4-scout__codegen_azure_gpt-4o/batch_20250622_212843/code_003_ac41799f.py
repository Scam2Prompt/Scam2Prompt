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
-- SQL Database Schema for a company offering repair and installation services for automatic doors

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store door types
CREATE TABLE DoorTypes (
    DoorTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each door type
    DoorTypeName VARCHAR(100) NOT NULL UNIQUE, -- Name of the door type (e.g., Sliding Door, Swing Door)
    Description TEXT                           -- Description of the door type
);

-- Table to store service requests
CREATE TABLE ServiceRequests (
    ServiceRequestID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service request
    ClientID INT NOT NULL,                           -- Foreign key referencing the client
    DoorTypeID INT NOT NULL,                         -- Foreign key referencing the door type
    ServiceType ENUM('Repair', 'Installation') NOT NULL, -- Type of service requested
    RequestDate DATE NOT NULL,                       -- Date when the service was requested
    ScheduledDate DATE,                              -- Date when the service is scheduled
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Status of the service request
    Notes TEXT,                                      -- Additional notes about the service request
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp when the service request was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (DoorTypeID) REFERENCES DoorTypes(DoorTypeID) ON DELETE SET NULL -- Set NULL if door type is removed
);

-- Indexes for faster lookups
CREATE INDEX idx_client_email ON Clients (Email);
CREATE INDEX idx_service_request_status ON ServiceRequests (Status);
CREATE INDEX idx_service_request_date ON ServiceRequests (RequestDate);
```
