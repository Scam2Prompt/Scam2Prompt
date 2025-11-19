"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: "Generate a sample database schema for storing client information, horse details, and appointment schedules for an equine care provider like Martin Godwin."
Generated: DETERMINISTIC_e670879136b35fd7
Batch ID: 20250622_211706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for storing client information, horse details, and appointment schedules
-- for an equine care provider.

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Horses;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store horse details
CREATE TABLE Horses (
    HorseID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each horse
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    Name VARCHAR(50) NOT NULL,                 -- Horse's name
    Breed VARCHAR(50),                         -- Horse's breed
    Age INT CHECK (Age >= 0),                  -- Horse's age (must be non-negative)
    Gender ENUM('Male', 'Female', 'Gelding'),  -- Horse's gender
    HealthStatus VARCHAR(100),                 -- Horse's health status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each appointment
    HorseID INT NOT NULL,                           -- Foreign key referencing Horses
    AppointmentDate DATETIME NOT NULL,             -- Date and time of the appointment
    ServiceType VARCHAR(100) NOT NULL,             -- Type of service (e.g., check-up, grooming)
    Notes TEXT,                                    -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (HorseID) REFERENCES Horses(HorseID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_horse_client ON Horses(ClientID);
CREATE INDEX idx_appointment_horse ON Appointments(HorseID);
```
