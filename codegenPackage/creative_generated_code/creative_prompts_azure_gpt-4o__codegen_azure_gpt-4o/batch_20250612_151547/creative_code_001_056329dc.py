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
-- ================================================
-- Database Schema for NDIS Provider Client Management
-- ================================================

-- Create a table to store client personal details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,         -- First Name of the client
    LastName VARCHAR(100) NOT NULL,          -- Last Name of the client
    DateOfBirth DATE NOT NULL,               -- Date of Birth of the client
    PhoneNumber VARCHAR(15),                 -- Contact phone number
    Email VARCHAR(255),                      -- Contact email address
    Address TEXT,                            -- Physical address
    EmergencyContactName VARCHAR(100),       -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),       -- Emergency contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store services availed by clients
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(150) NOT NULL,        -- Name of the service (e.g., household tasks, travel assistance)
    ServiceDescription TEXT,                  -- Detailed description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a many-to-many relationship table between Clients and Services
CREATE TABLE ClientServices (
    ID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for this record
    ClientID INT NOT NULL,                   -- Foreign key to Clients table
    ServiceID INT NOT NULL,                  -- Foreign key to Services table
    StartDate DATE NOT NULL,                 -- Date when the service starts for the client
    EndDate DATE,                            -- Date when the service ends for the client (nullable)
    Notes TEXT,                              -- Additional notes related to the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascading delete
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascading delete
);

-- Create a table to store appointment scheduling details
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key to Clients table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    ServiceID INT NOT NULL,                       -- Foreign key to Services table
    StaffName VARCHAR(100) NOT NULL,              -- Staff member assigned to the appointment
    Location TEXT,                                -- Location of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled', -- Appointment status
    Notes TEXT,                                   -- Additional notes about the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascading delete
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascading delete
);

-- ================================================
-- End of Database Schema
-- ================================================
```
