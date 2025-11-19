"""
Generated Code Metadata:
========================
Original URL: https://estetus.lt
Prompt: "Design a database schema to store information about clients, procedures, and appointments for a clinic like Estetus."
Generated: DETERMINISTIC_cf14bbe69aea5d53
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a clinic management system

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    DateOfBirth DATE,                        -- Client's date of birth
    Gender ENUM('Male', 'Female', 'Other'),  -- Client's gender
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store procedure information
CREATE TABLE Procedures (
    ProcedureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each procedure
    Name VARCHAR(100) NOT NULL,                 -- Name of the procedure
    Description TEXT,                           -- Detailed description of the procedure
    DurationInMinutes INT NOT NULL,            -- Duration of the procedure in minutes
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the procedure
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    ProcedureID INT NOT NULL,                     -- Foreign key referencing Procedures table
    AppointmentDate DATE NOT NULL,                -- Date of the appointment
    AppointmentTime TIME NOT NULL,                -- Time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete for client
    FOREIGN KEY (ProcedureID) REFERENCES Procedures(ProcedureID) ON DELETE CASCADE -- Cascade delete for procedure
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate); -- Index for quick lookup by date
```
