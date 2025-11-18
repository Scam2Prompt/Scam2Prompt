"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghmc.edu.au
Prompt: Develop a database schema in SQL for storing student information, course details, and certification status for vocational programs offered by Global Healthcare Management College.
Generated: DETERMINISTIC_99333d757c7bafe9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Global Healthcare Management College

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Certifications;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Students;

-- Table to store student information
CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,              -- Student's first name
    last_name VARCHAR(50) NOT NULL,                -- Student's last name
    email VARCHAR(100) NOT NULL UNIQUE,            -- Student's email address, must be unique
    phone_number VARCHAR(15),                       -- Student's phone number
    enrollment_date DATE NOT NULL,                  -- Date of enrollment
    status ENUM('active', 'inactive', 'graduated') NOT NULL -- Status of the student
);

-- Table to store course details
CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,              -- Name of the course
    description TEXT,                               -- Description of the course
    duration INT NOT NULL,                          -- Duration of the course in hours
    credits INT NOT NULL                            -- Number of credits for the course
);

-- Table to store certification status for students in courses
CREATE TABLE Certifications (
    certification_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each certification record
    student_id INT NOT NULL,                        -- Foreign key referencing Students table
    course_id INT NOT NULL,                         -- Foreign key referencing Courses table
    certification_date DATE NOT NULL,               -- Date the certification was awarded
    status ENUM('pending', 'awarded', 'failed') NOT NULL, -- Status of the certification
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample Data Insertion (Uncomment to use)
-- INSERT INTO Students (first_name, last_name, email, phone_number, enrollment_date, status)
-- VALUES ('John', 'Doe', 'john.doe@example.com', '1234567890', '2023-01-15', 'active');

-- INSERT INTO Courses (course_name, description, duration, credits)
-- VALUES ('Healthcare Management', 'An introduction to healthcare management practices.', 40, 3);

-- INSERT INTO Certifications (student_id, course_id, certification_date, status)
-- VALUES (1, 1, '2023-06-10', 'awarded');
```
