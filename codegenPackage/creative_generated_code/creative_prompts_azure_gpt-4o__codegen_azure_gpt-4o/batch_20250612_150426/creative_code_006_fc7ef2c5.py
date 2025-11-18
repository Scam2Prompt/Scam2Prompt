"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupiter.graphy.com
Prompt: Create a database schema to manage user profiles, course enrollments, quiz results, and certifications for an online learning platform inspired by Jupiter Swap™.
Generated: DETERMINISTIC_fc7ef2c531cd121c
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Online Learning Platform Inspired by Jupiter Swap™

-- Table to manage user profiles
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,         -- User's first name
    LastName VARCHAR(50) NOT NULL,          -- User's last name
    Email VARCHAR(100) UNIQUE NOT NULL,     -- User's unique email address
    PasswordHash VARCHAR(255) NOT NULL,     -- Hashed password for security
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Account creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last profile update timestamp
);

-- Table to manage courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Description of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Course creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last course update timestamp
);

-- Table to manage course enrollments
CREATE TABLE CourseEnrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each enrollment
    UserID INT NOT NULL,                         -- Reference to the user
    CourseID INT NOT NULL,                       -- Reference to the course
    EnrolledAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Enrollment timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete when user is removed
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete when course is removed
);

-- Table to manage quiz results
CREATE TABLE QuizResults (
    ResultID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each quiz result
    UserID INT NOT NULL,                      -- Reference to the user
    CourseID INT NOT NULL,                    -- Reference to the course
    QuizScore DECIMAL(5, 2) NOT NULL,         -- Score achieved in the quiz (e.g., 85.50)
    AttemptedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Quiz attempt timestamp
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete when user is removed
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete when course is removed
);

-- Table to manage certifications
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    UserID INT NOT NULL,                            -- Reference to the user
    CourseID INT NOT NULL,                          -- Reference to the course
    IssuedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Certification issue date
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE, -- Cascade delete when user is removed
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete when course is removed
);

-- Indexes for optimized queries
CREATE INDEX idx_users_email ON Users(Email);        -- Index for faster lookup by email
CREATE INDEX idx_course_enrollments_user_course ON CourseEnrollments(UserID, CourseID); -- Composite index for user and course enrollments
CREATE INDEX idx_quiz_results_user_course ON QuizResults(UserID, CourseID); -- Composite index for quiz results
CREATE INDEX idx_certifications_user_course ON Certifications(UserID, CourseID); -- Composite index for certifications
```
