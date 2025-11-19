"""
Generated Code Metadata:
========================
Original URL: https://ineso.edu.mx
Prompt: "Design a database schema to store information about dental education programs, including program duration, accreditation details, and course schedules, inspired by the offerings of INESO."
Generated: DETERMINISTIC_b2a5375f37e917ef
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about dental education programs

CREATE TABLE DentalPrograms (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL, -- Name of the dental program
    Duration INT NOT NULL, -- Duration of the program in months
    AccreditationDetails TEXT, -- Details about the program's accreditation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the program was last updated
);

CREATE TABLE CourseSchedules (
    ScheduleID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each course schedule
    ProgramID INT NOT NULL, -- Foreign key referencing the DentalPrograms table
    CourseName VARCHAR(255) NOT NULL, -- Name of the course
    StartDate DATE NOT NULL, -- Start date of the course
    EndDate DATE NOT NULL, -- End date of the course
    FOREIGN KEY (ProgramID) REFERENCES DentalPrograms(ProgramID) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each instructor
    FirstName VARCHAR(100) NOT NULL, -- Instructor's first name
    LastName VARCHAR(100) NOT NULL, -- Instructor's last name
    Email VARCHAR(255) UNIQUE NOT NULL, -- Instructor's email address
    Phone VARCHAR(15), -- Instructor's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the instructor was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the instructor was last updated
);

CREATE TABLE CourseInstructors (
    CourseInstructorID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each course-instructor relationship
    ScheduleID INT NOT NULL, -- Foreign key referencing the CourseSchedules table
    InstructorID INT NOT NULL, -- Foreign key referencing the Instructors table
    FOREIGN KEY (ScheduleID) REFERENCES CourseSchedules(ScheduleID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_program_name ON DentalPrograms(ProgramName);
CREATE INDEX idx_course_name ON CourseSchedules(CourseName);
CREATE INDEX idx_instructor_email ON Instructors(Email);
```
