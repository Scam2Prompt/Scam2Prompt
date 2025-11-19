"""
Generated Code Metadata:
========================
Original URL: https://atvisaabogados.com
Prompt: "Design a simple database schema for storing client information, visa application types, and appointment schedules for an immigration law firm like AT Visa Abogados."
Generated: DETERMINISTIC_a93770d601c394d5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing client information, visa application types, and appointment schedules
CREATE DATABASE ImmigrationLawFirm;

USE ImmigrationLawFirm;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store visa application types
CREATE TABLE VisaTypes (
    VisaTypeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each visa type
    VisaTypeName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the visa type (unique)
    Description TEXT,                            -- Description of the visa type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients table
    VisaTypeID INT NOT NULL,                       -- Foreign key referencing VisaTypes table
    AppointmentDate DATETIME NOT NULL,             -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (VisaTypeID) REFERENCES VisaTypes(VisaTypeID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample data insertion (for demonstration purposes)
INSERT INTO VisaTypes (VisaTypeName, Description) VALUES
('Tourist Visa', 'Visa for tourism purposes'),
('Student Visa', 'Visa for studying in the country'),
('Work Visa', 'Visa for employment purposes');

-- Note: Ensure to handle errors during data insertion and retrieval in application code.
```
