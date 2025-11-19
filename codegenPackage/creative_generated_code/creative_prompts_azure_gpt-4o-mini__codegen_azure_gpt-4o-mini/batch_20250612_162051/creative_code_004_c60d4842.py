"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Design a database schema for storing information about Agile certifications and course offerings, reflecting the structure used by CrestAgile.
Generated: DETERMINISTIC_c60d4842104cd79d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing Agile certifications and course offerings
CREATE DATABASE CrestAgileCertifications;

USE CrestAgileCertifications;

-- Table to store information about Agile certifications
CREATE TABLE Certifications (
    certification_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each certification
    name VARCHAR(255) NOT NULL,                       -- Name of the certification
    description TEXT,                                  -- Description of the certification
    provider VARCHAR(255) NOT NULL,                   -- Certification provider (e.g., Scrum Alliance, PMI)
    level ENUM('Beginner', 'Intermediate', 'Advanced'), -- Level of the certification
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the certification was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about courses related to certifications
CREATE TABLE Courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each course
    certification_id INT,                              -- Foreign key referencing the Certifications table
    name VARCHAR(255) NOT NULL,                        -- Name of the course
    description TEXT,                                  -- Description of the course
    duration INT NOT NULL,                             -- Duration of the course in hours
    price DECIMAL(10, 2) NOT NULL,                    -- Price of the course
    start_date DATE,                                  -- Start date of the course
    end_date DATE,                                    -- End date of the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the course was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (certification_id) REFERENCES Certifications(certification_id) ON DELETE CASCADE -- Define foreign key relationship
);

-- Table to store information about instructors
CREATE TABLE Instructors (
    instructor_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each instructor
    first_name VARCHAR(100) NOT NULL,                 -- Instructor's first name
    last_name VARCHAR(100) NOT NULL,                  -- Instructor's last name
    email VARCHAR(255) NOT NULL UNIQUE,               -- Instructor's email (must be unique)
    bio TEXT,                                         -- Short biography of the instructor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the instructor was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to link courses and instructors (many-to-many relationship)
CREATE TABLE Course_Instructors (
    course_id INT,                                    -- Foreign key referencing the Courses table
    instructor_id INT,                               -- Foreign key referencing the Instructors table
    PRIMARY KEY (course_id, instructor_id),          -- Composite primary key
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE, -- Define foreign key relationship
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id) ON DELETE CASCADE -- Define foreign key relationship
);

-- Table to store information about course enrollments
CREATE TABLE Enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each enrollment
    course_id INT,                                    -- Foreign key referencing the Courses table
    student_email VARCHAR(255) NOT NULL,              -- Student's email for enrollment
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the enrollment was made
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Define foreign key relationship
);
```
