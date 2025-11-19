"""
Generated Code Metadata:
========================
Original URL: https://mluce-ginza.net
Prompt: Design a database schema for storing client information, appointment details, and service records for an art makeup salon, focusing on scalability and security.
Generated: DETERMINISTIC_f81004e042056219
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an Art Makeup Salon

-- Create a database for the salon
CREATE DATABASE ArtMakeupSalon;

-- Use the created database
USE ArtMakeupSalon;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    CONSTRAINT chk_email CHECK (Email LIKE '%_@__%.__%')  -- Basic email format validation
);

-- Table to store appointment details
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    AppointmentDate DATETIME NOT NULL,             -- Date and time of the appointment
    ServiceType VARCHAR(50) NOT NULL,              -- Type of service booked
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store service records
CREATE TABLE ServiceRecords (
    ServiceRecordID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service record
    AppointmentID INT NOT NULL,                       -- Foreign key referencing Appointments
    ServiceDescription TEXT NOT NULL,                 -- Description of the service provided
    Price DECIMAL(10, 2) NOT NULL,                   -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
CREATE INDEX idx_service_record_price ON ServiceRecords(Price);

-- Security measures: Ensure that sensitive data is encrypted
-- Note: Actual encryption implementation would depend on the application layer
-- and is not included in this schema.

-- End of schema
```
