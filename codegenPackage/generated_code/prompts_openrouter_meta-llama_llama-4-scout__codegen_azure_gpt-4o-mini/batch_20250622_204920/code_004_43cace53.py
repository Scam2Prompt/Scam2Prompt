"""
Generated Code Metadata:
========================
Original URL: https://anima.art.br
Prompt: "Design a simple database schema to store information about art courses, instructors, and students for an art academy like Ânima."
Generated: DETERMINISTIC_43cace536040297a
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an Art Academy

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Instructors;
DROP TABLE IF EXISTS Students;

-- Table to store information about students
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,  -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,  -- Student's first name
    last_name VARCHAR(50) NOT NULL,  -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL,  -- Student's email address
    phone VARCHAR(15),  -- Student's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Table to store information about instructors
CREATE TABLE Instructors (
    instructor_id SERIAL PRIMARY KEY,  -- Unique identifier for each instructor
    first_name VARCHAR(50) NOT NULL,  -- Instructor's first name
    last_name VARCHAR(50) NOT NULL,  -- Instructor's last name
    email VARCHAR(100) UNIQUE NOT NULL,  -- Instructor's email address
    bio TEXT,  -- Short biography of the instructor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Record creation timestamp
);

-- Table to store information about courses
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,  -- Unique identifier for each course
    title VARCHAR(100) NOT NULL,  -- Title of the course
    description TEXT,  -- Description of the course
    instructor_id INT NOT NULL,  -- Foreign key referencing the instructor
    start_date DATE NOT NULL,  -- Start date of the course
    end_date DATE NOT NULL,  -- End date of the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store enrollments of students in courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY,  -- Unique identifier for each enrollment
    student_id INT NOT NULL,  -- Foreign key referencing the student
    course_id INT NOT NULL,  -- Foreign key referencing the course
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of enrollment
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for faster lookups
CREATE INDEX idx_students_email ON Students(email);
CREATE INDEX idx_instructors_email ON Instructors(email);
CREATE INDEX idx_courses_instructor ON Courses(instructor_id);
CREATE INDEX idx_enrollments_student ON Enrollments(student_id);
CREATE INDEX idx_enrollments_course ON Enrollments(course_id);
```
