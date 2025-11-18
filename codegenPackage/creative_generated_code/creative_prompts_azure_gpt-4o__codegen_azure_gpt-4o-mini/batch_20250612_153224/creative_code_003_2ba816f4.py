"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Develop a database schema for managing student records, including fields for academic history, workshop enrollment, and administrative requests, as outlined in the FAQ section of the Escuela Preparatoria Oficial N.73 website.
Generated: DETERMINISTIC_2ba816f4b47abf19
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing student records at Escuela Preparatoria Oficial N.73

-- Create the 'students' table to store basic student information
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,              -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,           -- Student's first name
    last_name VARCHAR(50) NOT NULL,            -- Student's last name
    date_of_birth DATE NOT NULL,                -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL,         -- Unique email address for each student
    phone_number VARCHAR(15),                   -- Optional phone number
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date the student enrolled
    status VARCHAR(20) NOT NULL DEFAULT 'active'  -- Status of the student (active, inactive)
);

-- Create the 'academic_history' table to store students' academic records
CREATE TABLE academic_history (
    history_id SERIAL PRIMARY KEY,              -- Unique identifier for each academic record
    student_id INT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE, -- FK to students table
    academic_year VARCHAR(10) NOT NULL,        -- Year of study
    grade DECIMAL(3, 2) NOT NULL,               -- Grade achieved (e.g., 90.00)
    subject VARCHAR(100) NOT NULL,              -- Subject of the record
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Create the 'workshop_enrollment' table for tracking students' workshop attendance
CREATE TABLE workshop_enrollment (
    enrollment_id SERIAL PRIMARY KEY,           -- Unique identifier for each workshop enrollment
    student_id INT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE, -- FK to students table
    workshop_name VARCHAR(100) NOT NULL,       -- Name of the workshop
    workshop_date DATE NOT NULL,                -- Date of the workshop
    status VARCHAR(20) NOT NULL DEFAULT 'enrolled' -- Status of enrollment (enrolled, completed, cancelled)
);

-- Create the 'administrative_requests' table to manage student requests
CREATE TABLE administrative_requests (
    request_id SERIAL PRIMARY KEY,              -- Unique identifier for each request
    student_id INT NOT NULL REFERENCES students(student_id) ON DELETE CASCADE, -- FK to students table
    request_type VARCHAR(100) NOT NULL,        -- Type of request (e.g., transcript, leave of absence)
    request_description TEXT NOT NULL,          -- Detailed description of the request
    request_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date request was made
    status VARCHAR(20) NOT NULL DEFAULT 'pending' -- Status of the request (pending, processed, denied)
);

-- Add indexes to improve query performance
CREATE INDEX idx_students_email ON students(email);
CREATE INDEX idx_academic_history_student ON academic_history(student_id);
CREATE INDEX idx_workshop_enrollment_student ON workshop_enrollment(student_id);
CREATE INDEX idx_admin_requests_student ON administrative_requests(student_id);
```
