"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubexperts.ch
Prompt: Generate code to create a database schema for storing client information, service details (e.g., company creation, auditing), and deadlines, based on the offerings of Hub Experts.
Generated: DETERMINISTIC_410650504a9d6ec0
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing client information, service details, and deadlines

-- Create a new database
CREATE DATABASE HubExpertsDB;

-- Use the new database
USE HubExpertsDB;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,       -- Client's email address (unique)
    Phone VARCHAR(15),                        -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store service details
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    ClientID INT NOT NULL,                       -- Foreign key to link to Clients table
    ServiceType ENUM('Company Creation', 'Auditing') NOT NULL,  -- Type of service provided
    Description TEXT,                            -- Description of the service
    ServiceStartDate DATE NOT NULL,             -- Start date of the service
    ServiceEndDate DATE NOT NULL,               -- End date of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure data integrity
);

-- Table to store deadlines for services
CREATE TABLE Deadlines (
    DeadlineID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each deadline
    ServiceID INT NOT NULL,                       -- Foreign key to link to Services table
    DeadlineDate DATE NOT NULL,                   -- Deadline date
    Notes TEXT,                                   -- Additional notes about the deadline
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure data integrity
);

-- Ensure that the schema is created successfully
SELECT 'Database schema for Hub Experts created successfully.' AS Message;
```
