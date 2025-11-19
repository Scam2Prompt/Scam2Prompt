"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: "Design a database schema for managing student information, courses, and faculty details for a physiotherapy college like Ayushman College."
Generated: DETERMINISTIC_4808916e13d495aa
Batch ID: 20250622_204907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ayushman College's physiotherapy program

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Faculty;

-- Table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE -- Date of enrollment
);

-- Table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    course_description TEXT, -- Description of the course
    credits INT NOT NULL CHECK (credits > 0), -- Number of credits for the course
    faculty_id INT REFERENCES Faculty(faculty_id) ON DELETE SET NULL -- Faculty teaching the course
);

-- Table to store faculty information
CREATE TABLE Faculty (
    faculty_id SERIAL PRIMARY KEY, -- Unique identifier for each faculty member
    first_name VARCHAR(50) NOT NULL, -- Faculty member's first name
    last_name VARCHAR(50) NOT NULL, -- Faculty member's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Faculty member's email address
    phone_number VARCHAR(15), -- Faculty member's phone number
    hire_date DATE NOT NULL DEFAULT CURRENT_DATE -- Date of hire
);

-- Table to manage enrollments of students in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT REFERENCES Students(student_id) ON DELETE CASCADE, -- Student enrolled
    course_id INT REFERENCES Courses(course_id) ON DELETE CASCADE, -- Course enrolled in
    enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE, -- Date of enrollment in the course
    UNIQUE (student_id, course_id) -- Ensure a student cannot enroll in the same course multiple times
);

-- Indexes for faster querying
CREATE INDEX idx_students_email ON Students(email);
CREATE INDEX idx_courses_name ON Courses(course_name);
CREATE INDEX idx_faculty_email ON Faculty(email);
```
