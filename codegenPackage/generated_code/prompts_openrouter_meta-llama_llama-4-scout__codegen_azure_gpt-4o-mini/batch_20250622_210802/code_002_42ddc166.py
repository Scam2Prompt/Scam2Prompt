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

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Caregivers;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    DateOfBirth DATE NOT NULL,                 -- Client's date of birth
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Email VARCHAR(100),                        -- Client's email address
    Address VARCHAR(255),                      -- Client's home address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store caregiver information
CREATE TABLE Caregivers (
    CaregiverID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each caregiver
    FirstName VARCHAR(50) NOT NULL,              -- Caregiver's first name
    LastName VARCHAR(50) NOT NULL,               -- Caregiver's last name
    PhoneNumber VARCHAR(15),                      -- Caregiver's phone number
    Email VARCHAR(100),                           -- Caregiver's email address
    Qualifications TEXT,                          -- Caregiver's qualifications
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,           -- Name of the service (e.g., companionship, personal care)
    Description TEXT,                             -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients
    CaregiverID INT NOT NULL,                      -- Foreign key referencing Caregivers
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,             -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (CaregiverID) REFERENCES Caregivers(CaregiverID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
