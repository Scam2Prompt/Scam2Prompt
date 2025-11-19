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
-- Database schema for storing patient data and therapy outcomes for a DBT clinic

-- Create a table to store patient information
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each patient
    FirstName VARCHAR(50) NOT NULL,            -- Patient's first name
    LastName VARCHAR(50) NOT NULL,              -- Patient's last name
    DateOfBirth DATE NOT NULL,                  -- Patient's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL,  -- Patient's gender
    ContactNumber VARCHAR(15),                   -- Patient's contact number
    Email VARCHAR(100),                          -- Patient's email address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create a table to store therapy sessions
CREATE TABLE TherapySessions (
    SessionID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each therapy session
    PatientID INT NOT NULL,                      -- Foreign key referencing Patients table
    SessionDate DATE NOT NULL,                   -- Date of the therapy session
    SessionType ENUM('Individual', 'Group') NOT NULL, -- Type of therapy session
    Notes TEXT,                                  -- Notes from the therapy session
    Outcome ENUM('Improved', 'Unchanged', 'Worsened') NOT NULL, -- Outcome of the session
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table to store therapy goals
CREATE TABLE TherapyGoals (
    GoalID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each therapy goal
    PatientID INT NOT NULL,                      -- Foreign key referencing Patients table
    GoalDescription TEXT NOT NULL,               -- Description of the therapy goal
    TargetDate DATE NOT NULL,                    -- Target date for achieving the goal
    Status ENUM('Pending', 'Achieved', 'Not Achieved') NOT NULL, -- Current status of the goal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Example SQL query to analyze therapy outcomes for patients
-- This query retrieves the number of sessions and the overall outcome for each patient
SELECT 
    p.PatientID,
    CONCAT(p.FirstName, ' ', p.LastName) AS PatientName,
    COUNT(ts.SessionID) AS TotalSessions,
    SUM(CASE WHEN ts.Outcome = 'Improved' THEN 1 ELSE 0 END) AS ImprovedSessions,
    SUM(CASE WHEN ts.Outcome = 'Worsened' THEN 1 ELSE 0 END) AS WorsenedSessions,
    SUM(CASE WHEN ts.Outcome = 'Unchanged' THEN 1 ELSE 0 END) AS UnchangedSessions
FROM 
    Patients p
LEFT JOIN 
    TherapySessions ts ON p.PatientID = ts.PatientID
GROUP BY 
    p.PatientID
ORDER BY 
    TotalSessions DESC;  -- Order by the number of sessions in descending order
```
