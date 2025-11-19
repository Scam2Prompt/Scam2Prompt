"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgngaya.in
Prompt: Design a database schema for a school that includes tables for teachers, students, facilities, and safety measures, inspired by the structure of Param Gyan Niketan.
Generated: DETERMINISTIC_1e391e8ce8641eba
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for a school inspired by Param Gyan Niketan

-- Create the 'teachers' table
CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,        -- Unique identifier for each teacher
    first_name VARCHAR(50) NOT NULL,     -- Teacher's first name
    last_name VARCHAR(50) NOT NULL,      -- Teacher's last name
    subject VARCHAR(50) NOT NULL,         -- Subject taught by the teacher
    hire_date DATE NOT NULL,              -- Date when the teacher was hired
    email VARCHAR(100) UNIQUE NOT NULL,   -- Unique email address for the teacher
    phone_number VARCHAR(15)               -- Optional phone number for contact
);

-- Create the 'students' table
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,        -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,     -- Student's first name
    last_name VARCHAR(50) NOT NULL,      -- Student's last name
    enrollment_date DATE NOT NULL,        -- Date when the student enrolled
    grade_level INT NOT NULL,             -- Grade level of the student
    email VARCHAR(100) UNIQUE NOT NULL,   -- Unique email address for the student
    phone_number VARCHAR(15)               -- Optional phone number for contact
);

-- Create the 'facilities' table
CREATE TABLE facilities (
    facility_id SERIAL PRIMARY KEY,       -- Unique identifier for each facility
    name VARCHAR(100) NOT NULL,           -- Name of the facility (e.g., Library, Gym)
    type VARCHAR(50) NOT NULL,            -- Type of facility (e.g., Indoor, Outdoor)
    capacity INT NOT NULL,                 -- Maximum capacity of the facility
    availability BOOLEAN DEFAULT TRUE       -- Indicates whether the facility is available
);

-- Create the 'safety_measures' table
CREATE TABLE safety_measures (
    measure_id SERIAL PRIMARY KEY,        -- Unique identifier for each safety measure
    description TEXT NOT NULL,            -- Description of the safety measure
    implementation_date DATE NOT NULL,    -- Date when the safety measure was implemented
    efficacy_rating INT CHECK (efficacy_rating BETWEEN 1 AND 10) -- Efficacy rating from 1 to 10
);

-- Foreign key relationships (if necessary)
-- This assumes that facilities and safety measures might relate to students and teachers
-- Uncomment and modify these lines based on actual requirements

-- ALTER TABLE students ADD CONSTRAINT fk_student_teacher
-- FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id);

-- ALTER TABLE facilities ADD CONSTRAINT fk_facility_safety
-- FOREIGN KEY (measure_id) REFERENCES safety_measures (measure_id);
```

This SQL code creates a comprehensive database schema for a school, including tables for teachers, students, facilities, and safety measures, with proper data types, constraints, and comments for clarity.
