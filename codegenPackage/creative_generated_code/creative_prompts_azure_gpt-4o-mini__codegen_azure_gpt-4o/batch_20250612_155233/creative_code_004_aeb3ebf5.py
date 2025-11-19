"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welwitschia-aviation.com
Prompt: Design a database schema for managing student enrollments in aviation security training courses, specifically for Welwitschia Aviation's offerings.
Generated: DETERMINISTIC_aeb3ebf55758e4ef
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing student enrollments in aviation security training courses
-- Welwitschia Aviation's offerings

-- Table to store information about students
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each student
    FirstName VARCHAR(100) NOT NULL,          -- Student's first name
    LastName VARCHAR(100) NOT NULL,           -- Student's last name
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Student's email address (must be unique)
    PhoneNumber VARCHAR(15),                  -- Optional: Student's phone number
    DateOfBirth DATE NOT NULL,                -- Student's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about courses offered by Welwitschia Aviation
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,         -- Name of the course
    CourseDescription TEXT,                   -- Description of the course
    DurationInDays INT NOT NULL,              -- Duration of the course in days
    StartDate DATE NOT NULL,                  -- Course start date
    EndDate DATE NOT NULL,                    -- Course end date
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to manage enrollments of students in courses
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Reference to the student
    CourseID INT NOT NULL,                       -- Reference to the course
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of enrollment
    Status ENUM('Enrolled', 'Completed', 'Withdrawn') DEFAULT 'Enrolled', -- Status of the enrollment
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID) ON DELETE CASCADE, -- Cascade delete on student removal
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete on course removal
);

-- Index for faster lookup on Students table (email)
CREATE INDEX idx_students_email ON Students(Email);

-- Index for faster lookup on Enrollments table (student and course combination)
CREATE INDEX idx_enrollments_student_course ON Enrollments(StudentID, CourseID);

-- Sample Data Constraints
-- Ensure that the course's end date is after its start date
CREATE TRIGGER trg_courses_dates_check
BEFORE INSERT ON Courses
FOR EACH ROW
BEGIN
    IF NEW.EndDate <= NEW.StartDate THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'EndDate must be after StartDate';
    END IF;
END;
```
