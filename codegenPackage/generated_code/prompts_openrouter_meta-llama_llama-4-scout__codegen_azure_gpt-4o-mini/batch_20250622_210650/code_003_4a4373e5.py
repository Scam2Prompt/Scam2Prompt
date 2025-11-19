"""
Generated Code Metadata:
========================
Original URL: https://vanaclochayasociados.com
Prompt: Design a database schema for storing information about law firm clients, cases, and appointments, using a relational database management system like MySQL.
Generated: DETERMINISTIC_4a4373e5d079a884
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a law firm management system

-- Create a database for the law firm
CREATE DATABASE LawFirmDB;

-- Use the created database
USE LawFirmDB;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    Phone VARCHAR(15),                         -- Client's phone number
    Address VARCHAR(255),                      -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store case information
CREATE TABLE Cases (
    CaseID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each case
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    CaseTitle VARCHAR(100) NOT NULL,          -- Title of the case
    CaseDescription TEXT,                      -- Detailed description of the case
    Status ENUM('Open', 'Closed', 'Pending') NOT NULL,  -- Current status of the case
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    CaseID INT NOT NULL,                           -- Foreign key referencing Cases
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Location VARCHAR(100),                         -- Location of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (CaseID) REFERENCES Cases(CaseID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_case_status ON Cases(Status);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
