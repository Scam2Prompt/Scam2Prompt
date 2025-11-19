"""
Generated Code Metadata:
========================
Original URL: https://depilarmg.com.br
Prompt: Generate a sample database schema to store client information, services offered, and appointment schedules for a business like Depilar MG.
Generated: DETERMINISTIC_2fde81f22b8c1d36
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for a business like Depilar MG

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service
    Description TEXT,                           -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the service
    Duration INT NOT NULL,                      -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Create a table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                         -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,             -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Create an index on AppointmentDate for faster queries
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
