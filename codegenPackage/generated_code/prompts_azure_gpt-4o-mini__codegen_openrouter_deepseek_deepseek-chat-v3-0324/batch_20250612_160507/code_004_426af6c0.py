"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Design a database schema for managing educational programs and participants, based on the NICER Foundation's focus on literacy and numeracy development.
Generated: DETERMINISTIC_426af6c09d8b203d
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for NICER Foundation's educational programs

-- Create the database
CREATE DATABASE IF NOT EXISTS nicer_education;
USE nicer_education;

-- Table for storing program information
CREATE TABLE IF NOT EXISTS programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    description TEXT,
    focus_area ENUM('literacy', 'numeracy', 'both') NOT NULL,
    target_age_group VARCHAR(50),
    duration_weeks INT,
    start_date DATE,
    end_date DATE,
    max_participants INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_dates CHECK (end_date >= start_date)
) ENGINE=InnoDB;

-- Table for storing participant information
CREATE TABLE IF NOT EXISTS participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('male', 'female', 'other', 'prefer_not_to_say'),
    contact_number VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    school_name VARCHAR(100),
    grade_level VARCHAR(20),
    guardian_name VARCHAR(100),
    guardian_contact VARCHAR(20),
    special_needs TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_name (last_name, first_name)
) ENGINE=InnoDB;

-- Table for program enrollment
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    participant_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_status ENUM('enrolled', 'completed', 'dropped') DEFAULT 'enrolled',
    completion_date DATE,
    performance_rating VARCHAR(20),
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    UNIQUE KEY unique_enrollment (program_id, participant_id),
    CONSTRAINT chk_completion_date CHECK (
        (completion_status = 'enrolled' AND completion_date IS NULL) OR
        (completion_status IN ('completed', 'dropped') AND completion_date IS NOT NULL)
    )
) ENGINE=InnoDB;

-- Table for tracking assessments
CREATE TABLE IF NOT EXISTS assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    assessment_name VARCHAR(100) NOT NULL,
    assessment_type ENUM('pre', 'post', 'mid', 'other') NOT NULL,
    assessment_date DATE NOT NULL,
    description TEXT,
    max_score DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Table for participant assessment results
CREATE TABLE IF NOT EXISTS assessment_results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    assessment_id INT NOT NULL,
    participant_id INT NOT NULL,
    score DECIMAL(5,2),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (assessment_id) REFERENCES assessments(assessment_id) ON DELETE CASCADE,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    UNIQUE KEY unique_assessment (assessment_id, participant_id)
) ENGINE=InnoDB;

-- Table for program facilitators/teachers
CREATE TABLE IF NOT EXISTS facilitators (
    facilitator_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    qualification VARCHAR(100),
    specialization VARCHAR(100),
    contact_number VARCHAR(20),
    email VARCHAR(100) NOT NULL,
    hire_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_facilitator_name (last_name, first_name)
) ENGINE=InnoDB;

-- Table for facilitator assignments to programs
CREATE TABLE IF NOT EXISTS facilitator_assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    facilitator_id INT NOT NULL,
    role VARCHAR(50),
    start_date DATE NOT NULL,
    end_date DATE,
    hours_per_week DECIMAL(4,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    FOREIGN KEY (facilitator_id) REFERENCES facilitators(facilitator_id) ON DELETE CASCADE,
    CONSTRAINT chk_assignment_dates CHECK (end_date >= start_date OR end_date IS NULL)
) ENGINE=InnoDB;

-- Table for tracking program resources
CREATE TABLE IF NOT EXISTS resources (
    resource_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT,
    resource_name VARCHAR(100) NOT NULL,
    resource_type ENUM('book', 'worksheet', 'digital', 'other') NOT NULL,
    quantity INT DEFAULT 1,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Table for tracking attendance
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    participant_id INT NOT NULL,
    session_date DATE NOT NULL,
    status ENUM('present', 'absent', 'excused') NOT NULL,
    notes TEXT,
    recorded_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    FOREIGN KEY (recorded_by) REFERENCES facilitators(facilitator_id) ON DELETE SET NULL,
    UNIQUE KEY unique_attendance (program_id, participant_id, session_date)
) ENGINE=InnoDB;
```
