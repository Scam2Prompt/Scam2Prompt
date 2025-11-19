"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Create a database schema for storing patient records in a digital format, including custom fields for dental quadrant annotations, inspired by LuxChart functionality in Luxteb.
Generated: DETERMINISTIC_59a3c6c21d3e1dcb
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing patient records with dental quadrant annotations

CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,          -- Patient's first name
    LastName VARCHAR(50) NOT NULL,           -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Patient's phone number
    Email VARCHAR(100),                       -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE DentalQuadrants (
    QuadrantID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each dental quadrant record
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    QuadrantNumber INT NOT NULL CHECK (QuadrantNumber BETWEEN 1 AND 4), -- Quadrant number (1-4)
    Annotations TEXT,                           -- Custom annotations for the dental quadrant
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE MedicalHistory (
    HistoryID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each medical history record
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    Condition VARCHAR(255),                     -- Medical condition description
    Treatment VARCHAR(255),                     -- Treatment description
    DateDiagnosed DATE,                         -- Date when the condition was diagnosed
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    ReasonForVisit VARCHAR(255),                 -- Reason for the visit
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_lastname ON Patients(LastName);
CREATE INDEX idx_patient_email ON Patients(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);
```
