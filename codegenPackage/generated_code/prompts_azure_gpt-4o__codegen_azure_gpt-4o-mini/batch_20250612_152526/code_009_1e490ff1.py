"""
Generated Code Metadata:
========================
Original URL: https://kigaliinstitute.rw
Prompt: Create a database schema for tracking student progress in short-term brokerage courses, inspired by Kigali Institute's balance of theoretical and practical training.
Generated: DETERMINISTIC_1e490ff1da6a216d
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking student progress in short-term brokerage courses

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Enrollment;
DROP TABLE IF EXISTS Progress;

-- Table to store course information
CREATE TABLE Course (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    description TEXT, -- Description of the course content
    start_date DATE NOT NULL, -- Start date of the course
    end_date DATE NOT NULL, -- End date of the course
    theoretical_hours INT NOT NULL, -- Number of hours dedicated to theoretical training
    practical_hours INT NOT NULL -- Number of hours dedicated to practical training
);

-- Table to store student information
CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    enrollment_date DATE NOT NULL -- Date when the student enrolled
);

-- Table to track student enrollments in courses
CREATE TABLE Enrollment (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL, -- Foreign key referencing Student
    course_id INT NOT NULL, -- Foreign key referencing Course
    enrollment_date DATE NOT NULL, -- Date of enrollment
    status VARCHAR(20) NOT NULL CHECK (status IN ('active', 'completed', 'dropped')), -- Enrollment status
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (course_id) REFERENCES Course(course_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to track student progress in courses
CREATE TABLE Progress (
    progress_id SERIAL PRIMARY KEY, -- Unique identifier for each progress record
    enrollment_id INT NOT NULL, -- Foreign key referencing Enrollment
    theoretical_score DECIMAL(5, 2) CHECK (theoretical_score BETWEEN 0 AND 100), -- Score in theoretical training
    practical_score DECIMAL(5, 2) CHECK (practical_score BETWEEN 0 AND 100), -- Score in practical training
    feedback TEXT, -- Instructor feedback on student performance
    FOREIGN KEY (enrollment_id) REFERENCES Enrollment(enrollment_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_student_email ON Student(email);
CREATE INDEX idx_course_name ON Course(course_name);
CREATE INDEX idx_enrollment_status ON Enrollment(status);
```
