"""
Generated Code Metadata:
========================
Original URL: https://healthcareventure.nl
Prompt: Develop a simple database schema to store information about clients, employees, and services provided by a youth mental healthcare company, considering the need for superior client-focused care.
Generated: DETERMINISTIC_26428b63e4d0423d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a youth mental healthcare company

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    DateOfBirth DATE NOT NULL,               -- Client's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Client's gender
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Email VARCHAR(100),                      -- Client's email address
    Address TEXT,                            -- Client's physical address
    EmergencyContactName VARCHAR(100),       -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),       -- Emergency contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store employee information
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(50) NOT NULL,            -- Employee's first name
    LastName VARCHAR(50) NOT NULL,             -- Employee's last name
    Role ENUM('Therapist', 'Counselor', 'Admin', 'Other') NOT NULL, -- Employee's role
    PhoneNumber VARCHAR(15),                   -- Employee's phone number
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Employee's email address
    HireDate DATE NOT NULL,                    -- Employee's hire date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services provided
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the service
    DurationInMinutes INT NOT NULL,           -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointments between clients and employees for services
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    EmployeeID INT NOT NULL,                      -- Foreign key referencing Employees table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE SET NULL, -- Set NULL if employee is deleted
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE SET NULL -- Set NULL if service is deleted
);

-- Table to store feedback from clients about services
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback entry
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                    -- Foreign key referencing Services table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the service (1-5 scale)
    Comments TEXT,                             -- Additional comments from the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE SET NULL -- Set NULL if service is deleted
);

-- Ensure the database is optimized for client-focused care
-- Indexes for faster lookups
CREATE INDEX idx_client_name ON Clients (FirstName, LastName);
CREATE INDEX idx_employee_name ON Employees (FirstName, LastName);
CREATE INDEX idx_service_name ON Services (ServiceName);
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate);
```
