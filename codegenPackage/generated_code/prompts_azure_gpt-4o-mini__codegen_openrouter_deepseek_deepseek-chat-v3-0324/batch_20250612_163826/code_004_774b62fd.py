"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Design a database schema in SQL for managing student records and course enrollments at a music school, including tables for instruments, faculty, and student information.
Generated: DETERMINISTIC_774b62fd0ba65a03
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a music school management system

-- Create the database
CREATE DATABASE music_school;
USE music_school;

-- Table for storing instrument information
CREATE TABLE instruments (
    instrument_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type VARCHAR(30) NOT NULL, -- e.g., string, wind, percussion
    difficulty_level VARCHAR(20),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_instrument_type CHECK (type IN ('string', 'wind', 'percussion', 'keyboard', 'electronic')),
    CONSTRAINT chk_difficulty_level CHECK (difficulty_level IN ('beginner', 'intermediate', 'advanced', 'professional'))
) ENGINE=InnoDB;

-- Table for faculty members
CREATE TABLE faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    hire_date DATE NOT NULL,
    specialization VARCHAR(100),
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for faculty instrument proficiency (junction table)
CREATE TABLE faculty_instruments (
    faculty_id INT NOT NULL,
    instrument_id INT NOT NULL,
    proficiency_level VARCHAR(20) NOT NULL,
    years_of_experience INT,
    PRIMARY KEY (faculty_id, instrument_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id) ON DELETE CASCADE,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id) ON DELETE CASCADE,
    CONSTRAINT chk_proficiency_level CHECK (proficiency_level IN ('beginner', 'intermediate', 'advanced', 'expert'))
) ENGINE=InnoDB;

-- Table for students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE NOT NULL,
    address TEXT,
    guardian_name VARCHAR(100),
    guardian_phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_student_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Table for courses
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    instrument_id INT NOT NULL,
    level VARCHAR(20) NOT NULL,
    max_capacity INT NOT NULL,
    duration_weeks INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id),
    CONSTRAINT chk_course_level CHECK (level IN ('beginner', 'intermediate', 'advanced')),
    CONSTRAINT chk_max_capacity CHECK (max_capacity > 0),
    CONSTRAINT chk_duration CHECK (duration_weeks > 0),
    CONSTRAINT chk_price CHECK (price >= 0)
) ENGINE=InnoDB;

-- Table for course schedules
CREATE TABLE course_schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    faculty_id INT NOT NULL,
    day_of_week VARCHAR(10) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    room_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id),
    CONSTRAINT chk_day_of_week CHECK (day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')),
    CONSTRAINT chk_time CHECK (end_time > start_time),
    CONSTRAINT chk_date CHECK (end_date > start_date)
) ENGINE=InnoDB;

-- Table for student enrollments
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    grade VARCHAR(2),
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    CONSTRAINT chk_status CHECK (status IN ('active', 'completed', 'withdrawn', 'failed')),
    CONSTRAINT chk_grade CHECK (grade IN ('A', 'B', 'C', 'D', 'F', NULL))
) ENGINE=InnoDB;

-- Table for student instrument proficiency
CREATE TABLE student_instruments (
    student_id INT NOT NULL,
    instrument_id INT NOT NULL,
    proficiency_level VARCHAR(20) NOT NULL,
    years_of_experience INT,
    PRIMARY KEY (student_id, instrument_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id) ON DELETE CASCADE,
    CONSTRAINT chk_student_proficiency CHECK (proficiency_level IN ('beginner', 'intermediate', 'advanced'))
) ENGINE=InnoDB;

-- Table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    payment_method VARCHAR(20) NOT NULL,
    transaction_id VARCHAR(100),
    status VARCHAR(20) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id),
    CONSTRAINT chk_payment_method CHECK (payment_method IN ('cash', 'credit_card', 'debit_card', 'bank_transfer', 'check')),
    CONSTRAINT chk_payment_status CHECK (status IN ('pending', 'completed', 'failed', 'refunded')),
    CONSTRAINT chk_amount CHECK (amount > 0)
) ENGINE=InnoDB;

-- Indexes for performance optimization
CREATE INDEX idx_student_name ON students(last_name, first_name);
CREATE INDEX idx_faculty_name ON faculty(last_name, first_name);
CREATE INDEX idx_course_instrument ON courses(instrument_id);
CREATE INDEX idx_enrollment_student ON enrollments(student_id);
CREATE INDEX idx_enrollment_course ON enrollments(course_id);
CREATE INDEX idx_payment_enrollment ON payments(enrollment_id);
```
