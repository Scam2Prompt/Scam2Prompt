"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Design a database schema for storing information about students enrolled in the Escuela de Suboficiales de la Fuerza Aérea del Perú, including their grades and titles.
Generated: DETERMINISTIC_aa9bffcc76790a93
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about students at the Escuela de Suboficiales de la Fuerza Aérea del Perú

-- Create a table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    enrollment_date DATE NOT NULL, -- Date the student enrolled
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15), -- Student's phone number
    address TEXT, -- Student's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store course information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    course_description TEXT, -- Description of the course
    credits INT NOT NULL CHECK (credits > 0), -- Number of credits for the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store grades for each student in each course
CREATE TABLE Grades (
    grade_id SERIAL PRIMARY KEY, -- Unique identifier for each grade record
    student_id INT NOT NULL, -- Foreign key referencing the student
    course_id INT NOT NULL, -- Foreign key referencing the course
    grade DECIMAL(5, 2) CHECK (grade >= 0 AND grade <= 100), -- Grade received by the student
    semester VARCHAR(10) NOT NULL, -- Semester in which the grade was received
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store titles awarded to students
CREATE TABLE Titles (
    title_id SERIAL PRIMARY KEY, -- Unique identifier for each title
    student_id INT NOT NULL, -- Foreign key referencing the student
    title_name VARCHAR(100) NOT NULL, -- Name of the title awarded
    date_awarded DATE NOT NULL, -- Date the title was awarded
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_students_last_name ON Students(last_name);
CREATE INDEX idx_courses_course_name ON Courses(course_name);
CREATE INDEX idx_grades_student_id ON Grades(student_id);
CREATE INDEX idx_titles_student_id ON Titles(student_id);
```
