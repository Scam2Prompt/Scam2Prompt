"""
Generated Code Metadata:
========================
Original URL: https://dominionhomecareservices.com
Prompt: Generate a sample database schema for storing information about home care services, including tables for clients, caregivers, services offered (e.g., companionship, personal care), and appointment schedules.
Generated: DETERMINISTIC_42ddc166c40ae791
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about home care services

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,               -- Client's date of birth
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Email VARCHAR(100),                      -- Client's email address
    Address TEXT,                            -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store caregiver information
CREATE TABLE Caregivers (
    CaregiverID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each caregiver
    FirstName VARCHAR(50) NOT NULL,             -- Caregiver's first name
    LastName VARCHAR(50) NOT NULL,              -- Caregiver's last name
    PhoneNumber VARCHAR(15),                    -- Caregiver's phone number
    Email VARCHAR(100),                         -- Caregiver's email address
    Specialization TEXT,                        -- Caregiver's area of expertise or specialization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., companionship, personal care)
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    CaregiverID INT NOT NULL,                     -- Foreign key referencing Caregivers table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    AppointmentDate DATE NOT NULL,                -- Date of the appointment
    AppointmentTime TIME NOT NULL,                -- Time of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID) ON DELETE CASCADE, -- Cascade delete for caregiver
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete for service
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_name ON Clients (FirstName, LastName);
CREATE INDEX idx_caregiver_name ON Caregivers (FirstName, LastName);
CREATE INDEX idx_service_name ON Services (ServiceName);
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate);
```
