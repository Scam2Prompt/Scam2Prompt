"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Design a database schema for storing patient information and hair transplant results at AuQual Hair Services, ensuring it includes fields for treatment type and cost.
Generated: DETERMINISTIC_cb88a39e0d877f75
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing patient information and hair transplant results
-- Designed for AuQual Hair Services

-- Table for storing patient details
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    ContactNumber VARCHAR(15),                -- Patient's contact number
    Email VARCHAR(100),                       -- Patient's email address
    Address TEXT                              -- Patient's residential address
);

-- Table for storing hair transplant treatments
CREATE TABLE HairTransplantResults (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment
    PatientID INT NOT NULL,                     -- Foreign key referencing Patients table
    TreatmentType VARCHAR(50) NOT NULL,         -- Type of hair transplant treatment performed
    TreatmentDate DATE NOT NULL,                -- Date the treatment was performed
    Cost DECIMAL(10, 2) NOT NULL,               -- Cost of the treatment
    ResultDescription TEXT,                     -- Description of the results achieved
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Indexes for optimizing common queries
CREATE INDEX idx_patient_name ON Patients (LastName, FirstName);
CREATE INDEX idx_treatment_date ON HairTransplantResults (TreatmentDate);
```
