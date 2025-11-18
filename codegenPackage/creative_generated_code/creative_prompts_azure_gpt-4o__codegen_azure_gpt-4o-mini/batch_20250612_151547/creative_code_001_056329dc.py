"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Create a database schema in SQL to manage client information for an NDIS provider, including tables for personal details, services availed (e.g., household tasks, travel assistance), and appointment scheduling.
Generated: DETERMINISTIC_056329dc44909096
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing client information for an NDIS provider

-- Create a database for the NDIS provider
CREATE DATABASE ndis_provider;
USE ndis_provider;

-- Table to store client personal details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    DateOfBirth DATE NOT NULL,                 -- Client's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Client's gender
    Phone VARCHAR(15),                         -- Client's phone number
    Email VARCHAR(100) UNIQUE,                 -- Client's email address
    Address VARCHAR(255),                       -- Client's home address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store types of services availed by clients
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL UNIQUE,    -- Name of the service (e.g., household tasks, travel assistance)
    Description TEXT,                             -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store the services availed by each client
CREATE TABLE ClientServices (
    ClientServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client-service record
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services
    StartDate DATE NOT NULL,                       -- Date the service was started
    EndDate DATE,                                  -- Date the service was ended, NULL if ongoing
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Cascade delete if client is deleted
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Cascade delete if service is deleted
);

-- Table to store appointment scheduling for clients
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    Notes TEXT,                                   -- Additional notes about the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Cascade delete if client is deleted
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Cascade delete if service is deleted
);

-- Ensure that the schema is properly indexed for performance
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
