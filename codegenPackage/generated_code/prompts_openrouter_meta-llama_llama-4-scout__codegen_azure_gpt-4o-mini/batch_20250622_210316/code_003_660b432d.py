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

-- Create a table to store information about spa services
CREATE TABLE SpaServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the spa service
    Description TEXT,                           -- Description of the service
    Duration INT NOT NULL,                      -- Duration of the service in minutes
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the service was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,            -- Client's first name
    LastName VARCHAR(50) NOT NULL,              -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                    -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the client was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                         -- Foreign key referencing SpaServices
    AppointmentDate DATETIME NOT NULL,              -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the appointment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES SpaServices(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create an index on AppointmentDate for faster queries
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
