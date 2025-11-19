"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Construct a database schema for a dental clinic that supports various treatments like chirurgia orale and igiene orale, reflecting the comprehensive services provided by Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_ed19c7e7b4dab480
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a dental clinic: Studio Dentistico dott.ssa Vira Palazzo

-- Create a table for storing information about patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email
    Address TEXT                              -- Patient's address
);

-- Create a table for storing information about treatments
CREATE TABLE Treatments (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment
    Name VARCHAR(100) NOT NULL,                 -- Name of the treatment (e.g., chirurgia orale, igiene orale)
    Description TEXT,                           -- Detailed description of the treatment
    Price DECIMAL(10, 2) NOT NULL,              -- Cost of the treatment
    DurationMinutes INT NOT NULL               -- Duration of the treatment in minutes
);

-- Create a table for storing appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    TreatmentID INT NOT NULL,                      -- Foreign key referencing Treatments table
    AppointmentDate DATETIME NOT NULL,             -- Date and time of the appointment
    Notes TEXT,                                    -- Additional notes for the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled', -- Status of the appointment
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete if patient is removed
    FOREIGN KEY (TreatmentID) REFERENCES Treatments(TreatmentID) ON DELETE CASCADE -- Cascade delete if treatment is removed
);

-- Create a table for storing staff information
CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,         -- Staff member's first name
    LastName VARCHAR(50) NOT NULL,          -- Staff member's last name
    Role VARCHAR(50) NOT NULL,              -- Role of the staff member (e.g., dentist, hygienist, receptionist)
    PhoneNumber VARCHAR(15),                -- Contact phone number
    Email VARCHAR(100),                     -- Contact email
    HireDate DATE NOT NULL                  -- Date the staff member was hired
);

-- Create a table for assigning staff to appointments
CREATE TABLE AppointmentStaff (
    AppointmentStaffID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    AppointmentID INT NOT NULL,                        -- Foreign key referencing Appointments table
    StaffID INT NOT NULL,                              -- Foreign key referencing Staff table
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE, -- Cascade delete if appointment is removed
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE CASCADE -- Cascade delete if staff member is removed
);

-- Create a table for storing payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    AppointmentID INT NOT NULL,               -- Foreign key referencing Appointments table
    Amount DECIMAL(10, 2) NOT NULL,           -- Payment amount
    PaymentDate DATETIME NOT NULL,            -- Date and time of the payment
    PaymentMethod ENUM('Cash', 'Credit Card', 'Debit Card', 'Insurance') NOT NULL, -- Payment method
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Cascade delete if appointment is removed
);

-- Create a table for storing feedback from patients
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback
    PatientID INT NOT NULL,                    -- Foreign key referencing Patients table
    AppointmentID INT NOT NULL,                -- Foreign key referencing Appointments table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the patient (1-5)
    Comments TEXT,                             -- Additional comments from the patient
    FeedbackDate DATETIME NOT NULL,            -- Date and time of the feedback
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete if patient is removed
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Cascade delete if appointment is removed
);
```
