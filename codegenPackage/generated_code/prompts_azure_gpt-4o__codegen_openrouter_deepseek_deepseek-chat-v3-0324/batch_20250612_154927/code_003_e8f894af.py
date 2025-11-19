"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Create a database schema for managing technical education programs, including "Enfermería Técnica" and "Producción Agropecuaria," based on the programs listed on the Instituto Pangoa website.
Generated: DETERMINISTIC_e8f894af6fb335d6
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for technical education programs management
CREATE DATABASE IF NOT EXISTS instituto_pangoa;
USE instituto_pangoa;

-- Table for storing program information
CREATE TABLE IF NOT EXISTS programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    program_code VARCHAR(20) NOT NULL UNIQUE,
    duration_months INT NOT NULL,
    description TEXT,
    degree_awarded VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (duration_months > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for storing program modules/courses
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) NOT NULL,
    semester INT NOT NULL,
    credits INT NOT NULL,
    hours_per_week INT NOT NULL,
    is_core BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    UNIQUE KEY (program_id, course_code),
    CHECK (semester > 0),
    CHECK (credits > 0),
    CHECK (hours_per_week > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for storing students
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(20) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    gender ENUM('M', 'F', 'O') NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    enrollment_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for student enrollments in programs
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    program_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    graduation_date DATE,
    status ENUM('active', 'graduated', 'dropped', 'transferred') DEFAULT 'active',
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, program_id, status),
    CHECK (graduation_date IS NULL OR graduation_date >= enrollment_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for student grades
CREATE TABLE IF NOT EXISTS grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    course_id INT NOT NULL,
    semester INT NOT NULL,
    grade DECIMAL(5,2) NOT NULL,
    grade_date DATE NOT NULL,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE KEY (enrollment_id, course_id, semester),
    CHECK (grade >= 0 AND grade <= 20), -- Assuming grading scale is 0-20
    CHECK (semester > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for teachers/instructors
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(20) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    gender ENUM('M', 'F', 'O') NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    specialization VARCHAR(100),
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for course assignments to teachers
CREATE TABLE IF NOT EXISTS course_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_id INT NOT NULL,
    course_id INT NOT NULL,
    semester INT NOT NULL,
    academic_year YEAR NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE KEY (teacher_id, course_id, semester, academic_year),
    CHECK (semester > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert initial programs (Enfermería Técnica and Producción Agropecuaria)
INSERT INTO programs (program_name, program_code, duration_months, description, degree_awarded)
VALUES 
    ('Enfermería Técnica', 'ENT', 36, 'Programa técnico en enfermería que prepara profesionales para el cuidado de pacientes.', 'Técnico en Enfermería'),
    ('Producción Agropecuaria', 'PAG', 24, 'Programa técnico en producción agropecuaria para el desarrollo rural sostenible.', 'Técnico en Producción Agropecuaria');
```
