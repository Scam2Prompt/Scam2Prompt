"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: Create a database schema for storing information about vocational courses, training centers, and student registrations, inspired by the structure of RSP Bharat.
Generated: DETERMINISTIC_1f31cc3e42727432
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about vocational courses, training centers, and student registrations

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS StudentRegistration;
DROP TABLE IF EXISTS TrainingCenter;
DROP TABLE IF EXISTS VocationalCourse;

-- Table to store information about vocational courses
CREATE TABLE VocationalCourse (
    CourseID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,        -- Name of the vocational course
    Description TEXT,                         -- Description of the course
    Duration INT NOT NULL,                    -- Duration of the course in hours
    Fee DECIMAL(10, 2) NOT NULL,             -- Fee for the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of course creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about training centers
CREATE TABLE TrainingCenter (
    CenterID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each training center
    CenterName VARCHAR(255) NOT NULL,        -- Name of the training center
    Address VARCHAR(255) NOT NULL,           -- Address of the training center
    ContactNumber VARCHAR(15),                -- Contact number for the training center
    Email VARCHAR(255),                       -- Email address for the training center
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of center creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store student registrations for courses
CREATE TABLE StudentRegistration (
    RegistrationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each registration
    StudentName VARCHAR(255) NOT NULL,            -- Name of the student
    CourseID INT NOT NULL,                         -- Foreign key referencing VocationalCourse
    CenterID INT NOT NULL,                         -- Foreign key referencing TrainingCenter
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the registration
    FOREIGN KEY (CourseID) REFERENCES VocationalCourse(CourseID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (CenterID) REFERENCES TrainingCenter(CenterID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_course_name ON VocationalCourse(CourseName);
CREATE INDEX idx_center_name ON TrainingCenter(CenterName);
CREATE INDEX idx_student_name ON StudentRegistration(StudentName);
```
