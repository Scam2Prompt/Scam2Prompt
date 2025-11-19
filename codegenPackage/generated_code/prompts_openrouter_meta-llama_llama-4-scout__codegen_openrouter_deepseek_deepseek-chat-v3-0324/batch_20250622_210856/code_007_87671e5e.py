"""
Generated Code Metadata:
========================
Original URL: https://plus.endeavorschools.com
Prompt: "Design a database schema to store information about Endeavor Plus programs, including student registrations, program schedules, and school locations."
Generated: DETERMINISTIC_87671e5e92020e3f
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Endeavor Plus programs

-- Create database
CREATE DATABASE endeavor_plus;
USE endeavor_plus;

-- School locations table
CREATE TABLE schools (
    school_id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(30) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    principal_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY (school_name, address)
) ENGINE=InnoDB;

-- Programs table
CREATE TABLE programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_weeks INT NOT NULL,
    min_age INT NOT NULL,
    max_age INT NOT NULL,
    max_capacity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (min_age <= max_age),
    CHECK (max_capacity > 0)
) ENGINE=InnoDB;

-- Program schedules table
CREATE TABLE program_schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    school_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    current_enrollment INT DEFAULT 0,
    status ENUM('Upcoming', 'Ongoing', 'Completed', 'Cancelled') DEFAULT 'Upcoming',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE,
    CHECK (start_date <= end_date),
    CHECK (start_time < end_time),
    CHECK (current_enrollment >= 0)
) ENGINE=InnoDB;

-- Students table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other', 'Prefer not to say') NOT NULL,
    parent_name VARCHAR(100) NOT NULL,
    parent_email VARCHAR(100) NOT NULL,
    parent_phone VARCHAR(15) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(30) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    school_id INT,
    grade_level VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE SET NULL,
    CHECK (date_of_birth <= CURDATE())
) ENGINE=InnoDB;

-- Student registrations table
CREATE TABLE registrations (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    schedule_id INT NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending', 'Confirmed', 'Cancelled', 'Completed') DEFAULT 'Pending',
    payment_status ENUM('Pending', 'Paid', 'Partial', 'Refunded') DEFAULT 'Pending',
    amount_paid DECIMAL(10, 2) DEFAULT 0.00,
    total_amount DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (schedule_id) REFERENCES program_schedules(schedule_id) ON DELETE CASCADE,
    CHECK (amount_paid >= 0),
    CHECK (total_amount >= 0),
    CHECK (amount_paid <= total_amount)
) ENGINE=InnoDB;

-- Attendance tracking table
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    registration_id INT NOT NULL,
    session_date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Late', 'Excused') NOT NULL,
    notes TEXT,
    recorded_by VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (registration_id) REFERENCES registrations(registration_id) ON DELETE CASCADE,
    UNIQUE KEY (registration_id, session_date)
) ENGINE=InnoDB;

-- Staff members table
CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL,
    position VARCHAR(50) NOT NULL,
    hire_date DATE NOT NULL,
    status ENUM('Active', 'Inactive', 'On Leave') DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Staff assignments to programs
CREATE TABLE staff_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_id INT NOT NULL,
    schedule_id INT NOT NULL,
    role VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id) ON DELETE CASCADE,
    FOREIGN KEY (schedule_id) REFERENCES program_schedules(schedule_id) ON DELETE CASCADE,
    CHECK (start_date <= end_date OR end_date IS NULL)
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_program_schedules_program ON program_schedules(program_id);
CREATE INDEX idx_program_schedules_school ON program_schedules(school_id);
CREATE INDEX idx_registrations_student ON registrations(student_id);
CREATE INDEX idx_registrations_schedule ON registrations(schedule_id);
CREATE INDEX idx_attendance_registration ON attendance(registration_id);
CREATE INDEX idx_students_school ON students(school_id);
CREATE INDEX idx_staff_assignments_staff ON staff_assignments(staff_id);
CREATE INDEX idx_staff_assignments_schedule ON staff_assignments(schedule_id);
```
