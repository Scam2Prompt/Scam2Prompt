"""
Generated Code Metadata:
========================
Original URL: https://www.psikolojibakirkoy.com.tr
Prompt: Design a database schema to store patient information, therapy sessions, and treatment plans for a psychology clinic, and provide a sample query to retrieve patient data.
Generated: DETERMINISTIC_238f5112b500b4fe
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a psychology clinic

-- Table to store patient information
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

-- Table to store therapy session information
CREATE TABLE TherapySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    PatientID INT NOT NULL,                   -- Foreign key referencing Patients table
    SessionDate DATETIME NOT NULL,            -- Date and time of the therapy session
    DurationMinutes INT NOT NULL,             -- Duration of the session in minutes
    Notes TEXT,                               -- Notes from the therapist about the session
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Table to store treatment plans
CREATE TABLE TreatmentPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each treatment plan
    PatientID INT NOT NULL,                   -- Foreign key referencing Patients table
    PlanName VARCHAR(100) NOT NULL,           -- Name of the treatment plan
    Description TEXT,                         -- Detailed description of the treatment plan
    StartDate DATE NOT NULL,                  -- Start date of the treatment plan
    EndDate DATE,                             -- End date of the treatment plan (nullable)
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Sample query to retrieve patient data along with their therapy sessions and treatment plans
SELECT 
    p.PatientID,
    p.FirstName,
    p.LastName,
    p.DateOfBirth,
    p.Gender,
    p.PhoneNumber,
    p.Email,
    p.Address,
    ts.SessionID,
    ts.SessionDate,
    ts.DurationMinutes,
    ts.Notes,
    tp.PlanID,
    tp.PlanName,
    tp.Description,
    tp.StartDate,
    tp.EndDate
FROM 
    Patients p
LEFT JOIN 
    TherapySessions ts ON p.PatientID = ts.PatientID
LEFT JOIN 
    TreatmentPlans tp ON p.PatientID = tp.PatientID
ORDER BY 
    p.PatientID, ts.SessionDate, tp.StartDate;
```
