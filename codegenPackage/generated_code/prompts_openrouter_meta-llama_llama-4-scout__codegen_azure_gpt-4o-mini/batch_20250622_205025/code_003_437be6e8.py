"""
Generated Code Metadata:
========================
Original URL: https://japkasai.net
Prompt: "Design a database schema for storing client information, appointment schedules, and service details for a men's grooming salon, considering factors like data privacy and scalability."
Generated: DETERMINISTIC_437be6e8d7ddf18d
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a men's grooming salon

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (unique)
    PhoneNumber VARCHAR(15) NOT NULL,         -- Client's phone number
    DateOfBirth DATE,                          -- Client's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    CONSTRAINT chk_email CHECK (Email LIKE '%_@__%.__%')  -- Basic email format validation
);

-- Create a table to store service details
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
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create an index on AppointmentDate for faster queries
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);

-- Create a table to store user roles for data privacy
CREATE TABLE UserRoles (
    RoleID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each role
    RoleName VARCHAR(50) NOT NULL UNIQUE,   -- Name of the role (e.g., Admin, Staff)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Create a table to store users with access to the system
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,       -- Unique username for login
    PasswordHash VARCHAR(255) NOT NULL,         -- Hashed password for security
    RoleID INT NOT NULL,                         -- Foreign key referencing UserRoles
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (RoleID) REFERENCES UserRoles(RoleID) ON DELETE RESTRICT  -- Ensure referential integrity
);
```
