"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Design a simple database schema for storing client information, services provided, and appointment schedules for a business like Style & Makeup Effect.
Generated: DETERMINISTIC_7cee35e1c48d1128
Batch ID: 20250622_205548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Style & Makeup Effect business

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

-- Create a table to store services provided by the business
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

-- Indexes for faster querying
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
