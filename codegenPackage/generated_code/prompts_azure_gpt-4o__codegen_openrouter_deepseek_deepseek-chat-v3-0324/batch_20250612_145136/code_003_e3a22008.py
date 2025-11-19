"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: Develop a SQL query to store and retrieve data about INESO's course offerings, such as the course name, duration, start date, and accreditation details.
Generated: DETERMINISTIC_e3a220085a52ab84
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store course offerings
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    duration_days INT NOT NULL CHECK (duration_days > 0),
    start_date DATE NOT NULL,
    is_accredited BOOLEAN DEFAULT FALSE,
    accreditation_body VARCHAR(100),
    accreditation_expiry DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Ensure accreditation details are provided if course is accredited
    CONSTRAINT chk_accreditation CHECK (
        (is_accredited = FALSE) OR 
        (is_accredited = TRUE AND accreditation_body IS NOT NULL AND accreditation_expiry IS NOT NULL)
    )
);

-- Insert a sample course
INSERT INTO courses (
    course_name, 
    duration_days, 
    start_date, 
    is_accredited, 
    accreditation_body, 
    accreditation_expiry
) VALUES (
    'Advanced Data Science', 
    90, 
    '2023-11-15', 
    TRUE, 
    'Data Science Council', 
    '2025-11-15'
);

-- Retrieve all courses
SELECT 
    course_id,
    course_name,
    duration_days,
    start_date,
    is_accredited,
    accreditation_body,
    accreditation_expiry,
    created_at,
    updated_at
FROM courses;

-- Retrieve courses starting after a specific date
SELECT 
    course_name,
    duration_days,
    start_date
FROM courses
WHERE start_date > '2023-01-01'
ORDER BY start_date;

-- Retrieve accredited courses
SELECT 
    course_name,
    accreditation_body,
    accreditation_expiry
FROM courses
WHERE is_accredited = TRUE
AND accreditation_expiry > CURRENT_DATE;

-- Update a course's details
UPDATE courses
SET 
    duration_days = 120,
    updated_at = CURRENT_TIMESTAMP
WHERE course_id = 1;

-- Delete a course
DELETE FROM courses
WHERE course_id = 1;
```
