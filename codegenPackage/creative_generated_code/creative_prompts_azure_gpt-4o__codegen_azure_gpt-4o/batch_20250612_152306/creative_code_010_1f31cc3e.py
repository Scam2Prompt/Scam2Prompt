"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Create a database schema for storing information about vocational courses, training centers, and student registrations, inspired by the structure of RSP Bharat.
Generated: DETERMINISTIC_1f31cc3e42727432
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Vocational Courses, Training Centers, and Student Registrations

-- Table to store information about vocational courses
CREATE TABLE VocationalCourses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,               -- Name of the vocational course
    Description TEXT,                               -- Detailed description of the course
    DurationInMonths INT NOT NULL,                 -- Duration of the course in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp when the course was created
);

-- Table to store information about training centers
CREATE TABLE TrainingCenters (
    CenterID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each training center
    CenterName VARCHAR(255) NOT NULL,              -- Name of the training center
    Address TEXT NOT NULL,                         -- Address of the training center
    ContactNumber VARCHAR(15),                     -- Contact number of the center
    Email VARCHAR(255),                            -- Email of the center
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp when the center was created
);

-- Table to store information about student registrations
CREATE TABLE StudentRegistrations (
    RegistrationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each registration
    StudentName VARCHAR(255) NOT NULL,             -- Name of the student
    StudentEmail VARCHAR(255) NOT NULL,            -- Email of the student
    StudentPhone VARCHAR(15),                      -- Phone number of the student
    CourseID INT NOT NULL,                         -- Foreign key referencing VocationalCourses.CourseID
    CenterID INT NOT NULL,                         -- Foreign key referencing TrainingCenters.CenterID
    RegistrationDate DATE NOT NULL,                -- Date of registration
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the registration was created
    FOREIGN KEY (CourseID) REFERENCES VocationalCourses(CourseID) ON DELETE CASCADE,
    FOREIGN KEY (CenterID) REFERENCES TrainingCenters(CenterID) ON DELETE CASCADE
);

-- Indexes for optimizing searches
CREATE INDEX idx_course_name ON VocationalCourses (CourseName);
CREATE INDEX idx_center_name ON TrainingCenters (CenterName);
CREATE INDEX idx_student_email ON StudentRegistrations (StudentEmail);

-- Error handling best practices:
-- Ensure that foreign key constraints are set properly to prevent orphaned records.
-- Use appropriate data types and validations (e.g., NOT NULL constraints) to avoid inconsistent data.
```
