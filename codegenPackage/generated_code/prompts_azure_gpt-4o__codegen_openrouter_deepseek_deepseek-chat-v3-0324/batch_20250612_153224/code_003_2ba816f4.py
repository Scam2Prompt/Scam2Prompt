"""
Generated Code Metadata:
========================
Original URL: https://preparatoriaoficial73.edu.mx
Prompt: Develop a database schema for managing student records, including fields for academic history, workshop enrollment, and administrative requests, as outlined in the FAQ section of the Escuela Preparatoria Oficial N.73 website.
Generated: DETERMINISTIC_2ba816f4b47abf19
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing student records
-- Includes tables for students, academic history, workshops, enrollment, and administrative requests

-- Students table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE NOT NULL,
    current_grade_level ENUM('1', '2', '3') NOT NULL,
    status ENUM('Active', 'Inactive', 'Graduated', 'Transferred') NOT NULL DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (last_name, first_name),
    INDEX (current_grade_level),
    INDEX (status)
) ENGINE=InnoDB;

-- Academic history table
CREATE TABLE academic_history (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    school_year VARCHAR(9) NOT NULL, -- Format: YYYY-YYYY
    grade_level ENUM('1', '2', '3') NOT NULL,
    final_gpa DECIMAL(3,2) NOT NULL,
    credits_earned DECIMAL(4,1) NOT NULL,
    attendance_rate DECIMAL(5,2) NOT NULL,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    INDEX (school_year),
    INDEX (grade_level)
) ENGINE=InnoDB;

-- Subjects table
CREATE TABLE subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_code VARCHAR(10) UNIQUE NOT NULL,
    subject_name VARCHAR(50) NOT NULL,
    description TEXT,
    credit_value DECIMAL(2,1) NOT NULL,
    grade_level ENUM('1', '2', '3', 'All') NOT NULL,
    is_core BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (subject_code),
    INDEX (subject_name)
) ENGINE=InnoDB;

-- Course grades table
CREATE TABLE course_grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    record_id INT NOT NULL,
    subject_id INT NOT NULL,
    final_grade DECIMAL(3,1) NOT NULL,
    semester_1_grade DECIMAL(3,1),
    semester_2_grade DECIMAL(3,1),
    teacher_comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (record_id) REFERENCES academic_history(record_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    INDEX (record_id),
    INDEX (subject_id)
) ENGINE=InnoDB;

-- Workshops table
CREATE TABLE workshops (
    workshop_id INT PRIMARY KEY AUTO_INCREMENT,
    workshop_code VARCHAR(10) UNIQUE NOT NULL,
    workshop_name VARCHAR(50) NOT NULL,
    description TEXT,
    instructor_name VARCHAR(100) NOT NULL,
    schedule VARCHAR(100) NOT NULL,
    capacity INT NOT NULL,
    current_enrollment INT NOT NULL DEFAULT 0,
    grade_level ENUM('1', '2', '3', 'All') NOT NULL,
    credit_value DECIMAL(2,1),
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (workshop_code),
    INDEX (workshop_name),
    INDEX (is_active)
) ENGINE=InnoDB;

-- Workshop enrollment table
CREATE TABLE workshop_enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    workshop_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_status ENUM('Enrolled', 'Completed', 'Dropped') NOT NULL DEFAULT 'Enrolled',
    final_grade DECIMAL(3,1),
    attendance_rate DECIMAL(5,2),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (workshop_id) REFERENCES workshops(workshop_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, workshop_id),
    INDEX (completion_status)
) ENGINE=InnoDB;

-- Administrative request types
CREATE TABLE request_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    requires_approval BOOLEAN NOT NULL DEFAULT TRUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (type_name)
) ENGINE=InnoDB;

-- Administrative requests table
CREATE TABLE administrative_requests (
    request_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    request_type_id INT NOT NULL,
    request_date DATE NOT NULL,
    status ENUM('Pending', 'Approved', 'Rejected', 'Completed') NOT NULL DEFAULT 'Pending',
    details TEXT,
    response TEXT,
    response_date DATE,
    responded_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (request_type_id) REFERENCES request_types(type_id) ON DELETE CASCADE,
    INDEX (status),
    INDEX (request_date)
) ENGINE=InnoDB;

-- Documents table
CREATE TABLE documents (
    document_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    document_type ENUM('Transcript', 'Certificate', 'ID', 'Other') NOT NULL,
    file_name VARCHAR(100) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    upload_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    INDEX (document_type),
    INDEX (upload_date)
) ENGINE=InnoDB;

-- Audit log table
CREATE TABLE audit_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    action VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    record_id INT,
    old_value TEXT,
    new_value TEXT,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX (action),
    INDEX (table_name),
    INDEX (action_timestamp)
) ENGINE=InnoDB;
```
