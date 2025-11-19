"""
Generated Code Metadata:
========================
Original URL: https://cuicalli.edu.mx
Prompt: Create a database schema to store information about Universidad Tecnológico Cuicalli's students, faculty, and courses, and write a SQL query to retrieve the data.
Generated: DETERMINISTIC_1cd0c67a2a308831
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Universidad Tecnológico Cuicalli

-- Create database
CREATE DATABASE IF NOT EXISTS utc_db;
USE utc_db;

-- Faculty table
CREATE TABLE IF NOT EXISTS faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50) NOT NULL,
    position VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_department (department)
) ENGINE=InnoDB;

-- Students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL,
    enrollment_date DATE NOT NULL,
    major VARCHAR(50) NOT NULL,
    current_semester INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_major (major),
    INDEX idx_semester (current_semester)
) ENGINE=InnoDB;

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    credits INT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_department (department)
) ENGINE=InnoDB;

-- Course offerings (sections)
CREATE TABLE IF NOT EXISTS course_offerings (
    offering_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    faculty_id INT NOT NULL,
    semester VARCHAR(20) NOT NULL,
    year INT NOT NULL,
    schedule VARCHAR(100) NOT NULL,
    classroom VARCHAR(20) NOT NULL,
    max_capacity INT NOT NULL,
    current_enrollment INT DEFAULT 0,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id) ON DELETE CASCADE,
    INDEX idx_semester_year (semester, year)
) ENGINE=InnoDB;

-- Student enrollments
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    offering_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    grade DECIMAL(3,2) DEFAULT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (offering_id) REFERENCES course_offerings(offering_id) ON DELETE CASCADE,
    UNIQUE KEY unique_enrollment (student_id, offering_id),
    INDEX idx_grade (grade)
) ENGINE=InnoDB;

-- Sample query to retrieve student information with their enrolled courses and grades
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    s.major,
    s.current_semester,
    c.course_code,
    c.course_name,
    co.semester,
    co.year,
    e.grade,
    CONCAT(f.first_name, ' ', f.last_name) AS instructor_name
FROM 
    students s
JOIN 
    enrollments e ON s.student_id = e.student_id
JOIN 
    course_offerings co ON e.offering_id = co.offering_id
JOIN 
    courses c ON co.course_id = c.course_id
JOIN 
    faculty f ON co.faculty_id = f.faculty_id
WHERE 
    s.student_id = 12345  -- Parameter would be replaced in application code
ORDER BY 
    co.year DESC, 
    co.semester DESC;
```
