"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luxteb.com
Prompt: Create a database schema for storing patient records in a digital format, including custom fields for dental quadrant annotations, inspired by LuxChart functionality in Luxteb.
Generated: DETERMINISTIC_59a3c6c21d3e1dcb
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing patient records with custom fields for dental quadrant annotations.
-- Inspired by LuxChart functionality in Luxteb.

CREATE DATABASE DentalClinic;

USE DentalClinic;

-- Table for storing patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,             -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the patient
    ContactNumber VARCHAR(15) NULL,             -- Contact number (optional)
    Email VARCHAR(100) NULL,                    -- Email address (optional)
    Address TEXT NULL,                          -- Patient's address (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record last update timestamp
);

-- Table for storing dental quadrant annotations
CREATE TABLE DentalAnnotations (
    AnnotationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each annotation
    PatientID INT NOT NULL,                      -- Foreign key referencing Patients table
    Quadrant ENUM('Upper-Left', 'Upper-Right', 'Lower-Left', 'Lower-Right') NOT NULL, -- Quadrant of dental annotation
    ToothNumber INT NOT NULL,                    -- Tooth number within quadrant
    AnnotationText TEXT NULL,                    -- Custom annotation or notes for the tooth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure annotations are deleted if patient is deleted
);

-- Table for storing additional patient records or custom fields
CREATE TABLE PatientRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each record
    PatientID INT NOT NULL,                        -- Foreign key referencing Patients table
    RecordType VARCHAR(50) NOT NULL,               -- Type of record (e.g., 'MedicalHistory', 'VisitNotes')
    RecordDetails TEXT NULL,                       -- Detailed information for the record
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record last update timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensure records are deleted if patient is deleted
);

-- Indexing for faster lookups
CREATE INDEX IDX_PatientID ON DentalAnnotations(PatientID);
CREATE INDEX IDX_RecordType ON PatientRecords(RecordType);

-- Error handling: Ensure database schema integrity
DELIMITER $$

CREATE TRIGGER BeforeInsertDentalAnnotations
BEFORE INSERT ON DentalAnnotations
FOR EACH ROW
BEGIN
    -- Ensure ToothNumber is between 1 and 32 (valid human tooth range)
    IF NEW.ToothNumber < 1 OR NEW.ToothNumber > 32 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid ToothNumber: must be between 1 and 32';
    END IF;
END$$

DELIMITER ;

-- The schema is now ready for deployment in a production environment.
```
