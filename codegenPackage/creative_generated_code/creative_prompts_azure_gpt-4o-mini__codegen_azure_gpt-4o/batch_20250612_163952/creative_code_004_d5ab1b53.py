"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.martingodwinequine.com
Prompt: Design a database schema for managing client information and appointment scheduling for an equine care service, taking cues from the organizational structure of Martin Godwin Equine Services.
Generated: DETERMINISTIC_d5ab1b53594d67ff
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Client Information and Appointment Scheduling

-- Create a table for storing client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,         -- First name of the client
    LastName VARCHAR(100) NOT NULL,          -- Last name of the client
    Email VARCHAR(150) UNIQUE,               -- Email address (unique for each client)
    PhoneNumber VARCHAR(15),                 -- Contact phone number
    Address TEXT,                            -- Address for billing or communication
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        ON UPDATE CURRENT_TIMESTAMP          -- Record last update time
);

-- Create a table to manage equine-related information
CREATE TABLE Horses (
    HorseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each horse
    ClientID INT NOT NULL,                   -- Foreign key referencing the client
    HorseName VARCHAR(100) NOT NULL,         -- Name of the horse
    Breed VARCHAR(100),                      -- Breed of the horse
    Age INT,                                 -- Age of the horse
    MedicalHistory TEXT,                     -- Medical history or notes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        ON UPDATE CURRENT_TIMESTAMP,         -- Record last update time
    CONSTRAINT FK_Horse_Client FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
        ON DELETE CASCADE                    -- Cascade delete if client is removed
);

-- Create a table for managing appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing the client
    HorseID INT NOT NULL,                         -- Foreign key referencing the horse
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    ServiceType VARCHAR(100) NOT NULL,           -- Type of service (e.g., grooming, veterinary care)
    Notes TEXT,                                  -- Additional notes for the appointment
    Status ENUM('Scheduled', 'Completed', 'Canceled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        ON UPDATE CURRENT_TIMESTAMP,             -- Record last update time
    CONSTRAINT FK_Appointment_Client FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
        ON DELETE CASCADE,                       -- Cascade delete if client is removed
    CONSTRAINT FK_Appointment_Horse FOREIGN KEY (HorseID) REFERENCES Horses(HorseID)
        ON DELETE CASCADE                        -- Cascade delete if horse is removed
);

-- Create a table for managing staff information
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each staff member
    FirstName VARCHAR(100) NOT NULL,            -- First name of the staff
    LastName VARCHAR(100) NOT NULL,             -- Last name of the staff
    Role VARCHAR(100) NOT NULL,                 -- Role or title (e.g., Vet, Groomer)
    Email VARCHAR(150) UNIQUE,                  -- Email address for communication
    PhoneNumber VARCHAR(15),                    -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation time
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        ON UPDATE CURRENT_TIMESTAMP             -- Record last update time
);

-- Create a table for linking staff with appointments
CREATE TABLE AppointmentStaff (
    ID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each entry
    AppointmentID INT NOT NULL,                 -- Foreign key referencing the appointment
    StaffID INT NOT NULL,                       -- Foreign key referencing the staff member
    Role VARCHAR(100),                          -- Specific role for this appointment (optional)
    CONSTRAINT FK_AppointmentStaff_Appointment FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
        ON DELETE CASCADE,                      -- Cascade delete if appointment is removed
    CONSTRAINT FK_AppointmentStaff_Staff FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
        ON DELETE CASCADE                       -- Cascade delete if staff is removed
);

-- Auxiliary indexes for optimization
CREATE INDEX IDX_ClientID ON Horses(ClientID);
CREATE INDEX IDX_ClientHorseID ON Appointments(ClientID, HorseID);
CREATE INDEX IDX_AppointmentID ON AppointmentStaff(AppointmentID);
CREATE INDEX IDX_StaffID ON AppointmentStaff(StaffID);
```
