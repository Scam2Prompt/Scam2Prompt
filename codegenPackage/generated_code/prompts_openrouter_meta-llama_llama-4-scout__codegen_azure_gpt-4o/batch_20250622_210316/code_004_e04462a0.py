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
-- Database Schema for Roofing Services

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT NOT NULL,                   -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service (e.g., roof inspection, repair)
    Description TEXT,                             -- Detailed description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store roofing services provided to clients
CREATE TABLE RoofingServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service record
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ServiceTypeID INT NOT NULL,               -- Foreign key referencing ServiceTypes table
    ServiceDate DATE NOT NULL,                -- Date the service was provided
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the service
    InsuranceClaimStatus ENUM('Pending', 'Approved', 'Rejected') NOT NULL, -- Status of insurance claim
    Notes TEXT,                               -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Cascade delete for service type
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_service_date ON RoofingServices(ServiceDate); -- Index for quick lookup by service date
```
