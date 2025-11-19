"""
Generated Code Metadata:
========================
Original URL: https://kigaliinstitute.rw
Prompt: "Design a database schema to store information about students, courses, and instructors for a brokerage training institution that offers online courses in stock trade and other fields."
Generated: DETERMINISTIC_87226146d0967577
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a brokerage training institution

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Instructors;
DROP TABLE IF EXISTS Students;

-- Table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date of registration
);

-- Table to store instructor information
CREATE TABLE Instructors (
    instructor_id SERIAL PRIMARY KEY, -- Unique identifier for each instructor
    first_name VARCHAR(50) NOT NULL, -- Instructor's first name
    last_name VARCHAR(50) NOT NULL, -- Instructor's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Instructor's email address
    bio TEXT, -- Short biography of the instructor
    hire_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date of hiring
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    description TEXT, -- Description of the course
    instructor_id INT NOT NULL, -- Foreign key referencing the instructor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date the course was created
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store enrollment information
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL, -- Foreign key referencing the student
    course_id INT NOT NULL, -- Foreign key referencing the course
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of enrollment
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE, -- Ensures referential integrity
    UNIQUE (student_id, course_id) -- Prevents duplicate enrollments for the same course
);

-- Indexes for performance optimization
CREATE INDEX idx_students_email ON Students(email);
CREATE INDEX idx_instructors_email ON Instructors(email);
CREATE INDEX idx_courses_instructor ON Courses(instructor_id);
CREATE INDEX idx_enrollments_student ON Enrollments(student_id);
CREATE INDEX idx_enrollments_course ON Enrollments(course_id);
```
