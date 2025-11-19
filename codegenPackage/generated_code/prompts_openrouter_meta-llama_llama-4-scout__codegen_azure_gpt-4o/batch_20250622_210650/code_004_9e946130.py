"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: Design a basic database schema for storing client information, appointments, and counseling session records for a text-based counseling service like the one offered on textcounsellingonline.com.au.
Generated: DETERMINISTIC_9e946130e3034460
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Text-Based Counseling Service

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    DateOfBirth DATE,                        -- Client's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment information
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    CounselorID INT NOT NULL,                     -- Foreign key referencing Counselors table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    Notes TEXT,                                   -- Optional notes about the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (CounselorID) REFERENCES Counselors(CounselorID) ON DELETE SET NULL -- Set to NULL if counselor is removed
);

-- Table to store counseling session records
CREATE TABLE CounselingSessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    AppointmentID INT NOT NULL,               -- Foreign key referencing Appointments table
    SessionNotes TEXT NOT NULL,               -- Detailed notes about the session
    SessionDuration INT NOT NULL,             -- Duration of the session in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Cascade delete if appointment is removed
);

-- Table to store counselor information
CREATE TABLE Counselors (
    CounselorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each counselor
    FirstName VARCHAR(50) NOT NULL,            -- Counselor's first name
    LastName VARCHAR(50) NOT NULL,             -- Counselor's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Counselor's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Counselor's phone number
    Specialization VARCHAR(100),               -- Counselor's area of expertise
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_counselor_email ON Counselors(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);

-- Error handling and constraints
-- Ensure email format is valid (can be enforced at application level or using regex constraints in some DBMS)
-- Ensure foreign key relationships are maintained properly
-- Use ENUM for status fields to restrict values to predefined options
```
