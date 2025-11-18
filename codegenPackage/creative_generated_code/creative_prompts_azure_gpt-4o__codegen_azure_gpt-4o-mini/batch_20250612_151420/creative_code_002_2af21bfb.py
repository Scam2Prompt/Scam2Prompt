"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Generate code to create a database schema for managing physiotherapy student records, including fields for course enrollment (e.g., MPT, BPTh.), clinical training schedules, and academic achievements, as described by Ayushman College.
Generated: DETERMINISTIC_2af21bfb04036deb
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Physiotherapy Student Records

-- Create a database for Ayushman College's physiotherapy student records
CREATE DATABASE IF NOT EXISTS AyushmanCollege;

-- Use the created database
USE AyushmanCollege;

-- Table to store student information
CREATE TABLE IF NOT EXISTS Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL,           -- Student's first name
    last_name VARCHAR(50) NOT NULL,            -- Student's last name
    dob DATE NOT NULL,                          -- Student's date of birth
    course_enrollment ENUM('MPT', 'BPTh') NOT NULL,  -- Course enrollment details
    email VARCHAR(100) UNIQUE NOT NULL,        -- Student's email address
    phone_number VARCHAR(15),                   -- Student's phone number
    enrollment_date DATE NOT NULL,              -- Date of enrollment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store clinical training schedules
CREATE TABLE IF NOT EXISTS ClinicalTrainingSchedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    student_id INT NOT NULL,                    -- Reference to student_id in Students table
    training_date DATE NOT NULL,                -- Date of clinical training
    training_location VARCHAR(100) NOT NULL,    -- Location of the clinical training
    notes TEXT,                                 -- Additional notes regarding the training
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store academic achievements
CREATE TABLE IF NOT EXISTS AcademicAchievements (
    achievement_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each achievement
    student_id INT NOT NULL,                      -- Reference to student_id in Students table
    achievement_date DATE NOT NULL,               -- Date of the achievement
    description TEXT NOT NULL,                    -- Description of the achievement
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Example of inserting a student record (to be executed outside of the schema creation)
-- INSERT INTO Students (first_name, last_name, dob, course_enrollment, email, phone_number, enrollment_date) 
-- VALUES ('John', 'Doe', '1995-05-15', 'MPT', 'john.doe@example.com', '1234567890', '2023-01-15');
```
