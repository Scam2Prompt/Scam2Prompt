"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jualessandraensina.com
Prompt: Design a database schema for managing student profiles and course enrollments in a makeup education platform similar to Ju Ensina, including fields for techniques learned and progress tracking.
Generated: DETERMINISTIC_5136e7179c738394
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing student profiles and course enrollments in a makeup education platform

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Techniques;
DROP TABLE IF EXISTS Students;

-- Table for storing student profiles
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,           -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,        -- Student's first name
    last_name VARCHAR(50) NOT NULL,         -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL,     -- Student's email, must be unique
    phone VARCHAR(15),                       -- Optional phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table for storing courses offered
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,            -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,      -- Name of the course
    description TEXT,                        -- Description of the course
    start_date DATE NOT NULL,                -- Start date of the course
    end_date DATE NOT NULL,                  -- End date of the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Update timestamp
);

-- Table for storing techniques taught in courses
CREATE TABLE Techniques (
    technique_id SERIAL PRIMARY KEY,         -- Unique identifier for each technique
    technique_name VARCHAR(100) NOT NULL,   -- Name of the technique
    description TEXT,                        -- Description of the technique
    course_id INT NOT NULL,                  -- Reference to the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Update timestamp
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table for managing student enrollments in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,        -- Unique identifier for each enrollment
    student_id INT NOT NULL,                 -- Reference to the student
    course_id INT NOT NULL,                  -- Reference to the course
    progress_percentage DECIMAL(5, 2) DEFAULT 0.00, -- Progress tracking (0.00 - 100.00)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Update timestamp
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE, -- Foreign key constraint
    UNIQUE (student_id, course_id)          -- Ensure a student cannot enroll in the same course multiple times
);

-- Indexes for improving query performance
CREATE INDEX idx_students_email ON Students(email);
CREATE INDEX idx_courses_name ON Courses(course_name);
CREATE INDEX idx_techniques_course ON Techniques(course_id);
```
