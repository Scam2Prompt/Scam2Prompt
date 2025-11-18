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
-- Database schema for storing information about vocational courses, training centers, and student registrations

-- Create a table for storing training centers
CREATE TABLE TrainingCenters (
    CenterID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each training center
    CenterName VARCHAR(255) NOT NULL,              -- Name of the training center
    Address VARCHAR(255) NOT NULL,                  -- Address of the training center
    PhoneNumber VARCHAR(15),                        -- Contact phone number (optional)
    Email VARCHAR(255) UNIQUE,                      -- Contact email (optional, must be unique)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for storing vocational courses
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,               -- Name of the vocational course
    Description TEXT,                               -- Description of the course (optional)
    Duration INT NOT NULL,                           -- Duration of the course in hours
    Fee DECIMAL(10, 2) NOT NULL,                    -- Fee for the course
    CenterID INT,                                   -- Foreign key referencing the Training Centers
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CenterID) REFERENCES TrainingCenters(CenterID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Create a table for storing student registrations
CREATE TABLE StudentRegistrations (
    RegistrationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each registration
    StudentName VARCHAR(255) NOT NULL,              -- Name of the student
    Email VARCHAR(255) NOT NULL UNIQUE,              -- Email of the student (must be unique)
    PhoneNumber VARCHAR(15),                        -- Contact phone number (optional)
    CourseID INT,                                   -- Foreign key referencing the Courses
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of registration
    Status ENUM('Registered', 'Completed', 'Cancelled') DEFAULT 'Registered', -- Status of the registration
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Create indexes for faster query performance (optional, depending on usage patterns)
CREATE INDEX idx_course_name ON Courses (CourseName);
CREATE INDEX idx_center_name ON TrainingCenters (CenterName);
CREATE INDEX idx_student_email ON StudentRegistrations (Email);
```
