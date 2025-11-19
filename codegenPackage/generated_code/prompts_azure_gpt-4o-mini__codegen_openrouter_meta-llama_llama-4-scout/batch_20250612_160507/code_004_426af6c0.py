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
-- Create database schema for educational programs and participants

-- Create database
CREATE DATABASE IF NOT EXISTS education_programs;

-- Use database
USE education_programs;

-- Create table for educational programs
CREATE TABLE programs (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `focus_area` ENUM('literacy', 'numeracy', 'both') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for program participants
CREATE TABLE participants (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for program enrollments
CREATE TABLE enrollments (
  `id` INT AUTO_INCREMENT,
  `program_id` INT NOT NULL,
  `participant_id` INT NOT NULL,
  `enrollment_date` DATE NOT NULL,
  `status` ENUM('active', 'inactive', 'completed') NOT NULL DEFAULT 'active',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`program_id`) REFERENCES programs(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`participant_id`) REFERENCES participants(`id`) ON DELETE CASCADE
);

-- Create table for program sessions
CREATE TABLE sessions (
  `id` INT AUTO_INCREMENT,
  `program_id` INT NOT NULL,
  `session_date` DATE NOT NULL,
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  `location` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`program_id`) REFERENCES programs(`id`) ON DELETE CASCADE
);

-- Create table for session attendance
CREATE TABLE attendance (
  `id` INT AUTO_INCREMENT,
  `session_id` INT NOT NULL,
  `participant_id` INT NOT NULL,
  `attendance_date` DATE NOT NULL,
  `is_present` BOOLEAN NOT NULL DEFAULT FALSE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`session_id`) REFERENCES sessions(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`participant_id`) REFERENCES participants(`id`) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_enrollments_program_id ON enrollments (program_id);
CREATE INDEX idx_enrollments_participant_id ON enrollments (participant_id);
CREATE INDEX idx_sessions_program_id ON sessions (program_id);
CREATE INDEX idx_attendance_session_id ON attendance (session_id);
CREATE INDEX idx_attendance_participant_id ON attendance (participant_id);
```

```sql
-- Example usage:

-- Insert a new program
INSERT INTO programs (name, description, focus_area)
VALUES ('Literacy Program', 'A program to improve literacy skills', 'literacy');

-- Insert a new participant
INSERT INTO participants (first_name, last_name, email)
VALUES ('John', 'Doe', 'john.doe@example.com');

-- Enroll a participant in a program
INSERT INTO enrollments (program_id, participant_id, enrollment_date)
VALUES (1, 1, '2022-01-01');

-- Insert a new program session
INSERT INTO sessions (program_id, session_date, start_time, end_time, location)
VALUES (1, '2022-01-15', '09:00:00', '10:30:00', 'Room 101');

-- Mark a participant's attendance for a session
INSERT INTO attendance (session_id, participant_id, attendance_date, is_present)
VALUES (1, 1, '2022-01-15', TRUE);
```
