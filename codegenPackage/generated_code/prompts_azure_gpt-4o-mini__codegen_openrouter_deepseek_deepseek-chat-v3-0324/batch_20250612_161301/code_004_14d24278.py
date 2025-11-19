"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Design a database schema in SQL for managing the administrative services of I.E Politécnico Municipal Cali, including tables for student information, academic programs, and faculty members.
Generated: DETERMINISTIC_14d24278b8d4f154
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for I.E Politécnico Municipal Cali administrative services

-- Create database
CREATE DATABASE IF NOT EXISTS ie_politecnico_municipal_cali;
USE ie_politecnico_municipal_cali;

-- Academic programs table
CREATE TABLE IF NOT EXISTS academic_programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    program_code VARCHAR(20) NOT NULL UNIQUE,
    duration_years INT NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_duration CHECK (duration_years > 0)
) ENGINE=InnoDB;

-- Faculty members table
CREATE TABLE IF NOT EXISTS faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    identification_number VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20),
    address TEXT,
    hire_date DATE NOT NULL,
    position VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    identification_number VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20),
    address TEXT,
    date_of_birth DATE NOT NULL,
    enrollment_date DATE NOT NULL,
    program_id INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES academic_programs(program_id)
) ENGINE=InnoDB;

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) NOT NULL UNIQUE,
    credits INT NOT NULL,
    program_id INT NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES academic_programs(program_id),
    CONSTRAINT chk_credits CHECK (credits > 0)
) ENGINE=InnoDB;

-- Class sections table
CREATE TABLE IF NOT EXISTS class_sections (
    section_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    faculty_id INT NOT NULL,
    section_code VARCHAR(20) NOT NULL,
    schedule VARCHAR(100) NOT NULL,
    classroom VARCHAR(20),
    semester VARCHAR(20) NOT NULL,
    academic_year YEAR NOT NULL,
    max_capacity INT NOT NULL,
    current_enrollment INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id),
    CONSTRAINT chk_capacity CHECK (current_enrollment <= max_capacity AND max_capacity > 0),
    UNIQUE KEY unique_section (course_id, section_code, semester, academic_year)
) ENGINE=InnoDB;

-- Student enrollments table
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    section_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    grade DECIMAL(3,1),
    status ENUM('active', 'completed', 'withdrawn') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (section_id) REFERENCES class_sections(section_id),
    UNIQUE KEY unique_enrollment (student_id, section_id)
) ENGINE=InnoDB;

-- Academic records table
CREATE TABLE IF NOT EXISTS academic_records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    program_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    graduation_date DATE,
    current_semester INT NOT NULL,
    gpa DECIMAL(3,2),
    status ENUM('active', 'graduated', 'withdrawn', 'suspended') DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (program_id) REFERENCES academic_programs(program_id),
    CONSTRAINT chk_semester CHECK (current_semester > 0)
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_student_identification ON students(identification_number);
CREATE INDEX idx_faculty_identification ON faculty(identification_number);
CREATE INDEX idx_student_program ON students(program_id);
CREATE INDEX idx_course_program ON courses(program_id);
CREATE INDEX idx_section_course ON class_sections(course_id);
CREATE INDEX idx_section_faculty ON class_sections(faculty_id);
CREATE INDEX idx_enrollment_student ON enrollments(student_id);
CREATE INDEX idx_enrollment_section ON enrollments(section_id);
CREATE INDEX idx_academic_record_student ON academic_records(student_id);
```
