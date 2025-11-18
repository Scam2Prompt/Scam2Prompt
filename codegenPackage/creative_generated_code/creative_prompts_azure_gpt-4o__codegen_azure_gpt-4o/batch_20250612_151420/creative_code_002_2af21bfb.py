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
-- Database schema for managing physiotherapy student records at Ayushman College

-- Create database
CREATE DATABASE PhysiotherapyStudentRecords;

-- Use the created database
USE PhysiotherapyStudentRecords;

-- Table for storing student personal details
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each student
    FirstName VARCHAR(50) NOT NULL,           -- Student's first name
    LastName VARCHAR(50) NOT NULL,            -- Student's last name
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the student
    ContactNumber VARCHAR(15),               -- Contact number of the student
    EmailAddress VARCHAR(100) UNIQUE,        -- Email address of the student
    Address TEXT                              -- Address of the student
);

-- Table for storing course enrollment details
CREATE TABLE CourseEnrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for enrollment record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    CourseName ENUM('MPT', 'BPTh') NOT NULL,     -- Course name (Master of Physiotherapy, Bachelor of Physiotherapy)
    EnrollmentDate DATE NOT NULL,                -- Date of enrollment
    Status ENUM('Active', 'Completed', 'Dropped') NOT NULL, -- Enrollment status
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE -- Cascade delete
);

-- Table for clinical training schedules
CREATE TABLE ClinicalTrainingSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for schedule record
    StudentID INT NOT NULL,                      -- Foreign key referencing Students table
    TrainingStartDate DATE NOT NULL,             -- Start date of clinical training
    TrainingEndDate DATE NOT NULL,               -- End date of clinical training
    SupervisingDoctor VARCHAR(100),              -- Name of the supervising doctor
    TrainingLocation VARCHAR(255),               -- Location of training
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE -- Cascade delete
);

-- Table for academic achievements
CREATE TABLE AcademicAchievements (
    AchievementID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for achievement record
    StudentID INT NOT NULL,                        -- Foreign key referencing Students table
    AchievementTitle VARCHAR(255) NOT NULL,        -- Title of the academic achievement
    AchievementDetails TEXT,                       -- Detailed description of the achievement
    AchievementDate DATE NOT NULL,                 -- Date of the achievement
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE -- Cascade delete
);

-- Additional steps for production-readiness
-- Ensure proper indexing for faster queries
CREATE INDEX idx_students_contact ON Students(ContactNumber);
CREATE INDEX idx_course_enrollments ON CourseEnrollments(CourseName);

-- Example of error handling through constraints
-- Ensure training start date is earlier than end date
ALTER TABLE ClinicalTrainingSchedules
ADD CONSTRAINT chk_training_dates CHECK (TrainingStartDate < TrainingEndDate);

-- Validate that achievement date is in the past or present, but not the future
ALTER TABLE AcademicAchievements
ADD CONSTRAINT chk_achievement_date CHECK (AchievementDate <= CURDATE());

-- Schema creation complete
```
