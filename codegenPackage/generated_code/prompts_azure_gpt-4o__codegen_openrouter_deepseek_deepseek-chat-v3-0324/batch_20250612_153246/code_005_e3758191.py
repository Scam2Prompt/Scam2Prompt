"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Write code to design a database schema for storing information about training programs, participants, and feedback, based on the association's focus on skill development and leadership training.
Generated: DETERMINISTIC_e375819184730d4f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for training programs management system

-- Create the database
CREATE DATABASE IF NOT EXISTS training_management;
USE training_management;

-- Participants table
CREATE TABLE IF NOT EXISTS participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    organization VARCHAR(100),
    job_title VARCHAR(100),
    join_date DATE NOT NULL,
    skills_level ENUM('Beginner', 'Intermediate', 'Advanced') DEFAULT 'Beginner',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_email CHECK (email LIKE '%@%.%')
) ENGINE=InnoDB;

-- Training programs table
CREATE TABLE IF NOT EXISTS programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    category ENUM('Leadership', 'Technical', 'Soft Skills', 'Management') NOT NULL,
    duration_hours INT NOT NULL,
    max_participants INT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_dates CHECK (end_date >= start_date)
) ENGINE=InnoDB;

-- Program sessions table
CREATE TABLE IF NOT EXISTS sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    program_id INT NOT NULL,
    session_number INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    location VARCHAR(100),
    facilitator VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    CONSTRAINT chk_time CHECK (end_time > start_time)
) ENGINE=InnoDB;

-- Participant enrollment table
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    participant_id INT NOT NULL,
    program_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    completion_status ENUM('Registered', 'In Progress', 'Completed', 'Dropped') DEFAULT 'Registered',
    certificate_issued BOOLEAN DEFAULT FALSE,
    certificate_issue_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
    UNIQUE KEY unique_enrollment (participant_id, program_id)
) ENGINE=InnoDB;

-- Attendance tracking table
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    session_id INT NOT NULL,
    attendance_status ENUM('Present', 'Absent', 'Late') NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE CASCADE,
    UNIQUE KEY unique_attendance (enrollment_id, session_id)
) ENGINE=InnoDB;

-- Feedback and evaluations table
CREATE TABLE IF NOT EXISTS feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL,
    session_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    feedback_date DATE NOT NULL,
    is_anonymous BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id) ON DELETE SET NULL
) ENGINE=InnoDB;

-- Skills assessment table
CREATE TABLE IF NOT EXISTS skills_assessment (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    participant_id INT NOT NULL,
    program_id INT NOT NULL,
    skill_name VARCHAR(100) NOT NULL,
    pre_training_level ENUM('Novice', 'Intermediate', 'Advanced', 'Expert') NOT NULL,
    post_training_level ENUM('Novice', 'Intermediate', 'Advanced', 'Expert'),
    assessment_date DATE NOT NULL,
    assessor VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (participant_id) REFERENCES participants(participant_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create indexes for performance
CREATE INDEX idx_participant_email ON participants(email);
CREATE INDEX idx_program_category ON programs(category);
CREATE INDEX idx_program_dates ON programs(start_date, end_date);
CREATE INDEX idx_enrollment_status ON enrollments(completion_status);
CREATE INDEX idx_feedback_rating ON feedback(rating);
```
