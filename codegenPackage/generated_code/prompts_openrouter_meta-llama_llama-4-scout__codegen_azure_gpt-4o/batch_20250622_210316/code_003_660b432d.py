"""
Generated Code Metadata:
========================
Original URL: https://tubalife.me
Prompt: Design a database schema to store information about spa services, clients, and appointments for a business like TUBA SPA.
Generated: DETERMINISTIC_660b432d67da1906
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for TUBA SPA

-- Table to store information about spa services
CREATE TABLE SpaServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    DurationMinutes INT NOT NULL,            -- Duration of the service in minutes
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- First name of the client
    LastName VARCHAR(50) NOT NULL,           -- Last name of the client
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Phone number of the client
    DateOfBirth DATE,                        -- Date of birth of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                       -- Foreign key referencing SpaServices table
    AppointmentDate DATE NOT NULL,                -- Date of the appointment
    AppointmentTime TIME NOT NULL,                -- Time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the appointment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (ServiceID) REFERENCES SpaServices(ServiceID) ON DELETE CASCADE -- Cascade delete for service
);

-- Indexes for optimizing queries
CREATE INDEX idx_appointment_client ON Appointments(ClientID);
CREATE INDEX idx_appointment_service ON Appointments(ServiceID);
CREATE INDEX idx_appointment_date_time ON Appointments(AppointmentDate, AppointmentTime);
```
