"""
Generated Code Metadata:
========================
Original URL: https://smart-medicalservices.com
Prompt: Design a database schema for a medical services company like Smart Medical Services, including tables for patients, services, appointments, and healthcare providers.
Generated: DETERMINISTIC_da479d314ca2472b
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a medical services company

-- Table: Patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact phone number
    Email VARCHAR(100),                       -- Contact email
    Address TEXT,                             -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: HealthcareProviders
CREATE TABLE HealthcareProviders (
    ProviderID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each provider
    FirstName VARCHAR(50) NOT NULL,            -- Provider's first name
    LastName VARCHAR(50) NOT NULL,             -- Provider's last name
    Specialty VARCHAR(100) NOT NULL,           -- Provider's medical specialty
    PhoneNumber VARCHAR(15),                   -- Contact phone number
    Email VARCHAR(100),                        -- Contact email
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the medical service
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    ProviderID INT NOT NULL,                      -- Foreign key referencing HealthcareProviders table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Appointment status
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete for patient
    FOREIGN KEY (ProviderID) REFERENCES HealthcareProviders(ProviderID) ON DELETE CASCADE, -- Cascade delete for provider
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete for service
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_name ON Patients (FirstName, LastName);
CREATE INDEX idx_provider_name ON HealthcareProviders (FirstName, LastName);
CREATE INDEX idx_service_name ON Services (ServiceName);
CREATE INDEX idx_appointment_date ON Appointments (AppointmentDate);
```
