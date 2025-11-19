"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Construct a database schema for a dental clinic that includes tables for patients, services, and reviews, based on the structure used by Buford Dental.
Generated: DETERMINISTIC_bfa42843abfded17
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a dental clinic

-- Table: Patients
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    PhoneNumber VARCHAR(15) NOT NULL,         -- Contact phone number
    Email VARCHAR(100) UNIQUE,                -- Contact email (must be unique)
    Address TEXT,                             -- Patient's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Services
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the dental service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Cost of the service
    DurationMinutes INT NOT NULL,             -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table: Reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    PatientID INT NOT NULL,                   -- Foreign key referencing Patients table
    ServiceID INT NOT NULL,                   -- Foreign key referencing Services table
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating for the service (1 to 5)
    Comments TEXT,                            -- Optional comments from the patient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE, -- Cascade delete if patient is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Cascade delete if service is removed
);

-- Indexes for performance optimization
CREATE INDEX idx_patient_email ON Patients(Email); -- Index for quick lookup by email
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for quick lookup by service name
CREATE INDEX idx_review_patient_service ON Reviews(PatientID, ServiceID); -- Composite index for reviews lookup
```
