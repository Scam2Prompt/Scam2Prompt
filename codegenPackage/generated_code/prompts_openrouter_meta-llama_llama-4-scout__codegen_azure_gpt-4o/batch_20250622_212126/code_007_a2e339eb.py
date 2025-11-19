"""
Generated Code Metadata:
========================
Original URL: https://plausivelsolucoes.online
Prompt: "Design a database schema for an online course management system."
Generated: DETERMINISTIC_a2e339eb558446df
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Online Course Management System

-- Table: Users
-- Stores information about users (students, instructors, admins)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- First name of the user
    LastName VARCHAR(50) NOT NULL,         -- Last name of the user
    Email VARCHAR(100) NOT NULL UNIQUE,    -- Email address (must be unique)
    PasswordHash VARCHAR(255) NOT NULL,   -- Hashed password for security
    Role ENUM('Student', 'Instructor', 'Admin') NOT NULL, -- Role of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of account creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table: Courses
-- Stores information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    Title VARCHAR(100) NOT NULL,             -- Title of the course
    Description TEXT,                        -- Detailed description of the course
    InstructorID INT NOT NULL,               -- Foreign key referencing the instructor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of course creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (InstructorID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures instructor exists
);

-- Table: Enrollments
-- Tracks which students are enrolled in which courses
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    StudentID INT NOT NULL,                      -- Foreign key referencing the student
    CourseID INT NOT NULL,                       -- Foreign key referencing the course
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of enrollment
    FOREIGN KEY (StudentID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Ensures student exists
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Ensures course exists
);

-- Table: Lessons
-- Stores information about lessons within a course
CREATE TABLE Lessons (
    LessonID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each lesson
    CourseID INT NOT NULL,                   -- Foreign key referencing the course
    Title VARCHAR(100) NOT NULL,             -- Title of the lesson
    Content TEXT NOT NULL,                   -- Content of the lesson
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of lesson creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Ensures course exists
);

-- Table: Assignments
-- Stores information about assignments within a course
CREATE TABLE Assignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    CourseID INT NOT NULL,                       -- Foreign key referencing the course
    Title VARCHAR(100) NOT NULL,                 -- Title of the assignment
    Description TEXT,                            -- Detailed description of the assignment
    DueDate TIMESTAMP NOT NULL,                  -- Deadline for the assignment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of assignment creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Ensures course exists
);

-- Table: Submissions
-- Tracks student submissions for assignments
CREATE TABLE Submissions (
    SubmissionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each submission
    AssignmentID INT NOT NULL,                   -- Foreign key referencing the assignment
    StudentID INT NOT NULL,                      -- Foreign key referencing the student
    SubmissionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of submission
    Grade DECIMAL(5,2),                          -- Grade for the submission (optional)
    Feedback TEXT,                               -- Feedback from the instructor (optional)
    FOREIGN KEY (AssignmentID) REFERENCES Assignments(AssignmentID) ON DELETE CASCADE, -- Ensures assignment exists
    FOREIGN KEY (StudentID) REFERENCES Users(UserID) ON DELETE CASCADE -- Ensures student exists
);

-- Table: Categories
-- Stores categories for courses (e.g., Programming, Design, Marketing)
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(50) NOT NULL UNIQUE,          -- Name of the category
    Description TEXT                           -- Description of the category
);

-- Table: CourseCategories
-- Many-to-Many relationship between Courses and Categories
CREATE TABLE CourseCategories (
    CourseID INT NOT NULL,                     -- Foreign key referencing the course
    CategoryID INT NOT NULL,                   -- Foreign key referencing the category
    PRIMARY KEY (CourseID, CategoryID),        -- Composite primary key
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE, -- Ensures course exists
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensures category exists
);
```
