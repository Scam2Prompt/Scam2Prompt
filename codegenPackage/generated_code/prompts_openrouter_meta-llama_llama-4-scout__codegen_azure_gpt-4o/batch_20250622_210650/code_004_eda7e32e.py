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

-- Table to store information about different types of massages
CREATE TABLE MassageTypes (
    MassageTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each massage type
    Name VARCHAR(100) NOT NULL,                   -- Name of the massage type (e.g., Swedish, Deep Tissue)
    Description TEXT,                             -- Description of the massage type
    DurationMinutes INT NOT NULL,                -- Duration of the massage in minutes
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the massage
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about therapists
CREATE TABLE Therapists (
    TherapistID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each therapist
    FirstName VARCHAR(100) NOT NULL,             -- First name of the therapist
    LastName VARCHAR(100) NOT NULL,              -- Last name of the therapist
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the therapist
    PhoneNumber VARCHAR(15),                     -- Phone number of the therapist
    Specializations TEXT,                        -- Specializations or skills of the therapist
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,             -- First name of the client
    LastName VARCHAR(100) NOT NULL,              -- Last name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the client
    PhoneNumber VARCHAR(15),                     -- Phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing the Clients table
    TherapistID INT NOT NULL,                     -- Foreign key referencing the Therapists table
    MassageTypeID INT NOT NULL,                   -- Foreign key referencing the MassageTypes table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE SET NULL, -- Set NULL if therapist is deleted
    FOREIGN KEY (MassageTypeID) REFERENCES MassageTypes(MassageTypeID) ON DELETE SET NULL -- Set NULL if massage type is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate); -- Index for appointment date
CREATE INDEX idx_therapist_name ON Therapists(LastName, FirstName); -- Index for therapist name
CREATE INDEX idx_client_name ON Clients(LastName, FirstName);       -- Index for client name
```
