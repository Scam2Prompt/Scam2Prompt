"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Design a database schema for storing information about students, teachers, and staff at a school like Ideal High School.
Generated: DETERMINISTIC_c04086b8a0ff90d3
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ideal High School

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Staff;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Enrollments;

-- Table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of enrollment
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    address TEXT -- Student's home address
);

-- Table to store teacher information
CREATE TABLE Teachers (
    teacher_id SERIAL PRIMARY KEY, -- Unique identifier for each teacher
    first_name VARCHAR(50) NOT NULL, -- Teacher's first name
    last_name VARCHAR(50) NOT NULL, -- Teacher's last name
    hire_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of hiring
    email VARCHAR(100) UNIQUE NOT NULL, -- Teacher's email address
    phone_number VARCHAR(15), -- Teacher's phone number
    subject VARCHAR(50) NOT NULL -- Subject taught by the teacher
);

-- Table to store staff information
CREATE TABLE Staff (
    staff_id SERIAL PRIMARY KEY, -- Unique identifier for each staff member
    first_name VARCHAR(50) NOT NULL, -- Staff member's first name
    last_name VARCHAR(50) NOT NULL, -- Staff member's last name
    hire_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of hiring
    email VARCHAR(100) UNIQUE NOT NULL, -- Staff member's email address
    phone_number VARCHAR(15), -- Staff member's phone number
    position VARCHAR(50) NOT NULL -- Position of the staff member
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    course_code VARCHAR(10) UNIQUE NOT NULL, -- Unique course code
    teacher_id INT REFERENCES Teachers(teacher_id) ON DELETE SET NULL, -- Teacher assigned to the course
    credits INT NOT NULL CHECK (credits > 0) -- Number of credits for the course
);

-- Table to store enrollments of students in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT REFERENCES Students(student_id) ON DELETE CASCADE, -- Student enrolled in the course
    course_id INT REFERENCES Courses(course_id) ON DELETE CASCADE, -- Course in which the student is enrolled
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of enrollment in the course
    UNIQUE (student_id, course_id) -- Ensure a student cannot enroll in the same course multiple times
);

-- Indexes for faster querying
CREATE INDEX idx_students_email ON Students(email);
CREATE INDEX idx_teachers_email ON Teachers(email);
CREATE INDEX idx_staff_email ON Staff(email);
CREATE INDEX idx_courses_teacher ON Courses(teacher_id);
CREATE INDEX idx_enrollments_student ON Enrollments(student_id);
CREATE INDEX idx_enrollments_course ON Enrollments(course_id);
```
