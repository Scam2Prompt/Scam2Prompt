"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Design a database schema to store patient data and therapy outcomes for a DBT clinic, and provide a SQL code example for data querying and analysis."
Generated: DETERMINISTIC_0583b3eae5a9ec88
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for a DBT Clinic

-- Table to store patient information
CREATE TABLE Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,           -- Patient's first name
    LastName VARCHAR(50) NOT NULL,            -- Patient's last name
    DateOfBirth DATE NOT NULL,                -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Patient's gender
    PhoneNumber VARCHAR(15),                  -- Contact number
    Email VARCHAR(100),                       -- Email address
    Address TEXT                              -- Residential address
);

-- Table to store therapy sessions
CREATE TABLE TherapySessions (
    SessionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each session
    PatientID INT NOT NULL,                   -- Foreign key linking to Patients table
    SessionDate DATE NOT NULL,                -- Date of the therapy session
    TherapistName VARCHAR(100) NOT NULL,      -- Name of the therapist conducting the session
    SessionNotes TEXT,                        -- Notes from the session
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE
);

-- Table to store therapy outcomes
CREATE TABLE TherapyOutcomes (
    OutcomeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each outcome record
    PatientID INT NOT NULL,                   -- Foreign key linking to Patients table
    SessionID INT NOT NULL,                   -- Foreign key linking to TherapySessions table
    OutcomeDate DATE NOT NULL,                -- Date the outcome was recorded
    OutcomeScore INT NOT NULL,                -- Numeric score representing therapy outcome
    OutcomeDescription TEXT,                  -- Detailed description of the outcome
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (SessionID) REFERENCES TherapySessions(SessionID) ON DELETE CASCADE
);

-- Example Query: Retrieve average therapy outcome scores for each patient
SELECT 
    P.PatientID,
    CONCAT(P.FirstName, ' ', P.LastName) AS FullName,
    AVG(O.OutcomeScore) AS AverageOutcomeScore
FROM 
    Patients P
JOIN 
    TherapyOutcomes O ON P.PatientID = O.PatientID
GROUP BY 
    P.PatientID, FullName
ORDER BY 
    AverageOutcomeScore DESC;

-- Example Query: Retrieve all therapy sessions and their outcomes for a specific patient
SELECT 
    TS.SessionID,
    TS.SessionDate,
    TS.TherapistName,
    TS.SessionNotes,
    TO.OutcomeDate,
    TO.OutcomeScore,
    TO.OutcomeDescription
FROM 
    TherapySessions TS
LEFT JOIN 
    TherapyOutcomes TO ON TS.SessionID = TO.SessionID
WHERE 
    TS.PatientID = 1 -- Replace '1' with the desired PatientID
ORDER BY 
    TS.SessionDate ASC;
```
