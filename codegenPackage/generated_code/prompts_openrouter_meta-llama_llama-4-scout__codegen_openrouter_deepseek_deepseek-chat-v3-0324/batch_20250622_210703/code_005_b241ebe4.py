"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: "Design a database schema for storing information about ENAFO's courses, instructors, and students, and write a simple query to demonstrate its usage."
Generated: DETERMINISTIC_b241ebe40a3922f4
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for ENAFO's course management system

-- Create database
CREATE DATABASE enafo_courses;
USE enafo_courses;

-- Create tables
CREATE TABLE instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    specialization VARCHAR(100),
    hire_date DATE NOT NULL,
    status ENUM('active', 'on_leave', 'inactive') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    enrollment_date DATE NOT NULL,
    status ENUM('active', 'graduated', 'withdrawn') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    credit_hours INT NOT NULL,
    duration_weeks INT NOT NULL,
    category VARCHAR(50),
    status ENUM('active', 'archived', 'planned') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE course_sections (
    section_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    instructor_id INT NOT NULL,
    section_code VARCHAR(20) NOT NULL,
    schedule VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    classroom VARCHAR(50),
    max_capacity INT NOT NULL,
    status ENUM('open', 'full', 'cancelled', 'completed') DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE,
    UNIQUE KEY (course_id, section_code)
) ENGINE=InnoDB;

CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    section_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_status ENUM('in_progress', 'completed', 'withdrawn') DEFAULT 'in_progress',
    grade DECIMAL(5,2),
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES course_sections(section_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, section_id)
) ENGINE=InnoDB;

-- Sample query: Get active courses with instructor names and student counts
SELECT 
    c.course_id,
    c.course_code,
    c.title,
    CONCAT(i.first_name, ' ', i.last_name) AS instructor_name,
    COUNT(e.student_id) AS enrolled_students,
    cs.max_capacity,
    cs.schedule,
    cs.start_date,
    cs.end_date
FROM 
    courses c
JOIN 
    course_sections cs ON c.course_id = cs.course_id
JOIN 
    instructors i ON cs.instructor_id = i.instructor_id
LEFT JOIN 
    enrollments e ON cs.section_id = e.section_id
WHERE 
    c.status = 'active' 
    AND cs.status = 'open'
GROUP BY 
    c.course_id, cs.section_id
ORDER BY 
    c.title, cs.start_date;
```
