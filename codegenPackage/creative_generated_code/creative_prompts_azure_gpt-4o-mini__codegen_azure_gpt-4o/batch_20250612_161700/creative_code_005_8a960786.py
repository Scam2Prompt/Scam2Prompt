"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Design a database schema for storing user progress in self-defense training courses, inspired by the offerings of Blue Training Academy.
Generated: DETERMINISTIC_8a960786b1e250b3
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for tracking user progress in self-defense training courses
-- Inspired by Blue Training Academy's offerings

CREATE DATABASE BlueTrainingAcademy;

USE BlueTrainingAcademy;

-- Table to store information about users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    FirstName VARCHAR(50) NOT NULL,        -- First name of the user
    LastName VARCHAR(50) NOT NULL,         -- Last name of the user
    Email VARCHAR(100) UNIQUE NOT NULL,    -- Email address of the user
    DateOfBirth DATE,                      -- Date of birth of the user
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the user was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to store information about courses
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each course
    CourseName VARCHAR(100) NOT NULL,        -- Name of the course
    Description TEXT,                        -- Detailed description of the course
    DifficultyLevel ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Difficulty level of the course
    DurationInHours INT,                     -- Duration of the course in hours
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the course was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Table to track user progress in courses
CREATE TABLE UserProgress (
    ProgressID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each progress entry
    UserID INT NOT NULL,                       -- Foreign key to the Users table
    CourseID INT NOT NULL,                     -- Foreign key to the Courses table
    CompletionPercentage DECIMAL(5, 2) DEFAULT 0.00, -- Progress percentage (e.g., 50.00 for 50%)
    IsCompleted BOOLEAN DEFAULT FALSE,         -- Flag to indicate if the course is completed
    LastAccessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the user's last access to the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the progress entry was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,  -- Cascade delete if the user is deleted
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID) ON DELETE CASCADE -- Cascade delete if the course is deleted
);

-- Indexes for faster search and retrieval
CREATE INDEX idx_UserProgress_UserID ON UserProgress(UserID);
CREATE INDEX idx_UserProgress_CourseID ON UserProgress(CourseID);

-- Example: Adding more tables for tracking assessments, instructors, etc. could extend functionality.
```
