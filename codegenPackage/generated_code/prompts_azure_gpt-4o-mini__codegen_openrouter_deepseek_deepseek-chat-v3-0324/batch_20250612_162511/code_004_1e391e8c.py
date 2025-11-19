"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: Design a database schema for a school that includes tables for teachers, students, facilities, and safety measures, inspired by the structure of Param Gyan Niketan.
Generated: DETERMINISTIC_1e391e8ce8641eba
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Param Gyan Niketan school management system

-- Teachers table to store teacher information
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    address TEXT NOT NULL,
    qualification VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    joining_date DATE NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (salary > 0)
);

-- Subjects table
CREATE TABLE subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(100) NOT NULL,
    subject_code VARCHAR(20) UNIQUE NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Teacher-subject mapping table
CREATE TABLE teacher_subjects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_id INT NOT NULL,
    subject_id INT NOT NULL,
    class_level VARCHAR(50) NOT NULL,
    academic_year VARCHAR(20) NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE,
    UNIQUE (teacher_id, subject_id, class_level, academic_year)
);

-- Students table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    address TEXT NOT NULL,
    parent_name VARCHAR(100) NOT NULL,
    parent_phone VARCHAR(15) NOT NULL,
    admission_date DATE NOT NULL,
    class_level VARCHAR(50) NOT NULL,
    roll_number VARCHAR(20) UNIQUE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Facilities table
CREATE TABLE facilities (
    facility_id INT PRIMARY KEY AUTO_INCREMENT,
    facility_name VARCHAR(100) NOT NULL,
    description TEXT,
    capacity INT,
    location VARCHAR(100) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    maintenance_schedule VARCHAR(100),
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (capacity > 0)
);

-- Safety measures table
CREATE TABLE safety_measures (
    measure_id INT PRIMARY KEY AUTO_INCREMENT,
    measure_name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    implementation_date DATE NOT NULL,
    responsible_person VARCHAR(100) NOT NULL,
    status ENUM('Active', 'Inactive', 'In Progress') NOT NULL DEFAULT 'Active',
    last_audit_date DATE,
    next_audit_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Emergency contacts table
CREATE TABLE emergency_contacts (
    contact_id INT PRIMARY KEY AUTO_INCREMENT,
    contact_name VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(15) NOT NULL,
    contact_type ENUM('Police', 'Hospital', 'Fire', 'Other') NOT NULL,
    description TEXT,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Attendance table for students
CREATE TABLE student_attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Late', 'Excused') NOT NULL,
    remarks TEXT,
    recorded_by INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    UNIQUE (student_id, date)
);

-- Staff attendance table
CREATE TABLE staff_attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_id INT NOT NULL,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Late', 'On Leave') NOT NULL,
    remarks TEXT,
    recorded_by INT NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    UNIQUE (teacher_id, date)
);

-- Incident reports table
CREATE TABLE incident_reports (
    report_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    incident_date DATETIME NOT NULL,
    location VARCHAR(100) NOT NULL,
    reported_by INT NOT NULL,
    severity ENUM('Low', 'Medium', 'High', 'Critical') NOT NULL,
    status ENUM('Open', 'In Progress', 'Resolved', 'Closed') NOT NULL DEFAULT 'Open',
    resolution TEXT,
    resolved_date DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (reported_by) REFERENCES teachers(teacher_id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_student_class ON students(class_level);
CREATE INDEX idx_teacher_active ON teachers(is_active);
CREATE INDEX idx_facility_available ON facilities(is_available);
CREATE INDEX idx_safety_status ON safety_measures(status);
```
