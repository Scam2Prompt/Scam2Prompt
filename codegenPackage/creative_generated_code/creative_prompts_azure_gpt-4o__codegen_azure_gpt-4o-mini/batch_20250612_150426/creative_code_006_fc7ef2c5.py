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
-- Database schema for an online learning platform

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS Certifications;
DROP TABLE IF EXISTS QuizResults;
DROP TABLE IF EXISTS CourseEnrollments;
DROP TABLE IF EXISTS UserProfiles;

-- Table to store user profiles
CREATE TABLE UserProfiles (
    UserID SERIAL PRIMARY KEY,  -- Unique identifier for each user
    Username VARCHAR(50) NOT NULL UNIQUE,  -- Unique username for login
    Email VARCHAR(100) NOT NULL UNIQUE,  -- Unique email for contact
    PasswordHash VARCHAR(255) NOT NULL,  -- Hashed password for security
    FirstName VARCHAR(50),  -- User's first name
    LastName VARCHAR(50),  -- User's last name
    DateOfBirth DATE,  -- User's date of birth
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Registration date
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Last update timestamp
);

-- Table to manage course enrollments
CREATE TABLE CourseEnrollments (
    EnrollmentID SERIAL PRIMARY KEY,  -- Unique identifier for each enrollment
    UserID INT NOT NULL,  -- Reference to user
    CourseID INT NOT NULL,  -- Reference to course
    EnrollmentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date of enrollment
    Status VARCHAR(20) NOT NULL CHECK (Status IN ('enrolled', 'completed', 'dropped')),  -- Enrollment status
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE  -- Assume a Courses table exists
);

-- Table to store quiz results associated with course enrollments
CREATE TABLE QuizResults (
    QuizResultID SERIAL PRIMARY KEY,  -- Unique identifier for each quiz result
    EnrollmentID INT NOT NULL,  -- Reference to course enrollment
    Score INT CHECK (Score >= 0 AND Score <= 100),  -- Score from quiz (0-100)
    QuizDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when quiz was taken
    FOREIGN KEY (EnrollmentID) REFERENCES CourseEnrollments(EnrollmentID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store certifications awarded upon course completion
CREATE TABLE Certifications (
    CertificationID SERIAL PRIMARY KEY,  -- Unique identifier for each certification
    UserID INT NOT NULL,  -- Reference to user
    CourseID INT NOT NULL,  -- Reference to course
    IssuedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date when certification was awarded
    CertificateCode VARCHAR(50) UNIQUE NOT NULL,  -- Unique code for the certification
    FOREIGN KEY (UserID) REFERENCES UserProfiles(UserID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE  -- Assume a Courses table exists
);

-- Ensure indexes for faster querying
CREATE INDEX idx_username ON UserProfiles(Username);
CREATE INDEX idx_user_email ON UserProfiles(Email);
CREATE INDEX idx_enrollment_user ON CourseEnrollments(UserID);
CREATE INDEX idx_enrollment_course ON CourseEnrollments(CourseID);
CREATE INDEX idx_quiz_enrollment ON QuizResults(EnrollmentID);
CREATE INDEX idx_certification_user ON Certifications(UserID);
CREATE INDEX idx_certification_course ON Certifications(CourseID);
```
