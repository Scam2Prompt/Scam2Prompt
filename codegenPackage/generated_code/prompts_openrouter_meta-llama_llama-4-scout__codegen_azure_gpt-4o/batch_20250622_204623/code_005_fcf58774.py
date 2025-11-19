"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Design a database schema to store patient information, treatment plans, and services offered by the San Diego Sleep and TMJ Center, including information about their doctors and staff.
Generated: DETERMINISTIC_fcf587744cd5a692
Batch ID: 20250622_204623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for San Diego Sleep and TMJ Center

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
<<<<<<< HEAD
    PhoneNumber VARCHAR(15),                  -- Patient's contact number
    Email VARCHAR(100),                       -- Patient's email address
    Address TEXT,                             -- Patient's residential address
    EmergencyContactName VARCHAR(100),       -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),       -- Emergency contact phone number
=======
    PhoneNumber VARCHAR(15),                  -- Patient's phone number
    Email VARCHAR(100),                       -- Patient's email address
    Address TEXT,                             -- Patient's address
    EmergencyContactName VARCHAR(100),        -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),        -- Emergency contact phone number
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store doctors and staff information
CREATE TABLE Staff (
<<<<<<< HEAD
    StaffID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,          -- Staff's first name
    LastName VARCHAR(50) NOT NULL,           -- Staff's last name
    Role ENUM('Doctor', 'Nurse', 'Admin', 'Technician') NOT NULL, -- Staff's role
    Specialty VARCHAR(100),                  -- Specialty (if applicable, e.g., "Sleep Disorders")
    PhoneNumber VARCHAR(15),                 -- Staff's contact number
    Email VARCHAR(100),                      -- Staff's email address
=======
    StaffID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each staff member
    FirstName VARCHAR(50) NOT NULL,           -- Staff's first name
    LastName VARCHAR(50) NOT NULL,            -- Staff's last name
    Role ENUM('Doctor', 'Nurse', 'Admin', 'Other') NOT NULL, -- Staff's role
    Specialty VARCHAR(100),                   -- Specialty (if applicable, e.g., TMJ specialist)
    PhoneNumber VARCHAR(15),                  -- Staff's phone number
    Email VARCHAR(100),                       -- Staff's email address
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services offered by the center
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
<<<<<<< HEAD
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., "Sleep Study")
=======
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store treatment plans for patients
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    StaffID INT NOT NULL,                           -- Foreign key referencing Staff table
<<<<<<< HEAD
    Diagnosis TEXT NOT NULL,                        -- Diagnosis for the patient
    TreatmentDescription TEXT NOT NULL,             -- Description of the treatment plan
=======
    Diagnosis TEXT NOT NULL,                        -- Diagnosis for the treatment plan
    TreatmentDetails TEXT NOT NULL,                 -- Detailed treatment plan
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    StartDate DATE NOT NULL,                        -- Start date of the treatment plan
    EndDate DATE,                                   -- End date of the treatment plan (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE SET NULL         -- Set NULL on staff deletion
);

<<<<<<< HEAD
-- Table to store appointments for services
=======
-- Table to store appointments for patients
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    StaffID INT NOT NULL,                         -- Foreign key referencing Staff table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) ON DELETE SET NULL,       -- Set NULL on staff deletion
<<<<<<< HEAD
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete
=======
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE SET NULL -- Set NULL on service deletion
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName);
CREATE INDEX idx_staff_role ON Staff (Role);
CREATE INDEX idx_service_name ON Services (ServiceName);
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate);
```
