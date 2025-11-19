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
-- SQL script to create a database schema for a reflexology clinic

-- Create a database for the clinic
CREATE DATABASE ReflexologyClinic;

-- Use the created database
USE ReflexologyClinic;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    PhoneNumber VARCHAR(15) NOT NULL,         -- Client's phone number
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients table
    AppointmentDate DATETIME NOT NULL,              -- Date and time of the appointment
    Duration INT NOT NULL,                          -- Duration of the appointment in minutes
    ServiceType VARCHAR(50) NOT NULL,              -- Type of service (e.g., reflexology, massage)
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
