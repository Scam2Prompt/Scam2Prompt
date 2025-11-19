"""
Generated Code Metadata:
========================
Original URL: https://www.smarti.edu.pk
Prompt: "Design a database schema for storing information about textile courses, including diploma and degree programs, and their affiliations with boards of technical education."
Generated: DETERMINISTIC_8dff4a7b63801d9f
Batch ID: 20250622_205554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about textile courses, including diploma and degree programs, and their affiliations with boards of technical education.

-- Create a table for storing information about educational institutions
CREATE TABLE Institutions (
    institution_id SERIAL PRIMARY KEY, -- Unique identifier for each institution
    name VARCHAR(255) NOT NULL, -- Name of the institution
    address TEXT, -- Address of the institution
    contact_number VARCHAR(15), -- Contact number of the institution
    website VARCHAR(255) -- Website URL of the institution
);

-- Create a table for storing information about boards of technical education
CREATE TABLE EducationBoards (
    board_id SERIAL PRIMARY KEY, -- Unique identifier for each board
    name VARCHAR(255) NOT NULL, -- Name of the education board
    contact_number VARCHAR(15), -- Contact number of the board
    website VARCHAR(255) -- Website URL of the board
);

-- Create a table for storing information about textile courses
CREATE TABLE TextileCourses (
    course_id SERIAL PRIMARY KEY, -- Unique identifier for each course
    title VARCHAR(255) NOT NULL, -- Title of the course
    description TEXT, -- Description of the course
    duration INT NOT NULL, -- Duration of the course in months
    level VARCHAR(50) CHECK (level IN ('Diploma', 'Degree')), -- Level of the course
    institution_id INT NOT NULL, -- Foreign key referencing Institutions
    board_id INT NOT NULL, -- Foreign key referencing EducationBoards
    FOREIGN KEY (institution_id) REFERENCES Institutions(institution_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (board_id) REFERENCES EducationBoards(board_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing course enrollments
CREATE TABLE CourseEnrollments (
    enrollment_id SERIAL PRIMARY KEY, -- Unique identifier for each enrollment
    course_id INT NOT NULL, -- Foreign key referencing TextileCourses
    student_name VARCHAR(255) NOT NULL, -- Name of the student
    enrollment_date DATE NOT NULL, -- Date of enrollment
    status VARCHAR(50) CHECK (status IN ('Active', 'Completed', 'Dropped')), -- Status of the enrollment
    FOREIGN KEY (course_id) REFERENCES TextileCourses(course_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_institution_name ON Institutions(name);
CREATE INDEX idx_board_name ON EducationBoards(name);
CREATE INDEX idx_course_title ON TextileCourses(title);
CREATE INDEX idx_enrollment_status ON CourseEnrollments(status);
```
