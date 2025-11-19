"""
Generated Code Metadata:
========================
Original URL: https://asbeviclin.com.br
Prompt: Design a database schema to store information about medical professionals, patients, and appointments for a healthcare provider like Asbeviclin.
Generated: DETERMINISTIC_2eb69e8d6e71f9c0
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a healthcare provider system

-- Table to store information about medical professionals
CREATE TABLE MedicalProfessionals (
    ProfessionalID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each medical professional
    FirstName VARCHAR(50) NOT NULL,                -- First name of the medical professional
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the medical professional
    Specialty VARCHAR(100) NOT NULL,               -- Area of specialization (e.g., cardiology, dermatology)
    PhoneNumber VARCHAR(15),                       -- Contact phone number
    Email VARCHAR(100) UNIQUE,                     -- Contact email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,                -- First name of the patient
    LastName VARCHAR(50) NOT NULL,                 -- Last name of the patient
    DateOfBirth DATE NOT NULL,                     -- Date of birth of the patient
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the patient
    PhoneNumber VARCHAR(15),                       -- Contact phone number
    Email VARCHAR(100) UNIQUE,                     -- Contact email address
    Address TEXT,                                  -- Address of the patient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    ProfessionalID INT NOT NULL,                   -- Foreign key referencing MedicalProfessionals table
    AppointmentDate DATETIME NOT NULL,             -- Date and time of the appointment
    ReasonForVisit TEXT,                           -- Reason for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete for patient
    FOREIGN KEY (ProfessionalID) REFERENCES MedicalProfessionals(ProfessionalID) ON DELETE CASCADE -- Cascade delete for professional
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_email ON Patients(Email); -- Index for quick lookup of patients by email
CREATE INDEX idx_professional_email ON MedicalProfessionals(Email); -- Index for quick lookup of professionals by email
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate); -- Index for quick lookup of appointments by date
```
