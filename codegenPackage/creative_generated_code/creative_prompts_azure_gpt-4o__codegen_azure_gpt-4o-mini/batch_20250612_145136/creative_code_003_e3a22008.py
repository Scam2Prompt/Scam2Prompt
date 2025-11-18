"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ineso.edu.mx
Prompt: Develop a SQL query to store and retrieve data about INESO's course offerings, such as the course name, duration, start date, and accreditation details.
Generated: DETERMINISTIC_e3a220085a52ab84
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store information about INESO's course offerings
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,       -- Name of the course
    Duration INT NOT NULL,                   -- Duration of the course in hours
    StartDate DATE NOT NULL,                 -- Start date of the course
    AccreditationDetails VARCHAR(255)        -- Accreditation details for the course
);

-- Insert sample course data into the Courses table
INSERT INTO Courses (CourseName, Duration, StartDate, AccreditationDetails)
VALUES 
    ('Introduction to Programming', 40, '2023-11-01', 'Accredited by XYZ'),
    ('Data Science Fundamentals', 60, '2023-11-15', 'Accredited by ABC'),
    ('Web Development Bootcamp', 80, '2023-12-01', 'Accredited by DEF');

-- Query to retrieve all course offerings
SELECT 
    CourseID, 
    CourseName, 
    Duration, 
    StartDate, 
    AccreditationDetails
FROM 
    Courses
ORDER BY 
    StartDate; -- Order courses by their start date

-- Query to retrieve a specific course by CourseID
SELECT 
    CourseID, 
    CourseName, 
    Duration, 
    StartDate, 
    AccreditationDetails
FROM 
    Courses
WHERE 
    CourseID = ?; -- Placeholder for course ID to fetch specific course details
```
