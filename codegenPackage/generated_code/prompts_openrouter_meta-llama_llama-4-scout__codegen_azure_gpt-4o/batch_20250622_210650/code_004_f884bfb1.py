"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Design a simple database schema to store client information and appointment schedules for a reflexology clinic like Red Horse Reflexology, and provide SQL code for creating the necessary tables.
Generated: DETERMINISTIC_f884bfb10e6bbc6a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing client information and appointment schedules
-- Reflexology Clinic: Red Horse Reflexology

-- Create table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE,               -- Client's email address (optional, must be unique if provided)
    PhoneNumber VARCHAR(15) NOT NULL,        -- Client's phone number
    DateOfBirth DATE,                        -- Client's date of birth (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create table for storing appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing the Clients table
    AppointmentDate DATE NOT NULL,               -- Date of the appointment
    AppointmentTime TIME NOT NULL,               -- Time of the appointment
    DurationMinutes INT NOT NULL,                -- Duration of the appointment in minutes
    Notes TEXT,                                  -- Optional notes about the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create table for storing reflexologists (optional, if needed for multi-staff clinics)
CREATE TABLE Reflexologists (
    ReflexologistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each reflexologist
    FirstName VARCHAR(50) NOT NULL,                 -- Reflexologist's first name
    LastName VARCHAR(50) NOT NULL,                  -- Reflexologist's last name
    Email VARCHAR(100) UNIQUE,                      -- Reflexologist's email address (optional, must be unique if provided)
    PhoneNumber VARCHAR(15),                        -- Reflexologist's phone number (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create table for assigning reflexologists to appointments (optional)
CREATE TABLE AppointmentAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    AppointmentID INT NOT NULL,                  -- Foreign key referencing the Appointments table
    ReflexologistID INT NOT NULL,                -- Foreign key referencing the Reflexologists table
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of assignment creation
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ReflexologistID) REFERENCES Reflexologists(ReflexologistID) ON DELETE SET NULL -- Reflexologist can be null if deleted
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_appointment_date_time ON Appointments(AppointmentDate, AppointmentTime);
CREATE INDEX idx_reflexologist_email ON Reflexologists(Email);
```
