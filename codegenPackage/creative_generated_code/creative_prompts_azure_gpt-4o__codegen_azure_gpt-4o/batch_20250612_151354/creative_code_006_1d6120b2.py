"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacip.edu.pe
Prompt: Write a SQL query to store and retrieve student enrollment data for courses like "Gestión Pública" and "Tributación," as described on the Enacip website.
Generated: DETERMINISTIC_1d6120b219645a6e
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create table to store student enrollment data
CREATE TABLE IF NOT EXISTS StudentEnrollment (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment record
    StudentID INT NOT NULL, -- Foreign key referencing the student
    CourseName VARCHAR(255) NOT NULL, -- Name of the course the student is enrolled in
    EnrollmentDate DATE NOT NULL, -- Date of enrollment
    Status ENUM('Active', 'Completed', 'Cancelled') DEFAULT 'Active', -- Current status of the enrollment
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Create table to store student information (if not already existing)
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(255) NOT NULL, -- First name of the student
    LastName VARCHAR(255) NOT NULL, -- Last name of the student
    Email VARCHAR(255) NOT NULL UNIQUE, -- Contact email of the student
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Insert sample data for demonstration purposes
INSERT INTO Students (FirstName, LastName, Email)
VALUES
('Juan', 'Perez', 'juan.perez@example.com'),
('Maria', 'Gomez', 'maria.gomez@example.com');

INSERT INTO StudentEnrollment (StudentID, CourseName, EnrollmentDate, Status)
VALUES
(1, 'Gestión Pública', '2023-10-01', 'Active'),
(2, 'Tributación', '2023-10-02', 'Active');

-- Query to retrieve all student enrollment data for specified courses
SELECT 
    SE.EnrollmentID,
    SE.StudentID,
    S.FirstName,
    S.LastName,
    SE.CourseName,
    SE.EnrollmentDate,
    SE.Status
FROM 
    StudentEnrollment SE
JOIN 
    Students S ON SE.StudentID = S.StudentID
WHERE 
    SE.CourseName IN ('Gestión Pública', 'Tributación')
ORDER BY 
    SE.EnrollmentDate ASC;

-- Query to update enrollment status (example: mark a student's enrollment as completed)
UPDATE StudentEnrollment
SET Status = 'Completed'
WHERE EnrollmentID = 1;

-- Query to delete an enrollment record (example: remove a cancelled enrollment)
DELETE FROM StudentEnrollment
WHERE EnrollmentID = 2 AND Status = 'Cancelled';
```
