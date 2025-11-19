"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: Design a database schema for managing client information and appointment scheduling for an equine care service, taking cues from the organizational structure of Martin Godwin Equine Services.
Generated: DETERMINISTIC_d5ab1b53594d67ff
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client information and appointment scheduling
-- for an equine care service.

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store horse information
CREATE TABLE Horses (
    HorseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each horse
    ClientID INT NOT NULL,                   -- Foreign key linking to the client
    Name VARCHAR(50) NOT NULL,               -- Horse's name
    Breed VARCHAR(50),                       -- Horse's breed
    Age INT,                                 -- Horse's age
    Gender ENUM('Male', 'Female'),           -- Horse's gender
    MedicalHistory TEXT,                     -- Medical history of the horse
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key linking to the client
    HorseID INT NOT NULL,                         -- Foreign key linking to the horse
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    ServiceType VARCHAR(100) NOT NULL,            -- Type of service (e.g., check-up, grooming)
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (HorseID) REFERENCES Horses(HorseID) ON DELETE CASCADE -- Cascade delete if horse is removed
);

-- Table to store staff information
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,         -- Staff member's first name
    LastName VARCHAR(50) NOT NULL,          -- Staff member's last name
    Email VARCHAR(100) UNIQUE NOT NULL,     -- Staff member's email address
    PhoneNumber VARCHAR(15),                -- Staff member's phone number
    Role VARCHAR(50) NOT NULL,              -- Staff member's role (e.g., veterinarian, assistant)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store staff assignments for appointments
CREATE TABLE StaffAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    AppointmentID INT NOT NULL,                  -- Foreign key linking to the appointment
    StaffID INT NOT NULL,                        -- Foreign key linking to the staff member
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the assignment was made
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE, -- Cascade delete if appointment is removed
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE CASCADE -- Cascade delete if staff member is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_horse_name ON Horses(Name);     -- Index for quick lookup by horse name
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate); -- Index for quick lookup by appointment date
CREATE INDEX idx_staff_email ON Staff(Email);    -- Index for quick lookup by staff email
```
