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
CREATE TABLE CourseOfferings (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,                 -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,                        -- Name of the course
    DurationWeeks INT NOT NULL,                              -- Duration of the course in weeks
    StartDate DATE NOT NULL,                                 -- Start date of the course
    AccreditationDetails VARCHAR(500),                      -- Accreditation details of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,           -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Insert sample data into the CourseOfferings table
INSERT INTO CourseOfferings (CourseName, DurationWeeks, StartDate, AccreditationDetails)
VALUES 
    ('Data Science Fundamentals', 12, '2024-01-15', 'Accredited by XYZ Organization'),
    ('Full Stack Web Development', 16, '2024-02-01', 'Accredited by ABC Institute'),
    ('Cybersecurity Essentials', 10, '2024-03-10', 'ISO Certified'),
    ('Cloud Computing Foundations', 8, '2024-04-05', 'Endorsed by DEF Alliance');

-- Query to retrieve all course offerings
SELECT 
    CourseID, 
    CourseName, 
    DurationWeeks, 
    StartDate, 
    AccreditationDetails, 
    CreatedAt, 
    UpdatedAt
FROM 
    CourseOfferings
ORDER BY 
    StartDate; -- Retrieve and order courses by their start date

-- Query to retrieve course details by CourseID (Example: Fetch details of CourseID = 1)
SELECT 
    CourseName, 
    DurationWeeks, 
    StartDate, 
    AccreditationDetails
FROM 
    CourseOfferings
WHERE 
    CourseID = 1;

-- Update course details (Example: Update the duration of course with CourseID = 1)
UPDATE 
    CourseOfferings
SET 
    DurationWeeks = 14,
    UpdatedAt = CURRENT_TIMESTAMP
WHERE 
    CourseID = 1;

-- Delete a course offering (Example: Delete the course with CourseID = 4)
DELETE FROM 
    CourseOfferings
WHERE 
    CourseID = 4;

-- Ensure proper error handling is implemented in your application code when interacting with this database.
```
