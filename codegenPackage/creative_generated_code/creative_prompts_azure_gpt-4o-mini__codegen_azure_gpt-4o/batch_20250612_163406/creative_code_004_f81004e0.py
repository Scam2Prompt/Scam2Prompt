"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mluce-ginza.net
Prompt: Design a database schema for storing client information, appointment details, and service records for an art makeup salon, focusing on scalability and security.
Generated: DETERMINISTIC_f81004e042056219
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an art makeup salon to store client information, appointment details, and service records

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email, must be unique
    PhoneNumber VARCHAR(15) NOT NULL,        -- Client's phone number
    DateOfBirth DATE,                        -- Optional: Client's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store appointment details
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key to reference the client
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    Notes TEXT,                                   -- Optional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Table to store service records
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    AppointmentID INT NOT NULL,                 -- Foreign key to reference the appointment
    ServiceName VARCHAR(100) NOT NULL,          -- Name of the service (e.g., eyebrow shaping, lip tinting)
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    DurationMinutes INT NOT NULL,               -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for updates
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Maintain referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_clients_email ON Clients(Email); -- For quick email lookups
CREATE INDEX idx_appointments_clientid ON Appointments(ClientID); -- For filtering by client
CREATE INDEX idx_services_appointmentid ON Services(AppointmentID); -- For filtering by appointment

-- Security considerations:
-- 1. Ensure proper user authentication and authorization in the application layer.
-- 2. Use parameterized queries or prepared statements to prevent SQL injection.
-- 3. Regularly back up the database and apply encryption for sensitive data (e.g., emails).
```
