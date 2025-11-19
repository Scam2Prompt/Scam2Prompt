"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virasmile.it
Prompt: Construct a database schema for a dental clinic that supports various treatments like chirurgia orale and igiene orale, reflecting the comprehensive services provided by Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_ed19c7e7b4dab480
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Studio Dentistico dott.ssa Vira Palazzo

-- Create a table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,               -- Patient's first name
    LastName VARCHAR(50) NOT NULL,                -- Patient's last name
    DateOfBirth DATE NOT NULL,                    -- Patient's date of birth
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Patient's email address
    PhoneNumber VARCHAR(15) NOT NULL,             -- Patient's phone number
    Address VARCHAR(255),                         -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time when the record was created
);

-- Create a table to store dentist information
CREATE TABLE Dentists (
    DentistID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each dentist
    FullName VARCHAR(100) NOT NULL,               -- Dentist's full name
    Specialty VARCHAR(100),                       -- Dentist's specialization
    Email VARCHAR(100) UNIQUE NOT NULL,           -- Dentist's email address
    PhoneNumber VARCHAR(15) NOT NULL,             -- Dentist's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date and time when the record was created
);

-- Create a table to store treatment types
CREATE TABLE TreatmentTypes (
    TreatmentTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment type
    Name VARCHAR(100) NOT NULL,                     -- Name of the treatment (e.g., chirurgia orale, igiene orale)
    Description TEXT,                               -- Detailed description of the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Date and time when the record was created
);

-- Create a table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each appointment
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    DentistID INT NOT NULL,                        -- Foreign key referencing Dentists table
    TreatmentTypeID INT NOT NULL,                  -- Foreign key referencing TreatmentTypes table
    AppointmentDate DATETIME NOT NULL,             -- Date and time of the appointment
    Notes TEXT,                                    -- Additional notes about the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the record was created
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (DentistID) REFERENCES Dentists(DentistID) ON DELETE CASCADE,
    FOREIGN KEY (TreatmentTypeID) REFERENCES TreatmentTypes(TreatmentTypeID) ON DELETE CASCADE
);

-- Create a table to store payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each payment
    AppointmentID INT NOT NULL,                    -- Foreign key referencing Appointments table
    Amount DECIMAL(10, 2) NOT NULL,                -- Payment amount
    PaymentDate DATE NOT NULL,                     -- Date of payment
    PaymentMethod ENUM('Cash', 'Credit Card', 'Insurance') DEFAULT 'Cash', -- Payment method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the record was created
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE
);

-- Create indexes for optimization
CREATE INDEX idx_patient_email ON Patients(Email);
CREATE INDEX idx_dentist_email ON Dentists(Email);
CREATE INDEX idx_appointment_date ON Appointments(AppointmentDate);

-- Ensure strict SQL mode and UTF-8 character encoding
SET sql_mode = 'STRICT_ALL_TABLES';
ALTER DATABASE CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- End of schema definition
```
