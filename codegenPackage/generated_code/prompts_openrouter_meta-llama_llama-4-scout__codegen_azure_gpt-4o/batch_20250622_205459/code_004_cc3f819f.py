"""
Generated Code Metadata:
========================
Original URL: https://webalancer.com
Prompt: Design a simple database schema for managing client domains and their development status, inspired by the services offered by IT-Kompass GmbH on webalancer.com.
Generated: DETERMINISTIC_cc3f819f533b74e7
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Managing Client Domains and Their Development Status

-- Table: Clients
-- This table stores information about clients.
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table: Domains
-- This table stores information about domains associated with clients.
CREATE TABLE Domains (
    DomainID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each domain
    ClientID INT NOT NULL,                   -- Foreign key referencing the Clients table
    DomainName VARCHAR(255) NOT NULL UNIQUE, -- Domain name (e.g., example.com)
    Status ENUM('Development', 'Testing', 'Live', 'Maintenance') NOT NULL, -- Development status of the domain
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the domain was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures domain is deleted if client is deleted
);

-- Table: DevelopmentLogs
-- This table stores logs related to the development status of domains.
CREATE TABLE DevelopmentLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each log entry
    DomainID INT NOT NULL,                   -- Foreign key referencing the Domains table
    Status ENUM('Development', 'Testing', 'Live', 'Maintenance') NOT NULL, -- Status at the time of the log
    Notes TEXT,                              -- Additional notes about the status change
    LoggedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the log entry was created
    FOREIGN KEY (DomainID) REFERENCES Domains(DomainID) ON DELETE CASCADE -- Ensures log is deleted if domain is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup of clients by email
CREATE INDEX idx_domain_name ON Domains(DomainName); -- Index for quick lookup of domains by name
CREATE INDEX idx_domain_status ON Domains(Status); -- Index for filtering domains by status
CREATE INDEX idx_log_domain_id ON DevelopmentLogs(DomainID); -- Index for filtering logs by domain ID
```
