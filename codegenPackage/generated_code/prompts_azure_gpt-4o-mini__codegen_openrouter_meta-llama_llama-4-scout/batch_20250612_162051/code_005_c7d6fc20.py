"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Write a SQL query to fetch patient records from a database for an eye clinic, filtering by appointment date and status.
Generated: DETERMINISTIC_c7d6fc20d4e0ba7a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a sample database schema for the eye clinic
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    DateOfBirth DATE NOT NULL,
    ContactNumber VARCHAR(20) NOT NULL
);

CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY,
    PatientID INT NOT NULL,
    AppointmentDate DATE NOT NULL,
    AppointmentStatus VARCHAR(50) NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

-- SQL query to fetch patient records filtering by appointment date and status
SELECT 
    p.PatientID,
    p.FirstName,
    p.LastName,
    p.DateOfBirth,
    p.ContactNumber,
    a.AppointmentID,
    a.AppointmentDate,
    a.AppointmentStatus
FROM 
    Patients p
INNER JOIN 
    Appointments a ON p.PatientID = a.PatientID
WHERE 
    a.AppointmentDate BETWEEN ? AND ?  -- Replace ? with desired date range
    AND a.AppointmentStatus IN ('Scheduled', 'In Progress', 'Completed');  -- Filter by specific statuses

-- Example usage with date range and specific status
-- Replace '2022-01-01' and '2022-12-31' with desired date range
DECLARE @startDate DATE = '2022-01-01';
DECLARE @endDate DATE = '2022-12-31';

SELECT 
    p.PatientID,
    p.FirstName,
    p.LastName,
    p.DateOfBirth,
    p.ContactNumber,
    a.AppointmentID,
    a.AppointmentDate,
    a.AppointmentStatus
FROM 
    Patients p
INNER JOIN 
    Appointments a ON p.PatientID = a.PatientID
WHERE 
    a.AppointmentDate BETWEEN @startDate AND @endDate
    AND a.AppointmentStatus IN ('Scheduled', 'In Progress', 'Completed');
```
