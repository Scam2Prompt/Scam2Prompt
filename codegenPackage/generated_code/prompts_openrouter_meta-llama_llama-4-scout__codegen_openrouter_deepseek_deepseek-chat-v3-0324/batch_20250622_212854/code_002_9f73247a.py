"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Generate a sample database schema for an IELTS training center like Ikogwe International Limited, including tables for student information, course enrollment, and exam results.
Generated: DETERMINISTIC_9f73247ab54013fd
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for IELTS Training Center

-- Create database
CREATE DATABASE IF NOT EXISTS ielts_training_center;
USE ielts_training_center;

-- Students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    passport_number VARCHAR(50) UNIQUE NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Active', 'Inactive', 'Graduated') DEFAULT 'Active',
    INDEX idx_email (email),
    INDEX idx_passport (passport_number)
) ENGINE=InnoDB;

-- Courses table
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_weeks INT NOT NULL,
    fee DECIMAL(10, 2) NOT NULL,
    level ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL,
    max_students INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_course_name (course_name)
) ENGINE=InnoDB;

-- Batches table
CREATE TABLE IF NOT EXISTS batches (
    batch_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    batch_name VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    schedule VARCHAR(100) NOT NULL,
    instructor_id INT,
    current_students INT DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    INDEX idx_start_date (start_date),
    INDEX idx_course_batch (course_id, batch_name)
) ENGINE=InnoDB;

-- Instructors table
CREATE TABLE IF NOT EXISTS instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    hire_date DATE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    INDEX idx_instructor_email (email)
) ENGINE=InnoDB;

-- Enrollment table
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    batch_id INT NOT NULL,
    enrollment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    fee_paid DECIMAL(10, 2) DEFAULT 0,
    payment_status ENUM('Paid', 'Partial', 'Unpaid') DEFAULT 'Unpaid',
    status ENUM('Active', 'Completed', 'Dropped') DEFAULT 'Active',
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id) ON DELETE CASCADE,
    INDEX idx_student_batch (student_id, batch_id)
) ENGINE=InnoDB;

-- Payments table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('Cash', 'Bank Transfer', 'Credit Card', 'Other') NOT NULL,
    transaction_reference VARCHAR(100),
    received_by INT,
    notes TEXT,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    INDEX idx_payment_date (payment_date)
) ENGINE=InnoDB;

-- Exam results table
CREATE TABLE IF NOT EXISTS exam_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    exam_type ENUM('Mock', 'Official') NOT NULL,
    exam_date DATE NOT NULL,
    listening_score DECIMAL(3, 1) CHECK (listening_score BETWEEN 0 AND 9),
    reading_score DECIMAL(3, 1) CHECK (reading_score BETWEEN 0 AND 9),
    writing_score DECIMAL(3, 1) CHECK (writing_score BETWEEN 0 AND 9),
    speaking_score DECIMAL(3, 1) CHECK (speaking_score BETWEEN 0 AND 9),
    overall_band DECIMAL(3, 1) GENERATED ALWAYS AS (
        (listening_score + reading_score + writing_score + speaking_score) / 4
    ) STORED,
    comments TEXT,
    recorded_by INT,
    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    INDEX idx_exam_date (exam_date),
    INDEX idx_overall_band (overall_band)
) ENGINE=InnoDB;

-- Attendance table
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    batch_id INT NOT NULL,
    class_date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Late', 'Excused') NOT NULL,
    remarks TEXT,
    recorded_by INT,
    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (batch_id) REFERENCES batches(batch_id) ON DELETE CASCADE,
    INDEX idx_class_date (class_date),
    UNIQUE KEY unique_attendance (student_id, batch_id, class_date)
) ENGINE=InnoDB;

-- Course materials table
CREATE TABLE IF NOT EXISTS course_materials (
    material_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    material_name VARCHAR(100) NOT NULL,
    material_type ENUM('Book', 'PDF', 'Video', 'Audio', 'Other') NOT NULL,
    file_path VARCHAR(255),
    url VARCHAR(255),
    added_by INT,
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    INDEX idx_course_material (course_id, material_name)
) ENGINE=InnoDB;
```
