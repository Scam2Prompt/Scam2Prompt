"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: Create a database schema for storing information about vocational courses, training centers, and student registrations, inspired by the structure of RSP Bharat.
Generated: DETERMINISTIC_1f31cc3e42727432
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for vocational courses, training centers, and student registrations

-- Create the database
CREATE DATABASE IF NOT EXISTS vocational_training_db;
USE vocational_training_db;

-- Training Centers Table
CREATE TABLE IF NOT EXISTS training_centers (
    center_id INT AUTO_INCREMENT PRIMARY KEY,
    center_name VARCHAR(100) NOT NULL,
    center_code VARCHAR(20) UNIQUE NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    pincode VARCHAR(10) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(15) NOT NULL,
    center_type ENUM('Government', 'Private', 'NGO') NOT NULL,
    accreditation_status ENUM('Approved', 'Pending', 'Rejected') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (city),
    INDEX (state)
) ENGINE=InnoDB;

-- Courses Table
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    description TEXT,
    duration_weeks INT NOT NULL,
    sector VARCHAR(50) NOT NULL,
    nqf_level VARCHAR(10),
    certification_body VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (sector)
) ENGINE=InnoDB;

-- Center Courses (Many-to-Many relationship between centers and courses)
CREATE TABLE IF NOT EXISTS center_courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    center_id INT NOT NULL,
    course_id INT NOT NULL,
    batch_capacity INT NOT NULL,
    current_batch_number INT DEFAULT 1,
    is_active BOOLEAN DEFAULT TRUE,
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (center_id) REFERENCES training_centers(center_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE KEY unique_center_course (center_id, course_id, current_batch_number),
    INDEX (is_active)
) ENGINE=InnoDB;

-- Students Table
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    aadhaar_number VARCHAR(12) UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    pincode VARCHAR(10) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(15) NOT NULL,
    education_qualification VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (city),
    INDEX (state)
) ENGINE=InnoDB;

-- Registrations Table
CREATE TABLE IF NOT EXISTS registrations (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    center_course_id INT NOT NULL,
    registration_date DATE NOT NULL,
    enrollment_number VARCHAR(20) UNIQUE,
    status ENUM('Registered', 'In Progress', 'Completed', 'Dropped Out') DEFAULT 'Registered',
    completion_date DATE,
    certificate_number VARCHAR(20),
    certificate_issued_date DATE,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (center_course_id) REFERENCES center_courses(id) ON DELETE CASCADE,
    INDEX (status),
    INDEX (enrollment_number)
) ENGINE=InnoDB;

-- Assessments Table
CREATE TABLE IF NOT EXISTS assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    center_course_id INT NOT NULL,
    assessment_type ENUM('Theory', 'Practical', 'Project') NOT NULL,
    assessment_date DATE NOT NULL,
    max_marks INT NOT NULL,
    passing_marks INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (center_course_id) REFERENCES center_courses(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Student Results Table
CREATE TABLE IF NOT EXISTS student_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    registration_id INT NOT NULL,
    assessment_id INT NOT NULL,
    marks_obtained INT NOT NULL,
    grade VARCHAR(5),
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (registration_id) REFERENCES registrations(registration_id) ON DELETE CASCADE,
    FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id) ON DELETE CASCADE,
    UNIQUE KEY unique_student_assessment (registration_id, assessment_id)
) ENGINE=InnoDB;

-- Payments Table
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    registration_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_mode ENUM('Cash', 'Cheque', 'Online Transfer', 'UPI') NOT NULL,
    transaction_reference VARCHAR(50),
    status ENUM('Pending', 'Completed', 'Failed') DEFAULT 'Pending',
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (registration_id) REFERENCES registrations(registration_id) ON DELETE CASCADE,
    INDEX (status)
) ENGINE=InnoDB;

-- Audit Log Table
CREATE TABLE IF NOT EXISTS audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT,
    old_values TEXT,
    new_values TEXT,
    ip_address VARCHAR(45),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX (table_name),
    INDEX (record_id)
) ENGINE=InnoDB;
```
