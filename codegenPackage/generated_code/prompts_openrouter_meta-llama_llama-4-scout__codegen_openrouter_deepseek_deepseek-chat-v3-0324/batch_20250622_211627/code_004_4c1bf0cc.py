"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Design a database schema to store information about Московский Колледж Импровизационной Музыки's courses, faculty, and students, and write SQL queries to retrieve data on course enrollment, student progress, and faculty workload.
Generated: DETERMINISTIC_4c1bf0cc179dbaf6
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Московский Колледж Импровизационной Музыки

-- Create database
CREATE DATABASE IF NOT EXISTS mkim_music_college;
USE mkim_music_college;

-- Faculty table
CREATE TABLE faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    specialization VARCHAR(100) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_faculty_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Courses table
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    description TEXT,
    credits INT NOT NULL,
    duration_weeks INT NOT NULL,
    max_capacity INT NOT NULL,
    faculty_id INT,
    CONSTRAINT fk_course_faculty FOREIGN KEY (faculty_id) 
        REFERENCES faculty(faculty_id) ON DELETE SET NULL,
    CONSTRAINT chk_course_credits CHECK (credits > 0),
    CONSTRAINT chk_course_duration CHECK (duration_weeks > 0)
) ENGINE=InnoDB;

-- Students table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    enrollment_date DATE NOT NULL,
    graduation_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    CONSTRAINT chk_student_email CHECK (email LIKE '%@%.%'),
    CONSTRAINT chk_graduation_date CHECK (
        graduation_date IS NULL OR graduation_date > enrollment_date
    )
) ENGINE=InnoDB;

-- Course enrollment table
CREATE TABLE course_enrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_date DATE,
    grade DECIMAL(3, 1),
    status ENUM('active', 'completed', 'withdrawn') DEFAULT 'active',
    CONSTRAINT fk_enrollment_student FOREIGN KEY (student_id) 
        REFERENCES students(student_id) ON DELETE CASCADE,
    CONSTRAINT fk_enrollment_course FOREIGN KEY (course_id) 
        REFERENCES courses(course_id) ON DELETE CASCADE,
    CONSTRAINT chk_grade CHECK (
        grade IS NULL OR (grade >= 0 AND grade <= 100)
    ),
    CONSTRAINT chk_completion_date CHECK (
        completion_date IS NULL OR completion_date >= enrollment_date
    ),
    UNIQUE KEY unique_enrollment (student_id, course_id)
) ENGINE=InnoDB;

-- Faculty workload tracking
CREATE TABLE faculty_workload (
    workload_id INT AUTO_INCREMENT PRIMARY KEY,
    faculty_id INT NOT NULL,
    course_id INT NOT NULL,
    semester VARCHAR(20) NOT NULL,
    hours_per_week DECIMAL(4, 1) NOT NULL,
    CONSTRAINT fk_workload_faculty FOREIGN KEY (faculty_id) 
        REFERENCES faculty(faculty_id) ON DELETE CASCADE,
    CONSTRAINT fk_workload_course FOREIGN KEY (course_id) 
        REFERENCES courses(course_id) ON DELETE CASCADE,
    CONSTRAINT chk_hours_per_week CHECK (hours_per_week > 0),
    UNIQUE KEY unique_workload (faculty_id, course_id, semester)
) ENGINE=InnoDB;

-- Sample SQL queries

-- 1. Get course enrollment counts
SELECT 
    c.course_id,
    c.course_name,
    COUNT(ce.student_id) AS enrolled_students,
    c.max_capacity,
    CONCAT(ROUND(COUNT(ce.student_id) / c.max_capacity * 100, 1), '%') AS capacity_percentage
FROM 
    courses c
LEFT JOIN 
    course_enrollment ce ON c.course_id = ce.course_id AND ce.status = 'active'
GROUP BY 
    c.course_id, c.course_name, c.max_capacity
ORDER BY 
    enrolled_students DESC;

-- 2. Get student progress report
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    c.course_name,
    ce.grade,
    CASE 
        WHEN ce.grade >= 90 THEN 'Excellent'
        WHEN ce.grade >= 75 THEN 'Good'
        WHEN ce.grade >= 60 THEN 'Satisfactory'
        WHEN ce.grade IS NULL THEN 'In Progress'
        ELSE 'Needs Improvement'
    END AS performance,
    DATEDIFF(IFNULL(ce.completion_date, CURDATE()), ce.enrollment_date) AS days_enrolled
FROM 
    students s
JOIN 
    course_enrollment ce ON s.student_id = ce.student_id
JOIN 
    courses c ON ce.course_id = c.course_id
WHERE 
    s.is_active = TRUE
ORDER BY 
    s.last_name, s.first_name, c.course_name;

-- 3. Get faculty workload report
SELECT 
    f.faculty_id,
    CONCAT(f.first_name, ' ', f.last_name) AS faculty_name,
    f.specialization,
    COUNT(DISTINCT w.course_id) AS courses_taught,
    SUM(w.hours_per_week) AS total_hours_per_week,
    GROUP_CONCAT(DISTINCT c.course_name SEPARATOR ', ') AS course_list
FROM 
    faculty f
JOIN 
    faculty_workload w ON f.faculty_id = w.faculty_id
JOIN 
    courses c ON w.course_id = c.course_id
WHERE 
    f.is_active = TRUE
GROUP BY 
    f.faculty_id, faculty_name, f.specialization
ORDER BY 
    total_hours_per_week DESC;

-- 4. Get students eligible for graduation
SELECT 
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    s.enrollment_date,
    COUNT(ce.course_id) AS courses_completed,
    SUM(c.credits) AS total_credits,
    AVG(ce.grade) AS average_grade
FROM 
    students s
JOIN 
    course_enrollment ce ON s.student_id = ce.student_id
JOIN 
    courses c ON ce.course_id = c.course_id
WHERE 
    s.is_active = TRUE
    AND ce.status = 'completed'
    AND s.graduation_date IS NULL
GROUP BY 
    s.student_id, student_name, s.enrollment_date
HAVING 
    SUM(c.credits) >= 120  -- Assuming 120 credits required for graduation
ORDER BY 
    total_credits DESC;

-- 5. Get courses needing more faculty
SELECT 
    c.course_id,
    c.course_name,
    c.max_capacity,
    COUNT(ce.student_id) AS current_enrollment,
    CONCAT(f.first_name, ' ', f.last_name) AS faculty_name,
    CASE 
        WHEN COUNT(ce.student_id) > c.max_capacity * 0.9 THEN 'Overcrowded'
        WHEN COUNT(ce.student_id) > c.max_capacity * 0.7 THEN 'Approaching Limit'
        ELSE 'Under Capacity'
    END AS status
FROM 
    courses c
LEFT JOIN 
    course_enrollment ce ON c.course_id = ce.course_id AND ce.status = 'active'
LEFT JOIN 
    faculty f ON c.faculty_id = f.faculty_id
GROUP BY 
    c.course_id, c.course_name, c.max_capacity, faculty_name
HAVING 
    status IN ('Overcrowded', 'Approaching Limit') OR c.faculty_id IS NULL
ORDER BY 
    status DESC;
```
