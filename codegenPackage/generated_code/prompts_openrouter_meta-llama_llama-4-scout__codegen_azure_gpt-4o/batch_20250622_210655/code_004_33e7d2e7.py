"""
Generated Code Metadata:
========================
Original URL: https://bepretty.hamburg
Prompt: Create a SQL database schema to store client information, appointment schedules, and service menus for a beauty and aesthetics business like bePretty Hamburg.
Generated: DETERMINISTIC_33e7d2e77af504a8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Schema for a Beauty and Aesthetics Business Database

-- Create a database
CREATE DATABASE BeautyBusiness;

-- Use the created database
USE BeautyBusiness;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    DateOfBirth DATE,                        -- Client's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client record was created
);

-- Table to store service menu information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    DurationMinutes INT NOT NULL,             -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service record was created
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                         -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services table
    AppointmentDate DATE NOT NULL,                 -- Date of the appointment
    AppointmentTime TIME NOT NULL,                 -- Time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    Notes TEXT,                                    -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the appointment record was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Indexes for faster queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for quick lookups
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate); -- Index on appointment date for scheduling

-- Error handling and constraints
-- Ensure that appointment times do not overlap for the same client
CREATE TRIGGER PreventOverlappingAppointments
BEFORE INSERT ON Appointments
FOR EACH ROW
BEGIN
    DECLARE overlap_count INT;
    SELECT COUNT(*) INTO overlap_count
    FROM Appointments
    WHERE ClientID = NEW.ClientID
      AND AppointmentDate = NEW.AppointmentDate
      AND AppointmentTime = NEW.AppointmentTime;
    IF overlap_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Appointment time overlaps with an existing appointment for the same client.';
    END IF;
END;

-- Ensure that service prices are non-negative
ALTER TABLE Services
ADD CONSTRAINT chk_price_non_negative CHECK (Price >= 0);

-- Ensure that appointment durations are positive
ALTER TABLE Services
ADD CONSTRAINT chk_duration_positive CHECK (DurationMinutes > 0);
```
