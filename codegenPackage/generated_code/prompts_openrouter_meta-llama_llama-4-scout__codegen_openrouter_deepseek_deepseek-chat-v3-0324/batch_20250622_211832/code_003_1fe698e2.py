"""
Generated Code Metadata:
========================
Original URL: https://smkn1kadipaten.sch.id
Prompt: Design a database schema for storing information about SMKN 1 Kadipaten's students, teachers, and staff, including details about their roles and responsibilities like the deputy leader Abdul Madjid, S.Pd., M.Pd.
Generated: DETERMINISTIC_1fe698e256a35b03
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for SMKN 1 Kadipaten school management system

-- Create database
CREATE DATABASE smkn1_kadipaten;
USE smkn1_kadipaten;

-- Table for storing positions/roles in the school
CREATE TABLE positions (
    position_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    is_teaching_position BOOLEAN DEFAULT FALSE,
    is_administrative BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for departments/divisions
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Table for storing all personnel (students, teachers, staff)
CREATE TABLE personnel (
    personnel_id INT AUTO_INCREMENT PRIMARY KEY,
    nik VARCHAR(20) UNIQUE COMMENT 'National Identification Number',
    nisn VARCHAR(20) UNIQUE COMMENT 'National Student Identification Number (for students)',
    nuptk VARCHAR(20) UNIQUE COMMENT 'Teacher Identification Number (for teachers)',
    name VARCHAR(100) NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    birth_date DATE,
    birth_place VARCHAR(100),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    photo_url VARCHAR(255),
    personnel_type ENUM('Student', 'Teacher', 'Staff') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (personnel_type),
    INDEX (is_active)
) ENGINE=InnoDB;

-- Table for personnel positions (assigning roles to people)
CREATE TABLE personnel_positions (
    personnel_position_id INT AUTO_INCREMENT PRIMARY KEY,
    personnel_id INT NOT NULL,
    position_id INT NOT NULL,
    department_id INT,
    start_date DATE NOT NULL,
    end_date DATE,
    is_current BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (personnel_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE,
    FOREIGN KEY (position_id) REFERENCES positions(position_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    INDEX (is_current)
) ENGINE=InnoDB;

-- Table for student-specific information
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    class VARCHAR(20) NOT NULL,
    major VARCHAR(100) NOT NULL,
    enrollment_year YEAR NOT NULL,
    FOREIGN KEY (student_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE,
    INDEX (class),
    INDEX (major),
    INDEX (enrollment_year)
) ENGINE=InnoDB;

-- Table for teacher-specific information
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY,
    education_level VARCHAR(100) COMMENT 'e.g., S.Pd., M.Pd.',
    specialization VARCHAR(100),
    certification_number VARCHAR(50),
    FOREIGN KEY (teacher_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for staff-specific information
CREATE TABLE staff (
    staff_id INT PRIMARY KEY,
    job_title VARCHAR(100),
    employment_type ENUM('Permanent', 'Contract', 'Part-time') NOT NULL,
    FOREIGN KEY (staff_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for storing credentials/login information
CREATE TABLE credentials (
    credential_id INT AUTO_INCREMENT PRIMARY KEY,
    personnel_id INT NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL COMMENT 'Stored as bcrypt hash',
    last_login TIMESTAMP NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (personnel_id) REFERENCES personnel(personnel_id) ON DELETE CASCADE,
    INDEX (is_active)
) ENGINE=InnoDB;

-- Insert sample position data
INSERT INTO positions (title, description, is_teaching_position, is_administrative) VALUES
('Headmaster', 'School principal', FALSE, TRUE),
('Deputy Leader', 'Vice principal', FALSE, TRUE),
('Head of Department', 'Department chair', TRUE, TRUE),
('Teacher', 'Teaching staff', TRUE, FALSE),
('Administrative Staff', 'School administration', FALSE, TRUE),
('Student', 'Learner', FALSE, FALSE);

-- Insert sample department data
INSERT INTO departments (name, description) VALUES
('Administration', 'School administration department'),
('Mathematics', 'Mathematics department'),
('Science', 'Science department'),
('Language', 'Language department'),
('Vocational', 'Vocational studies department');

-- Insert sample personnel data for deputy leader Abdul Madjid, S.Pd., M.Pd.
INSERT INTO personnel (
    nik, nuptk, name, gender, birth_date, birth_place, address, phone, email, personnel_type
) VALUES (
    '1234567890123456', '1234123412341234', 'Abdul Madjid, S.Pd., M.Pd.', 'Male', 
    '1975-05-15', 'Kadipaten', 'Jl. Pendidikan No. 1 Kadipaten', '081234567890', 
    'abdul.madjid@smkn1kadipaten.sch.id', 'Teacher'
);

-- Assign position to Abdul Madjid
INSERT INTO personnel_positions (
    personnel_id, position_id, department_id, start_date, is_current
) VALUES (
    (SELECT personnel_id FROM personnel WHERE name = 'Abdul Madjid, S.Pd., M.Pd.' LIMIT 1),
    (SELECT position_id FROM positions WHERE title = 'Deputy Leader' LIMIT 1),
    (SELECT department_id FROM departments WHERE name = 'Administration' LIMIT 1),
    '2015-01-01', TRUE
);

-- Add teacher-specific data for Abdul Madjid
INSERT INTO teachers (
    teacher_id, education_level, specialization, certification_number
) VALUES (
    (SELECT personnel_id FROM personnel WHERE name = 'Abdul Madjid, S.Pd., M.Pd.' LIMIT 1),
    'S.Pd., M.Pd.', 'Educational Management', '1234567890'
);
```
