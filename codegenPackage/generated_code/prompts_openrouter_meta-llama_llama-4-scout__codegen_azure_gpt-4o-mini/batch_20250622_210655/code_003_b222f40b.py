"""
Generated Code Metadata:
========================
Original URL: https://onedivepb.com
Prompt: Design a database schema to store information about scuba diving instructors, courses, and students for a diving school like One Dive.
Generated: DETERMINISTIC_b222f40b5c47c5d6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a scuba diving school

-- Table to store information about scuba diving instructors
CREATE TABLE Instructors (
    instructor_id SERIAL PRIMARY KEY, -- Unique identifier for each instructor
    first_name VARCHAR(50) NOT NULL,  -- Instructor's first name
    last_name VARCHAR(50) NOT NULL,   -- Instructor's last name
    certification_level VARCHAR(50) NOT NULL, -- Instructor's certification level (e.g., PADI, NAUI)
    email VARCHAR(100) UNIQUE NOT NULL, -- Instructor's email address
    phone_number VARCHAR(15),           -- Instructor's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about scuba diving courses
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course (e.g., Open Water Diver)
    description TEXT,               -- Description of the course
    duration INT NOT NULL,          -- Duration of the course in hours
    price DECIMAL(10, 2) NOT NULL,  -- Price of the course
    instructor_id INT NOT NULL,     -- Foreign key referencing the instructor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id) ON DELETE CASCADE -- Ensures instructor integrity
);

-- Table to store information about students
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL,  -- Student's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Student's email address
    phone_number VARCHAR(15),          -- Student's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store enrollment information linking students to courses
CREATE TABLE Enrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    student_id INT NOT NULL,          -- Foreign key referencing the student
    course_id INT NOT NULL,           -- Foreign key referencing the course
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Enrollment date
    status VARCHAR(20) DEFAULT 'active', -- Status of the enrollment (e.g., active, completed, canceled)
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Ensures student integrity
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensures course integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_instructor_email ON Instructors(email);
CREATE INDEX idx_course_name ON Courses(course_name);
CREATE INDEX idx_student_email ON Students(email);
```
