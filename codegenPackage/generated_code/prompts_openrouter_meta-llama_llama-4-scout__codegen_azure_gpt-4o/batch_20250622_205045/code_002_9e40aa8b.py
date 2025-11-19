"""
Generated Code Metadata:
========================
Original URL: https://solana2018.com
Prompt: Generate a sample database schema for storing patient information, therapy session records, and practitioner details for an整体 clinic with an online booking system.
Generated: DETERMINISTIC_9e40aa8b2681ff30
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an holistic clinic with patient information, therapy session records, 
-- practitioner details, and an online booking system.

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email address
    Address TEXT,                             -- Patient's address
    EmergencyContactName VARCHAR(100),        -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),        -- Emergency contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store practitioner details
CREATE TABLE Practitioners (
    PractitionerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each practitioner
    FirstName VARCHAR(50) NOT NULL,                -- Practitioner's first name
    LastName VARCHAR(50) NOT NULL,                 -- Practitioner's last name
    Specialty VARCHAR(100) NOT NULL,               -- Area of expertise or specialty
    PhoneNumber VARCHAR(15),                       -- Contact phone number
    Email VARCHAR(100),                            -- Contact email address
    Bio TEXT,                                      -- Short biography or description
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store therapy session records
CREATE TABLE TherapySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each session
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    PractitionerID INT NOT NULL,                   -- Foreign key referencing Practitioners table
    SessionDate DATETIME NOT NULL,                 -- Date and time of the session
    DurationMinutes INT NOT NULL,                  -- Duration of the session in minutes
    Notes TEXT,                                    -- Notes or observations from the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (PractitionerID) REFERENCES Practitioners(PractitionerID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store online booking information
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each booking
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    PractitionerID INT NOT NULL,                   -- Foreign key referencing Practitioners table
    BookingDate DATETIME NOT NULL,                 -- Date and time of the booking
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Booking status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (PractitionerID) REFERENCES Practitioners(PractitionerID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName);
CREATE INDEX idx_practitioner_name ON Practitioners (FirstName, LastName);
CREATE INDEX idx_session_date ON TherapySessions (SessionDate);
CREATE INDEX idx_booking_date ON Bookings (BookingDate);
```
