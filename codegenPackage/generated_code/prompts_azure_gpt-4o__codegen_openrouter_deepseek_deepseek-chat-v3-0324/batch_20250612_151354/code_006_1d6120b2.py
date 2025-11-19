"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: Write a SQL query to store and retrieve student enrollment data for courses like "Gestión Pública" and "Tributación," as described on the Enacip website.
Generated: DETERMINISTIC_1d6120b219645a6e
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for student enrollment system
CREATE DATABASE IF NOT EXISTS student_enrollment_db;
USE student_enrollment_db;

-- Create courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    description TEXT,
    credits INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create enrollments table
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    status ENUM('active', 'completed', 'withdrawn') DEFAULT 'active',
    grade DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE KEY unique_enrollment (student_id, course_id)
) ENGINE=InnoDB;

-- Insert sample courses
INSERT INTO courses (course_name, course_code, description, credits)
VALUES 
    ('Gestión Pública', 'GP101', 'Fundamentos de gestión pública y administración', 4),
    ('Tributación', 'TRIB202', 'Sistema tributario y normativa fiscal', 5)
ON DUPLICATE KEY UPDATE course_name = VALUES(course_name), description = VALUES(description), credits = VALUES(credits);

-- Query to get all enrollments for a specific course
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    s.email,
    c.course_name,
    e.enrollment_date,
    e.status,
    e.grade
FROM 
    enrollments e
JOIN 
    students s ON e.student_id = s.student_id
JOIN 
    courses c ON e.course_id = c.course_id
WHERE 
    c.course_name IN ('Gestión Pública', 'Tributación')
ORDER BY 
    c.course_name, s.last_name, s.first_name;

-- Query to get all courses a student is enrolled in
SELECT 
    c.course_id,
    c.course_name,
    c.course_code,
    c.credits,
    e.enrollment_date,
    e.status,
    e.grade
FROM 
    enrollments e
JOIN 
    courses c ON e.course_id = c.course_id
WHERE 
    e.student_id = :student_id
ORDER BY 
    e.enrollment_date DESC;

-- Query to enroll a student in a course
INSERT INTO enrollments (student_id, course_id, enrollment_date, status)
VALUES (:student_id, :course_id, CURDATE(), 'active')
ON DUPLICATE KEY UPDATE status = 'active', updated_at = CURRENT_TIMESTAMP;

-- Query to update enrollment status
UPDATE enrollments
SET 
    status = :new_status,
    grade = CASE WHEN :new_status = 'completed' THEN :grade ELSE grade END,
    updated_at = CURRENT_TIMESTAMP
WHERE 
    student_id = :student_id 
    AND course_id = :course_id;

-- Query to get course statistics
SELECT 
    c.course_id,
    c.course_name,
    COUNT(e.enrollment_id) AS total_enrollments,
    SUM(CASE WHEN e.status = 'active' THEN 1 ELSE 0 END) AS active_enrollments,
    SUM(CASE WHEN e.status = 'completed' THEN 1 ELSE 0 END) AS completed_enrollments,
    AVG(e.grade) AS average_grade
FROM 
    courses c
LEFT JOIN 
    enrollments e ON c.course_id = e.course_id
WHERE 
    c.course_name IN ('Gestión Pública', 'Tributación')
GROUP BY 
    c.course_id, c.course_name;
```
