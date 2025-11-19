"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Design a database schema for managing student enrollments in aviation security training courses, specifically for Welwitschia Aviation's offerings.
Generated: DETERMINISTIC_aeb3ebf55758e4ef
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing student enrollments in aviation security training courses
-- for Welwitschia Aviation.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS CourseEnrollments;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Students;

-- Table to store information about students
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,               -- Unique identifier for each student
    first_name VARCHAR(100) NOT NULL,           -- Student's first name
    last_name VARCHAR(100) NOT NULL,            -- Student's last name
    email VARCHAR(255) NOT NULL UNIQUE,         -- Student's email, must be unique
    phone_number VARCHAR(15),                    -- Student's phone number (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the record was created
);

-- Table to store information about courses
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,                -- Unique identifier for each course
    course_name VARCHAR(255) NOT NULL,          -- Name of the course
    description TEXT,                            -- Description of the course
    duration_hours INT NOT NULL,                 -- Duration of the course in hours
    start_date DATE NOT NULL,                    -- Start date of the course
    end_date DATE NOT NULL                       -- End date of the course
);

-- Table to manage enrollments of students in courses
CREATE TABLE CourseEnrollments (
    enrollment_id SERIAL PRIMARY KEY,            -- Unique identifier for each enrollment
    student_id INT NOT NULL,                     -- Reference to the student
    course_id INT NOT NULL,                      -- Reference to the course
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of enrollment
    status VARCHAR(50) CHECK (status IN ('Enrolled', 'Completed', 'Cancelled')) DEFAULT 'Enrolled', -- Status of the enrollment
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Foreign key to Students table
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE,   -- Foreign key to Courses table
    UNIQUE (student_id, course_id)              -- Ensure a student cannot enroll in the same course multiple times
);

-- Sample data insertion (commented out for production)
-- INSERT INTO Students (first_name, last_name, email, phone_number) VALUES ('John', 'Doe', 'john.doe@example.com', '123-456-7890');
-- INSERT INTO Courses (course_name, description, duration_hours, start_date, end_date) VALUES ('Aviation Security Basics', 'Introduction to aviation security.', 40, '2023-01-15', '2023-02-15');
-- INSERT INTO CourseEnrollments (student_id, course_id) VALUES (1, 1);
```
