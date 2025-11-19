"""
Generated Code Metadata:
========================
Original URL: https://vitalcs.net
Prompt: Design a database schema for a healthcare services company that handles patient data, billing, and medical records, taking into account the services provided by Vital Corporate Solutions.
Generated: DETERMINISTIC_95ddf4dab6d65feb
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a Healthcare Services Company

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

-- Table to store medical records
CREATE TABLE MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each medical record
    PatientID INT NOT NULL,                   -- Foreign key referencing Patients table
    Diagnosis TEXT NOT NULL,                  -- Diagnosis details
    Treatment TEXT,                           -- Treatment details
    Prescription TEXT,                        -- Prescription details
    DoctorName VARCHAR(100) NOT NULL,         -- Name of the doctor who handled the case
    RecordDate DATE NOT NULL,                 -- Date of the medical record
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store billing information
CREATE TABLE Billing (
    BillingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each billing record
    PatientID INT NOT NULL,                   -- Foreign key referencing Patients table
    ServiceDescription TEXT NOT NULL,         -- Description of the service provided
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount charged for the service
    PaymentStatus ENUM('Pending', 'Paid', 'Cancelled') NOT NULL, -- Payment status
    BillingDate DATE NOT NULL,                -- Date of the billing record
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store services provided by the company
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    ServiceDescription TEXT,                  -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    PatientID INT NOT NULL,                       -- Foreign key referencing Patients table
    ServiceID INT NOT NULL,                       -- Foreign key referencing Services table
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    DoctorName VARCHAR(100) NOT NULL,             -- Name of the doctor assigned to the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL, -- Appointment status
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store user accounts for system access
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,     -- Username for login
    PasswordHash VARCHAR(255) NOT NULL,       -- Hashed password for security
    Role ENUM('Admin', 'Doctor', 'Staff') NOT NULL, -- Role of the user in the system
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to log system activities for auditing purposes
CREATE TABLE AuditLogs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each log entry
    UserID INT NOT NULL,                      -- Foreign key referencing Users table
    Action VARCHAR(255) NOT NULL,             -- Description of the action performed
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the action
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensure referential integrity
);
```
