"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Design a database schema to store patient information, treatment plans, and therapy sessions for a center like Centro Abakadabra, including entities for patients, therapists, and services.
Generated: DETERMINISTIC_e6f2b962e0c00787
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a therapy center to store patient information, treatment plans, and therapy sessions

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email
    Address TEXT,                             -- Patient's address
    EmergencyContactName VARCHAR(100),        -- Emergency contact name
    EmergencyContactPhone VARCHAR(15),        -- Emergency contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store therapist information
CREATE TABLE Therapists (
    TherapistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each therapist
    FirstName VARCHAR(50) NOT NULL,             -- Therapist's first name
    LastName VARCHAR(50) NOT NULL,              -- Therapist's last name
    Specialization VARCHAR(100),                -- Therapist's area of specialization
    PhoneNumber VARCHAR(15),                    -- Contact phone number
    Email VARCHAR(100),                         -- Contact email
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services offered by the center
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    DurationInMinutes INT NOT NULL,           -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store treatment plans for patients
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                         -- Foreign key referencing Patients table
    TherapistID INT NOT NULL,                       -- Foreign key referencing Therapists table
    PlanDescription TEXT NOT NULL,                  -- Description of the treatment plan
    StartDate DATE NOT NULL,                        -- Start date of the treatment plan
    EndDate DATE,                                   -- End date of the treatment plan (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE
);

-- Table to store therapy sessions
CREATE TABLE TherapySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each therapy session
    TreatmentPlanID INT NOT NULL,             -- Foreign key referencing TreatmentPlans table
    ServiceID INT NOT NULL,                   -- Foreign key referencing Services table
    SessionDate DATETIME NOT NULL,            -- Date and time of the therapy session
    Notes TEXT,                               -- Notes about the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (TreatmentPlanID) REFERENCES TreatmentPlans(TreatmentPlanID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName);
CREATE INDEX idx_therapist_name ON Therapists (FirstName, LastName);
CREATE INDEX idx_service_name ON Services (ServiceName);
CREATE INDEX idx_treatment_plan_dates ON TreatmentPlans (StartDate, EndDate);
CREATE INDEX idx_session_date ON TherapySessions (SessionDate);
```
