"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Develop a basic SQL database schema to store patient data, appointment schedules, and medical records for a gastroenterology clinic that offers services such as endocrinologia, motilidade digestiva, and proctologia.
Generated: DETERMINISTIC_96e78c93bc4e5fc3
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for a Gastroenterology Clinic

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS MedicalRecords;
DROP TABLE IF EXISTS Services;

-- Table to store patient information
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

-- Table to store available services offered by the clinic
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the service (e.g., endocrinologia)
    Description TEXT                           -- Description of the service
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store medical records for patients
CREATE TABLE MedicalRecords (
    RecordID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each medical record
    PatientID INT NOT NULL,                      -- Foreign key referencing Patients
    RecordDate DATE NOT NULL,                    -- Date of the medical record
    Diagnosis TEXT,                              -- Diagnosis information
    Treatment TEXT,                              -- Treatment information
    Notes TEXT,                                  -- Additional notes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Insert sample services into the Services table
INSERT INTO Services (ServiceName, Description) VALUES
('Endocrinologia', 'Specialized care for endocrine system disorders.'),
('Motilidade Digestiva', 'Assessment and treatment of digestive motility issues.'),
('Proctologia', 'Diagnosis and treatment of rectal and anal disorders.');

-- Note: Ensure to handle errors during insertion and other operations in application code.
```
