"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esofa.edu.pe
Prompt: Design a database schema for storing information about students enrolled in the Escuela de Suboficiales de la Fuerza Aérea del Perú, including their grades and titles.
Generated: DETERMINISTIC_aa9bffcc76790a93
Batch ID: 20250612_162220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about students at the Escuela de Suboficiales de la Fuerza Aérea del Perú

-- Create a table for storing student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,          -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,       -- First name of the student
    last_name VARCHAR(50) NOT NULL,        -- Last name of the student
    date_of_birth DATE NOT NULL,            -- Date of birth of the student
    enrollment_date DATE NOT NULL,          -- Date when the student enrolled
    graduation_date DATE,                    -- Date when the student graduated (nullable)
    email VARCHAR(100) UNIQUE NOT NULL,     -- Email address of the student (unique)
    phone_number VARCHAR(15)                -- Phone number of the student (nullable)
);

-- Create a table for storing courses information
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,           -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,      -- Name of the course
    credits INT NOT NULL                     -- Number of credits awarded for the course
);

-- Create a table for storing grades information
CREATE TABLE Grades (
    grade_id SERIAL PRIMARY KEY,            -- Unique identifier for each grade entry
    student_id INT NOT NULL,                -- Foreign key referencing Students table
    course_id INT NOT NULL,                 -- Foreign key referencing Courses table
    grade DECIMAL(3,2) CHECK (grade >= 0 AND grade <= 20), -- Grade obtained by the student
    semester VARCHAR(10) NOT NULL,          -- Semester in which the grade was obtained
    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE
);

-- Create a table for storing titles awarded to students
CREATE TABLE Titles (
    title_id SERIAL PRIMARY KEY,            -- Unique identifier for each title
    student_id INT NOT NULL,                -- Foreign key referencing Students table
    title_name VARCHAR(100) NOT NULL,       -- Name of the title awarded
    date_awarded DATE NOT NULL,              -- Date when the title was awarded
    CONSTRAINT fk_student_title FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE
);

-- Optional: Create indexes for faster querying
CREATE INDEX idx_student_name ON Students (last_name, first_name);
CREATE INDEX idx_course_name ON Courses (course_name);
CREATE INDEX idx_student_grades ON Grades (student_id);
```
