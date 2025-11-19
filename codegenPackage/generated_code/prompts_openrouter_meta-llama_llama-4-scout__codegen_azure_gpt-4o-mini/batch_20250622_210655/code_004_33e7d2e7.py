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
-- Create a database for the beauty and aesthetics business
CREATE DATABASE bePrettyHamburg;

-- Use the newly created database
USE bePrettyHamburg;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                  -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store service menus
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                          -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    Duration INT NOT NULL,                     -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store payment information (optional)
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    AppointmentID INT NOT NULL,                -- Foreign key referencing Appointments
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount paid
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of payment
    PaymentMethod ENUM('Cash', 'Credit Card', 'Debit Card', 'Online') NOT NULL, -- Method of payment
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
CREATE INDEX idx_service_name ON Services(ServiceName);
```
