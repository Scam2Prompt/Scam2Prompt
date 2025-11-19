"""
Generated Code Metadata:
========================
Original URL: https://trentino.edu.pe
Prompt: "Design a database schema for managing information about students, courses, and certifications at an institution like Trentino Juan Pablo II."
Generated: DETERMINISTIC_d2d10cc4eab4e4b5
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing information about students, courses, and certifications

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Certifications;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Students;

-- Table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    date_of_birth DATE NOT NULL, -- Student's date of birth
    enrollment_date DATE DEFAULT CURRENT_DATE, -- Date when the student enrolled
    status VARCHAR(20) CHECK (status IN ('active', 'inactive', 'graduated')) DEFAULT 'active' -- Enrollment status
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    course_description TEXT, -- Description of the course
    credits INT CHECK (credits > 0), -- Number of credits for the course
    start_date DATE NOT NULL, -- Start date of the course
    end_date DATE NOT NULL, -- End date of the course
    instructor_name VARCHAR(100) -- Name of the instructor
);

-- Table to store certifications information
CREATE TABLE Certifications (
    certification_id SERIAL PRIMARY KEY, -- Unique identifier for each certification
    certification_name VARCHAR(100) NOT NULL, -- Name of the certification
    issuing_organization VARCHAR(100), -- Organization that issues the certification
    issue_date DATE NOT NULL, -- Date when the certification was issued
    expiration_date DATE, -- Date when the certification expires
    student_id INT REFERENCES Students(student_id) ON DELETE CASCADE -- Foreign key referencing Students
);

-- Table to manage the many-to-many relationship between students and courses
CREATE TABLE StudentCourses (
    student_id INT REFERENCES Students(student_id) ON DELETE CASCADE, -- Foreign key referencing Students
    course_id INT REFERENCES Courses(course_id) ON DELETE CASCADE, -- Foreign key referencing Courses
    enrollment_date DATE DEFAULT CURRENT_DATE, -- Date when the student enrolled in the course
    PRIMARY KEY (student_id, course_id) -- Composite primary key
);

-- Indexes for faster querying
CREATE INDEX idx_students_email ON Students(email);
CREATE INDEX idx_courses_name ON Courses(course_name);
CREATE INDEX idx_certifications_student ON Certifications(student_id);
```
