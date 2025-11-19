"""
Generated Code Metadata:
========================
Original URL: https://getupenergy.co.uk
Prompt: Design a basic database schema to store information about massage therapy services, including different types of massages, therapists, and client appointments.
Generated: DETERMINISTIC_eda7e32ee96a90e9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a massage therapy service

-- Create a table to store different types of massages
CREATE TABLE MassageTypes (
    MassageTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each massage type
    Name VARCHAR(100) NOT NULL,                    -- Name of the massage type
    Description TEXT,                               -- Description of the massage type
    Price DECIMAL(10, 2) NOT NULL                   -- Price of the massage
);

-- Create a table to store therapist information
CREATE TABLE Therapists (
    TherapistID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each therapist
    FirstName VARCHAR(50) NOT NULL,                -- Therapist's first name
    LastName VARCHAR(50) NOT NULL,                  -- Therapist's last name
    Specialization VARCHAR(100),                     -- Therapist's specialization
    Phone VARCHAR(15),                              -- Therapist's contact number
    Email VARCHAR(100) UNIQUE NOT NULL              -- Therapist's email address
);

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,                -- Client's first name
    LastName VARCHAR(50) NOT NULL,                  -- Client's last name
    Phone VARCHAR(15),                              -- Client's contact number
    Email VARCHAR(100) UNIQUE NOT NULL              -- Client's email address
);

-- Create a table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each appointment
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    TherapistID INT NOT NULL,                       -- Foreign key referencing Therapists
    MassageTypeID INT NOT NULL,                     -- Foreign key referencing MassageTypes
    AppointmentDate DATETIME NOT NULL,              -- Date and time of the appointment
    Duration INT NOT NULL,                          -- Duration of the appointment in minutes
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled', -- Status of the appointment
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (MassageTypeID) REFERENCES MassageTypes(MassageTypeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_therapist_email ON Therapists(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
