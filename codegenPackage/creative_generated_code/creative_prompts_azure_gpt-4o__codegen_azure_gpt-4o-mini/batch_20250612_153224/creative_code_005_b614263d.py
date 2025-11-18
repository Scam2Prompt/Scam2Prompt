"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Create a database schema for tracking student progress in a bilingual program, referencing the educational model of Magic Bear Canadian School.
Generated: DETERMINISTIC_b614263dd4b241cc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking student progress in a bilingual program
-- following the educational model of Magic Bear Canadian School.

CREATE DATABASE IF NOT EXISTS magic_bear_school;

USE magic_bear_school;

-- Table to store student information
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,           -- Student's first name
    last_name VARCHAR(50) NOT NULL,            -- Student's last name
    date_of_birth DATE NOT NULL,                -- Student's date of birth
    enrollment_date DATE NOT NULL,              -- Date when the student was enrolled
    language_preference ENUM('English', 'French') NOT NULL, -- Preferred language for instruction
    status ENUM('Active', 'Inactive') DEFAULT 'Active' -- Enrollment status
);

-- Table to store courses offered in the bilingual program
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,          -- Name of the course
    language_of_instruction ENUM('English', 'French') NOT NULL -- Language in which the course is taught
);

-- Table to track student enrollments in courses
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL,                      -- Foreign key referencing the students table
    course_id INT NOT NULL,                       -- Foreign key referencing the courses table
    enrollment_date DATE NOT NULL,                -- Date of enrollment in the course
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store progress reports for each student
CREATE TABLE IF NOT EXISTS progress_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each progress report
    student_id INT NOT NULL,                      -- Foreign key referencing the students table
    course_id INT NOT NULL,                       -- Foreign key referencing the courses table
    report_date DATE NOT NULL,                    -- Date of the progress report
    grade FLOAT CHECK (grade >= 0 AND grade <= 100), -- Student's grade for the course (0 to 100)
    comments TEXT,                                -- Additional comments regarding student progress
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample Data Insertion (Ensure to remove or modify in production)
INSERT INTO students (first_name, last_name, date_of_birth, enrollment_date, language_preference)
VALUES ('John', 'Doe', '2010-05-01', '2023-09-01', 'English');

INSERT INTO courses (course_name, language_of_instruction)
VALUES ('Mathematics', 'English'), ('Sciences', 'French');

INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES (1, 1, '2023-09-01'), (1, 2, '2023-09-01');

INSERT INTO progress_reports (student_id, course_id, report_date, grade, comments)
VALUES (1, 1, '2023-09-30', 85.5, 'Good performance in class.');
```
