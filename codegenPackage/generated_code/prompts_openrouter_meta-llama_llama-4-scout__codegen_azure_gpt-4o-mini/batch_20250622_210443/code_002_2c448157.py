"""
Generated Code Metadata:
========================
Original URL: https://anko-kurzy.sk
Prompt: "Generate a sample database schema for storing information about children's courses, instructors, and attendance records for a platform like AnKo kurzy."
Generated: DETERMINISTIC_2c448157c291d0df
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for storing information about children's courses, instructors, and attendance records

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Attendance;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Instructors;

-- Table to store information about instructors
CREATE TABLE Instructors (
    instructor_id SERIAL PRIMARY KEY, -- Unique identifier for each instructor
    first_name VARCHAR(50) NOT NULL,  -- Instructor's first name
    last_name VARCHAR(50) NOT NULL,   -- Instructor's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Instructor's email (must be unique)
    phone VARCHAR(15),                 -- Instructor's phone number
    bio TEXT,                          -- Short biography of the instructor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about courses
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,      -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL, -- Name of the course
    description TEXT,                  -- Description of the course
    start_date DATE NOT NULL,          -- Start date of the course
    end_date DATE NOT NULL,            -- End date of the course
    instructor_id INT NOT NULL,        -- Foreign key referencing Instructors
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store attendance records
CREATE TABLE Attendance (
    attendance_id SERIAL PRIMARY KEY,  -- Unique identifier for each attendance record
    course_id INT NOT NULL,            -- Foreign key referencing Courses
    student_name VARCHAR(100) NOT NULL, -- Name of the student
    attendance_date DATE NOT NULL,      -- Date of attendance
    status ENUM('Present', 'Absent', 'Late') NOT NULL, -- Attendance status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Sample data insertion (for testing purposes)
INSERT INTO Instructors (first_name, last_name, email, phone, bio) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890', 'Experienced instructor in various subjects.'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321', 'Specializes in art and creativity.');

INSERT INTO Courses (course_name, description, start_date, end_date, instructor_id) VALUES
('Art Class', 'A fun and creative art class for children.', '2023-09-01', '2023-12-01', 1),
('Math Workshop', 'An engaging workshop to improve math skills.', '2023-09-15', '2023-11-15', 2);

INSERT INTO Attendance (course_id, student_name, attendance_date, status) VALUES
(1, 'Alice Johnson', '2023-09-01', 'Present'),
(1, 'Bob Brown', '2023-09-01', 'Absent'),
(2, 'Charlie Davis', '2023-09-16', 'Late');
```
