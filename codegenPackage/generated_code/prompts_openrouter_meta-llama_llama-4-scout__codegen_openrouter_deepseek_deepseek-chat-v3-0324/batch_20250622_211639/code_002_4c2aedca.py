"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Generate a sample database schema for storing student information, attendance records, and exam results for a school with a similar setup to জি. কে. মাধ্যমিক বিদ্যালয়.
Generated: DETERMINISTIC_4c2aedcaf8646aca
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for school management system
-- Tables for student information, attendance, and exam results

-- Create database
CREATE DATABASE IF NOT EXISTS school_management_system;
USE school_management_system;

-- Table for storing class information
CREATE TABLE IF NOT EXISTS classes (
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50) NOT NULL,
    section VARCHAR(10),
    academic_year VARCHAR(20) NOT NULL,
    class_teacher_id INT,
    UNIQUE KEY (class_name, section, academic_year)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for storing subjects
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    subject_code VARCHAR(20) UNIQUE,
    is_elective BOOLEAN DEFAULT FALSE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for class-subject mapping
CREATE TABLE IF NOT EXISTS class_subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    class_id INT NOT NULL,
    subject_id INT NOT NULL,
    teacher_id INT,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    UNIQUE KEY (class_id, subject_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for storing student information
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    admission_number VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    blood_group VARCHAR(10),
    religion VARCHAR(50),
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'Bangladesh',
    phone_number VARCHAR(20),
    email VARCHAR(100),
    father_name VARCHAR(100),
    mother_name VARCHAR(100),
    guardian_name VARCHAR(100),
    guardian_contact VARCHAR(20),
    admission_date DATE NOT NULL,
    current_class_id INT,
    is_active BOOLEAN DEFAULT TRUE,
    photo_path VARCHAR(255),
    FOREIGN KEY (current_class_id) REFERENCES classes(class_id) ON DELETE SET NULL,
    INDEX (admission_number),
    INDEX (first_name, last_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for storing attendance records
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Late', 'Half Day') NOT NULL,
    remarks TEXT,
    recorded_by INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for exam types (e.g., First Term, Second Term, Final Exam)
CREATE TABLE IF NOT EXISTS exam_types (
    exam_type_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_name VARCHAR(100) NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    start_date DATE,
    end_date DATE,
    description TEXT,
    UNIQUE KEY (exam_name, academic_year)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for exam schedules
CREATE TABLE IF NOT EXISTS exam_schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_type_id INT NOT NULL,
    subject_id INT NOT NULL,
    class_id INT NOT NULL,
    exam_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    full_marks DECIMAL(5,2) NOT NULL,
    pass_marks DECIMAL(5,2) NOT NULL,
    exam_venue VARCHAR(100),
    FOREIGN KEY (exam_type_id) REFERENCES exam_types(exam_type_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE KEY (exam_type_id, subject_id, class_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for storing exam results
CREATE TABLE IF NOT EXISTS exam_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    schedule_id INT NOT NULL,
    marks_obtained DECIMAL(5,2) NOT NULL,
    grade VARCHAR(5),
    grade_point DECIMAL(3,2),
    remarks TEXT,
    recorded_by INT NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (schedule_id) REFERENCES exam_schedules(schedule_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, schedule_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for storing teachers
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    address TEXT NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    qualification TEXT,
    joining_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    photo_path VARCHAR(255),
    INDEX (first_name, last_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for user accounts (admin, teachers, etc.)
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role ENUM('Admin', 'Teacher', 'Accountant', 'Librarian', 'Student') NOT NULL,
    account_status ENUM('Active', 'Inactive', 'Suspended') DEFAULT 'Active',
    last_login DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    related_id INT COMMENT 'ID of related entity (teacher_id, student_id, etc.)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for academic calendar events
CREATE TABLE IF NOT EXISTS academic_calendar (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    event_type ENUM('Holiday', 'Exam', 'Meeting', 'Other') NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    created_by INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for student fees
CREATE TABLE IF NOT EXISTS fee_structure (
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    class_id INT NOT NULL,
    fee_name VARCHAR(100) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    frequency ENUM('One Time', 'Monthly', 'Quarterly', 'Yearly') NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    due_date DATE,
    FOREIGN KEY (class_id) REFERENCES classes(class_id) ON DELETE CASCADE,
    UNIQUE KEY (class_id, fee_name, academic_year)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table for student fee payments
CREATE TABLE IF NOT EXISTS fee_payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    fee_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method ENUM('Cash', 'Check', 'Bank Transfer', 'Mobile Banking') NOT NULL,
    transaction_id VARCHAR(100),
    received_by INT NOT NULL,
    remarks TEXT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (fee_id) REFERENCES fee_structure(fee_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
