"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: "Design a database schema for managing student information, courses, and faculty details for a physiotherapy college like Ayushman College."
Generated: DETERMINISTIC_4808916e13d495aa
Batch ID: 20250622_204907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a physiotherapy college management system

-- Create the database
CREATE DATABASE IF NOT EXISTS physiotherapy_college;
USE physiotherapy_college;

-- Faculty table to store faculty details
CREATE TABLE IF NOT EXISTS faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,
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
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_faculty_email CHECK (email LIKE '%@%.%')
);

-- Department table
CREATE TABLE IF NOT EXISTS department (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    hod_id INT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (hod_id) REFERENCES faculty(faculty_id) ON DELETE SET NULL
);

-- Course table
CREATE TABLE IF NOT EXISTS course (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_code VARCHAR(20) NOT NULL UNIQUE,
    course_name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    duration_years INT NOT NULL,
    total_semesters INT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES department(department_id) ON DELETE CASCADE,
    CONSTRAINT chk_duration CHECK (duration_years > 0),
    CONSTRAINT chk_semesters CHECK (total_semesters > 0)
);

-- Semester table
CREATE TABLE IF NOT EXISTS semester (
    semester_id INT AUTO_INCREMENT PRIMARY KEY,
    semester_number INT NOT NULL,
    course_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE,
    CONSTRAINT chk_semester_dates CHECK (start_date < end_date),
    UNIQUE KEY unique_semester (course_id, semester_number)
);

-- Subject table
CREATE TABLE IF NOT EXISTS subject (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_code VARCHAR(20) NOT NULL UNIQUE,
    subject_name VARCHAR(100) NOT NULL,
    semester_id INT NOT NULL,
    credits INT NOT NULL,
    theory_hours INT DEFAULT 0,
    practical_hours INT DEFAULT 0,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (semester_id) REFERENCES semester(semester_id) ON DELETE CASCADE,
    CONSTRAINT chk_credits CHECK (credits > 0)
);

-- Faculty subject mapping
CREATE TABLE IF NOT EXISTS faculty_subject (
    faculty_subject_id INT AUTO_INCREMENT PRIMARY KEY,
    faculty_id INT NOT NULL,
    subject_id INT NOT NULL,
    academic_year YEAR NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE,
    UNIQUE KEY unique_faculty_subject (faculty_id, subject_id, academic_year)
);

-- Student table
CREATE TABLE IF NOT EXISTS student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_number VARCHAR(20) NOT NULL UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    address TEXT NOT NULL,
    admission_date DATE NOT NULL,
    course_id INT NOT NULL,
    current_semester INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE RESTRICT,
    CONSTRAINT chk_student_email CHECK (email LIKE '%@%.%')
);

-- Student academic records
CREATE TABLE IF NOT EXISTS academic_record (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    semester_id INT NOT NULL,
    gpa DECIMAL(3,2) NOT NULL,
    total_credits INT NOT NULL,
    result_status ENUM('Pass', 'Fail', 'Supplementary') NOT NULL,
    remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (semester_id) REFERENCES semester(semester_id) ON DELETE CASCADE,
    UNIQUE KEY unique_student_semester (student_id, semester_id),
    CONSTRAINT chk_gpa CHECK (gpa >= 0 AND gpa <= 10)
);

-- Subject marks for students
CREATE TABLE IF NOT EXISTS subject_marks (
    marks_id INT AUTO_INCREMENT PRIMARY KEY,
    record_id INT NOT NULL,
    subject_id INT NOT NULL,
    theory_marks INT DEFAULT 0,
    practical_marks INT DEFAULT 0,
    internal_marks INT DEFAULT 0,
    total_marks INT GENERATED ALWAYS AS (theory_marks + practical_marks + internal_marks) STORED,
    grade CHAR(2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (record_id) REFERENCES academic_record(record_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE,
    UNIQUE KEY unique_record_subject (record_id, subject_id),
    CONSTRAINT chk_theory_marks CHECK (theory_marks >= 0 AND theory_marks <= 100),
    CONSTRAINT chk_practical_marks CHECK (practical_marks >= 0 AND practical_marks <= 100),
    CONSTRAINT chk_internal_marks CHECK (internal_marks >= 0 AND internal_marks <= 100)
);

-- Attendance table
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Leave') NOT NULL,
    recorded_by INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by) REFERENCES faculty(faculty_id) ON DELETE RESTRICT,
    UNIQUE KEY unique_attendance (student_id, subject_id, date)
);

-- Create indexes for performance
CREATE INDEX idx_student_course ON student(course_id);
CREATE INDEX idx_subject_semester ON subject(semester_id);
CREATE INDEX idx_academic_record_student ON academic_record(student_id);
CREATE INDEX idx_attendance_student_subject ON attendance(student_id, subject_id);
```
